import scraping
import scraping

def main():
    url="https://suumo.jp/chintai/jnc_000073405253/?bc=100277964465"
    bs = scraping.Suumo(url)
    print(bs.rent_fee())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
