var app = angular.module('Nyoom', []);

app.controller('MainController', [
    '$scope',
    function($scope){
        $scope.contactList = [
            {personName: 'i literally', personID: 0},
            {personName: 'want to', personID: 1},
            {personName: 'kill myself', personID: 2},
            {personName: 'please help', personID: 3}
        ];

        $scope.addContact = function(){
            $scope.contactList.push({personName: $scope.personName, personID: $scope.personID});
        };
    }]);

