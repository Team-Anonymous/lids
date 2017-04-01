var pcsc = require('pcsclite');

var pcsc = pcsc();
pcsc.on('reader', function(reader) {

    reader.on('status', function(status) {

    	var changes = this.state ^ status.state;
    	if (changes) {
    		if ((changes & this.SCARD_STATE_EMPTY) && (status.state & this.SCARD_STATE_EMPTY)) {
    			console.log("card removed");
    			reader.disconnect(reader.SCARD_LEAVE_CARD, function(err) {
    			if (err) {
                        //console.log(err);
                    } else {
                        //console.log('Disconnected');
                    }
		    process.exit();
                });
    		} else if ((changes & this.SCARD_STATE_PRESENT) && (status.state & this.SCARD_STATE_PRESENT)) {
    			console.log("card inserted");
    			reader.connect({ share_mode : this.SCARD_SHARE_SHARED }, function(err, protocol) {
    				if (err) {
                        
                    } else {
                        
                        reader.transmit(new Buffer([0x00, 0xB0, 0x00, 0x00, 0x20]), 40, protocol, function(err, data) {
                        	if (err) {
                               
                           } else {
                           	console.log(status.atr);
                           	console.log(data);
                           	reader.close();
                           	pcsc.close();
                           }
                       });
                    }
                });
    		}
    	}
    });

