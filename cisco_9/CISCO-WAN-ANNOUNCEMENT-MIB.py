# SNMP MIB module (CISCO-WAN-ANNOUNCEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WAN-ANNOUNCEMENT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:15 2025
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanAnnouncementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25)
)
if mibBuilder.loadTexts:
    ciscoWanAnnouncementMIB.setRevisions(
        ("2003-12-22 00:00",
         "2001-12-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AnnCodecType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("g711u", 1),
          ("g711a", 2),
          ("g726r32000", 3),
          ("g729a", 4),
          ("g729ab", 5),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r40000", 9),
          ("g723h", 11),
          ("g723ah", 12),
          ("g723l", 13),
          ("g723al", 14))
    )



# MIB Managed Objects in the order of their OIDs

_CwAnnounceGrpMIBObjects_ObjectIdentity = ObjectIdentity
cwAnnounceGrpMIBObjects = _CwAnnounceGrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1)
)
_CwAnnounceGeneric_ObjectIdentity = ObjectIdentity
cwAnnounceGeneric = _CwAnnounceGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1)
)
_CwAnnounceControlGrp_ObjectIdentity = ObjectIdentity
cwAnnounceControlGrp = _CwAnnounceControlGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1)
)


class _CwAnnMaximumSize_Type(Integer32):
    """Custom type cwAnnMaximumSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwAnnMaximumSize_Type.__name__ = "Integer32"
_CwAnnMaximumSize_Object = MibScalar
cwAnnMaximumSize = _CwAnnMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 1),
    _CwAnnMaximumSize_Type()
)
cwAnnMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwAnnMaximumSize.setStatus("current")


class _CwAnnFileServerName_Type(DisplayString):
    """Custom type cwAnnFileServerName based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwAnnFileServerName_Type.__name__ = "DisplayString"
_CwAnnFileServerName_Object = MibScalar
cwAnnFileServerName = _CwAnnFileServerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 2),
    _CwAnnFileServerName_Type()
)
cwAnnFileServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwAnnFileServerName.setStatus("current")


class _CwAnnAgeTime_Type(Integer32):
    """Custom type cwAnnAgeTime based on Integer32"""
    defaultValue = 10080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwAnnAgeTime_Type.__name__ = "Integer32"
_CwAnnAgeTime_Object = MibScalar
cwAnnAgeTime = _CwAnnAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 3),
    _CwAnnAgeTime_Type()
)
cwAnnAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwAnnAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    cwAnnAgeTime.setUnits("minutes")
_CwAnnPreferenceCodec_Type = AnnCodecType
_CwAnnPreferenceCodec_Object = MibScalar
cwAnnPreferenceCodec = _CwAnnPreferenceCodec_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 4),
    _CwAnnPreferenceCodec_Type()
)
cwAnnPreferenceCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwAnnPreferenceCodec.setStatus("current")


class _CwAnnPrefixPath_Type(DisplayString):
    """Custom type cwAnnPrefixPath based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwAnnPrefixPath_Type.__name__ = "DisplayString"
_CwAnnPrefixPath_Object = MibScalar
cwAnnPrefixPath = _CwAnnPrefixPath_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 5),
    _CwAnnPrefixPath_Type()
)
cwAnnPrefixPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwAnnPrefixPath.setStatus("current")


class _CwAnnReqTimeout_Type(Integer32):
    """Custom type cwAnnReqTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwAnnReqTimeout_Type.__name__ = "Integer32"
_CwAnnReqTimeout_Object = MibScalar
cwAnnReqTimeout = _CwAnnReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 6),
    _CwAnnReqTimeout_Type()
)
cwAnnReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwAnnReqTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cwAnnReqTimeout.setUnits("seconds")
_CwAnnounceTableGrp_ObjectIdentity = ObjectIdentity
cwAnnounceTableGrp = _CwAnnounceTableGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2)
)
_CwAnnounceTable_Object = MibTable
cwAnnounceTable = _CwAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwAnnounceTable.setStatus("current")
_CwAnnounceEntry_Object = MibTableRow
cwAnnounceEntry = _CwAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1)
)
cwAnnounceEntry.setIndexNames(
    (0, "CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceNumber"),
)
if mibBuilder.loadTexts:
    cwAnnounceEntry.setStatus("current")


class _CwAnnounceNumber_Type(Integer32):
    """Custom type cwAnnounceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwAnnounceNumber_Type.__name__ = "Integer32"
_CwAnnounceNumber_Object = MibTableColumn
cwAnnounceNumber = _CwAnnounceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 1),
    _CwAnnounceNumber_Type()
)
cwAnnounceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwAnnounceNumber.setStatus("current")


class _CwAnnFileStatus_Type(Integer32):
    """Custom type cwAnnFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 2),
          ("invalidFile", 3),
          ("loadFailed", 4))
    )


_CwAnnFileStatus_Type.__name__ = "Integer32"
_CwAnnFileStatus_Object = MibTableColumn
cwAnnFileStatus = _CwAnnFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 2),
    _CwAnnFileStatus_Type()
)
cwAnnFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwAnnFileStatus.setStatus("current")


class _CwAnnFileName_Type(DisplayString):
    """Custom type cwAnnFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwAnnFileName_Type.__name__ = "DisplayString"
_CwAnnFileName_Object = MibTableColumn
cwAnnFileName = _CwAnnFileName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 3),
    _CwAnnFileName_Type()
)
cwAnnFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwAnnFileName.setStatus("current")
_CwAnnFileCodec_Type = AnnCodecType
_CwAnnFileCodec_Object = MibTableColumn
cwAnnFileCodec = _CwAnnFileCodec_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 4),
    _CwAnnFileCodec_Type()
)
cwAnnFileCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwAnnFileCodec.setStatus("current")
_CwAnnRowStatus_Type = RowStatus
_CwAnnRowStatus_Object = MibTableColumn
cwAnnRowStatus = _CwAnnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 5),
    _CwAnnRowStatus_Type()
)
cwAnnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwAnnRowStatus.setStatus("current")
_CwAnnounceNotificationPrefix_ObjectIdentity = ObjectIdentity
cwAnnounceNotificationPrefix = _CwAnnounceNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 2)
)
_CwAnnounceNotifications_ObjectIdentity = ObjectIdentity
cwAnnounceNotifications = _CwAnnounceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 2, 0)
)
_CwAnnounceMIBConformance_ObjectIdentity = ObjectIdentity
cwAnnounceMIBConformance = _CwAnnounceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3)
)
_CwAnnounceMIBCompliances_ObjectIdentity = ObjectIdentity
cwAnnounceMIBCompliances = _CwAnnounceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 1)
)
_CwAnnounceMIBGroups_ObjectIdentity = ObjectIdentity
cwAnnounceMIBGroups = _CwAnnounceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2)
)

# Managed Objects groups

cwAnnounceControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2, 1)
)
cwAnnounceControlGroup.setObjects(
      *(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnMaximumSize"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileServerName"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnAgeTime"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnPreferenceCodec"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnPrefixPath"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnReqTimeout"))
)
if mibBuilder.loadTexts:
    cwAnnounceControlGroup.setStatus("current")

cwAnnounceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2, 2)
)
cwAnnounceTableGroup.setObjects(
      *(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileStatus"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileName"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileCodec"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnRowStatus"))
)
if mibBuilder.loadTexts:
    cwAnnounceTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

announceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 1, 1)
)
announceMIBCompliance.setObjects(
      *(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceControlGroup"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceTableGroup"))
)
if mibBuilder.loadTexts:
    announceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ANNOUNCEMENT-MIB",
    **{"AnnCodecType": AnnCodecType,
       "ciscoWanAnnouncementMIB": ciscoWanAnnouncementMIB,
       "cwAnnounceGrpMIBObjects": cwAnnounceGrpMIBObjects,
       "cwAnnounceGeneric": cwAnnounceGeneric,
       "cwAnnounceControlGrp": cwAnnounceControlGrp,
       "cwAnnMaximumSize": cwAnnMaximumSize,
       "cwAnnFileServerName": cwAnnFileServerName,
       "cwAnnAgeTime": cwAnnAgeTime,
       "cwAnnPreferenceCodec": cwAnnPreferenceCodec,
       "cwAnnPrefixPath": cwAnnPrefixPath,
       "cwAnnReqTimeout": cwAnnReqTimeout,
       "cwAnnounceTableGrp": cwAnnounceTableGrp,
       "cwAnnounceTable": cwAnnounceTable,
       "cwAnnounceEntry": cwAnnounceEntry,
       "cwAnnounceNumber": cwAnnounceNumber,
       "cwAnnFileStatus": cwAnnFileStatus,
       "cwAnnFileName": cwAnnFileName,
       "cwAnnFileCodec": cwAnnFileCodec,
       "cwAnnRowStatus": cwAnnRowStatus,
       "cwAnnounceNotificationPrefix": cwAnnounceNotificationPrefix,
       "cwAnnounceNotifications": cwAnnounceNotifications,
       "cwAnnounceMIBConformance": cwAnnounceMIBConformance,
       "cwAnnounceMIBCompliances": cwAnnounceMIBCompliances,
       "announceMIBCompliance": announceMIBCompliance,
       "cwAnnounceMIBGroups": cwAnnounceMIBGroups,
       "cwAnnounceControlGroup": cwAnnounceControlGroup,
       "cwAnnounceTableGroup": cwAnnounceTableGroup}
)
