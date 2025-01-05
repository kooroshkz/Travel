import pandas as pd

def load_country_data():
    """Load the data for visited places."""
    data = {
        # Albania
        'Tirana': {'Country': 'Albania', 'Latitude': 41.3275, 'Longitude': 19.8187, 'Flag': 'https://flagcdn.com/al.svg'},

        # Austria
        'Vienna': {'Country': 'Austria', 'Latitude': 48.2082, 'Longitude': 16.3738, 'Flag': 'https://flagcdn.com/at.svg'},
        'Salzburg': {'Country': 'Austria', 'Latitude': 47.8095, 'Longitude': 13.0550, 'Flag': 'https://flagcdn.com/at.svg'},

        # Belgium
        'Antwerp': {'Country': 'Belgium', 'Latitude': 51.2194, 'Longitude': 4.4025, 'Flag': 'https://flagcdn.com/be.svg'},

        # Czech Republic
        'Prague': {'Country': 'Czech Republic', 'Latitude': 50.0755, 'Longitude': 14.4378, 'Flag': 'https://flagcdn.com/cz.svg'},

        # France
        'Paris': {'Country': 'France', 'Latitude': 48.8566, 'Longitude': 2.3522, 'Flag': 'https://flagcdn.com/fr.svg'},
        'Versailles': {'Country': 'France', 'Latitude': 48.8014, 'Longitude': 2.1301, 'Flag': 'https://flagcdn.com/fr.svg'},

        # Germany
        'Dusseldorf': {'Country': 'Germany', 'Latitude': 51.2277, 'Longitude': 6.7735, 'Flag': 'https://flagcdn.com/de.svg'},
        'Cologne': {'Country': 'Germany', 'Latitude': 50.9375, 'Longitude': 6.9603, 'Flag': 'https://flagcdn.com/de.svg'},
        'Essen': {'Country': 'Germany', 'Latitude': 51.4556, 'Longitude': 7.0116, 'Flag': 'https://flagcdn.com/de.svg'},
        'Dresden': {'Country': 'Germany', 'Latitude': 51.0504, 'Longitude': 13.7373, 'Flag': 'https://flagcdn.com/de.svg'},
        'Frankfurt': {'Country': 'Germany', 'Latitude': 50.1109, 'Longitude': 8.6821, 'Flag': 'https://flagcdn.com/de.svg'},
        'Wiesbaden': {'Country': 'Germany', 'Latitude': 50.0782, 'Longitude': 8.2398, 'Flag': 'https://flagcdn.com/de.svg'},
        'Mainz': {'Country': 'Germany', 'Latitude': 49.9929, 'Longitude': 8.2473, 'Flag': 'https://flagcdn.com/de.svg'},
        'Bonn': {'Country': 'Germany', 'Latitude': 50.7374, 'Longitude': 7.0982, 'Flag': 'https://flagcdn.com/de.svg'},

        # Hungary
        'Budapest': {'Country': 'Hungary', 'Latitude': 47.4979, 'Longitude': 19.0402, 'Flag': 'https://flagcdn.com/hu.svg'},

        # Iran
        'Tehran': {'Country': 'Iran', 'Latitude': 35.6892, 'Longitude': 51.3890, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Shiraz': {'Country': 'Iran', 'Latitude': 29.5916, 'Longitude': 52.5836, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Isfahan': {'Country': 'Iran', 'Latitude': 32.4279, 'Longitude': 51.6874, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Yazd': {'Country': 'Iran', 'Latitude': 31.8795, 'Longitude': 54.2666, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qazvin': {'Country': 'Iran', 'Latitude': 36.2704, 'Longitude': 50.0041, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Kashan': {'Country': 'Iran', 'Latitude': 33.9831, 'Longitude': 51.4090, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Rasht': {'Country': 'Iran', 'Latitude': 37.2808, 'Longitude': 49.5832, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Mazandaran': {'Country': 'Iran', 'Latitude': 36.4270, 'Longitude': 52.6776, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Gorgan': {'Country': 'Iran', 'Latitude': 36.8176, 'Longitude': 54.4343, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qom': {'Country': 'Iran', 'Latitude': 34.6401, 'Longitude': 50.8764, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Kish Island': {'Country': 'Iran', 'Latitude': 26.5569, 'Longitude': 53.9676, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Qeshm Island': {'Country': 'Iran', 'Latitude': 26.9580, 'Longitude': 56.2719, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Bandar Abbas': {'Country': 'Iran', 'Latitude': 27.1832, 'Longitude': 56.2654, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Hormuz Island': {'Country': 'Iran', 'Latitude': 27.1384, 'Longitude': 56.2333, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Ardebil': {'Country': 'Iran', 'Latitude': 38.4853, 'Longitude': 47.8911, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Abianeh': {'Country': 'Iran', 'Latitude': 33.3093, 'Longitude': 51.7348, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Sarein': {'Country': 'Iran', 'Latitude': 38.1500, 'Longitude': 48.0667, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Asalem': {'Country': 'Iran', 'Latitude': 37.8325, 'Longitude': 48.9900, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Khalkhal': {'Country': 'Iran', 'Latitude': 37.6186, 'Longitude': 48.5253, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Bandar Anzali': {'Country': 'Iran', 'Latitude': 37.4724, 'Longitude': 49.4621, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Talesh': {'Country': 'Iran', 'Latitude': 37.8074, 'Longitude': 48.9016, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Sari': {'Country': 'Iran', 'Latitude': 36.5633, 'Longitude': 53.0601, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Babol': {'Country': 'Iran', 'Latitude': 36.5513, 'Longitude': 52.6787, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Babol Sar': {'Country': 'Iran', 'Latitude': 36.7020, 'Longitude': 52.6576, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Karaj': {'Country': 'Iran', 'Latitude': 35.8355, 'Longitude': 51.0107, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Najafabad': {'Country': 'Iran', 'Latitude': 32.6342, 'Longitude': 51.3667, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Fereydunkenar': {'Country': 'Iran', 'Latitude': 36.6864, 'Longitude': 52.5225, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Namakabrud': {'Country': 'Iran', 'Latitude': 36.6497, 'Longitude': 52.9106, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Noor': {'Country': 'Iran', 'Latitude': 36.5450, 'Longitude': 52.7947, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Noshahr': {'Country': 'Iran', 'Latitude': 36.6500, 'Longitude': 51.4960, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Ramsar': {'Country': 'Iran', 'Latitude': 36.8937, 'Longitude': 50.6550, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Chalus': {'Country': 'Iran', 'Latitude': 36.6548, 'Longitude': 51.4200, 'Flag': 'https://flagcdn.com/ir.svg'},
        'Lahijan': {'Country': 'Iran', 'Latitude': 37.2083, 'Longitude': 50.0036, 'Flag': 'https://flagcdn.com/ir.svg'},

        # Luxembourg
        'Luxembourg City': {'Country': 'Luxembourg', 'Latitude': 49.6116, 'Longitude': 6.1319, 'Flag': 'https://flagcdn.com/lu.svg'},

        # Malaysia
        'Kuala Lumpur': {'Country': 'Malaysia', 'Latitude': 3.139, 'Longitude': 101.6869, 'Flag': 'https://flagcdn.com/my.svg'},
        'Lankawi': {'Country': 'Malaysia', 'Latitude': 6.3500, 'Longitude': 99.8000, 'Flag': 'https://flagcdn.com/my.svg'},

        # Netherlands
        'The Hague': {'Country': 'Netherlands', 'Latitude': 52.0705, 'Longitude': 4.3007, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Amsterdam': {'Country': 'Netherlands', 'Latitude': 52.3676, 'Longitude': 4.9041, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Rotterdam': {'Country': 'Netherlands', 'Latitude': 51.9225, 'Longitude': 4.4792, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Utrecht': {'Country': 'Netherlands', 'Latitude': 52.0907, 'Longitude': 5.1214, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Groningen': {'Country': 'Netherlands', 'Latitude': 53.2194, 'Longitude': 6.5665, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Maastricht': {'Country': 'Netherlands', 'Latitude': 50.8514, 'Longitude': 5.6912, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Eindhoven': {'Country': 'Netherlands', 'Latitude': 51.4416, 'Longitude': 5.4697, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Valkenburg': {'Country': 'Netherlands', 'Latitude': 50.8627, 'Longitude': 5.8300, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Leiden': {'Country': 'Netherlands', 'Latitude': 52.1601, 'Longitude': 4.4970, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Delft': {'Country': 'Netherlands', 'Latitude': 52.0116, 'Longitude': 4.3571, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Schiedam': {'Country': 'Netherlands', 'Latitude': 51.9194, 'Longitude': 4.3883, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Scheiveningen': {'Country': 'Netherlands', 'Latitude': 52.1040, 'Longitude': 4.2754, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Haarlem': {'Country': 'Netherlands', 'Latitude': 52.3874, 'Longitude': 4.6462, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Zoetermeer': {'Country': 'Netherlands', 'Latitude': 52.0570, 'Longitude': 4.4936, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Zaandam': {'Country': 'Netherlands', 'Latitude': 52.4388, 'Longitude': 4.8255, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Katwijk': {'Country': 'Netherlands', 'Latitude': 52.2035, 'Longitude': 4.3962, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Noordwijk': {'Country': 'Netherlands', 'Latitude': 52.2379, 'Longitude': 4.4581, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Sassenheim': {'Country': 'Netherlands', 'Latitude': 52.2226, 'Longitude': 4.5186, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Leiderdorp': {'Country': 'Netherlands', 'Latitude': 52.1620, 'Longitude': 4.5268, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Oegstgeest': {'Country': 'Netherlands', 'Latitude': 52.1833, 'Longitude': 4.4699, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Leidschendam': {'Country': 'Netherlands', 'Latitude': 52.0786, 'Longitude': 4.3988, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Vorschooten': {'Country': 'Netherlands', 'Latitude': 52.1300, 'Longitude': 4.4260, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Wassenaar': {'Country': 'Netherlands', 'Latitude': 52.1480, 'Longitude': 4.4068, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Rijnsburg': {'Country': 'Netherlands', 'Latitude': 52.1910, 'Longitude': 4.4430, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Arnheim': {'Country': 'Netherlands', 'Latitude': 51.9851, 'Longitude': 5.8987, 'Flag': 'https://flagcdn.com/nl.svg'},
        'Rijswijk': {'Country': 'Netherlands', 'Latitude': 52.0373, 'Longitude': 4.3250, 'Flag': 'https://flagcdn.com/nl.svg'},

        # Russia
        'Moscow': {'Country': 'Russia', 'Latitude': 55.7558, 'Longitude': 37.6176, 'Flag': 'https://flagcdn.com/ru.svg'},
        'Saint Petersburg': {'Country': 'Russia', 'Latitude': 59.9343, 'Longitude': 30.3351, 'Flag': 'https://flagcdn.com/ru.svg'},

        # Slovakia
        'Bratislava': {'Country': 'Slovakia', 'Latitude': 48.1486, 'Longitude': 17.1077, 'Flag': 'https://flagcdn.com/sk.svg'},

        # Spain
        'Madrid': {'Country': 'Spain', 'Latitude': 40.4168, 'Longitude': -3.7038, 'Flag': 'https://flagcdn.com/es.svg'},
        'Barcelona': {'Country': 'Spain', 'Latitude': 41.3851, 'Longitude': 2.1734, 'Flag': 'https://flagcdn.com/es.svg'},

        # Switzerland
        'Geneva': {'Country': 'Switzerland', 'Latitude': 46.2044, 'Longitude': 6.1432, 'Flag': 'https://flagcdn.com/ch.svg'},
        'Lucerne': {'Country': 'Switzerland', 'Latitude': 47.0502, 'Longitude': 8.3093, 'Flag': 'https://flagcdn.com/ch.svg'},
        'Zurich': {'Country': 'Switzerland', 'Latitude': 47.3769, 'Longitude': 8.5417, 'Flag': 'https://flagcdn.com/ch.svg'},

        # Thailand
        'Bangkok': {'Country': 'Thailand', 'Latitude': 13.7563, 'Longitude': 100.5018, 'Flag': 'https://flagcdn.com/th.svg'},
        'Pataya': {'Country': 'Thailand', 'Latitude': 12.9276, 'Longitude': 100.8777, 'Flag': 'https://flagcdn.com/th.svg'},

        # Turkey
        'Istanbul': {'Country': 'Turkey', 'Latitude': 41.0082, 'Longitude': 28.9784, 'Flag': 'https://flagcdn.com/tr.svg'},
        'Ankara': {'Country': 'Turkey', 'Latitude': 39.9334, 'Longitude': 32.8597, 'Flag': 'https://flagcdn.com/tr.svg'},
        'Antalya': {'Country': 'Turkey', 'Latitude': 36.8969, 'Longitude': 30.7133, 'Flag': 'https://flagcdn.com/tr.svg'},
        'Adana': {'Country': 'Turkey', 'Latitude': 37.0017, 'Longitude': 35.3289, 'Flag': 'https://flagcdn.com/tr.svg'},
        'Izmir': {'Country': 'Turkey', 'Latitude': 38.4192, 'Longitude': 27.1287, 'Flag': 'https://flagcdn.com/tr.svg'},

        # United Arab Emirates
        'Dubai': {'Country': 'United Arab Emirates', 'Latitude': 25.276987, 'Longitude': 55.296249, 'Flag': 'https://flagcdn.com/ae.svg'},
        'Abu Dhabi': {'Country': 'United Arab Emirates', 'Latitude': 24.4539, 'Longitude': 54.3773, 'Flag': 'https://flagcdn.com/ae.svg'},

        # United Kingdom
        'London': {'Country': 'United Kingdom', 'Latitude': 51.5074, 'Longitude': -0.1278, 'Flag': 'https://flagcdn.com/gb.svg'},

        # Ukraine
        'Kiev': {'Country': 'Ukraine', 'Latitude': 50.4501, 'Longitude': 30.5234, 'Flag': 'https://flagcdn.com/ua.svg'}
    }

    return pd.DataFrame.from_dict(data, orient='index')
