# SNMP MIB module (VARMOUR-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/varmour_42825/VARMOUR-CHASSIS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:54 2025
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(varmourMibs,) = mibBuilder.importSymbols(
    "VARMOUR-SMI",
    "varmourMibs")

(VarmourDevice,) = mibBuilder.importSymbols(
    "VARMOUR-TC",
    "VarmourDevice")


# MODULE-IDENTITY

varmour_chassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VaChassis_ObjectIdentity = ObjectIdentity
vaChassis = _VaChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1)
)
_VaChDevConnect_Type = Integer32
_VaChDevConnect_Object = MibScalar
vaChDevConnect = _VaChDevConnect_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 1),
    _VaChDevConnect_Type()
)
vaChDevConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChDevConnect.setStatus("current")


class _VaChDevInactive_Type(OctetString):
    """Custom type vaChDevInactive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChDevInactive_Type.__name__ = "OctetString"
_VaChDevInactive_Object = MibScalar
vaChDevInactive = _VaChDevInactive_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 2),
    _VaChDevInactive_Type()
)
vaChDevInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChDevInactive.setStatus("current")


class _VaChDevLastJoin_Type(OctetString):
    """Custom type vaChDevLastJoin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChDevLastJoin_Type.__name__ = "OctetString"
_VaChDevLastJoin_Object = MibScalar
vaChDevLastJoin = _VaChDevLastJoin_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 3),
    _VaChDevLastJoin_Type()
)
vaChDevLastJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChDevLastJoin.setStatus("current")
_VaChPhysical_Type = Integer32
_VaChPhysical_Object = MibScalar
vaChPhysical = _VaChPhysical_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 4),
    _VaChPhysical_Type()
)
vaChPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChPhysical.setStatus("current")
_VaChLogical_Type = Integer32
_VaChLogical_Object = MibScalar
vaChLogical = _VaChLogical_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 5),
    _VaChLogical_Type()
)
vaChLogical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChLogical.setStatus("current")


class _VaChCtrlFabIf_Type(OctetString):
    """Custom type vaChCtrlFabIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChCtrlFabIf_Type.__name__ = "OctetString"
_VaChCtrlFabIf_Object = MibScalar
vaChCtrlFabIf = _VaChCtrlFabIf_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 6),
    _VaChCtrlFabIf_Type()
)
vaChCtrlFabIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChCtrlFabIf.setStatus("current")


class _VaChCntrlProto_Type(OctetString):
    """Custom type vaChCntrlProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChCntrlProto_Type.__name__ = "OctetString"
_VaChCntrlProto_Object = MibScalar
vaChCntrlProto = _VaChCntrlProto_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 7),
    _VaChCntrlProto_Type()
)
vaChCntrlProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChCntrlProto.setStatus("current")
_VaChCntlPort_Type = Integer32
_VaChCntlPort_Object = MibScalar
vaChCntlPort = _VaChCntlPort_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 8),
    _VaChCntlPort_Type()
)
vaChCntlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChCntlPort.setStatus("current")


class _VaChFabIP_Type(OctetString):
    """Custom type vaChFabIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChFabIP_Type.__name__ = "OctetString"
_VaChFabIP_Object = MibScalar
vaChFabIP = _VaChFabIP_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 9),
    _VaChFabIP_Type()
)
vaChFabIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChFabIP.setStatus("current")


class _VaChFabDefGway_Type(OctetString):
    """Custom type vaChFabDefGway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChFabDefGway_Type.__name__ = "OctetString"
_VaChFabDefGway_Object = MibScalar
vaChFabDefGway = _VaChFabDefGway_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 10),
    _VaChFabDefGway_Type()
)
vaChFabDefGway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChFabDefGway.setStatus("current")


class _VaChMgmtDefGway_Type(OctetString):
    """Custom type vaChMgmtDefGway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChMgmtDefGway_Type.__name__ = "OctetString"
_VaChMgmtDefGway_Object = MibScalar
vaChMgmtDefGway = _VaChMgmtDefGway_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 11),
    _VaChMgmtDefGway_Type()
)
vaChMgmtDefGway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChMgmtDefGway.setStatus("current")


class _VaChDatapathId_Type(OctetString):
    """Custom type vaChDatapathId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChDatapathId_Type.__name__ = "OctetString"
_VaChDatapathId_Object = MibScalar
vaChDatapathId = _VaChDatapathId_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 12),
    _VaChDatapathId_Type()
)
vaChDatapathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChDatapathId.setStatus("current")


class _VaChOFlowCtrlIp_Type(OctetString):
    """Custom type vaChOFlowCtrlIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChOFlowCtrlIp_Type.__name__ = "OctetString"
_VaChOFlowCtrlIp_Object = MibScalar
vaChOFlowCtrlIp = _VaChOFlowCtrlIp_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 13),
    _VaChOFlowCtrlIp_Type()
)
vaChOFlowCtrlIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChOFlowCtrlIp.setStatus("current")


class _VaChOFlowCtrlProto_Type(OctetString):
    """Custom type vaChOFlowCtrlProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChOFlowCtrlProto_Type.__name__ = "OctetString"
_VaChOFlowCtrlProto_Object = MibScalar
vaChOFlowCtrlProto = _VaChOFlowCtrlProto_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 14),
    _VaChOFlowCtrlProto_Type()
)
vaChOFlowCtrlProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChOFlowCtrlProto.setStatus("current")
_VaChOFlowPort_Type = Integer32
_VaChOFlowPort_Object = MibScalar
vaChOFlowPort = _VaChOFlowPort_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 15),
    _VaChOFlowPort_Type()
)
vaChOFlowPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChOFlowPort.setStatus("current")


class _VaChDevConSince_Type(OctetString):
    """Custom type vaChDevConSince based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChDevConSince_Type.__name__ = "OctetString"
_VaChDevConSince_Object = MibScalar
vaChDevConSince = _VaChDevConSince_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 16),
    _VaChDevConSince_Type()
)
vaChDevConSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChDevConSince.setStatus("current")


class _VaChSessDist_Type(OctetString):
    """Custom type vaChSessDist based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaChSessDist_Type.__name__ = "OctetString"
_VaChSessDist_Object = MibScalar
vaChSessDist = _VaChSessDist_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 17),
    _VaChSessDist_Type()
)
vaChSessDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChSessDist.setStatus("current")
_VaChVirtMacId_Type = Integer32
_VaChVirtMacId_Object = MibScalar
vaChVirtMacId = _VaChVirtMacId_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 1, 18),
    _VaChVirtMacId_Type()
)
vaChVirtMacId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaChVirtMacId.setStatus("current")
_VaChassisDev_ObjectIdentity = ObjectIdentity
vaChassisDev = _VaChassisDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 2)
)
_VaChassisDevSlot_ObjectIdentity = ObjectIdentity
vaChassisDevSlot = _VaChassisDevSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 3)
)
_VaChassisDevSlotNode_ObjectIdentity = ObjectIdentity
vaChassisDevSlotNode = _VaChassisDevSlotNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 4)
)
_VaChassisDevSlotNodeIf_ObjectIdentity = ObjectIdentity
vaChassisDevSlotNodeIf = _VaChassisDevSlotNodeIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VARMOUR-CHASSIS-MIB",
    **{"varmour-chassis": varmour_chassis,
       "vaChassis": vaChassis,
       "vaChDevConnect": vaChDevConnect,
       "vaChDevInactive": vaChDevInactive,
       "vaChDevLastJoin": vaChDevLastJoin,
       "vaChPhysical": vaChPhysical,
       "vaChLogical": vaChLogical,
       "vaChCtrlFabIf": vaChCtrlFabIf,
       "vaChCntrlProto": vaChCntrlProto,
       "vaChCntlPort": vaChCntlPort,
       "vaChFabIP": vaChFabIP,
       "vaChFabDefGway": vaChFabDefGway,
       "vaChMgmtDefGway": vaChMgmtDefGway,
       "vaChDatapathId": vaChDatapathId,
       "vaChOFlowCtrlIp": vaChOFlowCtrlIp,
       "vaChOFlowCtrlProto": vaChOFlowCtrlProto,
       "vaChOFlowPort": vaChOFlowPort,
       "vaChDevConSince": vaChDevConSince,
       "vaChSessDist": vaChSessDist,
       "vaChVirtMacId": vaChVirtMacId,
       "vaChassisDev": vaChassisDev,
       "vaChassisDevSlot": vaChassisDevSlot,
       "vaChassisDevSlotNode": vaChassisDevSlotNode,
       "vaChassisDevSlotNodeIf": vaChassisDevSlotNodeIf}
)
