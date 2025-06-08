# SNMP MIB module (CISCOSB-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-STACK-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:13:29 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107)
)
if mibBuilder.loadTexts:
    rlStack.setRevisions(
        ("2005-04-14 00:00",)
    )


# Types definitions



class StackMode(Integer32):
    """Custom type StackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("native", 2),
          ("basic-hybrid", 3),
          ("advanced-hybrid", 4),
          ("advanced-hybrid-XG", 5))
    )





class PortsPair(Integer32):
    """Custom type PortsPair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pair-s1s2", 1),
          ("pair-s3s4", 2),
          ("pair-s1s25G", 3),
          ("pair-s1s2Xg", 4),
          ("pair-lionXg", 5),
          ("pair-s1s2-xg1xg2-Xg", 6))
    )





class HybridStackPortSpeed(Integer32):
    """Custom type HybridStackPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("port-speed-1G", 1),
          ("port-speed-5G", 2),
          ("port-speed-10G", 3),
          ("port-speed-auto", 4),
          ("port-speed-down", 5))
    )





class HybridStackDeviceMode(Integer32):
    """Custom type HybridStackDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode-L2", 1),
          ("mode-L3", 2))
    )





class UnitModuleType(Integer32):
    """Custom type UnitModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unit-Sx500", 1),
          ("unit-SG500X", 2),
          ("unit-SG500XG", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStackActiveUnitIdTable_Object = MibTable
rlStackActiveUnitIdTable = _RlStackActiveUnitIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1)
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdTable.setStatus("current")
_RlStackActiveUnitIdEntry_Object = MibTableRow
rlStackActiveUnitIdEntry = _RlStackActiveUnitIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1)
)
rlStackActiveUnitIdEntry.setIndexNames(
    (0, "CISCOSB-STACK-MIB", "rlStackCurrentUnitId"),
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdEntry.setStatus("current")
_RlStackCurrentUnitId_Type = Integer32
_RlStackCurrentUnitId_Object = MibTableColumn
rlStackCurrentUnitId = _RlStackCurrentUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 1),
    _RlStackCurrentUnitId_Type()
)
rlStackCurrentUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlStackCurrentUnitId.setStatus("current")


class _RlStackActiveUnitIdAfterReset_Type(Integer32):
    """Custom type rlStackActiveUnitIdAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlStackActiveUnitIdAfterReset_Type.__name__ = "Integer32"
_RlStackActiveUnitIdAfterReset_Object = MibTableColumn
rlStackActiveUnitIdAfterReset = _RlStackActiveUnitIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 2),
    _RlStackActiveUnitIdAfterReset_Type()
)
rlStackActiveUnitIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackActiveUnitIdAfterReset.setStatus("current")


class _RlStackUnitModeAfterReset_Type(Integer32):
    """Custom type rlStackUnitModeAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("stack", 2))
    )


_RlStackUnitModeAfterReset_Type.__name__ = "Integer32"
_RlStackUnitModeAfterReset_Object = MibScalar
rlStackUnitModeAfterReset = _RlStackUnitModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 2),
    _RlStackUnitModeAfterReset_Type()
)
rlStackUnitModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitModeAfterReset.setStatus("current")


class _RlStackUnitMode_Type(Integer32):
    """Custom type rlStackUnitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("stack", 2))
    )


_RlStackUnitMode_Type.__name__ = "Integer32"
_RlStackUnitMode_Object = MibScalar
rlStackUnitMode = _RlStackUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 3),
    _RlStackUnitMode_Type()
)
rlStackUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackUnitMode.setStatus("current")
_RlStackUnitMacAddressAfterReset_Type = MacAddress
_RlStackUnitMacAddressAfterReset_Object = MibScalar
rlStackUnitMacAddressAfterReset = _RlStackUnitMacAddressAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 4),
    _RlStackUnitMacAddressAfterReset_Type()
)
rlStackUnitMacAddressAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitMacAddressAfterReset.setStatus("current")
_RlStackHybridTable_Object = MibTable
rlStackHybridTable = _RlStackHybridTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5)
)
if mibBuilder.loadTexts:
    rlStackHybridTable.setStatus("current")
_RlStackHybridEntry_Object = MibTableRow
rlStackHybridEntry = _RlStackHybridEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1)
)
rlStackHybridEntry.setIndexNames(
    (0, "CISCOSB-STACK-MIB", "rlStackHybridUnitId"),
)
if mibBuilder.loadTexts:
    rlStackHybridEntry.setStatus("current")


class _RlStackHybridUnitId_Type(Integer32):
    """Custom type rlStackHybridUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlStackHybridUnitId_Type.__name__ = "Integer32"
_RlStackHybridUnitId_Object = MibTableColumn
rlStackHybridUnitId = _RlStackHybridUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 1),
    _RlStackHybridUnitId_Type()
)
rlStackHybridUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlStackHybridUnitId.setStatus("current")
_RlStackHybridStackMode_Type = StackMode
_RlStackHybridStackMode_Object = MibTableColumn
rlStackHybridStackMode = _RlStackHybridStackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 2),
    _RlStackHybridStackMode_Type()
)
rlStackHybridStackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridStackMode.setStatus("current")
_RlStackHybridPortsPair_Type = PortsPair
_RlStackHybridPortsPair_Object = MibTableColumn
rlStackHybridPortsPair = _RlStackHybridPortsPair_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 3),
    _RlStackHybridPortsPair_Type()
)
rlStackHybridPortsPair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortsPair.setStatus("current")
_RlStackHybridPortNo1speedDeprecated_Type = HybridStackPortSpeed
_RlStackHybridPortNo1speedDeprecated_Object = MibTableColumn
rlStackHybridPortNo1speedDeprecated = _RlStackHybridPortNo1speedDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 4),
    _RlStackHybridPortNo1speedDeprecated_Type()
)
rlStackHybridPortNo1speedDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortNo1speedDeprecated.setStatus("current")
_RlStackHybridPortNo2speedDeprecated_Type = HybridStackPortSpeed
_RlStackHybridPortNo2speedDeprecated_Object = MibTableColumn
rlStackHybridPortNo2speedDeprecated = _RlStackHybridPortNo2speedDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 5),
    _RlStackHybridPortNo2speedDeprecated_Type()
)
rlStackHybridPortNo2speedDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortNo2speedDeprecated.setStatus("current")


class _RlStackHybridUnitIdAfterReset_Type(Integer32):
    """Custom type rlStackHybridUnitIdAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RlStackHybridUnitIdAfterReset_Type.__name__ = "Integer32"
_RlStackHybridUnitIdAfterReset_Object = MibTableColumn
rlStackHybridUnitIdAfterReset = _RlStackHybridUnitIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 6),
    _RlStackHybridUnitIdAfterReset_Type()
)
rlStackHybridUnitIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridUnitIdAfterReset.setStatus("current")
_RlStackHybridStackModeAfterReset_Type = StackMode
_RlStackHybridStackModeAfterReset_Object = MibTableColumn
rlStackHybridStackModeAfterReset = _RlStackHybridStackModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 7),
    _RlStackHybridStackModeAfterReset_Type()
)
rlStackHybridStackModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridStackModeAfterReset.setStatus("current")
_RlStackHybridPortsPairAfterReset_Type = PortsPair
_RlStackHybridPortsPairAfterReset_Object = MibTableColumn
rlStackHybridPortsPairAfterReset = _RlStackHybridPortsPairAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 8),
    _RlStackHybridPortsPairAfterReset_Type()
)
rlStackHybridPortsPairAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortsPairAfterReset.setStatus("current")
_RlStackHybridPortNo1speedAfterResetDeprecated_Type = HybridStackPortSpeed
_RlStackHybridPortNo1speedAfterResetDeprecated_Object = MibTableColumn
rlStackHybridPortNo1speedAfterResetDeprecated = _RlStackHybridPortNo1speedAfterResetDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 9),
    _RlStackHybridPortNo1speedAfterResetDeprecated_Type()
)
rlStackHybridPortNo1speedAfterResetDeprecated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortNo1speedAfterResetDeprecated.setStatus("current")
_RlStackHybridPortNo2speedAfterResetDeprecated_Type = HybridStackPortSpeed
_RlStackHybridPortNo2speedAfterResetDeprecated_Object = MibTableColumn
rlStackHybridPortNo2speedAfterResetDeprecated = _RlStackHybridPortNo2speedAfterResetDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 10),
    _RlStackHybridPortNo2speedAfterResetDeprecated_Type()
)
rlStackHybridPortNo2speedAfterResetDeprecated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortNo2speedAfterResetDeprecated.setStatus("current")
_RlStackHybridDeleteStartupAfterResetDeprecated_Type = TruthValue
_RlStackHybridDeleteStartupAfterResetDeprecated_Object = MibTableColumn
rlStackHybridDeleteStartupAfterResetDeprecated = _RlStackHybridDeleteStartupAfterResetDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 11),
    _RlStackHybridDeleteStartupAfterResetDeprecated_Type()
)
rlStackHybridDeleteStartupAfterResetDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridDeleteStartupAfterResetDeprecated.setStatus("current")
_RlStackHybridDeviceModeAfterReset_Type = HybridStackDeviceMode
_RlStackHybridDeviceModeAfterReset_Object = MibTableColumn
rlStackHybridDeviceModeAfterReset = _RlStackHybridDeviceModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 12),
    _RlStackHybridDeviceModeAfterReset_Type()
)
rlStackHybridDeviceModeAfterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridDeviceModeAfterReset.setStatus("current")
_RlStackHybridXgPortNo1NumDeprecated_Type = Integer32
_RlStackHybridXgPortNo1NumDeprecated_Object = MibTableColumn
rlStackHybridXgPortNo1NumDeprecated = _RlStackHybridXgPortNo1NumDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 13),
    _RlStackHybridXgPortNo1NumDeprecated_Type()
)
rlStackHybridXgPortNo1NumDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo1NumDeprecated.setStatus("current")
_RlStackHybridXgPortNo1NumAfterResetDeprecated_Type = Integer32
_RlStackHybridXgPortNo1NumAfterResetDeprecated_Object = MibTableColumn
rlStackHybridXgPortNo1NumAfterResetDeprecated = _RlStackHybridXgPortNo1NumAfterResetDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 14),
    _RlStackHybridXgPortNo1NumAfterResetDeprecated_Type()
)
rlStackHybridXgPortNo1NumAfterResetDeprecated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo1NumAfterResetDeprecated.setStatus("current")
_RlStackHybridXgPortNo2NumDeprecated_Type = Integer32
_RlStackHybridXgPortNo2NumDeprecated_Object = MibTableColumn
rlStackHybridXgPortNo2NumDeprecated = _RlStackHybridXgPortNo2NumDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 15),
    _RlStackHybridXgPortNo2NumDeprecated_Type()
)
rlStackHybridXgPortNo2NumDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo2NumDeprecated.setStatus("current")
_RlStackHybridXgPortNo2NumAfterResetDeprecated_Type = Integer32
_RlStackHybridXgPortNo2NumAfterResetDeprecated_Object = MibTableColumn
rlStackHybridXgPortNo2NumAfterResetDeprecated = _RlStackHybridXgPortNo2NumAfterResetDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 16),
    _RlStackHybridXgPortNo2NumAfterResetDeprecated_Type()
)
rlStackHybridXgPortNo2NumAfterResetDeprecated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo2NumAfterResetDeprecated.setStatus("current")
_RlStackHybridPortSpeed_Type = HybridStackPortSpeed
_RlStackHybridPortSpeed_Object = MibTableColumn
rlStackHybridPortSpeed = _RlStackHybridPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 17),
    _RlStackHybridPortSpeed_Type()
)
rlStackHybridPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortSpeed.setStatus("current")
_RlStackHybridPortSpeedAfterReset_Type = HybridStackPortSpeed
_RlStackHybridPortSpeedAfterReset_Object = MibTableColumn
rlStackHybridPortSpeedAfterReset = _RlStackHybridPortSpeedAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 18),
    _RlStackHybridPortSpeedAfterReset_Type()
)
rlStackHybridPortSpeedAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortSpeedAfterReset.setStatus("current")


class _RlStackHybridXgPortList_Type(OctetString):
    """Custom type rlStackHybridXgPortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_RlStackHybridXgPortList_Type.__name__ = "OctetString"
_RlStackHybridXgPortList_Object = MibTableColumn
rlStackHybridXgPortList = _RlStackHybridXgPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 19),
    _RlStackHybridXgPortList_Type()
)
rlStackHybridXgPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridXgPortList.setStatus("current")


class _RlStackHybridXgPortListAfterReset_Type(OctetString):
    """Custom type rlStackHybridXgPortListAfterReset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_RlStackHybridXgPortListAfterReset_Type.__name__ = "OctetString"
_RlStackHybridXgPortListAfterReset_Object = MibTableColumn
rlStackHybridXgPortListAfterReset = _RlStackHybridXgPortListAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 20),
    _RlStackHybridXgPortListAfterReset_Type()
)
rlStackHybridXgPortListAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridXgPortListAfterReset.setStatus("current")
_RlStackHybridUnitModuleType_Type = UnitModuleType
_RlStackHybridUnitModuleType_Object = MibTableColumn
rlStackHybridUnitModuleType = _RlStackHybridUnitModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 21),
    _RlStackHybridUnitModuleType_Type()
)
rlStackHybridUnitModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridUnitModuleType.setStatus("current")
_RlStackHybridMibVersion_Type = Integer32
_RlStackHybridMibVersion_Object = MibTableColumn
rlStackHybridMibVersion = _RlStackHybridMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 22),
    _RlStackHybridMibVersion_Type()
)
rlStackHybridMibVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridMibVersion.setStatus("current")


class _RlStackTopology_Type(Integer32):
    """Custom type rlStackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("topology-chain", 1),
          ("topology-ring", 2),
          ("topology-star", 3))
    )


_RlStackTopology_Type.__name__ = "Integer32"
_RlStackTopology_Object = MibScalar
rlStackTopology = _RlStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 6),
    _RlStackTopology_Type()
)
rlStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackTopology.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-STACK-MIB",
    **{"StackMode": StackMode,
       "PortsPair": PortsPair,
       "HybridStackPortSpeed": HybridStackPortSpeed,
       "HybridStackDeviceMode": HybridStackDeviceMode,
       "UnitModuleType": UnitModuleType,
       "rlStack": rlStack,
       "rlStackActiveUnitIdTable": rlStackActiveUnitIdTable,
       "rlStackActiveUnitIdEntry": rlStackActiveUnitIdEntry,
       "rlStackCurrentUnitId": rlStackCurrentUnitId,
       "rlStackActiveUnitIdAfterReset": rlStackActiveUnitIdAfterReset,
       "rlStackUnitModeAfterReset": rlStackUnitModeAfterReset,
       "rlStackUnitMode": rlStackUnitMode,
       "rlStackUnitMacAddressAfterReset": rlStackUnitMacAddressAfterReset,
       "rlStackHybridTable": rlStackHybridTable,
       "rlStackHybridEntry": rlStackHybridEntry,
       "rlStackHybridUnitId": rlStackHybridUnitId,
       "rlStackHybridStackMode": rlStackHybridStackMode,
       "rlStackHybridPortsPair": rlStackHybridPortsPair,
       "rlStackHybridPortNo1speedDeprecated": rlStackHybridPortNo1speedDeprecated,
       "rlStackHybridPortNo2speedDeprecated": rlStackHybridPortNo2speedDeprecated,
       "rlStackHybridUnitIdAfterReset": rlStackHybridUnitIdAfterReset,
       "rlStackHybridStackModeAfterReset": rlStackHybridStackModeAfterReset,
       "rlStackHybridPortsPairAfterReset": rlStackHybridPortsPairAfterReset,
       "rlStackHybridPortNo1speedAfterResetDeprecated": rlStackHybridPortNo1speedAfterResetDeprecated,
       "rlStackHybridPortNo2speedAfterResetDeprecated": rlStackHybridPortNo2speedAfterResetDeprecated,
       "rlStackHybridDeleteStartupAfterResetDeprecated": rlStackHybridDeleteStartupAfterResetDeprecated,
       "rlStackHybridDeviceModeAfterReset": rlStackHybridDeviceModeAfterReset,
       "rlStackHybridXgPortNo1NumDeprecated": rlStackHybridXgPortNo1NumDeprecated,
       "rlStackHybridXgPortNo1NumAfterResetDeprecated": rlStackHybridXgPortNo1NumAfterResetDeprecated,
       "rlStackHybridXgPortNo2NumDeprecated": rlStackHybridXgPortNo2NumDeprecated,
       "rlStackHybridXgPortNo2NumAfterResetDeprecated": rlStackHybridXgPortNo2NumAfterResetDeprecated,
       "rlStackHybridPortSpeed": rlStackHybridPortSpeed,
       "rlStackHybridPortSpeedAfterReset": rlStackHybridPortSpeedAfterReset,
       "rlStackHybridXgPortList": rlStackHybridXgPortList,
       "rlStackHybridXgPortListAfterReset": rlStackHybridXgPortListAfterReset,
       "rlStackHybridUnitModuleType": rlStackHybridUnitModuleType,
       "rlStackHybridMibVersion": rlStackHybridMibVersion,
       "rlStackTopology": rlStackTopology}
)
