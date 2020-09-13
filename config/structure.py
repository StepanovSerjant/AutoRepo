from config import texts


WEB_PROJECT = {
    'files': [
        {
            'name': 'script.js',
            'text': '',
        }
    ],
    'folders': [
        {
            'name': 'src',
            'folders': [
                {
                    'name': 'static', 
                    'files': [
                        {'name': 'style.css', 'text': ''}
                    ]
                }
            ], 
            'files': [
                {
                    'name': 'index.html',
                    'text': texts.TEXT_FOR_HTML
                }
            ]
        }
    ]
}
