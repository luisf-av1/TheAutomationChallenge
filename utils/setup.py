def handle_route(route):
    # Intercept network requests and block excluded resource types
    if route.request.resource_type in ['image', 'media', 'font', 'other', 'fetch']:
        route.fulfill(status=204)
    else:
        route.continue_()

def setUpPage(browser):
    
    # Setup context
    context = browser.new_context(ignore_https_errors=True) #Ignore failed requests
    context.set_offline(True)  # Simulate offline mode to skip requests

    # Setup Page
    page = browser.new_page()
    page.set_default_timeout(4000)  # lower timeouts
    page.evaluate("document.body.style.transition = 'none'")  # Disable animations
    page.route('**/*', handle_route)

    return page