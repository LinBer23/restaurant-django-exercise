from django.views.generic import TemplateView

class MenuPageView(TemplateView):
    template_name = "pages/menu.html"
    
    def get_context_data(self):

        menu_items = [
            {
                'title': 'Tomato Salad',
                'category': 'Salad'
            },
            {
                'title': 'Cucumber Salad',
                'category': 'Salad'
            },
            {
                'title': 'Chocolate Ice Cream',
                'category': 'Icecream'
            }
        ]

        return {
            'menus': {
                
                'salat':'Tomato Salad',
                'salat':'Cucumber Salad',                
                'ice': 'Chocolate Ice Cream',
            },
            'menu_items': menu_items
        }
