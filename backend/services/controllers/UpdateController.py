from services.models import *
from services.config import db, Config
import requests, random, time
from urllib.parse import urlencode


class UpdateController:
    @staticmethod
    def upload_salary_data():

        uploaded_ids = [city.cityStateID for city in SalaryData.query.with_entities(SalaryData.cityStateID).distinct().all()]

        allCities = [city for city in CityState.query.all() if city.id not in uploaded_ids]
        failed = []

        print('landed')
        for x in range(len(allCities)):
            num = random.randint(10, 15)
            print(f"Uploading {allCities[x].city}, {allCities[x].state}. ID: {allCities[x].id}")
            qs = {
                'keyword': '15-1252.00',
                'location': f'{allCities[x].city}, {allCities[x].state}',
                'enableMetaData': 'false',
            }
            url = f"https://api.careeronestop.org/v1/comparesalaries/{Config.userId}/wage?{urlencode(qs)}"
            headers = {
                'Authorization': f'Bearer {Config.token}',
                'Accept': 'application/json'
            }

            try:
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    result = response.json()['OccupationDetail']['Wages']["BLSAreaWagesList"]
                    for each in result:

                        # Insert into database
                        new_record = SalaryData(cityStateID=allCities[x].id,
                                            rateType=each.get('RateType'),
                                            pct10=each.get('Pct10'),
                                            pct25=each.get('Pct25'),
                                            median=each.get('Median'),
                                            pct75=each.get('Pct75'),
                                            pct90=each.get('Pct90'),
                                            stFips=each.get('StFips'),
                                            area=each.get('Area'))
                        db.session.add(new_record)
                        db.session.commit()
                        print(f"Data for { allCities[x].city } inserted into database.")
                else:
                    failed.append(allCities[x].id)
                    print("Error:", response.status_code)
            
            except Exception as e:
                print("You've hit the outer Exception:",str(e))
                # break
            
            print(f'{len(allCities) - x - 1} remaining. Sleeping for {num} seconds')
            time.sleep(num)

        print("Failed IDs:", failed)

    @staticmethod
    def upload_COL_data():
        
        url = "http://localhost:3000"
        cityStateIdsUploaded = list(set([data.cityStateID for data in SalaryData.query.all()]))



        for cityStateID in cityStateIdsUploaded:
            exists = CostItem.query.filter_by(cityState_id=cityStateID).first()

            if not exists:
                location = CityState.query.filter_by(id=cityStateID).first()
                location_city = location.city
                location_state = location.state
                combined = f"{location_city}-{location_state}"

                try:
                    num = random.randint(1,3)
                    city_string = combined
                    # Tries to grab the info at city-state as some states have the same city name, like Greenville
                    response = requests.get(f"{url}/:{city_string}?USD").json()

                    if not response['costs']:
                        city_string = location_city
                        # Otherwise just feeds in the city, and we'll have to guess which state because the API doesn't say.
                        response = requests.get(f"{url}/:{city_string}?USD").json()

                    if response['costs']:
                        print(f"Adding data for {city_string}")
                        for elem in response['costs']:
                            
                            item_to_enter = elem['item']
                            cost = elem['cost']
                            try:
                                low_range = elem['range']['low']
                            except:
                                low_range = None
                            
                            try:
                                high_range = elem['range']['high']
                            except:
                                high_range = None

                            new_entry = CostItem(cityState_id = cityStateID,
                                                 item=item_to_enter,
                                                 cost=cost,
                                                 low_range=low_range,
                                                 high_range=high_range)
                            db.session.add(new_entry)
                            db.session.commit()
                    else:
                        print(f"No data for {city_string}")

                    print(f"Sleeping 1 seconds\n\n")
                    time.sleep(1)

                except Exception as e:
                    print("Exception Hit")
                    print(str(e))
                    break