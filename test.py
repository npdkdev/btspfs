from order import AOAddOrder
import json
cq = json.loads("""{
    "client_id": 0,
    "cart_type": 1,
    "timestamp": 1670627531,
    "checkout_price_data": {
        "merchandise_subtotal": 12432000000,
        "shipping_subtotal_before_discount": 6100000000,
        "shipping_discount_subtotal": 0,
        "shipping_subtotal": 6100000000,
        "tax_payable": 0,
        "tax_exemption": 0,
        "custom_tax_subtotal": 0,
        "promocode_applied": null,
        "credit_card_promotion": null,
        "shopee_coins_redeemed": null,
        "group_buy_discount": 0,
        "bundle_deals_discount": null,
        "price_adjustment": null,
        "buyer_txn_fee": 100000000,
        "buyer_service_fee": 0,
        "insurance_subtotal": 0,
        "insurance_before_discount_subtotal": 0,
        "insurance_discount_subtotal": 0,
        "vat_subtotal": 0,
        "total_payable": 18632000000
    },
    "order_update_info": {},
    "dropshipping_info": {
        "enabled": false,
        "name": "",
        "phone_number": ""
    },
    "promotion_data": {
        "can_use_coins": false,
        "use_coins": false,
        "platform_vouchers": [],
        "free_shipping_voucher_info": {
            "free_shipping_voucher_id": 0,
            "free_shipping_voucher_code": "",
            "disabled_reason": null,
            "banner_info": {
                "msg": "",
                "learn_more_msg": ""
            },
            "required_be_channel_ids": [],
            "required_spm_channels": []
        },
        "highlighted_platform_voucher_type": -1,
        "shop_voucher_entrances": [
            {
                "shopid": 323663278,
                "status": true
            }
        ],
        "applied_voucher_code": null,
        "voucher_code": null,
        "voucher_info": {
            "coin_earned": 0,
            "voucher_code": null,
            "coin_percentage": 0,
            "discount_percentage": 0,
            "discount_value": 0,
            "promotionid": 0,
            "reward_type": 0,
            "used_price": 0
        },
        "invalid_message": "",
        "price_discount": 0,
        "coin_info": {
            "coin_offset": 0,
            "coin_used": 0,
            "coin_earn_by_voucher": 0,
            "coin_earn": 0
        },
        "card_promotion_id": null,
        "card_promotion_enabled": false,
        "promotion_msg": ""
    },
    "selected_payment_channel_data": {
        "version": 2,
        "option_info": "",
        "channel_id": 8005200,
        "channel_item_option_info": {
            "option_info": "89052003"
        },
        "text_info": {}
    },
    "shoporders": [
        {
            "shop": {
                "shopid": 323663278,
                "shop_name": "Songkok Wali Kota",
                "cb_option": false,
                "is_official_shop": false,
                "remark_type": 0,
                "support_ereceipt": false,
                "seller_user_id": 323682877,
                "shop_tag": 2
            },
            "items": [
                {
                    "itemid": 12129414285,
                    "modelid": 103139768778,
                    "quantity": 1,
                    "item_group_id": null,
                    "insurances": [
                        {
                            "insurance_product_id": "1690597860413811713",
                            "name": "Proteksi Kerusakan +",
                            "description": "Melindungi produkmu dari kerusakan/kerugian total selama 6 bulan.",
                            "product_detail_page_url": "https://insurance.shopee.co.id/product-protection/profile?from=mp_checkout&product_id=1690597860413811713",
                            "premium": 170000000,
                            "premium_before_discount": 170000000,
                            "insurance_quantity": 1,
                            "selected": false
                        }
                    ],
                    "shopid": 323663278,
                    "shippable": true,
                    "non_shippable_err": "",
                    "none_shippable_reason": "",
                    "none_shippable_full_reason": "",
                    "price": 12432000000,
                    "name": "Jas Hujan Rain Coat Mantel Hujan Motor Anti Rembes KAISAR Setelan Jaket Celena Pria Wanita Full Pres Original Awet Kuat Halus",
                    "model_name": "BIRU gdfBENHUR",
                    "add_on_deal_id": 0,
                    "is_add_on_sub_item": false,
                    "is_pre_order": false,
                    "is_streaming_price": false,
                    "image": "24a6ef647e7c6c5trce4808egdf0f539b871d",
                    "checkout": true,
                    "categories": [
                        {
                            "catids": [
                                100637,
                                100728,
                                101324
                            ]
                        }
                    ],
                    "is_spl_zero_interest": false,
                    "is_prescription": false,
                    "channel_exclusive_info": {
                        "source_id": 0,
                        "token": ""
                    },
                    "offerid": 0,
                    "supports_free_returns": false
                }
            ],
            "tax_info": {
                "use_new_custom_tax_msg": false,
                "custom_tax_msg": "",
                "custom_tax_msg_short": "",
                "remove_custom_tax_hint": false
            },
            "tax_payable": 0,
            "shipping_id": 1,
            "shipping_fee_discount": 0,
            "shipping_fee": 6100000000,
            "order_total_without_shipping": 12432000000,
            "order_total": 18532000000,
            "buyer_remark": "",
            "ext_ad_info_mappings": []
        }
    ],
    "shipping_orders": [
        {
            "shipping_id": 1,
            "shoporder_indexes": [
                0
            ],
            "selected_logistic_channelid": 8003,
            "selected_preferred_delivery_time_option_id": 0,
            "buyer_remark": "",
            "buyer_address_data": {
                "addressid": 52404512,
                "address_type": 0,
                "tax_address": ""
            },
            "fulfillment_info": {
                "fulfillment_flag": 64,
                "fulfillment_source": "",
                "managed_by_sbs": false,
                "order_fulfillment_type": 2,
                "warehouse_address_id": 0,
                "is_from_overseas": false
            },
            "order_total": 18532000000,
            "order_total_without_shipping": 12432000000,
            "selected_logistic_channelid_with_warning": null,
            "shipping_fee": 6100000000,
            "shipping_fee_discount": 0,
            "shipping_group_description": "",
            "shipping_group_icon": "",
            "tax_payable": 0,
            "is_fsv_applied": false,
            "prescription_info": {
                "images": null,
                "required": false,
                "max_allowed_images": 5
            }
        }
    ],
    "fsv_selection_infos": [],
    "client_event_info": {
        "is_platform_voucher_changed": false,
        "is_fsv_changed": false
    },
    "buyer_txn_fee_info": {
        "title": "Biaya Penanganan",
        "description": "Besar biaya penanganan adalah Rp1.000 dari total transaksi.",
        "learn_more_url": "https://shopee.co.id/m/biaya-penanganan-transferbanklainnya"
    },
    "disabled_checkout_info": {
        "description": "",
        "auto_popup": false,
        "error_infos": []
    },
    "can_checkout": true,
    "buyer_service_fee_info": {
        "learn_more_url": "https://shopee.co.id/m/biaya-layanan"
    },
    "_cft": [
        1236587
    ],
    "captcha_version": 1,
    "device_info": {}
}""")
add = AOAddOrder(
    timestamp=1212121,
    checkout_price_data=cq['checkout_price_data'],
    order_update_info=cq['order_update_info'],
    dropshipping_info=cq['dropshipping_info'],
    promotion_data=cq['promotion_data'],
    selected_payment_channel_data=cq['selected_payment_channel_data'],
    shoporders=cq['shoporders'],
    shipping_orders=cq['shipping_orders'],
    buyer_txn_fee_info=cq['buyer_txn_fee_info'],
    disabled_checkout_info=cq['disabled_checkout_info'],
    can_checkout=cq['can_checkout'],
    buyer_service_fee_info=cq['buyer_service_fee_info'],
    cft=cq['_cft'],
)
print(add.shoporders)