# SNMP MIB module (RUIJIE-AUTHEN-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AUTHEN-KEY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(ConfigStatus,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieAuthenKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24)
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieKeyTimeMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infinite", 1),
          ("duration", 2),
          ("end-time", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieAuthenKeyMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAuthenKeyMIBObjects = _RuijieAuthenKeyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1)
)
_RuijieAuthenKeyChainTable_Object = MibTable
ruijieAuthenKeyChainTable = _RuijieAuthenKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainTable.setStatus("current")
_RuijieAuthenKeyChainEntry_Object = MibTableRow
ruijieAuthenKeyChainEntry = _RuijieAuthenKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1)
)
ruijieAuthenKeyChainEntry.setIndexNames(
    (0, "RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyChainName"),
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainEntry.setStatus("current")


class _RuijieAuthenKeyChainName_Type(DisplayString):
    """Custom type ruijieAuthenKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAuthenKeyChainName_Type.__name__ = "DisplayString"
_RuijieAuthenKeyChainName_Object = MibTableColumn
ruijieAuthenKeyChainName = _RuijieAuthenKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1, 1),
    _RuijieAuthenKeyChainName_Type()
)
ruijieAuthenKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainName.setStatus("current")
_RuijieAuthenKeyChainEntryStatus_Type = ConfigStatus
_RuijieAuthenKeyChainEntryStatus_Object = MibTableColumn
ruijieAuthenKeyChainEntryStatus = _RuijieAuthenKeyChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1, 2),
    _RuijieAuthenKeyChainEntryStatus_Type()
)
ruijieAuthenKeyChainEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainEntryStatus.setStatus("current")
_RuijieAuthenKeyTable_Object = MibTable
ruijieAuthenKeyTable = _RuijieAuthenKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyTable.setStatus("current")
_RuijieAuthenKeyEntry_Object = MibTableRow
ruijieAuthenKeyEntry = _RuijieAuthenKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1)
)
ruijieAuthenKeyEntry.setIndexNames(
    (0, "RUIJIE-AUTHEN-KEY-MIB", "ruijieKeyChainName"),
    (0, "RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyNumber"),
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyEntry.setStatus("current")


class _RuijieKeyChainName_Type(DisplayString):
    """Custom type ruijieKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieKeyChainName_Type.__name__ = "DisplayString"
_RuijieKeyChainName_Object = MibTableColumn
ruijieKeyChainName = _RuijieKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 1),
    _RuijieKeyChainName_Type()
)
ruijieKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieKeyChainName.setStatus("current")


class _RuijieAuthenKeyNumber_Type(Integer32):
    """Custom type ruijieAuthenKeyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieAuthenKeyNumber_Type.__name__ = "Integer32"
_RuijieAuthenKeyNumber_Object = MibTableColumn
ruijieAuthenKeyNumber = _RuijieAuthenKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 2),
    _RuijieAuthenKeyNumber_Type()
)
ruijieAuthenKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenKeyNumber.setStatus("current")


class _RuijieKeyString_Type(DisplayString):
    """Custom type ruijieKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RuijieKeyString_Type.__name__ = "DisplayString"
_RuijieKeyString_Object = MibTableColumn
ruijieKeyString = _RuijieKeyString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 3),
    _RuijieKeyString_Type()
)
ruijieKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieKeyString.setStatus("current")
_RuijieAuthenKeyReceiveRuijieTime_Type = DateAndTime
_RuijieAuthenKeyReceiveRuijieTime_Object = MibTableColumn
ruijieAuthenKeyReceiveRuijieTime = _RuijieAuthenKeyReceiveRuijieTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 4),
    _RuijieAuthenKeyReceiveRuijieTime_Type()
)
ruijieAuthenKeyReceiveRuijieTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyReceiveRuijieTime.setStatus("current")
_RuijieAuthenKeyReceiveTimeMode_Type = RuijieKeyTimeMode
_RuijieAuthenKeyReceiveTimeMode_Object = MibTableColumn
ruijieAuthenKeyReceiveTimeMode = _RuijieAuthenKeyReceiveTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 5),
    _RuijieAuthenKeyReceiveTimeMode_Type()
)
ruijieAuthenKeyReceiveTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyReceiveTimeMode.setStatus("current")
_RuijieAuthenKeyReceiveEndTime_Type = DateAndTime
_RuijieAuthenKeyReceiveEndTime_Object = MibTableColumn
ruijieAuthenKeyReceiveEndTime = _RuijieAuthenKeyReceiveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 6),
    _RuijieAuthenKeyReceiveEndTime_Type()
)
ruijieAuthenKeyReceiveEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyReceiveEndTime.setStatus("current")
_RuijieAuthenKeyReceiveDuration_Type = Unsigned32
_RuijieAuthenKeyReceiveDuration_Object = MibTableColumn
ruijieAuthenKeyReceiveDuration = _RuijieAuthenKeyReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 7),
    _RuijieAuthenKeyReceiveDuration_Type()
)
ruijieAuthenKeyReceiveDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyReceiveDuration.setStatus("current")
_RuijieAuthenKeySendRuijieTime_Type = DateAndTime
_RuijieAuthenKeySendRuijieTime_Object = MibTableColumn
ruijieAuthenKeySendRuijieTime = _RuijieAuthenKeySendRuijieTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 8),
    _RuijieAuthenKeySendRuijieTime_Type()
)
ruijieAuthenKeySendRuijieTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeySendRuijieTime.setStatus("current")
_RuijieAuthenKeySendTimeMode_Type = RuijieKeyTimeMode
_RuijieAuthenKeySendTimeMode_Object = MibTableColumn
ruijieAuthenKeySendTimeMode = _RuijieAuthenKeySendTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 9),
    _RuijieAuthenKeySendTimeMode_Type()
)
ruijieAuthenKeySendTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeySendTimeMode.setStatus("current")
_RuijieAuthenKeySendEndTime_Type = DateAndTime
_RuijieAuthenKeySendEndTime_Object = MibTableColumn
ruijieAuthenKeySendEndTime = _RuijieAuthenKeySendEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 10),
    _RuijieAuthenKeySendEndTime_Type()
)
ruijieAuthenKeySendEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeySendEndTime.setStatus("current")
_RuijieAuthenKeySendDuration_Type = Unsigned32
_RuijieAuthenKeySendDuration_Object = MibTableColumn
ruijieAuthenKeySendDuration = _RuijieAuthenKeySendDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 11),
    _RuijieAuthenKeySendDuration_Type()
)
ruijieAuthenKeySendDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeySendDuration.setStatus("current")


class _RuijieAuthenReceiveKeyState_Type(Integer32):
    """Custom type ruijieAuthenReceiveKeyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RuijieAuthenReceiveKeyState_Type.__name__ = "Integer32"
_RuijieAuthenReceiveKeyState_Object = MibTableColumn
ruijieAuthenReceiveKeyState = _RuijieAuthenReceiveKeyState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 12),
    _RuijieAuthenReceiveKeyState_Type()
)
ruijieAuthenReceiveKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenReceiveKeyState.setStatus("current")


class _RuijieAuthenSendKeyState_Type(Integer32):
    """Custom type ruijieAuthenSendKeyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RuijieAuthenSendKeyState_Type.__name__ = "Integer32"
_RuijieAuthenSendKeyState_Object = MibTableColumn
ruijieAuthenSendKeyState = _RuijieAuthenSendKeyState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 13),
    _RuijieAuthenSendKeyState_Type()
)
ruijieAuthenSendKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthenSendKeyState.setStatus("current")
_RuijieAuthenKeyEntryStauts_Type = RowStatus
_RuijieAuthenKeyEntryStauts_Object = MibTableColumn
ruijieAuthenKeyEntryStauts = _RuijieAuthenKeyEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 14),
    _RuijieAuthenKeyEntryStauts_Type()
)
ruijieAuthenKeyEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAuthenKeyEntryStauts.setStatus("current")
_RuijieAuthenKeyChainMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAuthenKeyChainMIBConformance = _RuijieAuthenKeyChainMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2)
)
_RuijieAuthenKeyChainMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAuthenKeyChainMIBCompliances = _RuijieAuthenKeyChainMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 1)
)
_RuijieAuthenKeyChainMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAuthenKeyChainMIBGroups = _RuijieAuthenKeyChainMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 2)
)

# Managed Objects groups

ruijieAuthenKeyChainMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 2, 1)
)
ruijieAuthenKeyChainMIBGroup.setObjects(
      *(("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyChainName"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyChainEntryStatus"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieKeyChainName"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyNumber"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieKeyString"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyReceiveRuijieTime"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyReceiveTimeMode"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyReceiveEndTime"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyReceiveDuration"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeySendRuijieTime"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeySendTimeMode"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeySendEndTime"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeySendDuration"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenReceiveKeyState"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenSendKeyState"),
        ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyEntryStauts"))
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAuthenKeyChainMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 1, 1)
)
ruijieAuthenKeyChainMIBCompliance.setObjects(
    ("RUIJIE-AUTHEN-KEY-MIB", "ruijieAuthenKeyChainMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieAuthenKeyChainMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AUTHEN-KEY-MIB",
    **{"RuijieKeyTimeMode": RuijieKeyTimeMode,
       "ruijieAuthenKeyMIB": ruijieAuthenKeyMIB,
       "ruijieAuthenKeyMIBObjects": ruijieAuthenKeyMIBObjects,
       "ruijieAuthenKeyChainTable": ruijieAuthenKeyChainTable,
       "ruijieAuthenKeyChainEntry": ruijieAuthenKeyChainEntry,
       "ruijieAuthenKeyChainName": ruijieAuthenKeyChainName,
       "ruijieAuthenKeyChainEntryStatus": ruijieAuthenKeyChainEntryStatus,
       "ruijieAuthenKeyTable": ruijieAuthenKeyTable,
       "ruijieAuthenKeyEntry": ruijieAuthenKeyEntry,
       "ruijieKeyChainName": ruijieKeyChainName,
       "ruijieAuthenKeyNumber": ruijieAuthenKeyNumber,
       "ruijieKeyString": ruijieKeyString,
       "ruijieAuthenKeyReceiveRuijieTime": ruijieAuthenKeyReceiveRuijieTime,
       "ruijieAuthenKeyReceiveTimeMode": ruijieAuthenKeyReceiveTimeMode,
       "ruijieAuthenKeyReceiveEndTime": ruijieAuthenKeyReceiveEndTime,
       "ruijieAuthenKeyReceiveDuration": ruijieAuthenKeyReceiveDuration,
       "ruijieAuthenKeySendRuijieTime": ruijieAuthenKeySendRuijieTime,
       "ruijieAuthenKeySendTimeMode": ruijieAuthenKeySendTimeMode,
       "ruijieAuthenKeySendEndTime": ruijieAuthenKeySendEndTime,
       "ruijieAuthenKeySendDuration": ruijieAuthenKeySendDuration,
       "ruijieAuthenReceiveKeyState": ruijieAuthenReceiveKeyState,
       "ruijieAuthenSendKeyState": ruijieAuthenSendKeyState,
       "ruijieAuthenKeyEntryStauts": ruijieAuthenKeyEntryStauts,
       "ruijieAuthenKeyChainMIBConformance": ruijieAuthenKeyChainMIBConformance,
       "ruijieAuthenKeyChainMIBCompliances": ruijieAuthenKeyChainMIBCompliances,
       "ruijieAuthenKeyChainMIBCompliance": ruijieAuthenKeyChainMIBCompliance,
       "ruijieAuthenKeyChainMIBGroups": ruijieAuthenKeyChainMIBGroups,
       "ruijieAuthenKeyChainMIBGroup": ruijieAuthenKeyChainMIBGroup}
)
