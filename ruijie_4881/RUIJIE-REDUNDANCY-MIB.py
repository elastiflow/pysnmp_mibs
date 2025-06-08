# SNMP MIB module (RUIJIE-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-REDUNDANCY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34)
)
if mibBuilder.loadTexts:
    ruijieRedundancyMIB.setRevisions(
        ("2003-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRedundancyMIBObjects = _RuijieRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 1)
)
_RuijieRedundancyForceSwitchover_Type = Integer32
_RuijieRedundancyForceSwitchover_Object = MibScalar
ruijieRedundancyForceSwitchover = _RuijieRedundancyForceSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 1, 1),
    _RuijieRedundancyForceSwitchover_Type()
)
ruijieRedundancyForceSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRedundancyForceSwitchover.setStatus("current")


class _RuijieMainCPU_Type(Integer32):
    """Custom type ruijieMainCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("increasing", 0),
          ("decreasing", 1))
    )


_RuijieMainCPU_Type.__name__ = "Integer32"
_RuijieMainCPU_Object = MibScalar
ruijieMainCPU = _RuijieMainCPU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 1, 2),
    _RuijieMainCPU_Type()
)
ruijieMainCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMainCPU.setStatus("current")
_RuijiePluggableMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePluggableMIBObjects = _RuijiePluggableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2)
)
_RuijiePluggableModuleInfoTable_Object = MibTable
ruijiePluggableModuleInfoTable = _RuijiePluggableModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiePluggableModuleInfoTable.setStatus("current")
_RuijiePluggableModuleInfoEntry_Object = MibTableRow
ruijiePluggableModuleInfoEntry = _RuijiePluggableModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1)
)
ruijiePluggableModuleInfoEntry.setIndexNames(
    (0, "RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleInfoDeviceIndex"),
    (0, "RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleInfoSlotIndex"),
)
if mibBuilder.loadTexts:
    ruijiePluggableModuleInfoEntry.setStatus("current")
_RuijiePluggableModuleInfoDeviceIndex_Type = Integer32
_RuijiePluggableModuleInfoDeviceIndex_Object = MibTableColumn
ruijiePluggableModuleInfoDeviceIndex = _RuijiePluggableModuleInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 1),
    _RuijiePluggableModuleInfoDeviceIndex_Type()
)
ruijiePluggableModuleInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleInfoDeviceIndex.setStatus("current")
_RuijiePluggableModuleInfoSlotIndex_Type = Integer32
_RuijiePluggableModuleInfoSlotIndex_Object = MibTableColumn
ruijiePluggableModuleInfoSlotIndex = _RuijiePluggableModuleInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 2),
    _RuijiePluggableModuleInfoSlotIndex_Type()
)
ruijiePluggableModuleInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleInfoSlotIndex.setStatus("current")


class _RuijiePluggableModuleStatus_Type(Integer32):
    """Custom type ruijiePluggableModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ok", 1),
          ("installed", 2),
          ("conflict", 3),
          ("removed", 4),
          ("uninstalled", 5),
          ("verIncompatible", 6),
          ("cannot-ruijieup", 7),
          ("resetting", 8),
          ("master", 9),
          ("backup", 10))
    )


_RuijiePluggableModuleStatus_Type.__name__ = "Integer32"
_RuijiePluggableModuleStatus_Object = MibTableColumn
ruijiePluggableModuleStatus = _RuijiePluggableModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 3),
    _RuijiePluggableModuleStatus_Type()
)
ruijiePluggableModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleStatus.setStatus("current")


class _RuijiePluggableModuleConfigType_Type(Integer32):
    """Custom type ruijiePluggableModuleConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("m6800-24T-4SFP-4GT", 1),
          ("m6800-32T-4SFP-GT", 2),
          ("m6800-32FMT", 3),
          ("m6800-12GB", 4),
          ("m6800-24SFP", 5),
          ("m6800-12SFP-GT", 6),
          ("m6800-1XENPAK", 7),
          ("m6800-2XENPAK", 8),
          ("m6800-MSC", 9),
          ("m6800-CM", 10),
          ("m6800-24GT-8SFP", 11))
    )


_RuijiePluggableModuleConfigType_Type.__name__ = "Integer32"
_RuijiePluggableModuleConfigType_Object = MibTableColumn
ruijiePluggableModuleConfigType = _RuijiePluggableModuleConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 4),
    _RuijiePluggableModuleConfigType_Type()
)
ruijiePluggableModuleConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePluggableModuleConfigType.setStatus("current")


class _RuijiePluggableModuleConfigSwVer_Type(DisplayString):
    """Custom type ruijiePluggableModuleConfigSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijiePluggableModuleConfigSwVer_Type.__name__ = "DisplayString"
_RuijiePluggableModuleConfigSwVer_Object = MibTableColumn
ruijiePluggableModuleConfigSwVer = _RuijiePluggableModuleConfigSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 5),
    _RuijiePluggableModuleConfigSwVer_Type()
)
ruijiePluggableModuleConfigSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleConfigSwVer.setStatus("current")


class _RuijiePluggableModuleOnlineSwVer_Type(DisplayString):
    """Custom type ruijiePluggableModuleOnlineSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijiePluggableModuleOnlineSwVer_Type.__name__ = "DisplayString"
_RuijiePluggableModuleOnlineSwVer_Object = MibTableColumn
ruijiePluggableModuleOnlineSwVer = _RuijiePluggableModuleOnlineSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 6),
    _RuijiePluggableModuleOnlineSwVer_Type()
)
ruijiePluggableModuleOnlineSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleOnlineSwVer.setStatus("current")


class _RuijiePluggableModuleConfigInfoDescr_Type(DisplayString):
    """Custom type ruijiePluggableModuleConfigInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijiePluggableModuleConfigInfoDescr_Type.__name__ = "DisplayString"
_RuijiePluggableModuleConfigInfoDescr_Object = MibTableColumn
ruijiePluggableModuleConfigInfoDescr = _RuijiePluggableModuleConfigInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 7),
    _RuijiePluggableModuleConfigInfoDescr_Type()
)
ruijiePluggableModuleConfigInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleConfigInfoDescr.setStatus("current")


class _RuijiePluggableModuleOnlineInfoDescr_Type(DisplayString):
    """Custom type ruijiePluggableModuleOnlineInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijiePluggableModuleOnlineInfoDescr_Type.__name__ = "DisplayString"
_RuijiePluggableModuleOnlineInfoDescr_Object = MibTableColumn
ruijiePluggableModuleOnlineInfoDescr = _RuijiePluggableModuleOnlineInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 8),
    _RuijiePluggableModuleOnlineInfoDescr_Type()
)
ruijiePluggableModuleOnlineInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleOnlineInfoDescr.setStatus("current")
_RuijiePluggableModuleConfigPortsNum_Type = Integer32
_RuijiePluggableModuleConfigPortsNum_Object = MibTableColumn
ruijiePluggableModuleConfigPortsNum = _RuijiePluggableModuleConfigPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 9),
    _RuijiePluggableModuleConfigPortsNum_Type()
)
ruijiePluggableModuleConfigPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleConfigPortsNum.setStatus("current")
_RuijiePluggableModuleOnlinePortsNum_Type = Integer32
_RuijiePluggableModuleOnlinePortsNum_Object = MibTableColumn
ruijiePluggableModuleOnlinePortsNum = _RuijiePluggableModuleOnlinePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 10),
    _RuijiePluggableModuleOnlinePortsNum_Type()
)
ruijiePluggableModuleOnlinePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePluggableModuleOnlinePortsNum.setStatus("current")


class _RuijiePluggableModuleAction_Type(Integer32):
    """Custom type ruijiePluggableModuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1),
          ("clearAllConf", 2),
          ("uninstall", 3))
    )


_RuijiePluggableModuleAction_Type.__name__ = "Integer32"
_RuijiePluggableModuleAction_Object = MibTableColumn
ruijiePluggableModuleAction = _RuijiePluggableModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 2, 1, 1, 11),
    _RuijiePluggableModuleAction_Type()
)
ruijiePluggableModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePluggableModuleAction.setStatus("current")
_RuijieRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
ruijieRedundancyMIBConformance = _RuijieRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 3)
)
_RuijieRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieRedundancyMIBCompliances = _RuijieRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 3, 1)
)
_RuijieRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
ruijieRedundancyMIBGroups = _RuijieRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 3, 2)
)

# Managed Objects groups

ruijieRedundancyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 3, 2, 1)
)
ruijieRedundancyMIBGroup.setObjects(
      *(("RUIJIE-REDUNDANCY-MIB", "ruijieRedundancyForceSwitchover"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijieMainCPU"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleInfoDeviceIndex"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleInfoSlotIndex"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleStatus"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleConfigType"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleConfigSwVer"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleOnlineSwVer"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleConfigInfoDescr"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleOnlineInfoDescr"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleConfigPortsNum"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleOnlinePortsNum"),
        ("RUIJIE-REDUNDANCY-MIB", "ruijiePluggableModuleAction"))
)
if mibBuilder.loadTexts:
    ruijieRedundancyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 34, 3, 1, 1)
)
ruijieRedundancyMIBCompliance.setObjects(
    ("RUIJIE-REDUNDANCY-MIB", "ruijieRedundancyMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-REDUNDANCY-MIB",
    **{"ruijieRedundancyMIB": ruijieRedundancyMIB,
       "ruijieRedundancyMIBObjects": ruijieRedundancyMIBObjects,
       "ruijieRedundancyForceSwitchover": ruijieRedundancyForceSwitchover,
       "ruijieMainCPU": ruijieMainCPU,
       "ruijiePluggableMIBObjects": ruijiePluggableMIBObjects,
       "ruijiePluggableModuleInfoTable": ruijiePluggableModuleInfoTable,
       "ruijiePluggableModuleInfoEntry": ruijiePluggableModuleInfoEntry,
       "ruijiePluggableModuleInfoDeviceIndex": ruijiePluggableModuleInfoDeviceIndex,
       "ruijiePluggableModuleInfoSlotIndex": ruijiePluggableModuleInfoSlotIndex,
       "ruijiePluggableModuleStatus": ruijiePluggableModuleStatus,
       "ruijiePluggableModuleConfigType": ruijiePluggableModuleConfigType,
       "ruijiePluggableModuleConfigSwVer": ruijiePluggableModuleConfigSwVer,
       "ruijiePluggableModuleOnlineSwVer": ruijiePluggableModuleOnlineSwVer,
       "ruijiePluggableModuleConfigInfoDescr": ruijiePluggableModuleConfigInfoDescr,
       "ruijiePluggableModuleOnlineInfoDescr": ruijiePluggableModuleOnlineInfoDescr,
       "ruijiePluggableModuleConfigPortsNum": ruijiePluggableModuleConfigPortsNum,
       "ruijiePluggableModuleOnlinePortsNum": ruijiePluggableModuleOnlinePortsNum,
       "ruijiePluggableModuleAction": ruijiePluggableModuleAction,
       "ruijieRedundancyMIBConformance": ruijieRedundancyMIBConformance,
       "ruijieRedundancyMIBCompliances": ruijieRedundancyMIBCompliances,
       "ruijieRedundancyMIBCompliance": ruijieRedundancyMIBCompliance,
       "ruijieRedundancyMIBGroups": ruijieRedundancyMIBGroups,
       "ruijieRedundancyMIBGroup": ruijieRedundancyMIBGroup}
)
