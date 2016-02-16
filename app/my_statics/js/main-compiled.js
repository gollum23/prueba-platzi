(function () {
    "use strict";

    /* Initialize foundation */

    $(document).foundation();

    Stripe.setPublishableKey('pk_test_iUseMD28pgUXZB4YGLfWVSfs');

    $('#subscription_form').submit(function (event) {
        var $form = $(this);

        $form.find('button').prop('disabled', true);

        Stripe.card.createToken($form, stripeResponseHandler);

        return false;
    });

    function stripeResponseHandler(status, response) {
        var $form = $('#subscription_form');
        if (response.error) {
            $form.find('.card_error').text(response.error.message).fadeIn();
            $form.find('button').prop('disabled', false);
        } else {
            var token = response.id;

            $form.append($('<input type="hidden" name="stripeToken" />').val(token));
            $form.get(0).submit();
        }
    }
})();

//# sourceMappingURL=main-compiled.js.map