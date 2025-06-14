# SNMP MIB module (RBN-BULKSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-BULKSTATS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:52 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(vacmContextName,) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmContextName")

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

rbnBulkStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21)
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIB.setRevisions(
        ("2011-01-19 18:00",
         "2003-02-28 00:00",
         "2002-05-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnBulkStatsMIBNotifications_ObjectIdentity = ObjectIdentity
rbnBulkStatsMIBNotifications = _RbnBulkStatsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 0)
)
_RbnBulkStatsMIBObjects_ObjectIdentity = ObjectIdentity
rbnBulkStatsMIBObjects = _RbnBulkStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1)
)
_RbnBulkStatsLastTrfr_ObjectIdentity = ObjectIdentity
rbnBulkStatsLastTrfr = _RbnBulkStatsLastTrfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1)
)
_RbnBulkStatsLastTrfrIpAddrType_Type = InetAddressType
_RbnBulkStatsLastTrfrIpAddrType_Object = MibScalar
rbnBulkStatsLastTrfrIpAddrType = _RbnBulkStatsLastTrfrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 1),
    _RbnBulkStatsLastTrfrIpAddrType_Type()
)
rbnBulkStatsLastTrfrIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrIpAddrType.setStatus("obsolete")
_RbnBulkStatsLastTrfrIpAddr_Type = InetAddress
_RbnBulkStatsLastTrfrIpAddr_Object = MibScalar
rbnBulkStatsLastTrfrIpAddr = _RbnBulkStatsLastTrfrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 2),
    _RbnBulkStatsLastTrfrIpAddr_Type()
)
rbnBulkStatsLastTrfrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrIpAddr.setStatus("obsolete")


class _RbnBulkStatsLastTrfrStatus_Type(Integer32):
    """Custom type rbnBulkStatsLastTrfrStatus based on Integer32"""
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
        *(("none", 1),
          ("success", 2),
          ("genError", 3),
          ("loginFailed", 4),
          ("badFilename", 5),
          ("remoteHostFailed", 6),
          ("other", 7))
    )


_RbnBulkStatsLastTrfrStatus_Type.__name__ = "Integer32"
_RbnBulkStatsLastTrfrStatus_Object = MibScalar
rbnBulkStatsLastTrfrStatus = _RbnBulkStatsLastTrfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 3),
    _RbnBulkStatsLastTrfrStatus_Type()
)
rbnBulkStatsLastTrfrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrStatus.setStatus("obsolete")
_RbnBulkStatsLastTrfrTable_Object = MibTable
rbnBulkStatsLastTrfrTable = _RbnBulkStatsLastTrfrTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrTable.setStatus("current")
_RbnBulkStatsLastTrfrEntry_Object = MibTableRow
rbnBulkStatsLastTrfrEntry = _RbnBulkStatsLastTrfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1)
)
rbnBulkStatsLastTrfrEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"),
    (0, "RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrPolicy"),
)
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrEntry.setStatus("current")


class _RbnBulkStatsLastTrfrPolicy_Type(SnmpAdminString):
    """Custom type rbnBulkStatsLastTrfrPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RbnBulkStatsLastTrfrPolicy_Type.__name__ = "SnmpAdminString"
_RbnBulkStatsLastTrfrPolicy_Object = MibTableColumn
rbnBulkStatsLastTrfrPolicy = _RbnBulkStatsLastTrfrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 1),
    _RbnBulkStatsLastTrfrPolicy_Type()
)
rbnBulkStatsLastTrfrPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrPolicy.setStatus("current")
_RbnBulkStatsLastTrfrIpAddrType2_Type = InetAddressType
_RbnBulkStatsLastTrfrIpAddrType2_Object = MibTableColumn
rbnBulkStatsLastTrfrIpAddrType2 = _RbnBulkStatsLastTrfrIpAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 2),
    _RbnBulkStatsLastTrfrIpAddrType2_Type()
)
rbnBulkStatsLastTrfrIpAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrIpAddrType2.setStatus("current")
_RbnBulkStatsLastTrfrIpAddr2_Type = InetAddress
_RbnBulkStatsLastTrfrIpAddr2_Object = MibTableColumn
rbnBulkStatsLastTrfrIpAddr2 = _RbnBulkStatsLastTrfrIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 3),
    _RbnBulkStatsLastTrfrIpAddr2_Type()
)
rbnBulkStatsLastTrfrIpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrIpAddr2.setStatus("current")


class _RbnBulkStatsLastTrfrStatus2_Type(Integer32):
    """Custom type rbnBulkStatsLastTrfrStatus2 based on Integer32"""
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
        *(("none", 1),
          ("success", 2),
          ("genError", 3),
          ("loginFailed", 4),
          ("badFilename", 5),
          ("remoteHostFailed", 6),
          ("other", 7))
    )


_RbnBulkStatsLastTrfrStatus2_Type.__name__ = "Integer32"
_RbnBulkStatsLastTrfrStatus2_Object = MibTableColumn
rbnBulkStatsLastTrfrStatus2 = _RbnBulkStatsLastTrfrStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 4),
    _RbnBulkStatsLastTrfrStatus2_Type()
)
rbnBulkStatsLastTrfrStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrStatus2.setStatus("current")


class _RbnBulkStatsLastTrfrFiletype_Type(Integer32):
    """Custom type rbnBulkStatsLastTrfrFiletype based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("text", 1),
          ("xml", 2))
    )


_RbnBulkStatsLastTrfrFiletype_Type.__name__ = "Integer32"
_RbnBulkStatsLastTrfrFiletype_Object = MibTableColumn
rbnBulkStatsLastTrfrFiletype = _RbnBulkStatsLastTrfrFiletype_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 1, 1, 4, 1, 5),
    _RbnBulkStatsLastTrfrFiletype_Type()
)
rbnBulkStatsLastTrfrFiletype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBulkStatsLastTrfrFiletype.setStatus("current")
_RbnBulkStatsMIBConformance_ObjectIdentity = ObjectIdentity
rbnBulkStatsMIBConformance = _RbnBulkStatsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2)
)
_RbnBulkStatsMIBGroups_ObjectIdentity = ObjectIdentity
rbnBulkStatsMIBGroups = _RbnBulkStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1)
)
_RbnBulkStatsMIBCompliances_ObjectIdentity = ObjectIdentity
rbnBulkStatsMIBCompliances = _RbnBulkStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2)
)

# Managed Objects groups

rbnBulkStatsMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 1)
)
rbnBulkStatsMIBObjectGroup.setObjects(
      *(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus"))
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBObjectGroup.setStatus("obsolete")

rbnBulkStatsMIBObjectGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 3)
)
rbnBulkStatsMIBObjectGroup2.setObjects(
      *(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus2"))
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBObjectGroup2.setStatus("current")


# Notification objects

rbnBulkStatsTrfrFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 0, 1)
)
rbnBulkStatsTrfrFail.setObjects(
      *(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus"))
)
if mibBuilder.loadTexts:
    rbnBulkStatsTrfrFail.setStatus(
        "obsolete"
    )

rbnBulkStatsTrfrFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 0, 2)
)
rbnBulkStatsTrfrFail2.setObjects(
      *(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrFiletype"))
)
if mibBuilder.loadTexts:
    rbnBulkStatsTrfrFail2.setStatus(
        "current"
    )

rbnBulkStatsFileWrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 0, 3)
)
rbnBulkStatsFileWrapped.setObjects(
      *(("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddrType2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrIpAddr2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrStatus2"),
        ("RBN-BULKSTATS-MIB", "rbnBulkStatsLastTrfrFiletype"))
)
if mibBuilder.loadTexts:
    rbnBulkStatsFileWrapped.setStatus(
        "current"
    )


# Notifications groups

rbnBulkStatsMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 2)
)
rbnBulkStatsMIBNotificationGroup.setObjects(
    ("RBN-BULKSTATS-MIB", "rbnBulkStatsTrfrFail")
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBNotificationGroup.setStatus(
        "obsolete"
    )

rbnBulkStatsMIBNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 1, 4)
)
rbnBulkStatsMIBNotificationGroup2.setObjects(
    ("RBN-BULKSTATS-MIB", "rbnBulkStatsTrfrFail2")
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBNotificationGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnBulkStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2, 1)
)
rbnBulkStatsMIBCompliance.setObjects(
    ("RBN-BULKSTATS-MIB", "rbnBulkStatsMIBNotificationGroup")
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBCompliance.setStatus(
        "obsolete"
    )

rbnBulkStatsMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 21, 2, 2, 2)
)
rbnBulkStatsMIBCompliance2.setObjects(
    ("RBN-BULKSTATS-MIB", "rbnBulkStatsMIBNotificationGroup2")
)
if mibBuilder.loadTexts:
    rbnBulkStatsMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-BULKSTATS-MIB",
    **{"rbnBulkStatsMIB": rbnBulkStatsMIB,
       "rbnBulkStatsMIBNotifications": rbnBulkStatsMIBNotifications,
       "rbnBulkStatsTrfrFail": rbnBulkStatsTrfrFail,
       "rbnBulkStatsTrfrFail2": rbnBulkStatsTrfrFail2,
       "rbnBulkStatsFileWrapped": rbnBulkStatsFileWrapped,
       "rbnBulkStatsMIBObjects": rbnBulkStatsMIBObjects,
       "rbnBulkStatsLastTrfr": rbnBulkStatsLastTrfr,
       "rbnBulkStatsLastTrfrIpAddrType": rbnBulkStatsLastTrfrIpAddrType,
       "rbnBulkStatsLastTrfrIpAddr": rbnBulkStatsLastTrfrIpAddr,
       "rbnBulkStatsLastTrfrStatus": rbnBulkStatsLastTrfrStatus,
       "rbnBulkStatsLastTrfrTable": rbnBulkStatsLastTrfrTable,
       "rbnBulkStatsLastTrfrEntry": rbnBulkStatsLastTrfrEntry,
       "rbnBulkStatsLastTrfrPolicy": rbnBulkStatsLastTrfrPolicy,
       "rbnBulkStatsLastTrfrIpAddrType2": rbnBulkStatsLastTrfrIpAddrType2,
       "rbnBulkStatsLastTrfrIpAddr2": rbnBulkStatsLastTrfrIpAddr2,
       "rbnBulkStatsLastTrfrStatus2": rbnBulkStatsLastTrfrStatus2,
       "rbnBulkStatsLastTrfrFiletype": rbnBulkStatsLastTrfrFiletype,
       "rbnBulkStatsMIBConformance": rbnBulkStatsMIBConformance,
       "rbnBulkStatsMIBGroups": rbnBulkStatsMIBGroups,
       "rbnBulkStatsMIBObjectGroup": rbnBulkStatsMIBObjectGroup,
       "rbnBulkStatsMIBNotificationGroup": rbnBulkStatsMIBNotificationGroup,
       "rbnBulkStatsMIBObjectGroup2": rbnBulkStatsMIBObjectGroup2,
       "rbnBulkStatsMIBNotificationGroup2": rbnBulkStatsMIBNotificationGroup2,
       "rbnBulkStatsMIBCompliances": rbnBulkStatsMIBCompliances,
       "rbnBulkStatsMIBCompliance": rbnBulkStatsMIBCompliance,
       "rbnBulkStatsMIBCompliance2": rbnBulkStatsMIBCompliance2}
)
