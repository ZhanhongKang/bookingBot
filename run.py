from bookingcom.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go("New York")
        bot.select_dates(check_in_date="2022-02-01",check_out_date="2022-02-14")
        bot.select_adults(3)
        bot.click_search()
        bot.apply_filtration()
        #bot.close_ad()

        #A workaround to let bot to grab the data properly
        bot.refresh()

        #bot.private_room()
        #print(len(bot.report_results()))
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print('You are trying to run the bot from command line \n'
              'Please add to PATH your selenium Drivers \n'
              'Windows: \n'
              '     set PATH=%PATH%;C:path-to-your-folder \n\n'
              'Linux: \n'
              '     PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise