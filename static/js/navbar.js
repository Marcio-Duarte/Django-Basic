
switch (window.location.pathname) {
    case '/':
        $('.0').addClass('active');
        break;
    case '/users/':
        $('.1').addClass('active');
        break;
    case '/login/':
        $('.2').addClass('active');
        break;
    case '/about':
        $('.3').addClass('active');
}