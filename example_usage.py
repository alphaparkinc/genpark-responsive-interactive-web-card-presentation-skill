from client import ResponsiveInteractiveWebCardPresentationClient

def main():
    client = ResponsiveInteractiveWebCardPresentationClient()
    res = client.build_responsive_web_presentation('Global Renewable Energy Transition Roadmap 2030', 8)
    print('Web Deck: ' + res['web_deck_id'] + ' | ' + res['topic'])
    print('Cards: ' + str(res['cards_count']) + ' cards | Responsive: ' + str(res['mobile_desktop_responsive_pass']))
    print('Interactive Widgets: ' + str(res['embedded_interactive_widgets_count']) + ' | PDF Export: ' + str(res['pdf_vector_export_ready']))
    print('Share URL: ' + res['live_web_share_url'])

if __name__ == '__main__':
    main()
