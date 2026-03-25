# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.hw_drivers.tools.helpers import check_network_device

proxy_drivers = {}

class ProxyController(http.Controller):
    @http.route('/hw_proxy/hello', type='http', auth='none', cors='*')
    def hello(self):
        return "ping"

    @http.route('/hw_proxy/handshake', type='json', auth='none', cors='*')
    def handshake(self):
        return True

    @http.route('/hw_proxy/status_json', type='json', auth='none', cors='*')
    def status_json(self):
        statuses = {}
        for driver in proxy_drivers:
            statuses[driver] = proxy_drivers[driver].get_status()
        return statuses

    @http.route('/hw_proxy/check_device', type='json', auth='none', cors='*', csrf=False)
    def check_device(self, hostname, interface=None):
        """Quick connectivity check for IoT device pairing troubleshooting."""
        return check_network_device(hostname, interface=interface)
