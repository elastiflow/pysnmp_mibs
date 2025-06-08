# SNMP MIB module (RUIJIE-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-POE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijiePoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110)
)
if mibBuilder.loadTexts:
    ruijiePoeMIB.setRevisions(
        ("2012-02-14 00:00",
         "2012-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePoeConfigMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePoeConfigMIBObjects = _RuijiePoeConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1)
)
_RuijieIfPoeTable_Object = MibTable
ruijieIfPoeTable = _RuijieIfPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIfPoeTable.setStatus("current")
_RuijieIfPoeEntry_Object = MibTableRow
ruijieIfPoeEntry = _RuijieIfPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1)
)
ruijieIfPoeEntry.setIndexNames(
    (0, "RUIJIE-POE-MIB", "ifPoeIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfPoeEntry.setStatus("current")


class _IfPoeIndex_Type(Integer32):
    """Custom type ifPoeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfPoeIndex_Type.__name__ = "Integer32"
_IfPoeIndex_Object = MibTableColumn
ifPoeIndex = _IfPoeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 1),
    _IfPoeIndex_Type()
)
ifPoeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoeIndex.setStatus("current")
_IfIsPoe_Type = TruthValue
_IfIsPoe_Object = MibTableColumn
ifIsPoe = _IfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 2),
    _IfIsPoe_Type()
)
ifIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIsPoe.setStatus("current")


class _IfPoeEnable_Type(Integer32):
    """Custom type ifPoeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IfPoeEnable_Type.__name__ = "Integer32"
_IfPoeEnable_Object = MibTableColumn
ifPoeEnable = _IfPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 3),
    _IfPoeEnable_Type()
)
ifPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoeEnable.setStatus("current")


class _IfPoePwrStatus_Type(Integer32):
    """Custom type ifPoePwrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IfPoePwrStatus_Type.__name__ = "Integer32"
_IfPoePwrStatus_Object = MibTableColumn
ifPoePwrStatus = _IfPoePwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 4),
    _IfPoePwrStatus_Type()
)
ifPoePwrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoePwrStatus.setStatus("current")


class _IfPoeMaxPwrSet_Type(Integer32):
    """Custom type ifPoeMaxPwrSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfPoeMaxPwrSet_Type.__name__ = "Integer32"
_IfPoeMaxPwrSet_Object = MibTableColumn
ifPoeMaxPwrSet = _IfPoeMaxPwrSet_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 5),
    _IfPoeMaxPwrSet_Type()
)
ifPoeMaxPwrSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoeMaxPwrSet.setStatus("current")


class _IfPoePriority_Type(Integer32):
    """Custom type ifPoePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_IfPoePriority_Type.__name__ = "Integer32"
_IfPoePriority_Object = MibTableColumn
ifPoePriority = _IfPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 6),
    _IfPoePriority_Type()
)
ifPoePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPoePriority.setStatus("current")
_IfPoeConsumingPwr_Type = Integer32
_IfPoeConsumingPwr_Object = MibTableColumn
ifPoeConsumingPwr = _IfPoeConsumingPwr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 7),
    _IfPoeConsumingPwr_Type()
)
ifPoeConsumingPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPoeConsumingPwr.setStatus("current")
_IfIsHPoe_Type = TruthValue
_IfIsHPoe_Object = MibTableColumn
ifIsHPoe = _IfIsHPoe_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 1, 1, 1, 8),
    _IfIsHPoe_Type()
)
ifIsHPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIsHPoe.setStatus("current")
_RuijiePoeTraps_ObjectIdentity = ObjectIdentity
ruijiePoeTraps = _RuijiePoeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 2)
)

# Managed Objects groups


# Notification objects

ifPoePowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 2, 1)
)
ifPoePowerOffTrap.setObjects(
    ("RUIJIE-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePowerOffTrap.setStatus(
        "current"
    )

ifPoePowerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 2, 2)
)
ifPoePowerOnTrap.setObjects(
    ("RUIJIE-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePowerOnTrap.setStatus(
        "current"
    )

ifPoePboxAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 110, 2, 3)
)
ifPoePboxAbnormalTrap.setObjects(
    ("RUIJIE-POE-MIB", "ifPoeIndex")
)
if mibBuilder.loadTexts:
    ifPoePboxAbnormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-POE-MIB",
    **{"ruijiePoeMIB": ruijiePoeMIB,
       "ruijiePoeConfigMIBObjects": ruijiePoeConfigMIBObjects,
       "ruijieIfPoeTable": ruijieIfPoeTable,
       "ruijieIfPoeEntry": ruijieIfPoeEntry,
       "ifPoeIndex": ifPoeIndex,
       "ifIsPoe": ifIsPoe,
       "ifPoeEnable": ifPoeEnable,
       "ifPoePwrStatus": ifPoePwrStatus,
       "ifPoeMaxPwrSet": ifPoeMaxPwrSet,
       "ifPoePriority": ifPoePriority,
       "ifPoeConsumingPwr": ifPoeConsumingPwr,
       "ifIsHPoe": ifIsHPoe,
       "ruijiePoeTraps": ruijiePoeTraps,
       "ifPoePowerOffTrap": ifPoePowerOffTrap,
       "ifPoePowerOnTrap": ifPoePowerOnTrap,
       "ifPoePboxAbnormalTrap": ifPoePboxAbnormalTrap}
)
