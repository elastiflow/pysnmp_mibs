# SNMP MIB module (EXTREME-SNMPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-SNMPV3-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:33 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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


# MODULE-IDENTITY

extremeSnmpv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeTarget_ObjectIdentity = ObjectIdentity
extremeTarget = _ExtremeTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1)
)
_ExtremeTargetAddrExtTable_Object = MibTable
extremeTargetAddrExtTable = _ExtremeTargetAddrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    extremeTargetAddrExtTable.setStatus("current")
_ExtremeTargetAddrExtEntry_Object = MibTableRow
extremeTargetAddrExtEntry = _ExtremeTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    extremeTargetAddrExtEntry.setStatus("current")


class _ExtremeTargetAddrExtIgnoreMPModel_Type(TruthValue):
    """Custom type extremeTargetAddrExtIgnoreMPModel based on TruthValue"""
    defaultValue = 2


_ExtremeTargetAddrExtIgnoreMPModel_Type.__name__ = "TruthValue"
_ExtremeTargetAddrExtIgnoreMPModel_Object = MibTableColumn
extremeTargetAddrExtIgnoreMPModel = _ExtremeTargetAddrExtIgnoreMPModel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 1),
    _ExtremeTargetAddrExtIgnoreMPModel_Type()
)
extremeTargetAddrExtIgnoreMPModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtIgnoreMPModel.setStatus("current")


class _ExtremeTargetAddrExtStandardMode_Type(TruthValue):
    """Custom type extremeTargetAddrExtStandardMode based on TruthValue"""
    defaultValue = 2


_ExtremeTargetAddrExtStandardMode_Type.__name__ = "TruthValue"
_ExtremeTargetAddrExtStandardMode_Object = MibTableColumn
extremeTargetAddrExtStandardMode = _ExtremeTargetAddrExtStandardMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 2),
    _ExtremeTargetAddrExtStandardMode_Type()
)
extremeTargetAddrExtStandardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtStandardMode.setStatus("current")
_ExtremeTargetAddrExtTrapDestIndex_Type = Integer32
_ExtremeTargetAddrExtTrapDestIndex_Object = MibTableColumn
extremeTargetAddrExtTrapDestIndex = _ExtremeTargetAddrExtTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 3),
    _ExtremeTargetAddrExtTrapDestIndex_Type()
)
extremeTargetAddrExtTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTargetAddrExtTrapDestIndex.setStatus("current")


class _ExtremeTargetAddrExtUseEventComm_Type(TruthValue):
    """Custom type extremeTargetAddrExtUseEventComm based on TruthValue"""
    defaultValue = 1


_ExtremeTargetAddrExtUseEventComm_Type.__name__ = "TruthValue"
_ExtremeTargetAddrExtUseEventComm_Object = MibTableColumn
extremeTargetAddrExtUseEventComm = _ExtremeTargetAddrExtUseEventComm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 4),
    _ExtremeTargetAddrExtUseEventComm_Type()
)
extremeTargetAddrExtUseEventComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtUseEventComm.setStatus("current")
_ExtremeTargetAddrExtTrapSrcIp_Type = IpAddress
_ExtremeTargetAddrExtTrapSrcIp_Object = MibTableColumn
extremeTargetAddrExtTrapSrcIp = _ExtremeTargetAddrExtTrapSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 5),
    _ExtremeTargetAddrExtTrapSrcIp_Type()
)
extremeTargetAddrExtTrapSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtTrapSrcIp.setStatus("deprecated")


class _ExtremeTargetAddrExtVrName_Type(DisplayString):
    """Custom type extremeTargetAddrExtVrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeTargetAddrExtVrName_Type.__name__ = "DisplayString"
_ExtremeTargetAddrExtVrName_Object = MibTableColumn
extremeTargetAddrExtVrName = _ExtremeTargetAddrExtVrName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 6),
    _ExtremeTargetAddrExtVrName_Type()
)
extremeTargetAddrExtVrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtVrName.setStatus("current")
_ExtremeTargetAddrExtTrapSrcAddrType_Type = InetAddressType
_ExtremeTargetAddrExtTrapSrcAddrType_Object = MibTableColumn
extremeTargetAddrExtTrapSrcAddrType = _ExtremeTargetAddrExtTrapSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 7),
    _ExtremeTargetAddrExtTrapSrcAddrType_Type()
)
extremeTargetAddrExtTrapSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeTargetAddrExtTrapSrcAddrType.setStatus("current")
_ExtremeTargetAddrExtTrapSrcAddr_Type = InetAddress
_ExtremeTargetAddrExtTrapSrcAddr_Object = MibTableColumn
extremeTargetAddrExtTrapSrcAddr = _ExtremeTargetAddrExtTrapSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 8),
    _ExtremeTargetAddrExtTrapSrcAddr_Type()
)
extremeTargetAddrExtTrapSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeTargetAddrExtTrapSrcAddr.setStatus("current")
_ExtremeUsm_ObjectIdentity = ObjectIdentity
extremeUsm = _ExtremeUsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 2)
)
_ExtremeUsm3DESPrivProtocol_ObjectIdentity = ObjectIdentity
extremeUsm3DESPrivProtocol = _ExtremeUsm3DESPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    extremeUsm3DESPrivProtocol.setStatus("current")
_ExtremeUsmAesCfb192Protocol_ObjectIdentity = ObjectIdentity
extremeUsmAesCfb192Protocol = _ExtremeUsmAesCfb192Protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 2, 2)
)
if mibBuilder.loadTexts:
    extremeUsmAesCfb192Protocol.setStatus("current")
_ExtremeUsmAesCfb256Protocol_ObjectIdentity = ObjectIdentity
extremeUsmAesCfb256Protocol = _ExtremeUsmAesCfb256Protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 2, 3)
)
if mibBuilder.loadTexts:
    extremeUsmAesCfb256Protocol.setStatus("current")
snmpTargetAddrEntry.registerAugmentions(
    ("EXTREME-SNMPV3-MIB",
     "extremeTargetAddrExtEntry")
)
extremeTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SNMPV3-MIB",
    **{"extremeSnmpv3": extremeSnmpv3,
       "extremeTarget": extremeTarget,
       "extremeTargetAddrExtTable": extremeTargetAddrExtTable,
       "extremeTargetAddrExtEntry": extremeTargetAddrExtEntry,
       "extremeTargetAddrExtIgnoreMPModel": extremeTargetAddrExtIgnoreMPModel,
       "extremeTargetAddrExtStandardMode": extremeTargetAddrExtStandardMode,
       "extremeTargetAddrExtTrapDestIndex": extremeTargetAddrExtTrapDestIndex,
       "extremeTargetAddrExtUseEventComm": extremeTargetAddrExtUseEventComm,
       "extremeTargetAddrExtTrapSrcIp": extremeTargetAddrExtTrapSrcIp,
       "extremeTargetAddrExtVrName": extremeTargetAddrExtVrName,
       "extremeTargetAddrExtTrapSrcAddrType": extremeTargetAddrExtTrapSrcAddrType,
       "extremeTargetAddrExtTrapSrcAddr": extremeTargetAddrExtTrapSrcAddr,
       "extremeUsm": extremeUsm,
       "extremeUsm3DESPrivProtocol": extremeUsm3DESPrivProtocol,
       "extremeUsmAesCfb192Protocol": extremeUsmAesCfb192Protocol,
       "extremeUsmAesCfb256Protocol": extremeUsmAesCfb256Protocol}
)
