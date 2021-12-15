
pragma solidity >=0.8.1;

contract HelloWorld {

   event UpdatedMessages(string oldStr, string newStr);

   string public message;

   constructor(string memory initMessage) {

   }

   function update(string memory newMessage) public {
      string memory oldMsg = message;
      message = newMessage;
      emit UpdatedMessages(oldMsg, newMessage);
   }
}
