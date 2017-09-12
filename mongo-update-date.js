db.releases.find().forEach(function(el){
    el.date = new Date(el.date);
    if (el.contracts instanceof Array){
            el.contracts.forEach(function(e){
                e.dateSigned = new Date(e.dateSigned);
                e.period.startDate= new Date(e.period.startDate);
                e.period.endDate= new Date(e.period.endDate);
                if (e.documents instanceof Array){
                    e.documents.forEach(function(d){
                        d.datePublished= new Date(d.datePublished);
                        d.dateModified= new Date(d.dateModified);;
                        });
                    }
            });
        }
    if (el.awards instanceof Array){
            el.awards.forEach(function(e){
                if (e.date){
                    e.date = new Date(e.date);
                    if (e.documents instanceof Array){
                        e.documents.forEach(function(d){
                            d.datePublished= new Date(d.datePublished);
                            d.dateModified= new Date(d.dateModified);;
                            });
                        }
                    }
            });
        }
    if (el.tender.tenderPeriod){
        el.tender.tenderPeriod.startDate = new Date(el.tender.tenderPeriod.startDate);
        el.tender.tenderPeriod.endDate = new Date(el.tender.tenderPeriod.endDate);
        }
    if (el.tender.enquiryPeriod){
        el.tender.enquiryPeriod.startDate = new Date(el.tender.enquiryPeriod.startDate);
        el.tender.enquiryPeriod.endDate = new Date(el.tender.enquiryPeriod.endDate);
        }
    if (el.tender.documents instanceof Array){
        el.tender.documents.forEach(function(d){
            d.datePublished= new Date(d.datePublished);
            d.dateModified= new Date(d.dateModified);;
            });
        }
    db.releases.save(el)
});