
/* equal card height */
.row-equal > div[class*='col-'] {
    display: flex;
    flex: 1 0 auto;
}

.row-equal .card {
   width: 100%;
}

/* ensure equal card height inside carousel */
.carousel-inner>.row-equal.active, 
.carousel-inner>.row-equal.next, 
.carousel-inner>.row-equal.prev {
    display: flex;
}

/* prevent flicker during transition */
.carousel-inner>.row-equal.active.left, 
.carousel-inner>.row-equal.active.right {
    opacity: 0.5;
    display: flex;
}


/* control image height */
.card-img-top-250 {
    max-height: 250px;
    overflow:hidden;
}