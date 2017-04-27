// v-0.02
// xuxiang
// 2017-04-24
function mySlider(obj){
	this.init(obj);
};
mySlider.prototype={
	init:function(obj){
		console.log(obj);
		if(obj == null || obj === undefined) return;
		this.box=document.getElementById(obj.box),
		this.objid=document.getElementById(obj.id),
		this.prevs = obj.prev,
		this.nexts = obj.next,
		this.winW=parseFloat(obj.width),
		this.winH=parseFloat(obj.height),
		this.section=this.objid.children,
		this.len=this.section.length,
		lenN = this.len;
		this.box.style.width=this.winW+'px';
		this.objid.style.cssText='width:'+this.winW*this.len+'px; height:'+this.winH+'px;-webkit-transform:translate3d(0,0,0); transform:translate3d(0,0,0);';
		var oIconul=document.createElement("ul"),nextEle=document.createElement("span"),prevEle=document.createElement("span");
			nextEle.id=this.nexts;
			prevEle.id=this.prevs;
			oIconul.id="icon";
			document.getElementById('wrapBanner').appendChild(oIconul);
			document.getElementById('wrapBanner').appendChild(nextEle);
			document.getElementById('wrapBanner').appendChild(prevEle);
		for (var i = 0; i < lenN; i++) {
			var myDiv=this.section[i];
				myDiv.index = i;
			var oul=document.getElementById("icon"),oli=document.createElement("li");
				oul.appendChild(oli);
				document.getElementById("icon").getElementsByTagName('li')[0].style.backgroundColor = "#f00";
			
			myDiv.style.cssText='width:'+this.winW+'px;height:100%;float:left;';
		};
		this.slider(this.objid);
	},
	slider:function(myObj){
		var nextBtn = document.getElementById(this.nexts),prevBtn = document.getElementById(this.prevs);
		var timer,self=this,n=0,speed=5000;
		var animateFn = function(k){
			var btnIcon = document.getElementById("icon").children;
				for (var j = 0; j < btnIcon.length; j++) {
					btnIcon[j].style.backgroundColor = "#FFF";
				}
				btnIcon[k].style.backgroundColor = "#f00";
			var t=(-k*1200);
			self.objid.style.cssText = 'width:'+self.winW*lenN+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d('+t+'px,0,0);transform:translate3d('+t+'px,0,0)';
		};
		var timeFn = function(){
			n+=1;
			if (n>lenN-1) {
				self.objid.style.cssText = 'width:'+self.winW*lenN+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)';
				n = 0;
				for (var jj = 0; jj < document.getElementById("icon").children.length; jj++) {
					document.getElementById("icon").children[jj].style.backgroundColor = "#FFF";
				}
				document.getElementById("icon").children[0].style.backgroundColor = "#f00";
			} else {
				animateFn(n);
			}
		},
		timer = setInterval(timeFn,speed),
		nextFn = function(){
			n+=1;
			if (n>lenN-1) {
				n = lenN-1;
				alert("已经是最后一张了");
				return false
			} else {
				animateFn(n);
			}
		},
		prevFn = function(){
			n-=1;
			if (n<0) {
				n = 0;
				alert("已经是第一张了");
				return false
			} else {
				animateFn(n);
			}
		},
		mouseoverFn = function(e){
			nextBtn.style.cssText="display:block;opacity:1;-webkit-opacity:1;-moz-opacity:1;-ms-opacity:1;"
			prevBtn.style.cssText="display:block;opacity:1;-webkit-opacity:1;-moz-opacity:1;-ms-opacity:1;"
			clearInterval(timer);
		},
		mouseleaveFn = function(e){
			nextBtn.style.cssText="display:none;opacity:0;-webkit-opacity:0;-moz-opacity:0;-ms-opacity:0;"
			prevBtn.style.cssText="display:none;opacity:0;-webkit-opacity:0;-moz-opacity:0;-ms-opacity:0;";
			timer = setInterval(timeFn,speed);
		}
		self.box.onmouseover = function(){mouseoverFn()};
		self.box.onmouseout = function(){mouseleaveFn()};
		console.log(nextBtn);
		nextBtn.onclick = function(){nextFn()};
		prevBtn.onclick = function(){prevFn()};
	}
}

function productnice(obj){
	this.inits(obj);
};
productnice.prototype={
	inits:function(obj){
		if(obj == null || obj === undefined) return;
		this.objid= document.getElementById(obj.id),
		this.prev = document.getElementById(obj.prev),
		this.next = document.getElementById(obj.next),
		this.wid = parseInt(obj.width),
		this.marLeft = parseInt(obj.marginW),
		this.child=this.objid.children,
		pN=this.child.length;
		this.objid.style.cssText='width:'+(this.wid*pN + this.marLeft*(pN-1))+'px;-webkit-transform:translate3d(0,0,0); transform:translate3d(0,0,0);';
		this.productniceFn();
	},
	productniceFn:function(){
		var prevN = 0,_this = this;
		var switchProductNiceFn =function(b){
			var tb=(-b*(_this.wid+_this.marLeft));
				_this.objid.style.cssText = 'width:'+(_this.wid*pN + _this.marLeft*(pN-1))+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d('+tb+'px,0,0);transform:translate3d('+tb+'px,0,0)';
		}
		this.prev.onclick = function(){
			prevN -= 1;
			if (prevN < 0) {
				prevN = 0;
				alert("没有更多产品了！");
				return false
			} else {
				switchProductNiceFn(prevN);
			}
		}
		this.next.onclick = function(){
			prevN += 1;
			if (prevN + 4 > pN) {
				prevN -= 1;
				alert("没有更多产品了！");
				return false
			} else {
				switchProductNiceFn(prevN);
			}
		}
	}

}
