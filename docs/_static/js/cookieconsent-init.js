window.addEventListener('load', function() {
    const cc = initCookieConsent();

    cc.run({
        current_lang: 'en',
        autoclear_cookies: true,
        page_scripts: true,
        force_consent: true,

        onFirstAction: function(user_preferences, cookie) {
            // callback triggered only once on the first accept/reject action
        },
        onAccept: function () {
            if (cc.allowedCategory('analytics')) {
                gtag('consent', 'update', {
                    'analytics_storage': 'granted'
                });
            }

            if (cc.allowedCategory('targeting')) {
                gtag('consent', 'update', {
                    'ad_storage': 'granted'
                });
            }
        },
        onChange: function (cookie, changed_categories) {
            // callback triggered when user changes preferences after consent has already been given
        },

        gui_options: {
            consent_modal: {
                layout: 'box',                 // box/cloud/bar
                position: 'middle center',     // bottom/middle/top + left/right/center
                transition: 'zoom',            // zoom/slide
            },
            settings_modal: {
                transition: 'zoom'             // zoom/slide
            }
        },

        languages: {
            'en': {
                consent_modal: {
                    title: 'Mmmm Cookies...',
                    description: "Hypernode Docs uses cookies from Google to analyze activities on our website and to improve our documentation.<br><br>Read more about cookies in our <a href='https://www.hypernode.com/cookie-policy/' target='_blank' rel='noopener'>cookie policy</a> or take a look at our <a href='https://www.hypernode.com/privacy-policy/' target='_blank' rel='noopener'>privacy policy</a> to see how carefully we handle your personal data. If desired, you can change your preferences under ‘Preferences’.",
                    primary_btn: {
                        text: 'Accept all',
                        role: 'accept_all'
                    },
                    secondary_btn: {
                        text: 'Preferences',
                        role: 'settings'
                    }
                },
                settings_modal: {
                    title: 'Mmmm Cookies...',
                    save_settings_btn: 'Save preferences',
                    accept_all_btn: 'Accept all',
                    blocks: [
                        {
                            title: 'Functional',
                            description: 'The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.',
                            toggle: {
                                value: 'necessary',
                                enabled: true,
                                readonly: true          // cookie categories with readonly=true are all treated as "necessary cookies"
                            }
                        }, {
                            title: 'Statistics',
                            description: 'The technical storage or access that is used exclusively for statistical purposes.',
                            toggle: {
                                value: 'analytics',
                                enabled: false,
                                readonly: false
                            },
                        }, {
                            title: 'Marketing',
                            description: 'The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.',
                            toggle: {
                                value: 'targeting',
                                enabled: false,
                                readonly: false
                            }
                        }
                    ]
                }
            }
        }
    });
});
