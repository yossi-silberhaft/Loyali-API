from django.conf.urls import url
from views import MobileUserAPI, CheckUserCredentials, AddSubscription, VendorByIDAPI, \
    VendorWithCards, CustomersCards, SubscriptionsWithCardsInUse, \
    SubscriptionCardsByVendorID, TestingAPI, DeleteSubscriptionAPI, PunchCardAPI

urlpatterns = [

    url(r'^login/', CheckUserCredentials.as_view(), name='mobile_login'),

    url(r'^mobile/subscriptions/byCardID/', SubscriptionCardsByVendorID.as_view(), name='customer_subscriptions_by_card'),

    url(r'^mobile/subscriptions/', SubscriptionsWithCardsInUse.as_view(), name='customer_subscriptions'),

    url(r'^mobile/users/', MobileUserAPI.as_view(), name='mobile_user'),

    url(r'^mobile/vendorByID/', VendorByIDAPI.as_view(), name='vendor_by_id'),

    url(r'^createSubscription/', AddSubscription.as_view(), name='create_subscription'),

    url(r'^deleteSubscription/', DeleteSubscriptionAPI.as_view(), name='delete_subscriptions'),

    url(r'^mobile/vendorsAndCards/', VendorWithCards.as_view(), name='customers_vendors_and_cards'),

    url(r'^mobile/customerCards/', CustomersCards.as_view(), name='customers_cards'),

    url(r'^mobile/punchCard/', PunchCardAPI.as_view(), name='punch_card'),

    url(r'^testingAPI/', TestingAPI.as_view(), name='testing_api'),

]
