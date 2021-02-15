@ApplicationScoped
public class OrderService {

    @Inject
    private ValidationService validation;

    @Traced(operationName = "OrderService.placeOrder")
    public Receipt placeOrder(Order order, ShoppingCart shoppingCart) {
        validation.validateBillingAddress(order.getBillingAddress());

        validation.validateShippingData(order.getShippingData());

        /* calculate Order and prepare Receipt */

        return new Receipt(/* receipt data */);
    }
}
