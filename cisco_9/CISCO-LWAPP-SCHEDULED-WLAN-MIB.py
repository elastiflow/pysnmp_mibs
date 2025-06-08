# SNMP MIB module (CISCO-LWAPP-SCHEDULED-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-SCHEDULED-WLAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCapwapScheduledWlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864)
)
if mibBuilder.loadTexts:
    ciscoCapwapScheduledWlanMIB.setRevisions(
        ("2019-04-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappScheduledWlanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanMIBNotifs = _CiscoLwappScheduledWlanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 0)
)
_CiscoLwappScheduledWlanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanMIBObjects = _CiscoLwappScheduledWlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1)
)
_CiscoLwappScheduledWlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanConfig = _CiscoLwappScheduledWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1)
)
_CLCalendarProfileConfigTable_Object = MibTable
cLCalendarProfileConfigTable = _CLCalendarProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLCalendarProfileConfigTable.setStatus("current")
_CLCalendarProfileConfigEntry_Object = MibTableRow
cLCalendarProfileConfigEntry = _CLCalendarProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1)
)
cLCalendarProfileConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileName"),
)
if mibBuilder.loadTexts:
    cLCalendarProfileConfigEntry.setStatus("current")


class _CLCalendarProfileName_Type(SnmpAdminString):
    """Custom type cLCalendarProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLCalendarProfileName_Type.__name__ = "SnmpAdminString"
_CLCalendarProfileName_Object = MibTableColumn
cLCalendarProfileName = _CLCalendarProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1, 1),
    _CLCalendarProfileName_Type()
)
cLCalendarProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLCalendarProfileName.setStatus("current")
_CLCalendarProfileRowStatus_Type = RowStatus
_CLCalendarProfileRowStatus_Object = MibTableColumn
cLCalendarProfileRowStatus = _CLCalendarProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1, 2),
    _CLCalendarProfileRowStatus_Type()
)
cLCalendarProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLCalendarProfileRowStatus.setStatus("current")


class _CLCalendarProfileStartTime_Type(SnmpAdminString):
    """Custom type cLCalendarProfileStartTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLCalendarProfileStartTime_Type.__name__ = "SnmpAdminString"
_CLCalendarProfileStartTime_Object = MibTableColumn
cLCalendarProfileStartTime = _CLCalendarProfileStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1, 3),
    _CLCalendarProfileStartTime_Type()
)
cLCalendarProfileStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLCalendarProfileStartTime.setStatus("current")


class _CLCalendarProfileEndTime_Type(SnmpAdminString):
    """Custom type cLCalendarProfileEndTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLCalendarProfileEndTime_Type.__name__ = "SnmpAdminString"
_CLCalendarProfileEndTime_Object = MibTableColumn
cLCalendarProfileEndTime = _CLCalendarProfileEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1, 4),
    _CLCalendarProfileEndTime_Type()
)
cLCalendarProfileEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLCalendarProfileEndTime.setStatus("current")


class _CLCalendarProfileRecurrence_Type(Integer32):
    """Custom type cLCalendarProfileRecurrence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 0),
          ("weekly", 1),
          ("monthly", 2))
    )


_CLCalendarProfileRecurrence_Type.__name__ = "Integer32"
_CLCalendarProfileRecurrence_Object = MibTableColumn
cLCalendarProfileRecurrence = _CLCalendarProfileRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 1, 1, 5),
    _CLCalendarProfileRecurrence_Type()
)
cLCalendarProfileRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLCalendarProfileRecurrence.setStatus("current")
_CLCalendarProfileWeeklyConfigTable_Object = MibTable
cLCalendarProfileWeeklyConfigTable = _CLCalendarProfileWeeklyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLCalendarProfileWeeklyConfigTable.setStatus("current")
_CLCalendarProfileWeeklyConfigEntry_Object = MibTableRow
cLCalendarProfileWeeklyConfigEntry = _CLCalendarProfileWeeklyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 2, 1)
)
cLCalendarProfileWeeklyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileName"),
    (0, "CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileWeeklyProfileDay"),
)
if mibBuilder.loadTexts:
    cLCalendarProfileWeeklyConfigEntry.setStatus("current")


class _CLCalendarProfileWeeklyProfileDay_Type(Integer32):
    """Custom type cLCalendarProfileWeeklyProfileDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("sunday", 7))
    )


_CLCalendarProfileWeeklyProfileDay_Type.__name__ = "Integer32"
_CLCalendarProfileWeeklyProfileDay_Object = MibTableColumn
cLCalendarProfileWeeklyProfileDay = _CLCalendarProfileWeeklyProfileDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 2, 1, 1),
    _CLCalendarProfileWeeklyProfileDay_Type()
)
cLCalendarProfileWeeklyProfileDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLCalendarProfileWeeklyProfileDay.setStatus("current")
_CLCalendarProfileWeeklyProfileRowStatus_Type = RowStatus
_CLCalendarProfileWeeklyProfileRowStatus_Object = MibTableColumn
cLCalendarProfileWeeklyProfileRowStatus = _CLCalendarProfileWeeklyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 2, 1, 2),
    _CLCalendarProfileWeeklyProfileRowStatus_Type()
)
cLCalendarProfileWeeklyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLCalendarProfileWeeklyProfileRowStatus.setStatus("current")
_CLCalendarProfileMonthlyConfigTable_Object = MibTable
cLCalendarProfileMonthlyConfigTable = _CLCalendarProfileMonthlyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLCalendarProfileMonthlyConfigTable.setStatus("current")
_CLCalendarProfileMonthlyConfigEntry_Object = MibTableRow
cLCalendarProfileMonthlyConfigEntry = _CLCalendarProfileMonthlyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 3, 1)
)
cLCalendarProfileMonthlyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileName"),
    (0, "CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileMonthlyProfileDate"),
)
if mibBuilder.loadTexts:
    cLCalendarProfileMonthlyConfigEntry.setStatus("current")
_CLCalendarProfileMonthlyProfileDate_Type = Unsigned32
_CLCalendarProfileMonthlyProfileDate_Object = MibTableColumn
cLCalendarProfileMonthlyProfileDate = _CLCalendarProfileMonthlyProfileDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 3, 1, 1),
    _CLCalendarProfileMonthlyProfileDate_Type()
)
cLCalendarProfileMonthlyProfileDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLCalendarProfileMonthlyProfileDate.setStatus("current")
_CLCalendarProfileMonthlyProfileRowStatus_Type = RowStatus
_CLCalendarProfileMonthlyProfileRowStatus_Object = MibTableColumn
cLCalendarProfileMonthlyProfileRowStatus = _CLCalendarProfileMonthlyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 1, 1, 3, 1, 2),
    _CLCalendarProfileMonthlyProfileRowStatus_Type()
)
cLCalendarProfileMonthlyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLCalendarProfileMonthlyProfileRowStatus.setStatus("current")
_CiscoLwappScheduledWlanConform_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanConform = _CiscoLwappScheduledWlanConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 2)
)
_CiscoLwappScheduledWlanCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanCompliances = _CiscoLwappScheduledWlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 2, 1)
)
_CiscoLwappScheduledWlanGroups_ObjectIdentity = ObjectIdentity
ciscoLwappScheduledWlanGroups = _CiscoLwappScheduledWlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 2, 2)
)

# Managed Objects groups

ciscoLwappScheduledWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 2, 2, 1)
)
ciscoLwappScheduledWlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileRowStatus"),
        ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileStartTime"),
        ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileEndTime"),
        ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileRecurrence"),
        ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileWeeklyProfileRowStatus"),
        ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "cLCalendarProfileMonthlyProfileRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappScheduledWlanConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappScheduledWlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 864, 2, 1, 1)
)
ciscoLwappScheduledWlanCompliance.setObjects(
    ("CISCO-LWAPP-SCHEDULED-WLAN-MIB", "ciscoLwappScheduledWlanConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappScheduledWlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-SCHEDULED-WLAN-MIB",
    **{"ciscoCapwapScheduledWlanMIB": ciscoCapwapScheduledWlanMIB,
       "ciscoLwappScheduledWlanMIBNotifs": ciscoLwappScheduledWlanMIBNotifs,
       "ciscoLwappScheduledWlanMIBObjects": ciscoLwappScheduledWlanMIBObjects,
       "ciscoLwappScheduledWlanConfig": ciscoLwappScheduledWlanConfig,
       "cLCalendarProfileConfigTable": cLCalendarProfileConfigTable,
       "cLCalendarProfileConfigEntry": cLCalendarProfileConfigEntry,
       "cLCalendarProfileName": cLCalendarProfileName,
       "cLCalendarProfileRowStatus": cLCalendarProfileRowStatus,
       "cLCalendarProfileStartTime": cLCalendarProfileStartTime,
       "cLCalendarProfileEndTime": cLCalendarProfileEndTime,
       "cLCalendarProfileRecurrence": cLCalendarProfileRecurrence,
       "cLCalendarProfileWeeklyConfigTable": cLCalendarProfileWeeklyConfigTable,
       "cLCalendarProfileWeeklyConfigEntry": cLCalendarProfileWeeklyConfigEntry,
       "cLCalendarProfileWeeklyProfileDay": cLCalendarProfileWeeklyProfileDay,
       "cLCalendarProfileWeeklyProfileRowStatus": cLCalendarProfileWeeklyProfileRowStatus,
       "cLCalendarProfileMonthlyConfigTable": cLCalendarProfileMonthlyConfigTable,
       "cLCalendarProfileMonthlyConfigEntry": cLCalendarProfileMonthlyConfigEntry,
       "cLCalendarProfileMonthlyProfileDate": cLCalendarProfileMonthlyProfileDate,
       "cLCalendarProfileMonthlyProfileRowStatus": cLCalendarProfileMonthlyProfileRowStatus,
       "ciscoLwappScheduledWlanConform": ciscoLwappScheduledWlanConform,
       "ciscoLwappScheduledWlanCompliances": ciscoLwappScheduledWlanCompliances,
       "ciscoLwappScheduledWlanCompliance": ciscoLwappScheduledWlanCompliance,
       "ciscoLwappScheduledWlanGroups": ciscoLwappScheduledWlanGroups,
       "ciscoLwappScheduledWlanConfigGroup": ciscoLwappScheduledWlanConfigGroup}
)
