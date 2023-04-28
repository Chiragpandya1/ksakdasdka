#!/usr/bin/env python
# coding: utf-8

# In[ ]:


currency_list = {
    'ALL': 'Albania Lek',
    'AFN': 'Afghanistan Afghani',
    'ARS': 'Argentina Peso',
    'AWG': 'Aruba Guilder',
    'AUD': 'Australia Dollar',
    'AZN': 'Azerbaijan New Manat',
    'BSD': 'Bahamas Dollar',
    'BBD': 'Barbados Dollar',
    'BDT': 'Bangladeshi taka',
    'BYR': 'Belarus Ruble',
    'BZD': 'Belize Dollar',
    'BMD': 'Bermuda Dollar',
    'BOB': 'Bolivia Boliviano',
    'BAM': 'Bosnia and Herzegovina Convertible Marka',
    'BWP': 'Botswana Pula',
    'BGN': 'Bulgaria Lev',
    'BRL': 'Brazil Real',
    'BND': 'Brunei Darussalam Dollar',
    'KHR': 'Cambodia Riel',
    'CAD': 'Canada Dollar',
    'KYD': 'Cayman Islands Dollar',
    'CLP': 'Chile Peso',
    'CNY': 'China Yuan Renminbi',
    'COP': 'Colombia Peso',
    'CRC': 'Costa Rica Colon',
    'HRK': 'Croatia Kuna',
    'CUP': 'Cuba Peso',
    'CZK': 'Czech Republic Koruna',
    'DKK': 'Denmark Krone',
    'DOP': 'Dominican Republic Peso',
    'XCD': 'East Caribbean Dollar',
    'EGP': 'Egypt Pound',
    'SVC': 'El Salvador Colon',
    'EEK': 'Estonia Kroon',
    'EUR': 'Euro Member Countries',
    'FKP': 'Falkland Islands (Malvinas) Pound',
    'FJD': 'Fiji Dollar',
    'GHC': 'Ghana Cedis',
    'GIP': 'Gibraltar Pound',
    'GTQ': 'Guatemala Quetzal',
    'GGP': 'Guernsey Pound',
    'GYD': 'Guyana Dollar',
    'HNL': 'Honduras Lempira',
    'HKD': 'Hong Kong Dollar',
    'HUF': 'Hungary Forint',
    'ISK': 'Iceland Krona',
    'INR': 'India Rupee',
    'IDR': 'Indonesia Rupiah',
    'IRR': 'Iran Rial',
    'IMP': 'Isle of Man Pound',
    'ILS': 'Israel Shekel',
    'JMD': 'Jamaica Dollar',
    'JPY': 'Japan Yen',
    'JEP': 'Jersey Pound',
    'KZT': 'Kazakhstan Tenge',
    'KPW': 'Korea (North) Won',
    'KRW': 'Korea (South) Won',
    'KGS': 'Kyrgyzstan Som',
    'LAK': 'Laos Kip',
    'LVL': 'Latvia Lat',
    'LBP': 'Lebanon Pound',
    'LRD': 'Liberia Dollar',
    'LTL': 'Lithuania Litas',
    'MKD': 'Macedonia Denar',
    'MYR': 'Malaysia Ringgit',
    'MUR': 'Mauritius Rupee',
    'MXN': 'Mexico Peso',
    'MNT': 'Mongolia Tughrik',
    'MZN': 'Mozambique Metical',
    'NAD': 'Namibia Dollar',
    'NPR': 'Nepal Rupee',
    'ANG': 'Netherlands Antilles Guilder',
    'NZD': 'New Zealand Dollar',
    'NIO': 'Nicaragua Cordoba',
    'NGN': 'Nigeria Naira',
    'NOK': 'Norway Krone',
    'OMR': 'Oman Rial',
    'PKR': 'Pakistan Rupee',
    'PAB': 'Panama Balboa',
    'PYG': 'Paraguay Guarani',
    'PEN': 'Peru Nuevo Sol',
    'PHP': 'Philippines Peso',
    'PLN': 'Poland Zloty',
    'QAR': 'Qatar Riyal',
    'RON': 'Romania New Leu',
    'RUB': 'Russia Ruble',
    'SHP': 'Saint Helena Pound',
    'SAR': 'Saudi Arabia Riyal',
    'RSD': 'Serbia Dinar',
    'SCR': 'Seychelles Rupee',
    'SGD': 'Singapore Dollar',
    'SBD': 'Solomon Islands Dollar',
    'SOS': 'Somalia Shilling',
    'ZAR': 'South Africa Rand',
    'LKR': 'Sri Lanka Rupee',
    'SEK': 'Sweden Krona',
    'CHF': 'Switzerland Franc',
    'SRD': 'Suriname Dollar',
    'SYP': 'Syria Pound',
    'TWD': 'Taiwan New Dollar',
    'THB': 'Thailand Baht',
    'TTD': 'Trinidad and Tobago Dollar',
    'TRY': 'Turkey Lira',
    'TRL': 'Turkey Lira',
    'TVD': 'Tuvalu Dollar',
    'UAH': 'Ukraine Hryvna',
    'GBP': 'United Kingdom Pound',
    'USD': 'United States Dollar',
    'UYU': 'Uruguay Peso',
    'UZS': 'Uzbekistan Som',
    'VEF': 'Venezuela Bolivar',
    'VND': 'Viet Nam Dong',
    'YER': 'Yemen Rial',
    'ZWD': 'Zimbabwe Dollar'
}


# In[29]:


# making all currency pairs


currency_pairs = []

for base_currency in currency_list.keys():
    for quote_currency in currency_list.keys():
        if base_currency != quote_currency:
            currency_pairs.append(f"{base_currency}/{quote_currency}")

print(currency_pairs)


# In[23]:


import itertools

path1 = ["USD", "EUR", "GBP", "JPY", "CAD"]

exchange_rates ={
    'USD/EUR': 0.8539,
    'USD/GBP': 0.7285,
    'USD/JPY': 109.8200,
    'USD/CAD': 1.2635,
    'EUR/USD': 1.1709,
    'EUR/GBP': 0.8539,
    'EUR/JPY': 128.2000,
    'EUR/CAD': 1.4825,
    'GBP/USD': 1.3715,
    'GBP/EUR': 1.1709,
    'GBP/JPY': 151.0000,
    'GBP/CAD': 1.7325,
    'JPY/USD': 0.0091,
    'JPY/EUR': 0.0078,
    'JPY/GBP': 0.0066,
    'JPY/CAD': 0.0115,
    'CAD/USD': 0.7919,
    'CAD/EUR': 0.6741,
    'CAD/GBP': 0.5765,
    'CAD/JPY': 86.8700
}


combinations = []
for i in range(2, len(path1) + 1):
    for subset in itertools.combinations(path1, i):
        subset = list(subset)
        pairs = [f"{subset[j]}/{subset[j+1]}" for j in range(len(subset)-1)]
        rates = [exchange_rates[pair] for pair in pairs]
        combination = dict(zip(pairs, rates))
        combinations.append(combination)

for c in combinations:
    print(c)


# In[25]:


import itertools

path1 = ["EUR", "GBP", "JPY", "CAD"]

combinations = []
for i in range(1, len(path1) + 1):
    for subset in itertools.combinations(path1, i):
        subset = list(subset)
        pairs = ["USD/" + subset[0]] + [f"{subset[j]}/{subset[j+1]}" for j in range(len(subset)-1)] + [subset[-1] + "/USD"]
        rates = [exchange_rates[pair] for pair in pairs]
        combination = dict(zip(pairs, rates))
        if combination not in combinations:
            combinations.append(combination)

for c in combinations:
    print(c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[28]:


for i in combinations:
    def convert_currency(start_amount, i, final_currency):
        path = []
        amount = start_amount
        current_currency = final_currency
        for pair, rate in i.items():
            currencies = pair.split('/')
            if currencies[0] == current_currency:
                amount *= rate
                path.append(pair)
                print(f"Amount after applying {pair}: {amount}")
                current_currency = currencies[1]
        if current_currency != final_currency:
            final_rate = i[f"{current_currency}/{final_currency}"]
            amount /= final_rate
            path.append(f"{current_currency}/{final_currency}")
            print(f"Amount after applying {current_currency}/{final_currency}: {amount}")
        print("Conversion path: ", " -> ".join(path))
        return amount

    start_amount = 50000
    final_currency = "USD"
    print('Initial amount : ',start_amount)
    final_amount = convert_currency(start_amount, i, final_currency)
    print(f"Final amount in {final_currency}: {final_amount}")
    print('*********************************************************************************** ')
    print('Total profit/loss :',(final_amount- start_amount), f'{final_currency}')
    print('***********************************************************************************')
    print(' ')

