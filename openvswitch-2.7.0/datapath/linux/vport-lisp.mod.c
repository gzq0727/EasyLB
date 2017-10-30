#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xfc5ded98, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x635aa764, __VMLINUX_SYMBOL_STR(ovs_lisp_fill_metadata_dst) },
	{ 0xc600f291, __VMLINUX_SYMBOL_STR(rpl_lisp_xmit) },
	{ 0x926df6a6, __VMLINUX_SYMBOL_STR(ovs_netdev_tunnel_destroy) },
	{ 0xf4526e1b, __VMLINUX_SYMBOL_STR(ovs_vport_ops_unregister) },
	{ 0xe5cf9c62, __VMLINUX_SYMBOL_STR(__ovs_vport_ops_register) },
	{ 0x2a1c9168, __VMLINUX_SYMBOL_STR(ovs_vport_free) },
	{ 0x7bbce2b2, __VMLINUX_SYMBOL_STR(rpl_rtnl_delete_link) },
	{ 0xf3c9a5a1, __VMLINUX_SYMBOL_STR(ovs_netdev_link) },
	{ 0x6e720ff2, __VMLINUX_SYMBOL_STR(rtnl_unlock) },
	{ 0x7584255b, __VMLINUX_SYMBOL_STR(dev_change_flags) },
	{ 0x6f3f6b53, __VMLINUX_SYMBOL_STR(rpl_lisp_dev_create_fb) },
	{ 0xc7a4fbed, __VMLINUX_SYMBOL_STR(rtnl_lock) },
	{ 0x38e90e62, __VMLINUX_SYMBOL_STR(ovs_vport_alloc) },
	{ 0xcd279169, __VMLINUX_SYMBOL_STR(nla_find) },
	{ 0xdb7305a1, __VMLINUX_SYMBOL_STR(__stack_chk_fail) },
	{ 0x8afaebe7, __VMLINUX_SYMBOL_STR(nla_put) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=openvswitch";


MODULE_INFO(srcversion, "0D08FEE6E9874EE9A89C9E2");
