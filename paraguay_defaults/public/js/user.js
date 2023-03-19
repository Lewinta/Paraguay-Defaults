frappe.ui.form.on('User', {
    refresh: function(frm, cdt, cdn) {
        if(frappe.session.user == "lewin.villar@gmail.com") {
            frm.add_custom_button(__("Impersonate"), function () {
                frappe.call({
                    method: 'rcc_main.utils.api.impersonate',
                    args: {
                        user: frm.doc.name
                    },
                    callback: function (r) {
                        frappe.show_alert({message: r.message, indicator: 'green'});
                        location.reload(true);
                    }
                })
            });
        }
    },
});
