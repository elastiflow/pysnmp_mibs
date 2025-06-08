# SNMP MIB module (HH3C-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-FCOE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:36:50 2025
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

(fcmInstanceIndex,) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "fcmInstanceIndex")

(Hh3cFcNameId,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcNameId")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

hh3cFCoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120)
)
if mibBuilder.loadTexts:
    hh3cFCoE.setRevisions(
        ("2014-11-12 00:00",
         "2012-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cFCoEVfcBindType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceIndex", 1),
          ("macAddress", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cFCoEObjects_ObjectIdentity = ObjectIdentity
hh3cFCoEObjects = _Hh3cFCoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1)
)
_Hh3cFCoEConfig_ObjectIdentity = ObjectIdentity
hh3cFCoEConfig = _Hh3cFCoEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1)
)
_Hh3cFCoECfgTable_Object = MibTable
hh3cFCoECfgTable = _Hh3cFCoECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFCoECfgTable.setStatus("current")
_Hh3cFCoECfgEntry_Object = MibTableRow
hh3cFCoECfgEntry = _Hh3cFCoECfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1)
)
hh3cFCoECfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoECfgEntry.setStatus("current")


class _Hh3cFCoECfgFcmap_Type(OctetString):
    """Custom type hh3cFCoECfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Hh3cFCoECfgFcmap_Type.__name__ = "OctetString"
_Hh3cFCoECfgFcmap_Object = MibTableColumn
hh3cFCoECfgFcmap = _Hh3cFCoECfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 1),
    _Hh3cFCoECfgFcmap_Type()
)
hh3cFCoECfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgFcmap.setStatus("current")


class _Hh3cFCoECfgDynamicVfcCreation_Type(TruthValue):
    """Custom type hh3cFCoECfgDynamicVfcCreation based on TruthValue"""
    defaultValue = 2


_Hh3cFCoECfgDynamicVfcCreation_Type.__name__ = "TruthValue"
_Hh3cFCoECfgDynamicVfcCreation_Object = MibTableColumn
hh3cFCoECfgDynamicVfcCreation = _Hh3cFCoECfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 2),
    _Hh3cFCoECfgDynamicVfcCreation_Type()
)
hh3cFCoECfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDynamicVfcCreation.setStatus("current")


class _Hh3cFCoECfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type hh3cFCoECfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cFCoECfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_Hh3cFCoECfgDefaultFCFPriority_Object = MibTableColumn
hh3cFCoECfgDefaultFCFPriority = _Hh3cFCoECfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 3),
    _Hh3cFCoECfgDefaultFCFPriority_Type()
)
hh3cFCoECfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDefaultFCFPriority.setStatus("current")


class _Hh3cFCoECfgDATov_Type(Unsigned32):
    """Custom type hh3cFCoECfgDATov based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 600),
    )


_Hh3cFCoECfgDATov_Type.__name__ = "Unsigned32"
_Hh3cFCoECfgDATov_Object = MibTableColumn
hh3cFCoECfgDATov = _Hh3cFCoECfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 4),
    _Hh3cFCoECfgDATov_Type()
)
hh3cFCoECfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFCoECfgDATov.setUnits("seconds")


class _Hh3cFCoECfgAddressingMode_Type(Integer32):
    """Custom type hh3cFCoECfgAddressingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("spma", 2),
          ("fpmaAndSpma", 3))
    )


_Hh3cFCoECfgAddressingMode_Type.__name__ = "Integer32"
_Hh3cFCoECfgAddressingMode_Object = MibTableColumn
hh3cFCoECfgAddressingMode = _Hh3cFCoECfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 5),
    _Hh3cFCoECfgAddressingMode_Type()
)
hh3cFCoECfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgAddressingMode.setStatus("current")
_Hh3cFCoEVLANTable_Object = MibTable
hh3cFCoEVLANTable = _Hh3cFCoEVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFCoEVLANTable.setStatus("current")
_Hh3cFCoEVLANEntry_Object = MibTableRow
hh3cFCoEVLANEntry = _Hh3cFCoEVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1)
)
hh3cFCoEVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEVLANIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFabricIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEVLANEntry.setStatus("current")
_Hh3cFCoEVLANIndex_Type = VlanIndex
_Hh3cFCoEVLANIndex_Object = MibTableColumn
hh3cFCoEVLANIndex = _Hh3cFCoEVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 1),
    _Hh3cFCoEVLANIndex_Type()
)
hh3cFCoEVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEVLANIndex.setStatus("current")
_Hh3cFCoEFabricIndex_Type = T11FabricIndex
_Hh3cFCoEFabricIndex_Object = MibTableColumn
hh3cFCoEFabricIndex = _Hh3cFCoEFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 2),
    _Hh3cFCoEFabricIndex_Type()
)
hh3cFCoEFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFabricIndex.setStatus("current")


class _Hh3cFCoEVLANOperState_Type(Integer32):
    """Custom type hh3cFCoEVLANOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Hh3cFCoEVLANOperState_Type.__name__ = "Integer32"
_Hh3cFCoEVLANOperState_Object = MibTableColumn
hh3cFCoEVLANOperState = _Hh3cFCoEVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 3),
    _Hh3cFCoEVLANOperState_Type()
)
hh3cFCoEVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEVLANOperState.setStatus("current")
_Hh3cFCoEVLANRowStatus_Type = RowStatus
_Hh3cFCoEVLANRowStatus_Object = MibTableColumn
hh3cFCoEVLANRowStatus = _Hh3cFCoEVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 4),
    _Hh3cFCoEVLANRowStatus_Type()
)
hh3cFCoEVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVLANRowStatus.setStatus("current")
_Hh3cFCoEStaticVfcTable_Object = MibTable
hh3cFCoEStaticVfcTable = _Hh3cFCoEStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcTable.setStatus("current")
_Hh3cFCoEStaticVfcEntry_Object = MibTableRow
hh3cFCoEStaticVfcEntry = _Hh3cFCoEStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1)
)
hh3cFCoEStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcEntry.setStatus("current")


class _Hh3cFCoEStaticVfcIndex_Type(Unsigned32):
    """Custom type hh3cFCoEStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cFCoEStaticVfcIndex_Type.__name__ = "Unsigned32"
_Hh3cFCoEStaticVfcIndex_Object = MibTableColumn
hh3cFCoEStaticVfcIndex = _Hh3cFCoEStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 1),
    _Hh3cFCoEStaticVfcIndex_Type()
)
hh3cFCoEStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcIndex.setStatus("current")


class _Hh3cFCoEStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type hh3cFCoEStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cFCoEStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_Hh3cFCoEStaticVfcFCFPriority_Object = MibTableColumn
hh3cFCoEStaticVfcFCFPriority = _Hh3cFCoEStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 2),
    _Hh3cFCoEStaticVfcFCFPriority_Type()
)
hh3cFCoEStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcFCFPriority.setStatus("current")
_Hh3cFCoEStaticVfcBindType_Type = Hh3cFCoEVfcBindType
_Hh3cFCoEStaticVfcBindType_Object = MibTableColumn
hh3cFCoEStaticVfcBindType = _Hh3cFCoEStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 3),
    _Hh3cFCoEStaticVfcBindType_Type()
)
hh3cFCoEStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindType.setStatus("current")
_Hh3cFCoEStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_Hh3cFCoEStaticVfcBindIfIndex_Object = MibTableColumn
hh3cFCoEStaticVfcBindIfIndex = _Hh3cFCoEStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 4),
    _Hh3cFCoEStaticVfcBindIfIndex_Type()
)
hh3cFCoEStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindIfIndex.setStatus("current")
_Hh3cFCoEStaticVfcBindMACAddress_Type = MacAddress
_Hh3cFCoEStaticVfcBindMACAddress_Object = MibTableColumn
hh3cFCoEStaticVfcBindMACAddress = _Hh3cFCoEStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 5),
    _Hh3cFCoEStaticVfcBindMACAddress_Type()
)
hh3cFCoEStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindMACAddress.setStatus("current")
_Hh3cFCoEStaticVfcIfIndex_Type = InterfaceIndex
_Hh3cFCoEStaticVfcIfIndex_Object = MibTableColumn
hh3cFCoEStaticVfcIfIndex = _Hh3cFCoEStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 6),
    _Hh3cFCoEStaticVfcIfIndex_Type()
)
hh3cFCoEStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcIfIndex.setStatus("current")
_Hh3cFCoEStaticVfcCreationTime_Type = TimeStamp
_Hh3cFCoEStaticVfcCreationTime_Object = MibTableColumn
hh3cFCoEStaticVfcCreationTime = _Hh3cFCoEStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 7),
    _Hh3cFCoEStaticVfcCreationTime_Type()
)
hh3cFCoEStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcCreationTime.setStatus("current")
_Hh3cFCoEStaticVfcFailureCause_Type = SnmpAdminString
_Hh3cFCoEStaticVfcFailureCause_Object = MibTableColumn
hh3cFCoEStaticVfcFailureCause = _Hh3cFCoEStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 8),
    _Hh3cFCoEStaticVfcFailureCause_Type()
)
hh3cFCoEStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcFailureCause.setStatus("current")
_Hh3cFCoEStaticVfcRowStatus_Type = RowStatus
_Hh3cFCoEStaticVfcRowStatus_Object = MibTableColumn
hh3cFCoEStaticVfcRowStatus = _Hh3cFCoEStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 9),
    _Hh3cFCoEStaticVfcRowStatus_Type()
)
hh3cFCoEStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcRowStatus.setStatus("current")
_Hh3cFCoEFIPSnoopingTable_Object = MibTable
hh3cFCoEFIPSnoopingTable = _Hh3cFCoEFIPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingTable.setStatus("current")
_Hh3cFCoEFIPSnoopingEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingEntry = _Hh3cFCoEFIPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1)
)
hh3cFCoEFIPSnoopingEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVLANIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingVLANIndex_Type = VlanIndex
_Hh3cFCoEFIPSnoopingVLANIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingVLANIndex = _Hh3cFCoEFIPSnoopingVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 1),
    _Hh3cFCoEFIPSnoopingVLANIndex_Type()
)
hh3cFCoEFIPSnoopingVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVLANIndex.setStatus("current")


class _Hh3cFCoEFIPSnoopingEnable_Type(TruthValue):
    """Custom type hh3cFCoEFIPSnoopingEnable based on TruthValue"""
    defaultValue = 2


_Hh3cFCoEFIPSnoopingEnable_Type.__name__ = "TruthValue"
_Hh3cFCoEFIPSnoopingEnable_Object = MibTableColumn
hh3cFCoEFIPSnoopingEnable = _Hh3cFCoEFIPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 2),
    _Hh3cFCoEFIPSnoopingEnable_Type()
)
hh3cFCoEFIPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingEnable.setStatus("current")


class _Hh3cFCoEFIPSnoopingFcmap_Type(OctetString):
    """Custom type hh3cFCoEFIPSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Hh3cFCoEFIPSnoopingFcmap_Type.__name__ = "OctetString"
_Hh3cFCoEFIPSnoopingFcmap_Object = MibTableColumn
hh3cFCoEFIPSnoopingFcmap = _Hh3cFCoEFIPSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 3),
    _Hh3cFCoEFIPSnoopingFcmap_Type()
)
hh3cFCoEFIPSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFcmap.setStatus("current")
_Hh3cFCoEVlanCfgTable_Object = MibTable
hh3cFCoEVlanCfgTable = _Hh3cFCoEVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgTable.setStatus("current")
_Hh3cFCoEVlanCfgEntry_Object = MibTableRow
hh3cFCoEVlanCfgEntry = _Hh3cFCoEVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5, 1)
)
hh3cFCoEVlanCfgEntry.setIndexNames(
    (0, "HH3C-FCOE-MIB", "hh3cFCoEVLANIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgEntry.setStatus("current")


class _Hh3cFCoEVlanCfgFcmap_Type(OctetString):
    """Custom type hh3cFCoEVlanCfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Hh3cFCoEVlanCfgFcmap_Type.__name__ = "OctetString"
_Hh3cFCoEVlanCfgFcmap_Object = MibTableColumn
hh3cFCoEVlanCfgFcmap = _Hh3cFCoEVlanCfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5, 1, 1),
    _Hh3cFCoEVlanCfgFcmap_Type()
)
hh3cFCoEVlanCfgFcmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgFcmap.setStatus("current")


class _Hh3cFCoEVlanCfgFCFPriority_Type(Unsigned32):
    """Custom type hh3cFCoEVlanCfgFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cFCoEVlanCfgFCFPriority_Type.__name__ = "Unsigned32"
_Hh3cFCoEVlanCfgFCFPriority_Object = MibTableColumn
hh3cFCoEVlanCfgFCFPriority = _Hh3cFCoEVlanCfgFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5, 1, 2),
    _Hh3cFCoEVlanCfgFCFPriority_Type()
)
hh3cFCoEVlanCfgFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgFCFPriority.setStatus("current")


class _Hh3cFCoEVlanCfgDATov_Type(Unsigned32):
    """Custom type hh3cFCoEVlanCfgDATov based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 600),
    )


_Hh3cFCoEVlanCfgDATov_Type.__name__ = "Unsigned32"
_Hh3cFCoEVlanCfgDATov_Object = MibTableColumn
hh3cFCoEVlanCfgDATov = _Hh3cFCoEVlanCfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5, 1, 3),
    _Hh3cFCoEVlanCfgDATov_Type()
)
hh3cFCoEVlanCfgDATov.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgDATov.setUnits("seconds")
_Hh3cFCoEVlanCfgRowStatus_Type = RowStatus
_Hh3cFCoEVlanCfgRowStatus_Object = MibTableColumn
hh3cFCoEVlanCfgRowStatus = _Hh3cFCoEVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 5, 1, 4),
    _Hh3cFCoEVlanCfgRowStatus_Type()
)
hh3cFCoEVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVlanCfgRowStatus.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFTable_Object = MibTable
hh3cFCoEFIPSnoopingFCFTable = _Hh3cFCoEFIPSnoopingFCFTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFTable.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingFCFEntry = _Hh3cFCoEFIPSnoopingFCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1)
)
hh3cFCoEFIPSnoopingFCFEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingFCFVLANIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingFCFIfIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingFCFMAC"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFVLANIndex_Type = VlanIndex
_Hh3cFCoEFIPSnoopingFCFVLANIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFVLANIndex = _Hh3cFCoEFIPSnoopingFCFVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 1),
    _Hh3cFCoEFIPSnoopingFCFVLANIndex_Type()
)
hh3cFCoEFIPSnoopingFCFVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFVLANIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFIfIndex_Type = InterfaceIndex
_Hh3cFCoEFIPSnoopingFCFIfIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFIfIndex = _Hh3cFCoEFIPSnoopingFCFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 2),
    _Hh3cFCoEFIPSnoopingFCFIfIndex_Type()
)
hh3cFCoEFIPSnoopingFCFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFIfIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFMAC_Type = MacAddress
_Hh3cFCoEFIPSnoopingFCFMAC_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFMAC = _Hh3cFCoEFIPSnoopingFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 3),
    _Hh3cFCoEFIPSnoopingFCFMAC_Type()
)
hh3cFCoEFIPSnoopingFCFMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFMAC.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFSwitchName_Type = Hh3cFcNameId
_Hh3cFCoEFIPSnoopingFCFSwitchName_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFSwitchName = _Hh3cFCoEFIPSnoopingFCFSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 4),
    _Hh3cFCoEFIPSnoopingFCFSwitchName_Type()
)
hh3cFCoEFIPSnoopingFCFSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFSwitchName.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFFabricName_Type = Hh3cFcNameId
_Hh3cFCoEFIPSnoopingFCFFabricName_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFFabricName = _Hh3cFCoEFIPSnoopingFCFFabricName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 5),
    _Hh3cFCoEFIPSnoopingFCFFabricName_Type()
)
hh3cFCoEFIPSnoopingFCFFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFFabricName.setStatus("current")
_Hh3cFCoEFIPSnoopingFCFENodeCount_Type = Unsigned32
_Hh3cFCoEFIPSnoopingFCFENodeCount_Object = MibTableColumn
hh3cFCoEFIPSnoopingFCFENodeCount = _Hh3cFCoEFIPSnoopingFCFENodeCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 6, 1, 6),
    _Hh3cFCoEFIPSnoopingFCFENodeCount_Type()
)
hh3cFCoEFIPSnoopingFCFENodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFCFENodeCount.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeTable_Object = MibTable
hh3cFCoEFIPSnoopingENodeTable = _Hh3cFCoEFIPSnoopingENodeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeTable.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingENodeEntry = _Hh3cFCoEFIPSnoopingENodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7, 1)
)
hh3cFCoEFIPSnoopingENodeEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingENodeVLANIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingENodeIfIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingENodeMAC"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeVLANIndex_Type = VlanIndex
_Hh3cFCoEFIPSnoopingENodeVLANIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingENodeVLANIndex = _Hh3cFCoEFIPSnoopingENodeVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7, 1, 1),
    _Hh3cFCoEFIPSnoopingENodeVLANIndex_Type()
)
hh3cFCoEFIPSnoopingENodeVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeVLANIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeIfIndex_Type = InterfaceIndex
_Hh3cFCoEFIPSnoopingENodeIfIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingENodeIfIndex = _Hh3cFCoEFIPSnoopingENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7, 1, 2),
    _Hh3cFCoEFIPSnoopingENodeIfIndex_Type()
)
hh3cFCoEFIPSnoopingENodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeIfIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeMAC_Type = MacAddress
_Hh3cFCoEFIPSnoopingENodeMAC_Object = MibTableColumn
hh3cFCoEFIPSnoopingENodeMAC = _Hh3cFCoEFIPSnoopingENodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7, 1, 3),
    _Hh3cFCoEFIPSnoopingENodeMAC_Type()
)
hh3cFCoEFIPSnoopingENodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeMAC.setStatus("current")
_Hh3cFCoEFIPSnoopingENodeName_Type = Hh3cFcNameId
_Hh3cFCoEFIPSnoopingENodeName_Object = MibTableColumn
hh3cFCoEFIPSnoopingENodeName = _Hh3cFCoEFIPSnoopingENodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 7, 1, 4),
    _Hh3cFCoEFIPSnoopingENodeName_Type()
)
hh3cFCoEFIPSnoopingENodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingENodeName.setStatus("current")
_Hh3cFCoEFIPSnoopingVNTable_Object = MibTable
hh3cFCoEFIPSnoopingVNTable = _Hh3cFCoEFIPSnoopingVNTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNTable.setStatus("current")
_Hh3cFCoEFIPSnoopingVNEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingVNEntry = _Hh3cFCoEFIPSnoopingVNEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1)
)
hh3cFCoEFIPSnoopingVNEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVNVLANIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVNENodeIfIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVNENodeMAC"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVNFCFMAC"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVNMAC"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingVNVLANIndex_Type = VlanIndex
_Hh3cFCoEFIPSnoopingVNVLANIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNVLANIndex = _Hh3cFCoEFIPSnoopingVNVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 1),
    _Hh3cFCoEFIPSnoopingVNVLANIndex_Type()
)
hh3cFCoEFIPSnoopingVNVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNVLANIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingVNENodeIfIndex_Type = InterfaceIndex
_Hh3cFCoEFIPSnoopingVNENodeIfIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNENodeIfIndex = _Hh3cFCoEFIPSnoopingVNENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 2),
    _Hh3cFCoEFIPSnoopingVNENodeIfIndex_Type()
)
hh3cFCoEFIPSnoopingVNENodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNENodeIfIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingVNENodeMAC_Type = MacAddress
_Hh3cFCoEFIPSnoopingVNENodeMAC_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNENodeMAC = _Hh3cFCoEFIPSnoopingVNENodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 3),
    _Hh3cFCoEFIPSnoopingVNENodeMAC_Type()
)
hh3cFCoEFIPSnoopingVNENodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNENodeMAC.setStatus("current")
_Hh3cFCoEFIPSnoopingVNFCFMAC_Type = MacAddress
_Hh3cFCoEFIPSnoopingVNFCFMAC_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNFCFMAC = _Hh3cFCoEFIPSnoopingVNFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 4),
    _Hh3cFCoEFIPSnoopingVNFCFMAC_Type()
)
hh3cFCoEFIPSnoopingVNFCFMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNFCFMAC.setStatus("current")
_Hh3cFCoEFIPSnoopingVNMAC_Type = MacAddress
_Hh3cFCoEFIPSnoopingVNMAC_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNMAC = _Hh3cFCoEFIPSnoopingVNMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 5),
    _Hh3cFCoEFIPSnoopingVNMAC_Type()
)
hh3cFCoEFIPSnoopingVNMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNMAC.setStatus("current")
_Hh3cFCoEFIPSnoopingVNName_Type = Hh3cFcNameId
_Hh3cFCoEFIPSnoopingVNName_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNName = _Hh3cFCoEFIPSnoopingVNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 6),
    _Hh3cFCoEFIPSnoopingVNName_Type()
)
hh3cFCoEFIPSnoopingVNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNName.setStatus("current")
_Hh3cFCoEFIPSnoopingVNFCFIfIndex_Type = InterfaceIndex
_Hh3cFCoEFIPSnoopingVNFCFIfIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingVNFCFIfIndex = _Hh3cFCoEFIPSnoopingVNFCFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 8, 1, 7),
    _Hh3cFCoEFIPSnoopingVNFCFIfIndex_Type()
)
hh3cFCoEFIPSnoopingVNFCFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVNFCFIfIndex.setStatus("current")
_Hh3cFCoEFIPSnoopingIfCfgTable_Object = MibTable
hh3cFCoEFIPSnoopingIfCfgTable = _Hh3cFCoEFIPSnoopingIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingIfCfgTable.setStatus("current")
_Hh3cFCoEFIPSnoopingIfCfgEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingIfCfgEntry = _Hh3cFCoEFIPSnoopingIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 9, 1)
)
hh3cFCoEFIPSnoopingIfCfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingIfCfgEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingIfCfgIfIndex_Type = InterfaceIndex
_Hh3cFCoEFIPSnoopingIfCfgIfIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingIfCfgIfIndex = _Hh3cFCoEFIPSnoopingIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 9, 1, 1),
    _Hh3cFCoEFIPSnoopingIfCfgIfIndex_Type()
)
hh3cFCoEFIPSnoopingIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingIfCfgIfIndex.setStatus("current")


class _Hh3cFCoEFIPSnoopingIfCfgPortType_Type(Integer32):
    """Custom type hh3cFCoEFIPSnoopingIfCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcf", 1),
          ("enode", 2))
    )


_Hh3cFCoEFIPSnoopingIfCfgPortType_Type.__name__ = "Integer32"
_Hh3cFCoEFIPSnoopingIfCfgPortType_Object = MibTableColumn
hh3cFCoEFIPSnoopingIfCfgPortType = _Hh3cFCoEFIPSnoopingIfCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 9, 1, 2),
    _Hh3cFCoEFIPSnoopingIfCfgPortType_Type()
)
hh3cFCoEFIPSnoopingIfCfgPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingIfCfgPortType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FCOE-MIB",
    **{"Hh3cFCoEVfcBindType": Hh3cFCoEVfcBindType,
       "hh3cFCoE": hh3cFCoE,
       "hh3cFCoEObjects": hh3cFCoEObjects,
       "hh3cFCoEConfig": hh3cFCoEConfig,
       "hh3cFCoECfgTable": hh3cFCoECfgTable,
       "hh3cFCoECfgEntry": hh3cFCoECfgEntry,
       "hh3cFCoECfgFcmap": hh3cFCoECfgFcmap,
       "hh3cFCoECfgDynamicVfcCreation": hh3cFCoECfgDynamicVfcCreation,
       "hh3cFCoECfgDefaultFCFPriority": hh3cFCoECfgDefaultFCFPriority,
       "hh3cFCoECfgDATov": hh3cFCoECfgDATov,
       "hh3cFCoECfgAddressingMode": hh3cFCoECfgAddressingMode,
       "hh3cFCoEVLANTable": hh3cFCoEVLANTable,
       "hh3cFCoEVLANEntry": hh3cFCoEVLANEntry,
       "hh3cFCoEVLANIndex": hh3cFCoEVLANIndex,
       "hh3cFCoEFabricIndex": hh3cFCoEFabricIndex,
       "hh3cFCoEVLANOperState": hh3cFCoEVLANOperState,
       "hh3cFCoEVLANRowStatus": hh3cFCoEVLANRowStatus,
       "hh3cFCoEStaticVfcTable": hh3cFCoEStaticVfcTable,
       "hh3cFCoEStaticVfcEntry": hh3cFCoEStaticVfcEntry,
       "hh3cFCoEStaticVfcIndex": hh3cFCoEStaticVfcIndex,
       "hh3cFCoEStaticVfcFCFPriority": hh3cFCoEStaticVfcFCFPriority,
       "hh3cFCoEStaticVfcBindType": hh3cFCoEStaticVfcBindType,
       "hh3cFCoEStaticVfcBindIfIndex": hh3cFCoEStaticVfcBindIfIndex,
       "hh3cFCoEStaticVfcBindMACAddress": hh3cFCoEStaticVfcBindMACAddress,
       "hh3cFCoEStaticVfcIfIndex": hh3cFCoEStaticVfcIfIndex,
       "hh3cFCoEStaticVfcCreationTime": hh3cFCoEStaticVfcCreationTime,
       "hh3cFCoEStaticVfcFailureCause": hh3cFCoEStaticVfcFailureCause,
       "hh3cFCoEStaticVfcRowStatus": hh3cFCoEStaticVfcRowStatus,
       "hh3cFCoEFIPSnoopingTable": hh3cFCoEFIPSnoopingTable,
       "hh3cFCoEFIPSnoopingEntry": hh3cFCoEFIPSnoopingEntry,
       "hh3cFCoEFIPSnoopingVLANIndex": hh3cFCoEFIPSnoopingVLANIndex,
       "hh3cFCoEFIPSnoopingEnable": hh3cFCoEFIPSnoopingEnable,
       "hh3cFCoEFIPSnoopingFcmap": hh3cFCoEFIPSnoopingFcmap,
       "hh3cFCoEVlanCfgTable": hh3cFCoEVlanCfgTable,
       "hh3cFCoEVlanCfgEntry": hh3cFCoEVlanCfgEntry,
       "hh3cFCoEVlanCfgFcmap": hh3cFCoEVlanCfgFcmap,
       "hh3cFCoEVlanCfgFCFPriority": hh3cFCoEVlanCfgFCFPriority,
       "hh3cFCoEVlanCfgDATov": hh3cFCoEVlanCfgDATov,
       "hh3cFCoEVlanCfgRowStatus": hh3cFCoEVlanCfgRowStatus,
       "hh3cFCoEFIPSnoopingFCFTable": hh3cFCoEFIPSnoopingFCFTable,
       "hh3cFCoEFIPSnoopingFCFEntry": hh3cFCoEFIPSnoopingFCFEntry,
       "hh3cFCoEFIPSnoopingFCFVLANIndex": hh3cFCoEFIPSnoopingFCFVLANIndex,
       "hh3cFCoEFIPSnoopingFCFIfIndex": hh3cFCoEFIPSnoopingFCFIfIndex,
       "hh3cFCoEFIPSnoopingFCFMAC": hh3cFCoEFIPSnoopingFCFMAC,
       "hh3cFCoEFIPSnoopingFCFSwitchName": hh3cFCoEFIPSnoopingFCFSwitchName,
       "hh3cFCoEFIPSnoopingFCFFabricName": hh3cFCoEFIPSnoopingFCFFabricName,
       "hh3cFCoEFIPSnoopingFCFENodeCount": hh3cFCoEFIPSnoopingFCFENodeCount,
       "hh3cFCoEFIPSnoopingENodeTable": hh3cFCoEFIPSnoopingENodeTable,
       "hh3cFCoEFIPSnoopingENodeEntry": hh3cFCoEFIPSnoopingENodeEntry,
       "hh3cFCoEFIPSnoopingENodeVLANIndex": hh3cFCoEFIPSnoopingENodeVLANIndex,
       "hh3cFCoEFIPSnoopingENodeIfIndex": hh3cFCoEFIPSnoopingENodeIfIndex,
       "hh3cFCoEFIPSnoopingENodeMAC": hh3cFCoEFIPSnoopingENodeMAC,
       "hh3cFCoEFIPSnoopingENodeName": hh3cFCoEFIPSnoopingENodeName,
       "hh3cFCoEFIPSnoopingVNTable": hh3cFCoEFIPSnoopingVNTable,
       "hh3cFCoEFIPSnoopingVNEntry": hh3cFCoEFIPSnoopingVNEntry,
       "hh3cFCoEFIPSnoopingVNVLANIndex": hh3cFCoEFIPSnoopingVNVLANIndex,
       "hh3cFCoEFIPSnoopingVNENodeIfIndex": hh3cFCoEFIPSnoopingVNENodeIfIndex,
       "hh3cFCoEFIPSnoopingVNENodeMAC": hh3cFCoEFIPSnoopingVNENodeMAC,
       "hh3cFCoEFIPSnoopingVNFCFMAC": hh3cFCoEFIPSnoopingVNFCFMAC,
       "hh3cFCoEFIPSnoopingVNMAC": hh3cFCoEFIPSnoopingVNMAC,
       "hh3cFCoEFIPSnoopingVNName": hh3cFCoEFIPSnoopingVNName,
       "hh3cFCoEFIPSnoopingVNFCFIfIndex": hh3cFCoEFIPSnoopingVNFCFIfIndex,
       "hh3cFCoEFIPSnoopingIfCfgTable": hh3cFCoEFIPSnoopingIfCfgTable,
       "hh3cFCoEFIPSnoopingIfCfgEntry": hh3cFCoEFIPSnoopingIfCfgEntry,
       "hh3cFCoEFIPSnoopingIfCfgIfIndex": hh3cFCoEFIPSnoopingIfCfgIfIndex,
       "hh3cFCoEFIPSnoopingIfCfgPortType": hh3cFCoEFIPSnoopingIfCfgPortType}
)
