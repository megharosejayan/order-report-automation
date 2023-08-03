import xlrd
import pandas as pd

def get_daily_report():
  fileloc = '/content/Orders_0803.xlsx'
  df = pd.read_excel(fileloc)
  return df

def get_paid_report():
  fileloc= '/content/Orders_0803_paid.xlsx'
  df = pd.read_excel(fileloc)
  return df

province_mapping = {
    'Hokkaido': '北海道',
    'Hokkaidō': '北海道',
    'Aomori': '青森県',
    'Iwate': '岩手県',
    'Miyagi': '宮城県',
    'Akita': '秋田県',
    'Yamagata': '山形県',
    'Fukushima': '福島県',
    'Ibaraki': '茨城県',
    'Tochigi': '栃木県',
    'Gunma': '群馬県',
    'Saitama': '埼玉県',
    'Chiba': '千葉県',
    'Tokyo': '東京都',
    'Tōkyō': '東京都',
    'Kanagawa': '神奈川県',
    'Niigata': '新潟県',
    'Toyama': '富山県',
    'Ishikawa': '石川県',
    'Fukui': '福井県',
    'Yamanashi': '山梨県',
    'Nagano': '長野県',
    'Gifu': '岐阜県',
    'Shizuoka': '静岡県',
    'Aichi': '愛知県',
    'Mie': '三重県',
    'Shiga': '滋賀県',
    'Kyoto': '京都府',
    'Kyōto': '京都府',
    'Osaka': '大阪府',
    'Ōsaka': '大阪府',
    'Hyōgo': '兵庫県',
    'Nara': '奈良県',
    'Wakayama': '和歌山県',
    'Tottori': '鳥取県',
    'Shimane': '島根県',
    'Okayama': '岡山県',
    'Hiroshima': '広島県',
    'Yamaguchi': '山口県',
    'Tokushima': '徳島県',
    'Kagawa': '香川県',
    'Ehime': '愛媛県',
    'Kochi': '高知県',
    'Fukuoka': '福岡県',
    'Saga': '佐賀県',
    'Nagasaki': '長崎県',
    'Kumamoto': '熊本県',
    'Oita': '大分県',
    'Miyazaki': '宮崎県',
    'Kagoshima': '鹿児島県',
    'Okinawa': '沖縄県'
    }

def edit_daily_report():
  df = get_daily_report()
  df2 = get_paid_report()

  # fill all the nan values in the Order number column
  df['注文番号'] = df['注文番号'].fillna(0)

  # copy order number details to note col
  df['note'] = df['注文番号']

  # add extra column for multiple order case
  df.insert(df.columns.get_loc('姓') + 1, 'note2', '')

  # change prefecture names to Japanese
  df['配送先住所 province'] = df['配送先住所 province'].replace(province_mapping)
  df['請求先住所 province'] = df['請求先住所 province'].replace(province_mapping)

  # create complete shipping and billing address
  df['配送先住所'] = df['配送先住所 province'].astype(str) + df['配送先住所 市'].astype(str) + df['配送先住所 １'] + df['配送先住所 ２']
  df['請求先住所'] = df['請求先住所 province'].astype(str) + df['請求先住所 市'].astype(str) + df['請求先住所1']+ df['請求先住所2']

  return df