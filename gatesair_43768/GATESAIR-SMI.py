# SNMP MIB module (GATESAIR-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gatesair_43768/GATESAIR-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:36 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gatesAirSmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 1)
)
if mibBuilder.loadTexts:
    gatesAirSmi.setRevisions(
        ("2014-12-18 11:04",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GatesAir_ObjectIdentity = ObjectIdentity
gatesAir = _GatesAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768)
)
if mibBuilder.loadTexts:
    gatesAir.setStatus("current")
_GatesAirMibs_ObjectIdentity = ObjectIdentity
gatesAirMibs = _GatesAirMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1)
)
if mibBuilder.loadTexts:
    gatesAirMibs.setStatus("current")
_TransmissionMibs_ObjectIdentity = ObjectIdentity
transmissionMibs = _TransmissionMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 2)
)
if mibBuilder.loadTexts:
    transmissionMibs.setStatus("current")
_IntraplexMibs_ObjectIdentity = ObjectIdentity
intraplexMibs = _IntraplexMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 3)
)
if mibBuilder.loadTexts:
    intraplexMibs.setStatus("current")
_GatesAirGeneric_ObjectIdentity = ObjectIdentity
gatesAirGeneric = _GatesAirGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2)
)
if mibBuilder.loadTexts:
    gatesAirGeneric.setStatus("current")
_TransmissionGeneric_ObjectIdentity = ObjectIdentity
transmissionGeneric = _TransmissionGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1)
)
if mibBuilder.loadTexts:
    transmissionGeneric.setStatus("current")
_Modulations_ObjectIdentity = ObjectIdentity
modulations = _Modulations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 1, 1)
)
if mibBuilder.loadTexts:
    modulations.setStatus("current")
_IntraplexGeneric_ObjectIdentity = ObjectIdentity
intraplexGeneric = _IntraplexGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 2)
)
if mibBuilder.loadTexts:
    intraplexGeneric.setStatus("current")
_GatesAirProducts_ObjectIdentity = ObjectIdentity
gatesAirProducts = _GatesAirProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3)
)
if mibBuilder.loadTexts:
    gatesAirProducts.setStatus("current")
_TransmissionProducts_ObjectIdentity = ObjectIdentity
transmissionProducts = _TransmissionProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1)
)
if mibBuilder.loadTexts:
    transmissionProducts.setStatus("current")
_Transmitters_ObjectIdentity = ObjectIdentity
transmitters = _Transmitters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 1)
)
if mibBuilder.loadTexts:
    transmitters.setStatus("current")
_Uax_ObjectIdentity = ObjectIdentity
uax = _Uax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    uax.setStatus("current")
_Vax_ObjectIdentity = ObjectIdentity
vax = _Vax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vax.setStatus("current")
_ExcitersA_ObjectIdentity = ObjectIdentity
excitersA = _ExcitersA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 2)
)
if mibBuilder.loadTexts:
    excitersA.setStatus("current")
_ExcitersB_ObjectIdentity = ObjectIdentity
excitersB = _ExcitersB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 3)
)
if mibBuilder.loadTexts:
    excitersB.setStatus("current")
_Supervisors_ObjectIdentity = ObjectIdentity
supervisors = _Supervisors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 4)
)
if mibBuilder.loadTexts:
    supervisors.setStatus("current")
_Receivers_ObjectIdentity = ObjectIdentity
receivers = _Receivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 5)
)
if mibBuilder.loadTexts:
    receivers.setStatus("current")
_Gpio_ObjectIdentity = ObjectIdentity
gpio = _Gpio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 6)
)
if mibBuilder.loadTexts:
    gpio.setStatus("current")
_Exciter_ObjectIdentity = ObjectIdentity
exciter = _Exciter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 7)
)
if mibBuilder.loadTexts:
    exciter.setStatus("current")
_Nplus1_ObjectIdentity = ObjectIdentity
nplus1 = _Nplus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 8)
)
if mibBuilder.loadTexts:
    nplus1.setStatus("current")
_Custspecial_ObjectIdentity = ObjectIdentity
custspecial = _Custspecial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 1, 9)
)
if mibBuilder.loadTexts:
    custspecial.setStatus("current")
_IntraplexProducts_ObjectIdentity = ObjectIdentity
intraplexProducts = _IntraplexProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2)
)
if mibBuilder.loadTexts:
    intraplexProducts.setStatus("current")
_Netxpress_ObjectIdentity = ObjectIdentity
netxpress = _Netxpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 1)
)
if mibBuilder.loadTexts:
    netxpress.setStatus("current")
_NetworkInterfaceModules_ObjectIdentity = ObjectIdentity
networkInterfaceModules = _NetworkInterfaceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    networkInterfaceModules.setStatus("current")
_NetxpressGeneric_ObjectIdentity = ObjectIdentity
netxpressGeneric = _NetxpressGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    netxpressGeneric.setStatus("current")
_Hdlink_ObjectIdentity = ObjectIdentity
hdlink = _Hdlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hdlink.setStatus("current")
_HdlinkNetworkModules_ObjectIdentity = ObjectIdentity
hdlinkNetworkModules = _HdlinkNetworkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hdlinkNetworkModules.setStatus("current")
_HdlinkGenericModules_ObjectIdentity = ObjectIdentity
hdlinkGenericModules = _HdlinkGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hdlinkGenericModules.setStatus("current")
_HdlinkRFModules_ObjectIdentity = ObjectIdentity
hdlinkRFModules = _HdlinkRFModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hdlinkRFModules.setStatus("current")
_NetxpressLX_ObjectIdentity = ObjectIdentity
netxpressLX = _NetxpressLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 3)
)
if mibBuilder.loadTexts:
    netxpressLX.setStatus("current")
_LxnetworkInterfaceModules_ObjectIdentity = ObjectIdentity
lxnetworkInterfaceModules = _LxnetworkInterfaceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lxnetworkInterfaceModules.setStatus("current")
_LxShelfModule_ObjectIdentity = ObjectIdentity
lxShelfModule = _LxShelfModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lxShelfModule.setStatus("current")
_Iplink_ObjectIdentity = ObjectIdentity
iplink = _Iplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4)
)
if mibBuilder.loadTexts:
    iplink.setStatus("current")
_IplinkTrapModule_ObjectIdentity = ObjectIdentity
iplinkTrapModule = _IplinkTrapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    iplinkTrapModule.setStatus("current")
_IplinkNetworkModules_ObjectIdentity = ObjectIdentity
iplinkNetworkModules = _IplinkNetworkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    iplinkNetworkModules.setStatus("current")
_IplinkGenericModules_ObjectIdentity = ObjectIdentity
iplinkGenericModules = _IplinkGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    iplinkGenericModules.setStatus("current")
_IplinkChannelModules_ObjectIdentity = ObjectIdentity
iplinkChannelModules = _IplinkChannelModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 4)
)
if mibBuilder.loadTexts:
    iplinkChannelModules.setStatus("current")
_IplinkRTPStreamModules_ObjectIdentity = ObjectIdentity
iplinkRTPStreamModules = _IplinkRTPStreamModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 5)
)
if mibBuilder.loadTexts:
    iplinkRTPStreamModules.setStatus("current")
_IplinkHTTPStreamModules_ObjectIdentity = ObjectIdentity
iplinkHTTPStreamModules = _IplinkHTTPStreamModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 6)
)
if mibBuilder.loadTexts:
    iplinkHTTPStreamModules.setStatus("current")
_IplinkRedundancyModules_ObjectIdentity = ObjectIdentity
iplinkRedundancyModules = _IplinkRedundancyModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 3, 2, 4, 7)
)
if mibBuilder.loadTexts:
    iplinkRedundancyModules.setStatus("current")
_GatesAirAgentCaps_ObjectIdentity = ObjectIdentity
gatesAirAgentCaps = _GatesAirAgentCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 4)
)
if mibBuilder.loadTexts:
    gatesAirAgentCaps.setStatus("current")
_GatesAirMgmtReqs_ObjectIdentity = ObjectIdentity
gatesAirMgmtReqs = _GatesAirMgmtReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 5)
)
if mibBuilder.loadTexts:
    gatesAirMgmtReqs.setStatus("current")
_GatesAirTemporary_ObjectIdentity = ObjectIdentity
gatesAirTemporary = _GatesAirTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 6)
)
if mibBuilder.loadTexts:
    gatesAirTemporary.setStatus("current")
_TransmissionTemporary_ObjectIdentity = ObjectIdentity
transmissionTemporary = _TransmissionTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 6, 1)
)
if mibBuilder.loadTexts:
    transmissionTemporary.setStatus("current")
_IntraplexTemporary_ObjectIdentity = ObjectIdentity
intraplexTemporary = _IntraplexTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 6, 2)
)
if mibBuilder.loadTexts:
    intraplexTemporary.setStatus("current")
_GatesAirRegs_ObjectIdentity = ObjectIdentity
gatesAirRegs = _GatesAirRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7)
)
if mibBuilder.loadTexts:
    gatesAirRegs.setStatus("current")
_TransmissionRegs_ObjectIdentity = ObjectIdentity
transmissionRegs = _TransmissionRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1)
)
if mibBuilder.loadTexts:
    transmissionRegs.setStatus("current")
_TransmitterRegs_ObjectIdentity = ObjectIdentity
transmitterRegs = _TransmitterRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1)
)
if mibBuilder.loadTexts:
    transmitterRegs.setStatus("current")
_FaxHPReg_ObjectIdentity = ObjectIdentity
faxHPReg = _FaxHPReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    faxHPReg.setStatus("current")
_FaxLPReg_ObjectIdentity = ObjectIdentity
faxLPReg = _FaxLPReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    faxLPReg.setStatus("current")
_UaxReg_ObjectIdentity = ObjectIdentity
uaxReg = _UaxReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    uaxReg.setStatus("current")
_VaxReg_ObjectIdentity = ObjectIdentity
vaxReg = _VaxReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vaxReg.setStatus("current")
_UlxReg_ObjectIdentity = ObjectIdentity
ulxReg = _UlxReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ulxReg.setStatus("current")
_VlxReg_ObjectIdentity = ObjectIdentity
vlxReg = _VlxReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vlxReg.setStatus("current")
_UlxtReg_ObjectIdentity = ObjectIdentity
ulxtReg = _UlxtReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ulxtReg.setStatus("current")
_UaxtReg_ObjectIdentity = ObjectIdentity
uaxtReg = _UaxtReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    uaxtReg.setStatus("current")
_VaxtReg_ObjectIdentity = ObjectIdentity
vaxtReg = _VaxtReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 1, 9)
)
if mibBuilder.loadTexts:
    vaxtReg.setStatus("current")
_ExciterRegs_ObjectIdentity = ObjectIdentity
exciterRegs = _ExciterRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 2)
)
if mibBuilder.loadTexts:
    exciterRegs.setStatus("current")
_M2xReg_ObjectIdentity = ObjectIdentity
m2xReg = _M2xReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    m2xReg.setStatus("current")
_NPlus1Regs_ObjectIdentity = ObjectIdentity
nPlus1Regs = _NPlus1Regs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 3)
)
if mibBuilder.loadTexts:
    nPlus1Regs.setStatus("current")
_MscReg_ObjectIdentity = ObjectIdentity
mscReg = _MscReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mscReg.setStatus("current")
_Msc2Reg_ObjectIdentity = ObjectIdentity
msc2Reg = _Msc2Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    msc2Reg.setStatus("current")
_CustSpecialRegs_ObjectIdentity = ObjectIdentity
custSpecialRegs = _CustSpecialRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 1, 4)
)
if mibBuilder.loadTexts:
    custSpecialRegs.setStatus("current")
_IntraplexRegs_ObjectIdentity = ObjectIdentity
intraplexRegs = _IntraplexRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2)
)
if mibBuilder.loadTexts:
    intraplexRegs.setStatus("current")
_NetxpressRegs_ObjectIdentity = ObjectIdentity
netxpressRegs = _NetxpressRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1)
)
if mibBuilder.loadTexts:
    netxpressRegs.setStatus("current")
_NetworkInterfaceModuleRegs_ObjectIdentity = ObjectIdentity
networkInterfaceModuleRegs = _NetworkInterfaceModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    networkInterfaceModuleRegs.setStatus("current")
_Nim1Reg_ObjectIdentity = ObjectIdentity
nim1Reg = _Nim1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nim1Reg.setStatus("current")
_Cm30Reg_ObjectIdentity = ObjectIdentity
cm30Reg = _Cm30Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cm30Reg.setStatus("current")
_ChannelAccessModuleRegs_ObjectIdentity = ObjectIdentity
channelAccessModuleRegs = _ChannelAccessModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    channelAccessModuleRegs.setStatus("current")
_PowerSupplyRegs_ObjectIdentity = ObjectIdentity
powerSupplyRegs = _PowerSupplyRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    powerSupplyRegs.setStatus("current")
_Ac80wattReg_ObjectIdentity = ObjectIdentity
ac80wattReg = _Ac80wattReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ac80wattReg.setStatus("current")
_Ac150wattReg_ObjectIdentity = ObjectIdentity
ac150wattReg = _Ac150wattReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ac150wattReg.setStatus("current")
_ShelvesRegs_ObjectIdentity = ObjectIdentity
shelvesRegs = _ShelvesRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 4)
)
if mibBuilder.loadTexts:
    shelvesRegs.setStatus("current")
_Legacy3RUReg_ObjectIdentity = ObjectIdentity
legacy3RUReg = _Legacy3RUReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    legacy3RUReg.setStatus("current")
_Legacy1RULXReg_ObjectIdentity = ObjectIdentity
legacy1RULXReg = _Legacy1RULXReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    legacy1RULXReg.setStatus("current")
_ModuleInterfaceUnitRegs_ObjectIdentity = ObjectIdentity
moduleInterfaceUnitRegs = _ModuleInterfaceUnitRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 5)
)
if mibBuilder.loadTexts:
    moduleInterfaceUnitRegs.setStatus("current")
_Miu201Reg_ObjectIdentity = ObjectIdentity
miu201Reg = _Miu201Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    miu201Reg.setStatus("current")
_LegacyRegs_ObjectIdentity = ObjectIdentity
legacyRegs = _LegacyRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2)
)
if mibBuilder.loadTexts:
    legacyRegs.setStatus("current")
_CommonModuleRegs_ObjectIdentity = ObjectIdentity
commonModuleRegs = _CommonModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    commonModuleRegs.setStatus("current")
_ChannelModuleRegs_ObjectIdentity = ObjectIdentity
channelModuleRegs = _ChannelModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    channelModuleRegs.setStatus("current")
_ModuleAdapterRegs_ObjectIdentity = ObjectIdentity
moduleAdapterRegs = _ModuleAdapterRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3)
)
if mibBuilder.loadTexts:
    moduleAdapterRegs.setStatus("current")
_Ma301Reg_ObjectIdentity = ObjectIdentity
ma301Reg = _Ma301Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ma301Reg.setStatus("current")
_Ma303Reg_ObjectIdentity = ObjectIdentity
ma303Reg = _Ma303Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ma303Reg.setStatus("current")
_Ma305Reg_ObjectIdentity = ObjectIdentity
ma305Reg = _Ma305Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ma305Reg.setStatus("current")
_Ma305bReg_ObjectIdentity = ObjectIdentity
ma305bReg = _Ma305bReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ma305bReg.setStatus("current")
_Ma306Reg_ObjectIdentity = ObjectIdentity
ma306Reg = _Ma306Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    ma306Reg.setStatus("current")
_Ma308Reg_ObjectIdentity = ObjectIdentity
ma308Reg = _Ma308Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    ma308Reg.setStatus("current")
_Ma308bReg_ObjectIdentity = ObjectIdentity
ma308bReg = _Ma308bReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    ma308bReg.setStatus("current")
_Ma309Reg_ObjectIdentity = ObjectIdentity
ma309Reg = _Ma309Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    ma309Reg.setStatus("current")
_Ma404Reg_ObjectIdentity = ObjectIdentity
ma404Reg = _Ma404Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    ma404Reg.setStatus("current")
_Ma406iReg_ObjectIdentity = ObjectIdentity
ma406iReg = _Ma406iReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    ma406iReg.setStatus("current")
_Ma407iReg_ObjectIdentity = ObjectIdentity
ma407iReg = _Ma407iReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    ma407iReg.setStatus("current")
_Ma408iReg_ObjectIdentity = ObjectIdentity
ma408iReg = _Ma408iReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 12)
)
if mibBuilder.loadTexts:
    ma408iReg.setStatus("current")
_Ma409iReg_ObjectIdentity = ObjectIdentity
ma409iReg = _Ma409iReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 13)
)
if mibBuilder.loadTexts:
    ma409iReg.setStatus("current")
_Ma410iReg_ObjectIdentity = ObjectIdentity
ma410iReg = _Ma410iReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 14)
)
if mibBuilder.loadTexts:
    ma410iReg.setStatus("current")
_Ma412Reg_ObjectIdentity = ObjectIdentity
ma412Reg = _Ma412Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 15)
)
if mibBuilder.loadTexts:
    ma412Reg.setStatus("current")
_Ma413Reg_ObjectIdentity = ObjectIdentity
ma413Reg = _Ma413Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    ma413Reg.setStatus("current")
_Ma414Reg_ObjectIdentity = ObjectIdentity
ma414Reg = _Ma414Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 17)
)
if mibBuilder.loadTexts:
    ma414Reg.setStatus("current")
_Ma415Reg_ObjectIdentity = ObjectIdentity
ma415Reg = _Ma415Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 18)
)
if mibBuilder.loadTexts:
    ma415Reg.setStatus("current")
_Ma416Reg_ObjectIdentity = ObjectIdentity
ma416Reg = _Ma416Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 19)
)
if mibBuilder.loadTexts:
    ma416Reg.setStatus("current")
_Ma417aReg_ObjectIdentity = ObjectIdentity
ma417aReg = _Ma417aReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 20)
)
if mibBuilder.loadTexts:
    ma417aReg.setStatus("current")
_Ma418Reg_ObjectIdentity = ObjectIdentity
ma418Reg = _Ma418Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 21)
)
if mibBuilder.loadTexts:
    ma418Reg.setStatus("current")
_Ma420Reg_ObjectIdentity = ObjectIdentity
ma420Reg = _Ma420Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 22)
)
if mibBuilder.loadTexts:
    ma420Reg.setStatus("current")
_Ma421Reg_ObjectIdentity = ObjectIdentity
ma421Reg = _Ma421Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 23)
)
if mibBuilder.loadTexts:
    ma421Reg.setStatus("current")
_Ma425Reg_ObjectIdentity = ObjectIdentity
ma425Reg = _Ma425Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 24)
)
if mibBuilder.loadTexts:
    ma425Reg.setStatus("current")
_Ma426Reg_ObjectIdentity = ObjectIdentity
ma426Reg = _Ma426Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 25)
)
if mibBuilder.loadTexts:
    ma426Reg.setStatus("current")
_Ma427Reg_ObjectIdentity = ObjectIdentity
ma427Reg = _Ma427Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 26)
)
if mibBuilder.loadTexts:
    ma427Reg.setStatus("current")
_Ma429Reg_ObjectIdentity = ObjectIdentity
ma429Reg = _Ma429Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 27)
)
if mibBuilder.loadTexts:
    ma429Reg.setStatus("current")
_Ma455Reg_ObjectIdentity = ObjectIdentity
ma455Reg = _Ma455Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 28)
)
if mibBuilder.loadTexts:
    ma455Reg.setStatus("current")
_Ma503Reg_ObjectIdentity = ObjectIdentity
ma503Reg = _Ma503Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 29)
)
if mibBuilder.loadTexts:
    ma503Reg.setStatus("current")
_Ma504Reg_ObjectIdentity = ObjectIdentity
ma504Reg = _Ma504Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 30)
)
if mibBuilder.loadTexts:
    ma504Reg.setStatus("current")
_Ma505Reg_ObjectIdentity = ObjectIdentity
ma505Reg = _Ma505Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 31)
)
if mibBuilder.loadTexts:
    ma505Reg.setStatus("current")
_Ma506Reg_ObjectIdentity = ObjectIdentity
ma506Reg = _Ma506Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 32)
)
if mibBuilder.loadTexts:
    ma506Reg.setStatus("current")
_Ma507Reg_ObjectIdentity = ObjectIdentity
ma507Reg = _Ma507Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 33)
)
if mibBuilder.loadTexts:
    ma507Reg.setStatus("current")
_Ma508Reg_ObjectIdentity = ObjectIdentity
ma508Reg = _Ma508Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 34)
)
if mibBuilder.loadTexts:
    ma508Reg.setStatus("current")
_Ma509Reg_ObjectIdentity = ObjectIdentity
ma509Reg = _Ma509Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 35)
)
if mibBuilder.loadTexts:
    ma509Reg.setStatus("current")
_Ma510Reg_ObjectIdentity = ObjectIdentity
ma510Reg = _Ma510Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 36)
)
if mibBuilder.loadTexts:
    ma510Reg.setStatus("current")
_Ma551Reg_ObjectIdentity = ObjectIdentity
ma551Reg = _Ma551Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 37)
)
if mibBuilder.loadTexts:
    ma551Reg.setStatus("current")
_Ma555Reg_ObjectIdentity = ObjectIdentity
ma555Reg = _Ma555Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 38)
)
if mibBuilder.loadTexts:
    ma555Reg.setStatus("current")
_Ma556Reg_ObjectIdentity = ObjectIdentity
ma556Reg = _Ma556Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 39)
)
if mibBuilder.loadTexts:
    ma556Reg.setStatus("current")
_Ma480Reg_ObjectIdentity = ObjectIdentity
ma480Reg = _Ma480Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    ma480Reg.setStatus("current")
_Ma511Reg_ObjectIdentity = ObjectIdentity
ma511Reg = _Ma511Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 41)
)
if mibBuilder.loadTexts:
    ma511Reg.setStatus("current")
_Ma311Reg_ObjectIdentity = ObjectIdentity
ma311Reg = _Ma311Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 42)
)
if mibBuilder.loadTexts:
    ma311Reg.setStatus("current")
_Ma558Reg_ObjectIdentity = ObjectIdentity
ma558Reg = _Ma558Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 43)
)
if mibBuilder.loadTexts:
    ma558Reg.setStatus("current")
_Ma559Reg_ObjectIdentity = ObjectIdentity
ma559Reg = _Ma559Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 44)
)
if mibBuilder.loadTexts:
    ma559Reg.setStatus("current")
_Ma428Reg_ObjectIdentity = ObjectIdentity
ma428Reg = _Ma428Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 2, 3, 45)
)
if mibBuilder.loadTexts:
    ma428Reg.setStatus("current")
_HdlinkRegs_ObjectIdentity = ObjectIdentity
hdlinkRegs = _HdlinkRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hdlinkRegs.setStatus("current")
_HdlinkNetworkModulesRegs_ObjectIdentity = ObjectIdentity
hdlinkNetworkModulesRegs = _HdlinkNetworkModulesRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hdlinkNetworkModulesRegs.setStatus("current")
_HdlinkChannelAccessModuleRegs_ObjectIdentity = ObjectIdentity
hdlinkChannelAccessModuleRegs = _HdlinkChannelAccessModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 7, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hdlinkChannelAccessModuleRegs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GATESAIR-SMI",
    **{"gatesAir": gatesAir,
       "gatesAirMibs": gatesAirMibs,
       "gatesAirSmi": gatesAirSmi,
       "transmissionMibs": transmissionMibs,
       "intraplexMibs": intraplexMibs,
       "gatesAirGeneric": gatesAirGeneric,
       "transmissionGeneric": transmissionGeneric,
       "modulations": modulations,
       "intraplexGeneric": intraplexGeneric,
       "gatesAirProducts": gatesAirProducts,
       "transmissionProducts": transmissionProducts,
       "transmitters": transmitters,
       "uax": uax,
       "vax": vax,
       "excitersA": excitersA,
       "excitersB": excitersB,
       "supervisors": supervisors,
       "receivers": receivers,
       "gpio": gpio,
       "exciter": exciter,
       "nplus1": nplus1,
       "custspecial": custspecial,
       "intraplexProducts": intraplexProducts,
       "netxpress": netxpress,
       "networkInterfaceModules": networkInterfaceModules,
       "netxpressGeneric": netxpressGeneric,
       "hdlink": hdlink,
       "hdlinkNetworkModules": hdlinkNetworkModules,
       "hdlinkGenericModules": hdlinkGenericModules,
       "hdlinkRFModules": hdlinkRFModules,
       "netxpressLX": netxpressLX,
       "lxnetworkInterfaceModules": lxnetworkInterfaceModules,
       "lxShelfModule": lxShelfModule,
       "iplink": iplink,
       "iplinkTrapModule": iplinkTrapModule,
       "iplinkNetworkModules": iplinkNetworkModules,
       "iplinkGenericModules": iplinkGenericModules,
       "iplinkChannelModules": iplinkChannelModules,
       "iplinkRTPStreamModules": iplinkRTPStreamModules,
       "iplinkHTTPStreamModules": iplinkHTTPStreamModules,
       "iplinkRedundancyModules": iplinkRedundancyModules,
       "gatesAirAgentCaps": gatesAirAgentCaps,
       "gatesAirMgmtReqs": gatesAirMgmtReqs,
       "gatesAirTemporary": gatesAirTemporary,
       "transmissionTemporary": transmissionTemporary,
       "intraplexTemporary": intraplexTemporary,
       "gatesAirRegs": gatesAirRegs,
       "transmissionRegs": transmissionRegs,
       "transmitterRegs": transmitterRegs,
       "faxHPReg": faxHPReg,
       "faxLPReg": faxLPReg,
       "uaxReg": uaxReg,
       "vaxReg": vaxReg,
       "ulxReg": ulxReg,
       "vlxReg": vlxReg,
       "ulxtReg": ulxtReg,
       "uaxtReg": uaxtReg,
       "vaxtReg": vaxtReg,
       "exciterRegs": exciterRegs,
       "m2xReg": m2xReg,
       "nPlus1Regs": nPlus1Regs,
       "mscReg": mscReg,
       "msc2Reg": msc2Reg,
       "custSpecialRegs": custSpecialRegs,
       "intraplexRegs": intraplexRegs,
       "netxpressRegs": netxpressRegs,
       "networkInterfaceModuleRegs": networkInterfaceModuleRegs,
       "nim1Reg": nim1Reg,
       "cm30Reg": cm30Reg,
       "channelAccessModuleRegs": channelAccessModuleRegs,
       "powerSupplyRegs": powerSupplyRegs,
       "ac80wattReg": ac80wattReg,
       "ac150wattReg": ac150wattReg,
       "shelvesRegs": shelvesRegs,
       "legacy3RUReg": legacy3RUReg,
       "legacy1RULXReg": legacy1RULXReg,
       "moduleInterfaceUnitRegs": moduleInterfaceUnitRegs,
       "miu201Reg": miu201Reg,
       "legacyRegs": legacyRegs,
       "commonModuleRegs": commonModuleRegs,
       "channelModuleRegs": channelModuleRegs,
       "moduleAdapterRegs": moduleAdapterRegs,
       "ma301Reg": ma301Reg,
       "ma303Reg": ma303Reg,
       "ma305Reg": ma305Reg,
       "ma305bReg": ma305bReg,
       "ma306Reg": ma306Reg,
       "ma308Reg": ma308Reg,
       "ma308bReg": ma308bReg,
       "ma309Reg": ma309Reg,
       "ma404Reg": ma404Reg,
       "ma406iReg": ma406iReg,
       "ma407iReg": ma407iReg,
       "ma408iReg": ma408iReg,
       "ma409iReg": ma409iReg,
       "ma410iReg": ma410iReg,
       "ma412Reg": ma412Reg,
       "ma413Reg": ma413Reg,
       "ma414Reg": ma414Reg,
       "ma415Reg": ma415Reg,
       "ma416Reg": ma416Reg,
       "ma417aReg": ma417aReg,
       "ma418Reg": ma418Reg,
       "ma420Reg": ma420Reg,
       "ma421Reg": ma421Reg,
       "ma425Reg": ma425Reg,
       "ma426Reg": ma426Reg,
       "ma427Reg": ma427Reg,
       "ma429Reg": ma429Reg,
       "ma455Reg": ma455Reg,
       "ma503Reg": ma503Reg,
       "ma504Reg": ma504Reg,
       "ma505Reg": ma505Reg,
       "ma506Reg": ma506Reg,
       "ma507Reg": ma507Reg,
       "ma508Reg": ma508Reg,
       "ma509Reg": ma509Reg,
       "ma510Reg": ma510Reg,
       "ma551Reg": ma551Reg,
       "ma555Reg": ma555Reg,
       "ma556Reg": ma556Reg,
       "ma480Reg": ma480Reg,
       "ma511Reg": ma511Reg,
       "ma311Reg": ma311Reg,
       "ma558Reg": ma558Reg,
       "ma559Reg": ma559Reg,
       "ma428Reg": ma428Reg,
       "hdlinkRegs": hdlinkRegs,
       "hdlinkNetworkModulesRegs": hdlinkNetworkModulesRegs,
       "hdlinkChannelAccessModuleRegs": hdlinkChannelAccessModuleRegs}
)
