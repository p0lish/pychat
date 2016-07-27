angular.module('h5chat.login',['ui.router'])
    .config(loginConfig);



function loginConfig($stateProvider, $urlRouterProvider){
    $stateProvider
        .state('h5chat.login',{
            url: "login",
            templateUrl: "static/app_modules/login/login.html",
            controller: "h5chat.login.controller"
        });
}