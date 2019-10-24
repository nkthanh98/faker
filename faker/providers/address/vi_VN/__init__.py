# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    # https://vi.wikipedia.org/wiki/T%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam
    cities = (
        'An Giang',
        'Bà Rịa - Vũng Tàu',
        'Bắc Giang',
        'Bắc Kạn',
        'Bạc Liêu',
        'Bắc Ninh',
        'Bến Tre',
        'Bình Định',
        'Bình Dương',
        'Bình Phước',
        'Bình Thuận',
        'Cà Mau',
        'Cao Bằng',
        'Đắk Lắk',
        'Đắk Nông',
        'Điện Biên',
        'Đồng Nai',
        'Đồng Tháp',
        'Gia Lai',
        'Hà Giang',
        'Hà Nam',
        'Hà Tĩnh',
        'Hải Dương',
        'Hậu Giang',
        'Hòa Bình',
        'Hưng Yên',
        'Khánh Hòa',
        'Kiên Giang',
        'Kon Tum',
        'Lai Châu',
        'Lâm Đồng',
        'Lạng Sơn',
        'Lào Cai',
        'Long An',
        'Nam Định',
        'Nghệ An',
        'Ninh Bình',
        'Ninh Thuận',
        'Phú Thọ',
        'Quảng Bình',
        'Quảng Nam',
        'Quảng Ngãi',
        'Quảng Ninh',
        'Quảng Trị',
        'Sóc Trăng',
        'Sơn La',
        'Tây Ninh',
        'Thái Bình',
        'Thái Nguyên',
        'Thanh Hóa',
        'Thừa Thiên Huế',
        'Tiền Giang',
        'Trà Vinh',
        'Tuyên Quang',
        'Vĩnh Long',
        'Vĩnh Phúc',
        'Yên Bái',
        'Phú Yên',
    )

    # https://www.101languages.net/vietnamese/country-names-vietnamese/
    countries = (
        'Afghanistan',
        'Albania',
        'Algérie',
        'Andorra',
        'Angola',
        'Antigua và Barbuda',
        'Argentina',
        'Armenia',
        'Úc',
        'Áo',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Bỉ',
        'Belize',
        'Bénin',
        'Bhutan',
        'Bolivia',
        'Bosna và Hercegovina',
        'Botswana',
        'Brasil',
        'Brunei',
        'Bulgaria',
        'Burkina Faso',
        'Burundi',
        'Campuchia',
        'Cameroon',
        'Canada',
        'Cabo Verde',
        'Cộng hòa Trung Phi',
        'Tchad',
        'Chile',
        'Trung Quốc',
        'Colombia',
        'Comoros',
        'Costa Rica',
        'Bờ Biển Ngà',
        'Croatia',
        'Cuba',
        'Síp',
        'Cộng hòa Séc',
        'Cộng hòa Dân chủ Congo',
        'Đan Mạch',
        'Djibouti',
        'Dominica',
        'Cộng hòa Dominica',
        'Đông Timor',
        'Ecuador',
        'Ai Cập',
        'El Salvador',
        'Guinea Xích Đạo',
        'Eritrea',
        'Estonia',
        'Ethiopia',
        'Fiji',
        'Phần Lan',
        'Pháp',
        'Gabon',
        'Gambia',
        'Gruzia',
        'Đức',
        'Ghana',
        'Hy Lạp',
        'Grenada',
        'Guatemala',
        'Guinée',
        'Guiné-Bissau',
        'Guyana',
        'Haiti',
        'Honduras',
        'Hungary',
        'Iceland',
        'Ấn Độ',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ai-len',
        'Israel',
        'Ý',
        'Jamaica',
        'Nhật Bản',
        'Jordan',
        'Kazakhstan',
        'Kenya',
        'Kiribati',
        'Kuwait',
        'Kyrgyzstan',
        'Lào',
        'Latvia',
        'Liban',
        'Lesotho',
        'Liberia',
        'Libya',
        'Liechtenstein',
        'Litva',
        'Luxembourg',
        'Madagascar',
        'Malawi',
        'Malaysia',
        'Maldives',
        'Mali',
        'Malta',
        'Quần đảo Marshall',
        'Mauritanie',
        'Mauritius',
        'México',
        'Micronesia',
        'Moldova',
        'Monaco',
        'Mông Cổ',
        'Montenegro',
        'Maroc',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Nepal',
        'Hà Lan',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigeria',
        'Bắc Triều Tiên',
        'Na Uy',
        'Oman',
        'Pakistan',
        'Palau',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Philippines',
        'Ba Lan',
        'Bồ Đào Nha',
        'Qatar',
        'Cộng hòa Congo',
        'Cộng hòa Macedonia',
        'Romania',
        'Nga',
        'Rwanda',
        'Saint Kitts và Nevis',
        'Saint Lucia',
        'Saint Vincent và Grenadines',
        'Samoa',
        'San Marino',
        'São Tomé và Príncipe',
        'Ả Rập Saudi',
        'Sénégal',
        'Serbia',
        'Seychelles',
        'Sierra Leone',
        'Singapore',
        'Slovakia',
        'Slovenia',
        'Quần đảo Solomon',
        'Somalia',
        'Nam Phi',
        'Hàn Quốc',
        'Nam Sudan',
        'Tây Ban Nha',
        'Sri Lanka',
        'Sudan',
        'Suriname',
        'Swaziland',
        'Thụy Điển',
        'Thụy Sĩ',
        'Syria',
        'Tajikistan',
        'Tanzania',
        'Thái Lan',
        'Togo',
        'Tonga',
        'Trinidad và Tobago',
        'Tunisia',
        'Thổ Nhĩ Kỳ',
        'Turkmenistan',
        'Tuvalu',
        'Uganda',
        'Ukraina',
        'Ả Rập Thống nhất',
        'Vương quốc Liên hiệp Anh và Bắc Ireland',
        'Chủng Quốc Hoa Kỳ',
        'Uruguay',
        'Uzbekistan',
        'Vanuatu',
        'Venezuela',
        'Việt Nam',
        'Yemen',
        'Zambia',
        'Zimbabwe',
    )

    # https://vi.wikipedia.org/wiki/H%C3%A0_N%E1%BB%99i#T%E1%BB%95_ch%E1%BB%A9c_h%C3%A0nh_ch%C3%ADnh
    states = (
        'Ba Đình',
        'Hoàn Kiếm',
        'Hai Bà Trưng',
        'Đống Đa',
        'Tây Hồ',
        'Cầu Giấy',
        'Thanh Xuân',
        'Hoàng Mai',
        'Long Biên',
        'Bắc Từ Liêm',
        'Thanh Trì',
        'Gia Lâm',
        'Đông Anh',
        'Sóc Sơn',
        'Hà Đông',
        'Sơn Tây',
        'Ba Vì',
        'Phúc Thọ',
        'Thạch Thất',
        'Quốc Oai',
        'Chương Mỹ',
        'Đan Phượng',
        'Hoài Đức',
        'Thanh Oai ',
        'Mỹ Đức',
        'Ứng Hoà',
        'Thường Tín',
        'Phú Xuyên',
        'Mê Linh',
        'Nam Từ Liên',
    )

    address_formats = (
        "{{state}}, {{city}}",
    )

    def country(self):
        return self.random_element(Provider.countries)

    def city(self):
        return self.random_element(Provider.cities)

    def state(self):
        return self.random_element(Provider.states)
