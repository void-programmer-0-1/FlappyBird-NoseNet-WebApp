

function isMobile(){
    let regexp = /android|iphone|kindle|ipad/i;
    let isMobileDevice = regexp.test(navigator.userAgent);
    return isMobileDevice;
}
