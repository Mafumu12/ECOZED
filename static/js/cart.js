var updatebuttons = document.getElementsByClassName('update-cart');

for (var i = 0; i < updatebuttons.length; i++) {
    updatebuttons[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);

        if (user == 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);
        }

        // Move the location.reload() here
        location.reload();
    });
}

function addCookieItem(productId, action) {
    console.log('not logged in..');

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 };
        } else {
            cart[productId]['quantity'] += 1;
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1;
        if (cart[productId]['quantity'] <= 0) {
            console.log('Remove Item');
            delete cart[productId];
        }
    }

    console.log('cart:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + "; domain=; path=/";
}


function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data..')
    var url = '/updateItem/'
    fetch(url, {
        method: 'POST',
        headers:
        {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
        })


}

let quantityField = document.getElementsByClassName('quantity');

for (let i = 0; i < quantityField.length; i++) {
    quantityField[i].addEventListener('change', function () {
        let quantityFieldValue = quantityField[i].value;
        let quantityFieldProduct = quantityField[i].parentElement.parentElement.children[1].children[0].innerText;
        let url = "/updateQuantity/";
        console.log("Quantity Field Value:", quantityFieldValue);
        console.log("Quantity Field Product:", quantityFieldProduct);
        console.log("URL:", url);
        fetch(url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                "qfv": quantityFieldValue,
                "qfp": quantityFieldProduct,
            })
        })
            .then(response => response.json())
            .then(data => console.log(data));
    });
}
