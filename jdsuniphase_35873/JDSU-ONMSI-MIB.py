# SNMP MIB module (JDSU-ONMSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/jdsuniphase_35873/JDSU-ONMSI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:53:13 2025
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(jdsuOnmsi,) = mibBuilder.importSymbols(
    "JDSU-SMI-MIB",
    "jdsuOnmsi")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jdsuOnmsiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiMib.setRevisions(
        ("2020-03-11 16:27",
         "2019-11-20 16:01",
         "2018-09-04 15:59",
         "2017-07-05 11:00",
         "2012-10-25 11:38",
         "2011-10-04 11:15",
         "2011-09-27 14:49",
         "2010-06-09 09:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JdsuOnmsiAlarmAckStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 1),
          ("unacknowledged", 2))
    )



class JdsuOnmsiAlarmClearStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("uncleared", 2))
    )



class JdsuOnmsiAlarmEventType(TextualConvention, Integer32):
    status = "current"
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
        *(("newAlarmEvent", 1),
          ("changedAlarmEvent", 2),
          ("ackStateChangedEvent", 3),
          ("clearStateChangedEvent", 4),
          ("alarmCommentsEvent", 5))
    )



class JdsuOnmsiInternalKey(TextualConvention, Unsigned32):
    status = "current"


class JdsuOnmsiOtdrPosition(TextualConvention, Integer32):
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
        *(("top", 1),
          ("bottom", 2),
          ("center", 3))
    )



class JdsuOnmsiPeakStatus(TextualConvention, OctetString):
    status = "current"


class JdsuOnmsiPeakType(TextualConvention, Integer32):
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
        *(("notReferenced", 1),
          ("notHome", 2),
          ("home", 3))
    )



class JdsuOnmsiSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("indeterminate", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )



class JdsuOnmsiUtf8String(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_JdsuOnmsiProduct_ObjectIdentity = ObjectIdentity
jdsuOnmsiProduct = _JdsuOnmsiProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1)
)
_JdsuOnmsiProductDescr_Type = JdsuOnmsiUtf8String
_JdsuOnmsiProductDescr_Object = MibScalar
jdsuOnmsiProductDescr = _JdsuOnmsiProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1, 1),
    _JdsuOnmsiProductDescr_Type()
)
jdsuOnmsiProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiProductDescr.setStatus("current")
_JdsuOnmsiProductObjectID_Type = ObjectIdentifier
_JdsuOnmsiProductObjectID_Object = MibScalar
jdsuOnmsiProductObjectID = _JdsuOnmsiProductObjectID_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1, 2),
    _JdsuOnmsiProductObjectID_Type()
)
jdsuOnmsiProductObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiProductObjectID.setStatus("current")
_JdsuOnmsiProductContact_Type = JdsuOnmsiUtf8String
_JdsuOnmsiProductContact_Object = MibScalar
jdsuOnmsiProductContact = _JdsuOnmsiProductContact_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1, 3),
    _JdsuOnmsiProductContact_Type()
)
jdsuOnmsiProductContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiProductContact.setStatus("current")
_JdsuOnmsiProductName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiProductName_Object = MibScalar
jdsuOnmsiProductName = _JdsuOnmsiProductName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1, 4),
    _JdsuOnmsiProductName_Type()
)
jdsuOnmsiProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiProductName.setStatus("current")
_JdsuOnmsiProductLocation_Type = JdsuOnmsiUtf8String
_JdsuOnmsiProductLocation_Object = MibScalar
jdsuOnmsiProductLocation = _JdsuOnmsiProductLocation_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 1, 5),
    _JdsuOnmsiProductLocation_Type()
)
jdsuOnmsiProductLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiProductLocation.setStatus("current")
_JdsuOnmsiAdministration_ObjectIdentity = ObjectIdentity
jdsuOnmsiAdministration = _JdsuOnmsiAdministration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2)
)
_JdsuOnmsiSnmpConfig_ObjectIdentity = ObjectIdentity
jdsuOnmsiSnmpConfig = _JdsuOnmsiSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 1)
)
_JdsuOnmsiSnmpConfigurationReload_Type = Integer32
_JdsuOnmsiSnmpConfigurationReload_Object = MibScalar
jdsuOnmsiSnmpConfigurationReload = _JdsuOnmsiSnmpConfigurationReload_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 1, 1),
    _JdsuOnmsiSnmpConfigurationReload_Type()
)
jdsuOnmsiSnmpConfigurationReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiSnmpConfigurationReload.setStatus("current")
_JdsuOnmsiImAlive_ObjectIdentity = ObjectIdentity
jdsuOnmsiImAlive = _JdsuOnmsiImAlive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 2)
)
_JdsuOnmsiImAlivePeriodMin_Type = Integer32
_JdsuOnmsiImAlivePeriodMin_Object = MibScalar
jdsuOnmsiImAlivePeriodMin = _JdsuOnmsiImAlivePeriodMin_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 2, 1),
    _JdsuOnmsiImAlivePeriodMin_Type()
)
jdsuOnmsiImAlivePeriodMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiImAlivePeriodMin.setStatus("current")
_JdsuOnmsiImAliveText_Type = DisplayString
_JdsuOnmsiImAliveText_Object = MibScalar
jdsuOnmsiImAliveText = _JdsuOnmsiImAliveText_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 2, 2),
    _JdsuOnmsiImAliveText_Type()
)
jdsuOnmsiImAliveText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiImAliveText.setStatus("current")
_JdsuOnmsiImAliveAlarmEventSequence_Type = Unsigned32
_JdsuOnmsiImAliveAlarmEventSequence_Object = MibScalar
jdsuOnmsiImAliveAlarmEventSequence = _JdsuOnmsiImAliveAlarmEventSequence_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 2, 2, 3),
    _JdsuOnmsiImAliveAlarmEventSequence_Type()
)
jdsuOnmsiImAliveAlarmEventSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiImAliveAlarmEventSequence.setStatus("current")
_JdsuOnmsiServices_ObjectIdentity = ObjectIdentity
jdsuOnmsiServices = _JdsuOnmsiServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3)
)
_JdsuOnmsiHomeService_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeService = _JdsuOnmsiHomeService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1)
)
_JdsuOnmsiHomeData_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeData = _JdsuOnmsiHomeData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1)
)
_JdsuOnmsiHomeTable_Object = MibTable
jdsuOnmsiHomeTable = _JdsuOnmsiHomeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTable.setStatus("current")
_JdsuOnmsiHomeEntry_Object = MibTableRow
jdsuOnmsiHomeEntry = _JdsuOnmsiHomeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1)
)
jdsuOnmsiHomeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntry.setStatus("current")
_JdsuOnmsiHomeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiHomeEntryInternalKey = _JdsuOnmsiHomeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 1),
    _JdsuOnmsiHomeEntryInternalKey_Type()
)
jdsuOnmsiHomeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryInternalKey.setStatus("current")
_JdsuOnmsiHomeEntryHomeIdentifier_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeEntryHomeIdentifier_Object = MibTableColumn
jdsuOnmsiHomeEntryHomeIdentifier = _JdsuOnmsiHomeEntryHomeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 2),
    _JdsuOnmsiHomeEntryHomeIdentifier_Type()
)
jdsuOnmsiHomeEntryHomeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryHomeIdentifier.setStatus("current")
_JdsuOnmsiHomeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeEntryName_Object = MibTableColumn
jdsuOnmsiHomeEntryName = _JdsuOnmsiHomeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 3),
    _JdsuOnmsiHomeEntryName_Type()
)
jdsuOnmsiHomeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryName.setStatus("current")
_JdsuOnmsiHomeEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeEntryDescription_Object = MibTableColumn
jdsuOnmsiHomeEntryDescription = _JdsuOnmsiHomeEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 4),
    _JdsuOnmsiHomeEntryDescription_Type()
)
jdsuOnmsiHomeEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryDescription.setStatus("current")
_JdsuOnmsiHomeEntryPonInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeEntryPonInternalKey_Object = MibTableColumn
jdsuOnmsiHomeEntryPonInternalKey = _JdsuOnmsiHomeEntryPonInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 5),
    _JdsuOnmsiHomeEntryPonInternalKey_Type()
)
jdsuOnmsiHomeEntryPonInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryPonInternalKey.setStatus("current")
_JdsuOnmsiHomeEntryHomeTerminationTypeInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeEntryHomeTerminationTypeInternalKey_Object = MibTableColumn
jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey = _JdsuOnmsiHomeEntryHomeTerminationTypeInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 6),
    _JdsuOnmsiHomeEntryHomeTerminationTypeInternalKey_Type()
)
jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey.setStatus("current")
_JdsuOnmsiHomeEntryLatestPeakInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeEntryLatestPeakInternalKey_Object = MibTableColumn
jdsuOnmsiHomeEntryLatestPeakInternalKey = _JdsuOnmsiHomeEntryLatestPeakInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 7),
    _JdsuOnmsiHomeEntryLatestPeakInternalKey_Type()
)
jdsuOnmsiHomeEntryLatestPeakInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryLatestPeakInternalKey.setStatus("current")
_JdsuOnmsiHomeEntryLatestPeakSeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiHomeEntryLatestPeakSeverity_Object = MibTableColumn
jdsuOnmsiHomeEntryLatestPeakSeverity = _JdsuOnmsiHomeEntryLatestPeakSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 8),
    _JdsuOnmsiHomeEntryLatestPeakSeverity_Type()
)
jdsuOnmsiHomeEntryLatestPeakSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryLatestPeakSeverity.setStatus("current")
_JdsuOnmsiHomeEntryLatestPeakStatus_Type = JdsuOnmsiPeakStatus
_JdsuOnmsiHomeEntryLatestPeakStatus_Object = MibTableColumn
jdsuOnmsiHomeEntryLatestPeakStatus = _JdsuOnmsiHomeEntryLatestPeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 9),
    _JdsuOnmsiHomeEntryLatestPeakStatus_Type()
)
jdsuOnmsiHomeEntryLatestPeakStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryLatestPeakStatus.setStatus("current")
_JdsuOnmsiHomeEntryVip_Type = TruthValue
_JdsuOnmsiHomeEntryVip_Object = MibTableColumn
jdsuOnmsiHomeEntryVip = _JdsuOnmsiHomeEntryVip_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 1, 1, 10),
    _JdsuOnmsiHomeEntryVip_Type()
)
jdsuOnmsiHomeEntryVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeEntryVip.setStatus("current")
_JdsuOnmsiHomeAdditionalAttributeTable_Object = MibTable
jdsuOnmsiHomeAdditionalAttributeTable = _JdsuOnmsiHomeAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiHomeAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiHomeAdditionalAttributeEntry = _JdsuOnmsiHomeAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 2, 1)
)
jdsuOnmsiHomeAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiHomeAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiHomeAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiHomeAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiHomeAdditionalAttributeEntryInternalKey = _JdsuOnmsiHomeAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 2, 1, 1),
    _JdsuOnmsiHomeAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiHomeAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiHomeAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiHomeAdditionalAttributeEntryName = _JdsuOnmsiHomeAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 2, 1, 2),
    _JdsuOnmsiHomeAdditionalAttributeEntryName_Type()
)
jdsuOnmsiHomeAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiHomeAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiHomeAdditionalAttributeEntryValue = _JdsuOnmsiHomeAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 2, 1, 3),
    _JdsuOnmsiHomeAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiHomeAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiHomeTerminationTypeTable_Object = MibTable
jdsuOnmsiHomeTerminationTypeTable = _JdsuOnmsiHomeTerminationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeTable.setStatus("current")
_JdsuOnmsiHomeTerminationTypeEntry_Object = MibTableRow
jdsuOnmsiHomeTerminationTypeEntry = _JdsuOnmsiHomeTerminationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 3, 1)
)
jdsuOnmsiHomeTerminationTypeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeEntry.setStatus("current")
_JdsuOnmsiHomeTerminationTypeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeTerminationTypeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiHomeTerminationTypeEntryInternalKey = _JdsuOnmsiHomeTerminationTypeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 3, 1, 1),
    _JdsuOnmsiHomeTerminationTypeEntryInternalKey_Type()
)
jdsuOnmsiHomeTerminationTypeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeEntryInternalKey.setStatus("current")
_JdsuOnmsiHomeTerminationTypeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeTerminationTypeEntryName_Object = MibTableColumn
jdsuOnmsiHomeTerminationTypeEntryName = _JdsuOnmsiHomeTerminationTypeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 3, 1, 2),
    _JdsuOnmsiHomeTerminationTypeEntryName_Type()
)
jdsuOnmsiHomeTerminationTypeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeEntryName.setStatus("current")
_JdsuOnmsiHomeTerminationTypeEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeTerminationTypeEntryDescription_Object = MibTableColumn
jdsuOnmsiHomeTerminationTypeEntryDescription = _JdsuOnmsiHomeTerminationTypeEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 3, 1, 3),
    _JdsuOnmsiHomeTerminationTypeEntryDescription_Type()
)
jdsuOnmsiHomeTerminationTypeEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeEntryDescription.setStatus("current")
_JdsuOnmsiHomeAttributeTable_Object = MibTable
jdsuOnmsiHomeAttributeTable = _JdsuOnmsiHomeAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeTable.setStatus("current")
_JdsuOnmsiHomeAttributeEntry_Object = MibTableRow
jdsuOnmsiHomeAttributeEntry = _JdsuOnmsiHomeAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4, 1)
)
jdsuOnmsiHomeAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeEntry.setStatus("current")
_JdsuOnmsiHomeAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeAttributeEntryName_Object = MibTableColumn
jdsuOnmsiHomeAttributeEntryName = _JdsuOnmsiHomeAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4, 1, 1),
    _JdsuOnmsiHomeAttributeEntryName_Type()
)
jdsuOnmsiHomeAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeEntryName.setStatus("current")
_JdsuOnmsiHomeAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiHomeAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiHomeAttributeEntryAdditional = _JdsuOnmsiHomeAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4, 1, 2),
    _JdsuOnmsiHomeAttributeEntryAdditional_Type()
)
jdsuOnmsiHomeAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiHomeAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiHomeAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiHomeAttributeEntryFindable = _JdsuOnmsiHomeAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4, 1, 3),
    _JdsuOnmsiHomeAttributeEntryFindable_Type()
)
jdsuOnmsiHomeAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeEntryFindable.setStatus("current")
_JdsuOnmsiHomeAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiHomeAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiHomeAttributeEntryUpdatable = _JdsuOnmsiHomeAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 1, 4, 1, 4),
    _JdsuOnmsiHomeAttributeEntryUpdatable_Type()
)
jdsuOnmsiHomeAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiHomeFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeFunctions = _JdsuOnmsiHomeFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2)
)
_JdsuOnmsiHomeTerminationTypeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeTerminationTypeLoad = _JdsuOnmsiHomeTerminationTypeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 1)
)
_JdsuOnmsiHomeTerminationTypeLoadExecute_Type = Integer32
_JdsuOnmsiHomeTerminationTypeLoadExecute_Object = MibScalar
jdsuOnmsiHomeTerminationTypeLoadExecute = _JdsuOnmsiHomeTerminationTypeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 1, 1),
    _JdsuOnmsiHomeTerminationTypeLoadExecute_Type()
)
jdsuOnmsiHomeTerminationTypeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeLoadExecute.setStatus("current")
_JdsuOnmsiHomeTerminationTypeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeTerminationTypeLoadError_Object = MibScalar
jdsuOnmsiHomeTerminationTypeLoadError = _JdsuOnmsiHomeTerminationTypeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 1, 2),
    _JdsuOnmsiHomeTerminationTypeLoadError_Type()
)
jdsuOnmsiHomeTerminationTypeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeLoadError.setStatus("current")
_JdsuOnmsiHomeGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeGet = _JdsuOnmsiHomeGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 2)
)
_JdsuOnmsiHomeGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeGetParamInternalKey_Object = MibScalar
jdsuOnmsiHomeGetParamInternalKey = _JdsuOnmsiHomeGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 2, 1),
    _JdsuOnmsiHomeGetParamInternalKey_Type()
)
jdsuOnmsiHomeGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeGetParamInternalKey.setStatus("current")
_JdsuOnmsiHomeGetExecute_Type = Integer32
_JdsuOnmsiHomeGetExecute_Object = MibScalar
jdsuOnmsiHomeGetExecute = _JdsuOnmsiHomeGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 2, 2),
    _JdsuOnmsiHomeGetExecute_Type()
)
jdsuOnmsiHomeGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeGetExecute.setStatus("current")
_JdsuOnmsiHomeGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeGetError_Object = MibScalar
jdsuOnmsiHomeGetError = _JdsuOnmsiHomeGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 2, 3),
    _JdsuOnmsiHomeGetError_Type()
)
jdsuOnmsiHomeGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeGetError.setStatus("current")
_JdsuOnmsiHomeFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeFind = _JdsuOnmsiHomeFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 3)
)
_JdsuOnmsiHomeFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeFindParamAttribute_Object = MibScalar
jdsuOnmsiHomeFindParamAttribute = _JdsuOnmsiHomeFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 3, 1),
    _JdsuOnmsiHomeFindParamAttribute_Type()
)
jdsuOnmsiHomeFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeFindParamAttribute.setStatus("current")
_JdsuOnmsiHomeFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeFindParamValue_Object = MibScalar
jdsuOnmsiHomeFindParamValue = _JdsuOnmsiHomeFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 3, 2),
    _JdsuOnmsiHomeFindParamValue_Type()
)
jdsuOnmsiHomeFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeFindParamValue.setStatus("current")
_JdsuOnmsiHomeFindExecute_Type = Integer32
_JdsuOnmsiHomeFindExecute_Object = MibScalar
jdsuOnmsiHomeFindExecute = _JdsuOnmsiHomeFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 3, 3),
    _JdsuOnmsiHomeFindExecute_Type()
)
jdsuOnmsiHomeFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeFindExecute.setStatus("current")
_JdsuOnmsiHomeFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeFindError_Object = MibScalar
jdsuOnmsiHomeFindError = _JdsuOnmsiHomeFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 3, 4),
    _JdsuOnmsiHomeFindError_Type()
)
jdsuOnmsiHomeFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeFindError.setStatus("current")
_JdsuOnmsiHomeStartTest_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeStartTest = _JdsuOnmsiHomeStartTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 4)
)
_JdsuOnmsiHomeStartTestParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiHomeStartTestParamInternalKey_Object = MibScalar
jdsuOnmsiHomeStartTestParamInternalKey = _JdsuOnmsiHomeStartTestParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 4, 1),
    _JdsuOnmsiHomeStartTestParamInternalKey_Type()
)
jdsuOnmsiHomeStartTestParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeStartTestParamInternalKey.setStatus("current")
_JdsuOnmsiHomeStartTestExecute_Type = Integer32
_JdsuOnmsiHomeStartTestExecute_Object = MibScalar
jdsuOnmsiHomeStartTestExecute = _JdsuOnmsiHomeStartTestExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 4, 2),
    _JdsuOnmsiHomeStartTestExecute_Type()
)
jdsuOnmsiHomeStartTestExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeStartTestExecute.setStatus("current")
_JdsuOnmsiHomeStartTestError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeStartTestError_Object = MibScalar
jdsuOnmsiHomeStartTestError = _JdsuOnmsiHomeStartTestError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 4, 3),
    _JdsuOnmsiHomeStartTestError_Type()
)
jdsuOnmsiHomeStartTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeStartTestError.setStatus("current")
_JdsuOnmsiHomeAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiHomeAttributeLoad = _JdsuOnmsiHomeAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 5)
)
_JdsuOnmsiHomeAttributeLoadExecute_Type = Integer32
_JdsuOnmsiHomeAttributeLoadExecute_Object = MibScalar
jdsuOnmsiHomeAttributeLoadExecute = _JdsuOnmsiHomeAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 5, 1),
    _JdsuOnmsiHomeAttributeLoadExecute_Type()
)
jdsuOnmsiHomeAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeLoadExecute.setStatus("current")
_JdsuOnmsiHomeAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiHomeAttributeLoadError_Object = MibScalar
jdsuOnmsiHomeAttributeLoadError = _JdsuOnmsiHomeAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 1, 2, 5, 2),
    _JdsuOnmsiHomeAttributeLoadError_Type()
)
jdsuOnmsiHomeAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiHomeAttributeLoadError.setStatus("current")
_JdsuOnmsiPonService_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonService = _JdsuOnmsiPonService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2)
)
_JdsuOnmsiPonData_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonData = _JdsuOnmsiPonData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1)
)
_JdsuOnmsiPonTable_Object = MibTable
jdsuOnmsiPonTable = _JdsuOnmsiPonTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonTable.setStatus("current")
_JdsuOnmsiPonEntry_Object = MibTableRow
jdsuOnmsiPonEntry = _JdsuOnmsiPonEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1)
)
jdsuOnmsiPonEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntry.setStatus("current")
_JdsuOnmsiPonEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonEntryInternalKey_Object = MibTableColumn
jdsuOnmsiPonEntryInternalKey = _JdsuOnmsiPonEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 1),
    _JdsuOnmsiPonEntryInternalKey_Type()
)
jdsuOnmsiPonEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryInternalKey.setStatus("current")
_JdsuOnmsiPonEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonEntryName_Object = MibTableColumn
jdsuOnmsiPonEntryName = _JdsuOnmsiPonEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 2),
    _JdsuOnmsiPonEntryName_Type()
)
jdsuOnmsiPonEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryName.setStatus("current")
_JdsuOnmsiPonEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonEntryDescription_Object = MibTableColumn
jdsuOnmsiPonEntryDescription = _JdsuOnmsiPonEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 3),
    _JdsuOnmsiPonEntryDescription_Type()
)
jdsuOnmsiPonEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryDescription.setStatus("current")
_JdsuOnmsiPonEntryLatestTestInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonEntryLatestTestInternalKey_Object = MibTableColumn
jdsuOnmsiPonEntryLatestTestInternalKey = _JdsuOnmsiPonEntryLatestTestInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 4),
    _JdsuOnmsiPonEntryLatestTestInternalKey_Type()
)
jdsuOnmsiPonEntryLatestTestInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryLatestTestInternalKey.setStatus("current")
_JdsuOnmsiPonEntryOtuInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonEntryOtuInternalKey_Object = MibTableColumn
jdsuOnmsiPonEntryOtuInternalKey = _JdsuOnmsiPonEntryOtuInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 5),
    _JdsuOnmsiPonEntryOtuInternalKey_Type()
)
jdsuOnmsiPonEntryOtuInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryOtuInternalKey.setStatus("current")
_JdsuOnmsiPonEntryPortInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonEntryPortInternalKey_Object = MibTableColumn
jdsuOnmsiPonEntryPortInternalKey = _JdsuOnmsiPonEntryPortInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 6),
    _JdsuOnmsiPonEntryPortInternalKey_Type()
)
jdsuOnmsiPonEntryPortInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntryPortInternalKey.setStatus("current")
_JdsuOnmsiPonEntrySeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiPonEntrySeverity_Object = MibTableColumn
jdsuOnmsiPonEntrySeverity = _JdsuOnmsiPonEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 7),
    _JdsuOnmsiPonEntrySeverity_Type()
)
jdsuOnmsiPonEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntrySeverity.setStatus("current")
_JdsuOnmsiPonEntrySchedulingConfiguration_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonEntrySchedulingConfiguration_Object = MibTableColumn
jdsuOnmsiPonEntrySchedulingConfiguration = _JdsuOnmsiPonEntrySchedulingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 1, 1, 8),
    _JdsuOnmsiPonEntrySchedulingConfiguration_Type()
)
jdsuOnmsiPonEntrySchedulingConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonEntrySchedulingConfiguration.setStatus("current")
_JdsuOnmsiPonAdditionalAttributeTable_Object = MibTable
jdsuOnmsiPonAdditionalAttributeTable = _JdsuOnmsiPonAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiPonAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiPonAdditionalAttributeEntry = _JdsuOnmsiPonAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 2, 1)
)
jdsuOnmsiPonAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiPonAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiPonAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiPonAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiPonAdditionalAttributeEntryInternalKey = _JdsuOnmsiPonAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 2, 1, 1),
    _JdsuOnmsiPonAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiPonAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiPonAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiPonAdditionalAttributeEntryName = _JdsuOnmsiPonAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 2, 1, 2),
    _JdsuOnmsiPonAdditionalAttributeEntryName_Type()
)
jdsuOnmsiPonAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiPonAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiPonAdditionalAttributeEntryValue = _JdsuOnmsiPonAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 2, 1, 3),
    _JdsuOnmsiPonAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiPonAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiPonAttributeTable_Object = MibTable
jdsuOnmsiPonAttributeTable = _JdsuOnmsiPonAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeTable.setStatus("current")
_JdsuOnmsiPonAttributeEntry_Object = MibTableRow
jdsuOnmsiPonAttributeEntry = _JdsuOnmsiPonAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3, 1)
)
jdsuOnmsiPonAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeEntry.setStatus("current")
_JdsuOnmsiPonAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonAttributeEntryName_Object = MibTableColumn
jdsuOnmsiPonAttributeEntryName = _JdsuOnmsiPonAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3, 1, 1),
    _JdsuOnmsiPonAttributeEntryName_Type()
)
jdsuOnmsiPonAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeEntryName.setStatus("current")
_JdsuOnmsiPonAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiPonAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiPonAttributeEntryAdditional = _JdsuOnmsiPonAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3, 1, 2),
    _JdsuOnmsiPonAttributeEntryAdditional_Type()
)
jdsuOnmsiPonAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiPonAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiPonAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiPonAttributeEntryFindable = _JdsuOnmsiPonAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3, 1, 3),
    _JdsuOnmsiPonAttributeEntryFindable_Type()
)
jdsuOnmsiPonAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeEntryFindable.setStatus("current")
_JdsuOnmsiPonAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiPonAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiPonAttributeEntryUpdatable = _JdsuOnmsiPonAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 1, 3, 1, 4),
    _JdsuOnmsiPonAttributeEntryUpdatable_Type()
)
jdsuOnmsiPonAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiPonFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonFunctions = _JdsuOnmsiPonFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2)
)
_JdsuOnmsiPonGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonGet = _JdsuOnmsiPonGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 1)
)
_JdsuOnmsiPonGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonGetParamInternalKey_Object = MibScalar
jdsuOnmsiPonGetParamInternalKey = _JdsuOnmsiPonGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 1, 1),
    _JdsuOnmsiPonGetParamInternalKey_Type()
)
jdsuOnmsiPonGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonGetParamInternalKey.setStatus("current")
_JdsuOnmsiPonGetExecute_Type = Integer32
_JdsuOnmsiPonGetExecute_Object = MibScalar
jdsuOnmsiPonGetExecute = _JdsuOnmsiPonGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 1, 2),
    _JdsuOnmsiPonGetExecute_Type()
)
jdsuOnmsiPonGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonGetExecute.setStatus("current")
_JdsuOnmsiPonGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonGetError_Object = MibScalar
jdsuOnmsiPonGetError = _JdsuOnmsiPonGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 1, 3),
    _JdsuOnmsiPonGetError_Type()
)
jdsuOnmsiPonGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonGetError.setStatus("current")
_JdsuOnmsiPonFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonFind = _JdsuOnmsiPonFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 2)
)
_JdsuOnmsiPonFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonFindParamAttribute_Object = MibScalar
jdsuOnmsiPonFindParamAttribute = _JdsuOnmsiPonFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 2, 1),
    _JdsuOnmsiPonFindParamAttribute_Type()
)
jdsuOnmsiPonFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonFindParamAttribute.setStatus("current")
_JdsuOnmsiPonFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonFindParamValue_Object = MibScalar
jdsuOnmsiPonFindParamValue = _JdsuOnmsiPonFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 2, 2),
    _JdsuOnmsiPonFindParamValue_Type()
)
jdsuOnmsiPonFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonFindParamValue.setStatus("current")
_JdsuOnmsiPonFindExecute_Type = Integer32
_JdsuOnmsiPonFindExecute_Object = MibScalar
jdsuOnmsiPonFindExecute = _JdsuOnmsiPonFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 2, 3),
    _JdsuOnmsiPonFindExecute_Type()
)
jdsuOnmsiPonFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonFindExecute.setStatus("current")
_JdsuOnmsiPonFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonFindError_Object = MibScalar
jdsuOnmsiPonFindError = _JdsuOnmsiPonFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 2, 4),
    _JdsuOnmsiPonFindError_Type()
)
jdsuOnmsiPonFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonFindError.setStatus("current")
_JdsuOnmsiPonStartTest_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonStartTest = _JdsuOnmsiPonStartTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 3)
)
_JdsuOnmsiPonStartTestParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPonStartTestParamInternalKey_Object = MibScalar
jdsuOnmsiPonStartTestParamInternalKey = _JdsuOnmsiPonStartTestParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 3, 1),
    _JdsuOnmsiPonStartTestParamInternalKey_Type()
)
jdsuOnmsiPonStartTestParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonStartTestParamInternalKey.setStatus("current")
_JdsuOnmsiPonStartTestExecute_Type = Integer32
_JdsuOnmsiPonStartTestExecute_Object = MibScalar
jdsuOnmsiPonStartTestExecute = _JdsuOnmsiPonStartTestExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 3, 2),
    _JdsuOnmsiPonStartTestExecute_Type()
)
jdsuOnmsiPonStartTestExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonStartTestExecute.setStatus("current")
_JdsuOnmsiPonStartTestError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonStartTestError_Object = MibScalar
jdsuOnmsiPonStartTestError = _JdsuOnmsiPonStartTestError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 3, 3),
    _JdsuOnmsiPonStartTestError_Type()
)
jdsuOnmsiPonStartTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonStartTestError.setStatus("current")
_JdsuOnmsiPonAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiPonAttributeLoad = _JdsuOnmsiPonAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 4)
)
_JdsuOnmsiPonAttributeLoadExecute_Type = Integer32
_JdsuOnmsiPonAttributeLoadExecute_Object = MibScalar
jdsuOnmsiPonAttributeLoadExecute = _JdsuOnmsiPonAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 4, 1),
    _JdsuOnmsiPonAttributeLoadExecute_Type()
)
jdsuOnmsiPonAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeLoadExecute.setStatus("current")
_JdsuOnmsiPonAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPonAttributeLoadError_Object = MibScalar
jdsuOnmsiPonAttributeLoadError = _JdsuOnmsiPonAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 2, 2, 4, 2),
    _JdsuOnmsiPonAttributeLoadError_Type()
)
jdsuOnmsiPonAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPonAttributeLoadError.setStatus("current")
_JdsuOnmsiPeakService_ObjectIdentity = ObjectIdentity
jdsuOnmsiPeakService = _JdsuOnmsiPeakService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3)
)
_JdsuOnmsiPeakData_ObjectIdentity = ObjectIdentity
jdsuOnmsiPeakData = _JdsuOnmsiPeakData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1)
)
_JdsuOnmsiPeakTable_Object = MibTable
jdsuOnmsiPeakTable = _JdsuOnmsiPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiPeakTable.setStatus("current")
_JdsuOnmsiPeakEntry_Object = MibTableRow
jdsuOnmsiPeakEntry = _JdsuOnmsiPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1)
)
jdsuOnmsiPeakEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntry.setStatus("current")
_JdsuOnmsiPeakEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPeakEntryInternalKey_Object = MibTableColumn
jdsuOnmsiPeakEntryInternalKey = _JdsuOnmsiPeakEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 1),
    _JdsuOnmsiPeakEntryInternalKey_Type()
)
jdsuOnmsiPeakEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryInternalKey.setStatus("current")
_JdsuOnmsiPeakEntryTestInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPeakEntryTestInternalKey_Object = MibTableColumn
jdsuOnmsiPeakEntryTestInternalKey = _JdsuOnmsiPeakEntryTestInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 2),
    _JdsuOnmsiPeakEntryTestInternalKey_Type()
)
jdsuOnmsiPeakEntryTestInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryTestInternalKey.setStatus("current")
_JdsuOnmsiPeakEntryDate_Type = DateAndTime
_JdsuOnmsiPeakEntryDate_Object = MibTableColumn
jdsuOnmsiPeakEntryDate = _JdsuOnmsiPeakEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 3),
    _JdsuOnmsiPeakEntryDate_Type()
)
jdsuOnmsiPeakEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryDate.setStatus("current")
_JdsuOnmsiPeakEntryIsAReference_Type = TruthValue
_JdsuOnmsiPeakEntryIsAReference_Object = MibTableColumn
jdsuOnmsiPeakEntryIsAReference = _JdsuOnmsiPeakEntryIsAReference_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 4),
    _JdsuOnmsiPeakEntryIsAReference_Type()
)
jdsuOnmsiPeakEntryIsAReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryIsAReference.setStatus("current")
_JdsuOnmsiPeakEntryDistance_Type = Integer32
_JdsuOnmsiPeakEntryDistance_Object = MibTableColumn
jdsuOnmsiPeakEntryDistance = _JdsuOnmsiPeakEntryDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 5),
    _JdsuOnmsiPeakEntryDistance_Type()
)
jdsuOnmsiPeakEntryDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryDistance.setStatus("current")
_JdsuOnmsiPeakEntryLevel_Type = Integer32
_JdsuOnmsiPeakEntryLevel_Object = MibTableColumn
jdsuOnmsiPeakEntryLevel = _JdsuOnmsiPeakEntryLevel_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 6),
    _JdsuOnmsiPeakEntryLevel_Type()
)
jdsuOnmsiPeakEntryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryLevel.setStatus("current")
_JdsuOnmsiPeakEntryPower_Type = Integer32
_JdsuOnmsiPeakEntryPower_Object = MibTableColumn
jdsuOnmsiPeakEntryPower = _JdsuOnmsiPeakEntryPower_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 7),
    _JdsuOnmsiPeakEntryPower_Type()
)
jdsuOnmsiPeakEntryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryPower.setStatus("current")
_JdsuOnmsiPeakEntryIsPowerMeasured_Type = TruthValue
_JdsuOnmsiPeakEntryIsPowerMeasured_Object = MibTableColumn
jdsuOnmsiPeakEntryIsPowerMeasured = _JdsuOnmsiPeakEntryIsPowerMeasured_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 8),
    _JdsuOnmsiPeakEntryIsPowerMeasured_Type()
)
jdsuOnmsiPeakEntryIsPowerMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryIsPowerMeasured.setStatus("current")
_JdsuOnmsiPeakEntrySeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiPeakEntrySeverity_Object = MibTableColumn
jdsuOnmsiPeakEntrySeverity = _JdsuOnmsiPeakEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 9),
    _JdsuOnmsiPeakEntrySeverity_Type()
)
jdsuOnmsiPeakEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntrySeverity.setStatus("current")
_JdsuOnmsiPeakEntryStatus_Type = JdsuOnmsiPeakStatus
_JdsuOnmsiPeakEntryStatus_Object = MibTableColumn
jdsuOnmsiPeakEntryStatus = _JdsuOnmsiPeakEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 10),
    _JdsuOnmsiPeakEntryStatus_Type()
)
jdsuOnmsiPeakEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryStatus.setStatus("current")
_JdsuOnmsiPeakEntryRefDistance_Type = Integer32
_JdsuOnmsiPeakEntryRefDistance_Object = MibTableColumn
jdsuOnmsiPeakEntryRefDistance = _JdsuOnmsiPeakEntryRefDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 11),
    _JdsuOnmsiPeakEntryRefDistance_Type()
)
jdsuOnmsiPeakEntryRefDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryRefDistance.setStatus("current")
_JdsuOnmsiPeakEntryRefLevel_Type = Integer32
_JdsuOnmsiPeakEntryRefLevel_Object = MibTableColumn
jdsuOnmsiPeakEntryRefLevel = _JdsuOnmsiPeakEntryRefLevel_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 12),
    _JdsuOnmsiPeakEntryRefLevel_Type()
)
jdsuOnmsiPeakEntryRefLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryRefLevel.setStatus("current")
_JdsuOnmsiPeakEntryRefPower_Type = Integer32
_JdsuOnmsiPeakEntryRefPower_Object = MibTableColumn
jdsuOnmsiPeakEntryRefPower = _JdsuOnmsiPeakEntryRefPower_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 13),
    _JdsuOnmsiPeakEntryRefPower_Type()
)
jdsuOnmsiPeakEntryRefPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryRefPower.setStatus("current")
_JdsuOnmsiPeakEntryRefIsPowerMeasured_Type = TruthValue
_JdsuOnmsiPeakEntryRefIsPowerMeasured_Object = MibTableColumn
jdsuOnmsiPeakEntryRefIsPowerMeasured = _JdsuOnmsiPeakEntryRefIsPowerMeasured_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 14),
    _JdsuOnmsiPeakEntryRefIsPowerMeasured_Type()
)
jdsuOnmsiPeakEntryRefIsPowerMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryRefIsPowerMeasured.setStatus("current")
_JdsuOnmsiPeakEntryRefDate_Type = DateAndTime
_JdsuOnmsiPeakEntryRefDate_Object = MibTableColumn
jdsuOnmsiPeakEntryRefDate = _JdsuOnmsiPeakEntryRefDate_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 15),
    _JdsuOnmsiPeakEntryRefDate_Type()
)
jdsuOnmsiPeakEntryRefDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryRefDate.setStatus("current")
_JdsuOnmsiPeakEntryType_Type = JdsuOnmsiPeakType
_JdsuOnmsiPeakEntryType_Object = MibTableColumn
jdsuOnmsiPeakEntryType = _JdsuOnmsiPeakEntryType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 16),
    _JdsuOnmsiPeakEntryType_Type()
)
jdsuOnmsiPeakEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryType.setStatus("current")
_JdsuOnmsiPeakEntryHomeTerminationTypeInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPeakEntryHomeTerminationTypeInternalKey_Object = MibTableColumn
jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey = _JdsuOnmsiPeakEntryHomeTerminationTypeInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 17),
    _JdsuOnmsiPeakEntryHomeTerminationTypeInternalKey_Type()
)
jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey.setStatus("current")
_JdsuOnmsiPeakEntryHomeInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPeakEntryHomeInternalKey_Object = MibTableColumn
jdsuOnmsiPeakEntryHomeInternalKey = _JdsuOnmsiPeakEntryHomeInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 1, 1, 1, 18),
    _JdsuOnmsiPeakEntryHomeInternalKey_Type()
)
jdsuOnmsiPeakEntryHomeInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakEntryHomeInternalKey.setStatus("current")
_JdsuOnmsiPeakFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiPeakFunctions = _JdsuOnmsiPeakFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2)
)
_JdsuOnmsiPeakGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiPeakGet = _JdsuOnmsiPeakGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 1)
)
_JdsuOnmsiPeakGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiPeakGetParamInternalKey_Object = MibScalar
jdsuOnmsiPeakGetParamInternalKey = _JdsuOnmsiPeakGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 1, 1),
    _JdsuOnmsiPeakGetParamInternalKey_Type()
)
jdsuOnmsiPeakGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakGetParamInternalKey.setStatus("current")
_JdsuOnmsiPeakGetExecute_Type = Integer32
_JdsuOnmsiPeakGetExecute_Object = MibScalar
jdsuOnmsiPeakGetExecute = _JdsuOnmsiPeakGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 1, 2),
    _JdsuOnmsiPeakGetExecute_Type()
)
jdsuOnmsiPeakGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakGetExecute.setStatus("current")
_JdsuOnmsiPeakGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPeakGetError_Object = MibScalar
jdsuOnmsiPeakGetError = _JdsuOnmsiPeakGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 1, 3),
    _JdsuOnmsiPeakGetError_Type()
)
jdsuOnmsiPeakGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakGetError.setStatus("current")
_JdsuOnmsiPeakFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiPeakFind = _JdsuOnmsiPeakFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 2)
)
_JdsuOnmsiPeakFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPeakFindParamAttribute_Object = MibScalar
jdsuOnmsiPeakFindParamAttribute = _JdsuOnmsiPeakFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 2, 1),
    _JdsuOnmsiPeakFindParamAttribute_Type()
)
jdsuOnmsiPeakFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakFindParamAttribute.setStatus("current")
_JdsuOnmsiPeakFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPeakFindParamValue_Object = MibScalar
jdsuOnmsiPeakFindParamValue = _JdsuOnmsiPeakFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 2, 2),
    _JdsuOnmsiPeakFindParamValue_Type()
)
jdsuOnmsiPeakFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakFindParamValue.setStatus("current")
_JdsuOnmsiPeakFindExecute_Type = Integer32
_JdsuOnmsiPeakFindExecute_Object = MibScalar
jdsuOnmsiPeakFindExecute = _JdsuOnmsiPeakFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 2, 3),
    _JdsuOnmsiPeakFindExecute_Type()
)
jdsuOnmsiPeakFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakFindExecute.setStatus("current")
_JdsuOnmsiPeakFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiPeakFindError_Object = MibScalar
jdsuOnmsiPeakFindError = _JdsuOnmsiPeakFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 3, 2, 2, 4),
    _JdsuOnmsiPeakFindError_Type()
)
jdsuOnmsiPeakFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiPeakFindError.setStatus("current")
_JdsuOnmsiLinkService_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkService = _JdsuOnmsiLinkService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4)
)
_JdsuOnmsiLinkData_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkData = _JdsuOnmsiLinkData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1)
)
_JdsuOnmsiLinkTable_Object = MibTable
jdsuOnmsiLinkTable = _JdsuOnmsiLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkTable.setStatus("current")
_JdsuOnmsiLinkEntry_Object = MibTableRow
jdsuOnmsiLinkEntry = _JdsuOnmsiLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1)
)
jdsuOnmsiLinkEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntry.setStatus("current")
_JdsuOnmsiLinkEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiLinkEntryInternalKey_Object = MibTableColumn
jdsuOnmsiLinkEntryInternalKey = _JdsuOnmsiLinkEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 1),
    _JdsuOnmsiLinkEntryInternalKey_Type()
)
jdsuOnmsiLinkEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntryInternalKey.setStatus("current")
_JdsuOnmsiLinkEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkEntryName_Object = MibTableColumn
jdsuOnmsiLinkEntryName = _JdsuOnmsiLinkEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 2),
    _JdsuOnmsiLinkEntryName_Type()
)
jdsuOnmsiLinkEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntryName.setStatus("current")
_JdsuOnmsiLinkEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkEntryDescription_Object = MibTableColumn
jdsuOnmsiLinkEntryDescription = _JdsuOnmsiLinkEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 3),
    _JdsuOnmsiLinkEntryDescription_Type()
)
jdsuOnmsiLinkEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntryDescription.setStatus("current")
_JdsuOnmsiLinkEntryMeasureEnabled_Type = TruthValue
_JdsuOnmsiLinkEntryMeasureEnabled_Object = MibTableColumn
jdsuOnmsiLinkEntryMeasureEnabled = _JdsuOnmsiLinkEntryMeasureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 4),
    _JdsuOnmsiLinkEntryMeasureEnabled_Type()
)
jdsuOnmsiLinkEntryMeasureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntryMeasureEnabled.setStatus("current")
_JdsuOnmsiLinkEntryOtuInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiLinkEntryOtuInternalKey_Object = MibTableColumn
jdsuOnmsiLinkEntryOtuInternalKey = _JdsuOnmsiLinkEntryOtuInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 5),
    _JdsuOnmsiLinkEntryOtuInternalKey_Type()
)
jdsuOnmsiLinkEntryOtuInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntryOtuInternalKey.setStatus("current")
_JdsuOnmsiLinkEntrySeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiLinkEntrySeverity_Object = MibTableColumn
jdsuOnmsiLinkEntrySeverity = _JdsuOnmsiLinkEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 1, 1, 6),
    _JdsuOnmsiLinkEntrySeverity_Type()
)
jdsuOnmsiLinkEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkEntrySeverity.setStatus("current")
_JdsuOnmsiLinkAdditionalAttributeTable_Object = MibTable
jdsuOnmsiLinkAdditionalAttributeTable = _JdsuOnmsiLinkAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiLinkAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiLinkAdditionalAttributeEntry = _JdsuOnmsiLinkAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 2, 1)
)
jdsuOnmsiLinkAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiLinkAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiLinkAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiLinkAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiLinkAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiLinkAdditionalAttributeEntryInternalKey = _JdsuOnmsiLinkAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 2, 1, 1),
    _JdsuOnmsiLinkAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiLinkAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiLinkAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiLinkAdditionalAttributeEntryName = _JdsuOnmsiLinkAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 2, 1, 2),
    _JdsuOnmsiLinkAdditionalAttributeEntryName_Type()
)
jdsuOnmsiLinkAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiLinkAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiLinkAdditionalAttributeEntryValue = _JdsuOnmsiLinkAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 2, 1, 3),
    _JdsuOnmsiLinkAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiLinkAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiLinkAttributeTable_Object = MibTable
jdsuOnmsiLinkAttributeTable = _JdsuOnmsiLinkAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeTable.setStatus("current")
_JdsuOnmsiLinkAttributeEntry_Object = MibTableRow
jdsuOnmsiLinkAttributeEntry = _JdsuOnmsiLinkAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3, 1)
)
jdsuOnmsiLinkAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeEntry.setStatus("current")
_JdsuOnmsiLinkAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkAttributeEntryName_Object = MibTableColumn
jdsuOnmsiLinkAttributeEntryName = _JdsuOnmsiLinkAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3, 1, 1),
    _JdsuOnmsiLinkAttributeEntryName_Type()
)
jdsuOnmsiLinkAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeEntryName.setStatus("current")
_JdsuOnmsiLinkAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiLinkAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiLinkAttributeEntryAdditional = _JdsuOnmsiLinkAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3, 1, 2),
    _JdsuOnmsiLinkAttributeEntryAdditional_Type()
)
jdsuOnmsiLinkAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiLinkAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiLinkAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiLinkAttributeEntryFindable = _JdsuOnmsiLinkAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3, 1, 3),
    _JdsuOnmsiLinkAttributeEntryFindable_Type()
)
jdsuOnmsiLinkAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeEntryFindable.setStatus("current")
_JdsuOnmsiLinkAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiLinkAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiLinkAttributeEntryUpdatable = _JdsuOnmsiLinkAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 1, 3, 1, 4),
    _JdsuOnmsiLinkAttributeEntryUpdatable_Type()
)
jdsuOnmsiLinkAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiLinkFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkFunctions = _JdsuOnmsiLinkFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2)
)
_JdsuOnmsiLinkGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkGet = _JdsuOnmsiLinkGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 1)
)
_JdsuOnmsiLinkGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiLinkGetParamInternalKey_Object = MibScalar
jdsuOnmsiLinkGetParamInternalKey = _JdsuOnmsiLinkGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 1, 1),
    _JdsuOnmsiLinkGetParamInternalKey_Type()
)
jdsuOnmsiLinkGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkGetParamInternalKey.setStatus("current")
_JdsuOnmsiLinkGetExecute_Type = Integer32
_JdsuOnmsiLinkGetExecute_Object = MibScalar
jdsuOnmsiLinkGetExecute = _JdsuOnmsiLinkGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 1, 2),
    _JdsuOnmsiLinkGetExecute_Type()
)
jdsuOnmsiLinkGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkGetExecute.setStatus("current")
_JdsuOnmsiLinkGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkGetError_Object = MibScalar
jdsuOnmsiLinkGetError = _JdsuOnmsiLinkGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 1, 3),
    _JdsuOnmsiLinkGetError_Type()
)
jdsuOnmsiLinkGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkGetError.setStatus("current")
_JdsuOnmsiLinkFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkFind = _JdsuOnmsiLinkFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 2)
)
_JdsuOnmsiLinkFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkFindParamAttribute_Object = MibScalar
jdsuOnmsiLinkFindParamAttribute = _JdsuOnmsiLinkFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 2, 1),
    _JdsuOnmsiLinkFindParamAttribute_Type()
)
jdsuOnmsiLinkFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkFindParamAttribute.setStatus("current")
_JdsuOnmsiLinkFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkFindParamValue_Object = MibScalar
jdsuOnmsiLinkFindParamValue = _JdsuOnmsiLinkFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 2, 2),
    _JdsuOnmsiLinkFindParamValue_Type()
)
jdsuOnmsiLinkFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkFindParamValue.setStatus("current")
_JdsuOnmsiLinkFindExecute_Type = Integer32
_JdsuOnmsiLinkFindExecute_Object = MibScalar
jdsuOnmsiLinkFindExecute = _JdsuOnmsiLinkFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 2, 3),
    _JdsuOnmsiLinkFindExecute_Type()
)
jdsuOnmsiLinkFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkFindExecute.setStatus("current")
_JdsuOnmsiLinkFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkFindError_Object = MibScalar
jdsuOnmsiLinkFindError = _JdsuOnmsiLinkFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 2, 4),
    _JdsuOnmsiLinkFindError_Type()
)
jdsuOnmsiLinkFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkFindError.setStatus("current")
_JdsuOnmsiLinkUpdate_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkUpdate = _JdsuOnmsiLinkUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 3)
)
_JdsuOnmsiLinkUpdateParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiLinkUpdateParamInternalKey_Object = MibScalar
jdsuOnmsiLinkUpdateParamInternalKey = _JdsuOnmsiLinkUpdateParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 3, 1),
    _JdsuOnmsiLinkUpdateParamInternalKey_Type()
)
jdsuOnmsiLinkUpdateParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkUpdateParamInternalKey.setStatus("current")
_JdsuOnmsiLinkUpdateExecute_Type = Integer32
_JdsuOnmsiLinkUpdateExecute_Object = MibScalar
jdsuOnmsiLinkUpdateExecute = _JdsuOnmsiLinkUpdateExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 3, 2),
    _JdsuOnmsiLinkUpdateExecute_Type()
)
jdsuOnmsiLinkUpdateExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkUpdateExecute.setStatus("current")
_JdsuOnmsiLinkUpdateError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkUpdateError_Object = MibScalar
jdsuOnmsiLinkUpdateError = _JdsuOnmsiLinkUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 3, 3),
    _JdsuOnmsiLinkUpdateError_Type()
)
jdsuOnmsiLinkUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkUpdateError.setStatus("current")
_JdsuOnmsiLinkAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiLinkAttributeLoad = _JdsuOnmsiLinkAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 4)
)
_JdsuOnmsiLinkAttributeLoadExecute_Type = Integer32
_JdsuOnmsiLinkAttributeLoadExecute_Object = MibScalar
jdsuOnmsiLinkAttributeLoadExecute = _JdsuOnmsiLinkAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 4, 1),
    _JdsuOnmsiLinkAttributeLoadExecute_Type()
)
jdsuOnmsiLinkAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeLoadExecute.setStatus("current")
_JdsuOnmsiLinkAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiLinkAttributeLoadError_Object = MibScalar
jdsuOnmsiLinkAttributeLoadError = _JdsuOnmsiLinkAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 4, 2, 4, 2),
    _JdsuOnmsiLinkAttributeLoadError_Type()
)
jdsuOnmsiLinkAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiLinkAttributeLoadError.setStatus("current")
_JdsuOnmsiMonitoringTestService_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestService = _JdsuOnmsiMonitoringTestService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5)
)
_JdsuOnmsiMonitoringTestData_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestData = _JdsuOnmsiMonitoringTestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1)
)
_JdsuOnmsiMonitoringTestTable_Object = MibTable
jdsuOnmsiMonitoringTestTable = _JdsuOnmsiMonitoringTestTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestTable.setStatus("current")
_JdsuOnmsiMonitoringTestEntry_Object = MibTableRow
jdsuOnmsiMonitoringTestEntry = _JdsuOnmsiMonitoringTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1)
)
jdsuOnmsiMonitoringTestEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntry.setStatus("current")
_JdsuOnmsiMonitoringTestEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiMonitoringTestEntryInternalKey_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryInternalKey = _JdsuOnmsiMonitoringTestEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 1),
    _JdsuOnmsiMonitoringTestEntryInternalKey_Type()
)
jdsuOnmsiMonitoringTestEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryInternalKey.setStatus("current")
_JdsuOnmsiMonitoringTestEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestEntryName_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryName = _JdsuOnmsiMonitoringTestEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 2),
    _JdsuOnmsiMonitoringTestEntryName_Type()
)
jdsuOnmsiMonitoringTestEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryName.setStatus("current")
_JdsuOnmsiMonitoringTestEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestEntryDescription_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryDescription = _JdsuOnmsiMonitoringTestEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 3),
    _JdsuOnmsiMonitoringTestEntryDescription_Type()
)
jdsuOnmsiMonitoringTestEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryDescription.setStatus("current")
_JdsuOnmsiMonitoringTestEntryLinkInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiMonitoringTestEntryLinkInternalKey_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryLinkInternalKey = _JdsuOnmsiMonitoringTestEntryLinkInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 4),
    _JdsuOnmsiMonitoringTestEntryLinkInternalKey_Type()
)
jdsuOnmsiMonitoringTestEntryLinkInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryLinkInternalKey.setStatus("current")
_JdsuOnmsiMonitoringTestEntryDisplayOrder_Type = Integer32
_JdsuOnmsiMonitoringTestEntryDisplayOrder_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryDisplayOrder = _JdsuOnmsiMonitoringTestEntryDisplayOrder_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 5),
    _JdsuOnmsiMonitoringTestEntryDisplayOrder_Type()
)
jdsuOnmsiMonitoringTestEntryDisplayOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryDisplayOrder.setStatus("current")
_JdsuOnmsiMonitoringTestEntrySeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiMonitoringTestEntrySeverity_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntrySeverity = _JdsuOnmsiMonitoringTestEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 6),
    _JdsuOnmsiMonitoringTestEntrySeverity_Type()
)
jdsuOnmsiMonitoringTestEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntrySeverity.setStatus("current")
_JdsuOnmsiMonitoringTestEntryDetectionConfiguration_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestEntryDetectionConfiguration_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryDetectionConfiguration = _JdsuOnmsiMonitoringTestEntryDetectionConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 7),
    _JdsuOnmsiMonitoringTestEntryDetectionConfiguration_Type()
)
jdsuOnmsiMonitoringTestEntryDetectionConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryDetectionConfiguration.setStatus("current")
_JdsuOnmsiMonitoringTestEntryLocalizationConfiguration_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestEntryLocalizationConfiguration_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntryLocalizationConfiguration = _JdsuOnmsiMonitoringTestEntryLocalizationConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 8),
    _JdsuOnmsiMonitoringTestEntryLocalizationConfiguration_Type()
)
jdsuOnmsiMonitoringTestEntryLocalizationConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntryLocalizationConfiguration.setStatus("current")
_JdsuOnmsiMonitoringTestEntrySchedulingConfiguration_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestEntrySchedulingConfiguration_Object = MibTableColumn
jdsuOnmsiMonitoringTestEntrySchedulingConfiguration = _JdsuOnmsiMonitoringTestEntrySchedulingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 1, 1, 9),
    _JdsuOnmsiMonitoringTestEntrySchedulingConfiguration_Type()
)
jdsuOnmsiMonitoringTestEntrySchedulingConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestEntrySchedulingConfiguration.setStatus("current")
_JdsuOnmsiMonitoringTestAdditionalAttributeTable_Object = MibTable
jdsuOnmsiMonitoringTestAdditionalAttributeTable = _JdsuOnmsiMonitoringTestAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiMonitoringTestAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiMonitoringTestAdditionalAttributeEntry = _JdsuOnmsiMonitoringTestAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 2, 1)
)
jdsuOnmsiMonitoringTestAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey = _JdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 2, 1, 1),
    _JdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiMonitoringTestAdditionalAttributeEntryName = _JdsuOnmsiMonitoringTestAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 2, 1, 2),
    _JdsuOnmsiMonitoringTestAdditionalAttributeEntryName_Type()
)
jdsuOnmsiMonitoringTestAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue = _JdsuOnmsiMonitoringTestAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 2, 1, 3),
    _JdsuOnmsiMonitoringTestAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeTable_Object = MibTable
jdsuOnmsiMonitoringTestAttributeTable = _JdsuOnmsiMonitoringTestAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeTable.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeEntry_Object = MibTableRow
jdsuOnmsiMonitoringTestAttributeEntry = _JdsuOnmsiMonitoringTestAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3, 1)
)
jdsuOnmsiMonitoringTestAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeEntry.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestAttributeEntryName_Object = MibTableColumn
jdsuOnmsiMonitoringTestAttributeEntryName = _JdsuOnmsiMonitoringTestAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3, 1, 1),
    _JdsuOnmsiMonitoringTestAttributeEntryName_Type()
)
jdsuOnmsiMonitoringTestAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeEntryName.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiMonitoringTestAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiMonitoringTestAttributeEntryAdditional = _JdsuOnmsiMonitoringTestAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3, 1, 2),
    _JdsuOnmsiMonitoringTestAttributeEntryAdditional_Type()
)
jdsuOnmsiMonitoringTestAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiMonitoringTestAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiMonitoringTestAttributeEntryFindable = _JdsuOnmsiMonitoringTestAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3, 1, 3),
    _JdsuOnmsiMonitoringTestAttributeEntryFindable_Type()
)
jdsuOnmsiMonitoringTestAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeEntryFindable.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiMonitoringTestAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiMonitoringTestAttributeEntryUpdatable = _JdsuOnmsiMonitoringTestAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 1, 3, 1, 4),
    _JdsuOnmsiMonitoringTestAttributeEntryUpdatable_Type()
)
jdsuOnmsiMonitoringTestAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiMonitoringTestFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestFunctions = _JdsuOnmsiMonitoringTestFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2)
)
_JdsuOnmsiMonitoringTestGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestGet = _JdsuOnmsiMonitoringTestGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 1)
)
_JdsuOnmsiMonitoringTestGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiMonitoringTestGetParamInternalKey_Object = MibScalar
jdsuOnmsiMonitoringTestGetParamInternalKey = _JdsuOnmsiMonitoringTestGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 1, 1),
    _JdsuOnmsiMonitoringTestGetParamInternalKey_Type()
)
jdsuOnmsiMonitoringTestGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestGetParamInternalKey.setStatus("current")
_JdsuOnmsiMonitoringTestGetExecute_Type = Integer32
_JdsuOnmsiMonitoringTestGetExecute_Object = MibScalar
jdsuOnmsiMonitoringTestGetExecute = _JdsuOnmsiMonitoringTestGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 1, 2),
    _JdsuOnmsiMonitoringTestGetExecute_Type()
)
jdsuOnmsiMonitoringTestGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestGetExecute.setStatus("current")
_JdsuOnmsiMonitoringTestGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestGetError_Object = MibScalar
jdsuOnmsiMonitoringTestGetError = _JdsuOnmsiMonitoringTestGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 1, 3),
    _JdsuOnmsiMonitoringTestGetError_Type()
)
jdsuOnmsiMonitoringTestGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestGetError.setStatus("current")
_JdsuOnmsiMonitoringTestFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestFind = _JdsuOnmsiMonitoringTestFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 2)
)
_JdsuOnmsiMonitoringTestFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestFindParamAttribute_Object = MibScalar
jdsuOnmsiMonitoringTestFindParamAttribute = _JdsuOnmsiMonitoringTestFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 2, 1),
    _JdsuOnmsiMonitoringTestFindParamAttribute_Type()
)
jdsuOnmsiMonitoringTestFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestFindParamAttribute.setStatus("current")
_JdsuOnmsiMonitoringTestFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestFindParamValue_Object = MibScalar
jdsuOnmsiMonitoringTestFindParamValue = _JdsuOnmsiMonitoringTestFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 2, 2),
    _JdsuOnmsiMonitoringTestFindParamValue_Type()
)
jdsuOnmsiMonitoringTestFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestFindParamValue.setStatus("current")
_JdsuOnmsiMonitoringTestFindExecute_Type = Integer32
_JdsuOnmsiMonitoringTestFindExecute_Object = MibScalar
jdsuOnmsiMonitoringTestFindExecute = _JdsuOnmsiMonitoringTestFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 2, 3),
    _JdsuOnmsiMonitoringTestFindExecute_Type()
)
jdsuOnmsiMonitoringTestFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestFindExecute.setStatus("current")
_JdsuOnmsiMonitoringTestFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestFindError_Object = MibScalar
jdsuOnmsiMonitoringTestFindError = _JdsuOnmsiMonitoringTestFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 2, 4),
    _JdsuOnmsiMonitoringTestFindError_Type()
)
jdsuOnmsiMonitoringTestFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestFindError.setStatus("current")
_JdsuOnmsiMonitoringTestStartTest_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestStartTest = _JdsuOnmsiMonitoringTestStartTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 3)
)
_JdsuOnmsiMonitoringTestStartTestParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiMonitoringTestStartTestParamInternalKey_Object = MibScalar
jdsuOnmsiMonitoringTestStartTestParamInternalKey = _JdsuOnmsiMonitoringTestStartTestParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 3, 1),
    _JdsuOnmsiMonitoringTestStartTestParamInternalKey_Type()
)
jdsuOnmsiMonitoringTestStartTestParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestStartTestParamInternalKey.setStatus("current")
_JdsuOnmsiMonitoringTestStartTestExecute_Type = Integer32
_JdsuOnmsiMonitoringTestStartTestExecute_Object = MibScalar
jdsuOnmsiMonitoringTestStartTestExecute = _JdsuOnmsiMonitoringTestStartTestExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 3, 2),
    _JdsuOnmsiMonitoringTestStartTestExecute_Type()
)
jdsuOnmsiMonitoringTestStartTestExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestStartTestExecute.setStatus("current")
_JdsuOnmsiMonitoringTestStartTestError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestStartTestError_Object = MibScalar
jdsuOnmsiMonitoringTestStartTestError = _JdsuOnmsiMonitoringTestStartTestError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 3, 3),
    _JdsuOnmsiMonitoringTestStartTestError_Type()
)
jdsuOnmsiMonitoringTestStartTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestStartTestError.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiMonitoringTestAttributeLoad = _JdsuOnmsiMonitoringTestAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 4)
)
_JdsuOnmsiMonitoringTestAttributeLoadExecute_Type = Integer32
_JdsuOnmsiMonitoringTestAttributeLoadExecute_Object = MibScalar
jdsuOnmsiMonitoringTestAttributeLoadExecute = _JdsuOnmsiMonitoringTestAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 4, 1),
    _JdsuOnmsiMonitoringTestAttributeLoadExecute_Type()
)
jdsuOnmsiMonitoringTestAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeLoadExecute.setStatus("current")
_JdsuOnmsiMonitoringTestAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiMonitoringTestAttributeLoadError_Object = MibScalar
jdsuOnmsiMonitoringTestAttributeLoadError = _JdsuOnmsiMonitoringTestAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 5, 2, 4, 2),
    _JdsuOnmsiMonitoringTestAttributeLoadError_Type()
)
jdsuOnmsiMonitoringTestAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestAttributeLoadError.setStatus("current")
_JdsuOnmsiAlarmService_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmService = _JdsuOnmsiAlarmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6)
)
_JdsuOnmsiAlarmData_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmData = _JdsuOnmsiAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1)
)
_JdsuOnmsiAlarmTypesTable_Object = MibTable
jdsuOnmsiAlarmTypesTable = _JdsuOnmsiAlarmTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmTypesTable.setStatus("current")
_JdsuOnmsiAlarmTypesEntry_Object = MibTableRow
jdsuOnmsiAlarmTypesEntry = _JdsuOnmsiAlarmTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 1, 1)
)
jdsuOnmsiAlarmTypesEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiAlarmTypeName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmTypesEntry.setStatus("current")
_JdsuOnmsiAlarmTypeName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmTypeName_Object = MibTableColumn
jdsuOnmsiAlarmTypeName = _JdsuOnmsiAlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 1, 1, 1),
    _JdsuOnmsiAlarmTypeName_Type()
)
jdsuOnmsiAlarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmTypeName.setStatus("current")
_JdsuOnmsiAlarmSpecificProblemsTable_Object = MibTable
jdsuOnmsiAlarmSpecificProblemsTable = _JdsuOnmsiAlarmSpecificProblemsTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSpecificProblemsTable.setStatus("current")
_JdsuOnmsiAlarmSpecificProblemsEntry_Object = MibTableRow
jdsuOnmsiAlarmSpecificProblemsEntry = _JdsuOnmsiAlarmSpecificProblemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 2, 1)
)
jdsuOnmsiAlarmSpecificProblemsEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSpecificProblemName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSpecificProblemsEntry.setStatus("current")
_JdsuOnmsiAlarmSpecificProblemName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmSpecificProblemName_Object = MibTableColumn
jdsuOnmsiAlarmSpecificProblemName = _JdsuOnmsiAlarmSpecificProblemName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 2, 1, 1),
    _JdsuOnmsiAlarmSpecificProblemName_Type()
)
jdsuOnmsiAlarmSpecificProblemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSpecificProblemName.setStatus("current")
_JdsuOnmsiAlarmEventTable_Object = MibTable
jdsuOnmsiAlarmEventTable = _JdsuOnmsiAlarmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventTable.setStatus("current")
_JdsuOnmsiAlarmEventEntry_Object = MibTableRow
jdsuOnmsiAlarmEventEntry = _JdsuOnmsiAlarmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1)
)
jdsuOnmsiAlarmEventEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntrySequence"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntry.setStatus("current")
_JdsuOnmsiAlarmEventEntrySequence_Type = Unsigned32
_JdsuOnmsiAlarmEventEntrySequence_Object = MibTableColumn
jdsuOnmsiAlarmEventEntrySequence = _JdsuOnmsiAlarmEventEntrySequence_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 1),
    _JdsuOnmsiAlarmEventEntrySequence_Type()
)
jdsuOnmsiAlarmEventEntrySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntrySequence.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmEventEntryEventInternalKey_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventInternalKey = _JdsuOnmsiAlarmEventEntryEventInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 2),
    _JdsuOnmsiAlarmEventEntryEventInternalKey_Type()
)
jdsuOnmsiAlarmEventEntryEventInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventInternalKey.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventType_Type = JdsuOnmsiAlarmEventType
_JdsuOnmsiAlarmEventEntryEventType_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventType = _JdsuOnmsiAlarmEventEntryEventType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 3),
    _JdsuOnmsiAlarmEventEntryEventType_Type()
)
jdsuOnmsiAlarmEventEntryEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventType.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventTime_Type = DateAndTime
_JdsuOnmsiAlarmEventEntryEventTime_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventTime = _JdsuOnmsiAlarmEventEntryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 4),
    _JdsuOnmsiAlarmEventEntryEventTime_Type()
)
jdsuOnmsiAlarmEventEntryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventTime.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventClearStatus_Type = JdsuOnmsiAlarmClearStatus
_JdsuOnmsiAlarmEventEntryEventClearStatus_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventClearStatus = _JdsuOnmsiAlarmEventEntryEventClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 5),
    _JdsuOnmsiAlarmEventEntryEventClearStatus_Type()
)
jdsuOnmsiAlarmEventEntryEventClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventClearStatus.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventAckStatus_Type = JdsuOnmsiAlarmAckStatus
_JdsuOnmsiAlarmEventEntryEventAckStatus_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventAckStatus = _JdsuOnmsiAlarmEventEntryEventAckStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 6),
    _JdsuOnmsiAlarmEventEntryEventAckStatus_Type()
)
jdsuOnmsiAlarmEventEntryEventAckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventAckStatus.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventPerceivedSeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiAlarmEventEntryEventPerceivedSeverity_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventPerceivedSeverity = _JdsuOnmsiAlarmEventEntryEventPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 7),
    _JdsuOnmsiAlarmEventEntryEventPerceivedSeverity_Type()
)
jdsuOnmsiAlarmEventEntryEventPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventPerceivedSeverity.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventProbableCause_Type = IANAItuProbableCause
_JdsuOnmsiAlarmEventEntryEventProbableCause_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventProbableCause = _JdsuOnmsiAlarmEventEntryEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 8),
    _JdsuOnmsiAlarmEventEntryEventProbableCause_Type()
)
jdsuOnmsiAlarmEventEntryEventProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventProbableCause.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventAdditionalText_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventAdditionalText_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventAdditionalText = _JdsuOnmsiAlarmEventEntryEventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 9),
    _JdsuOnmsiAlarmEventEntryEventAdditionalText_Type()
)
jdsuOnmsiAlarmEventEntryEventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventAdditionalText.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventUserIdentifier_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventUserIdentifier_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventUserIdentifier = _JdsuOnmsiAlarmEventEntryEventUserIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 10),
    _JdsuOnmsiAlarmEventEntryEventUserIdentifier_Type()
)
jdsuOnmsiAlarmEventEntryEventUserIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventUserIdentifier.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos = _JdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 11),
    _JdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos = _JdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 12),
    _JdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos = _JdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 13),
    _JdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventPeakSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventPeakSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos = _JdsuOnmsiAlarmEventEntryEventPeakSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 14),
    _JdsuOnmsiAlarmEventEntryEventPeakSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventOrlSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventOrlSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos = _JdsuOnmsiAlarmEventEntryEventOrlSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 15),
    _JdsuOnmsiAlarmEventEntryEventOrlSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos = _JdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 16),
    _JdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos = _JdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 17),
    _JdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmEventEntryAlarmInternalKey_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmInternalKey = _JdsuOnmsiAlarmEventEntryAlarmInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 18),
    _JdsuOnmsiAlarmEventEntryAlarmInternalKey_Type()
)
jdsuOnmsiAlarmEventEntryAlarmInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmInternalKey.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmType_Type = IANAItuEventType
_JdsuOnmsiAlarmEventEntryAlarmType_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmType = _JdsuOnmsiAlarmEventEntryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 19),
    _JdsuOnmsiAlarmEventEntryAlarmType_Type()
)
jdsuOnmsiAlarmEventEntryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmType.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmRaisedTime_Type = DateAndTime
_JdsuOnmsiAlarmEventEntryAlarmRaisedTime_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmRaisedTime = _JdsuOnmsiAlarmEventEntryAlarmRaisedTime_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 20),
    _JdsuOnmsiAlarmEventEntryAlarmRaisedTime_Type()
)
jdsuOnmsiAlarmEventEntryAlarmRaisedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmRaisedTime.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmChangedTime_Type = DateAndTime
_JdsuOnmsiAlarmEventEntryAlarmChangedTime_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmChangedTime = _JdsuOnmsiAlarmEventEntryAlarmChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 21),
    _JdsuOnmsiAlarmEventEntryAlarmChangedTime_Type()
)
jdsuOnmsiAlarmEventEntryAlarmChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmChangedTime.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmClearStatus_Type = JdsuOnmsiAlarmClearStatus
_JdsuOnmsiAlarmEventEntryAlarmClearStatus_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmClearStatus = _JdsuOnmsiAlarmEventEntryAlarmClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 22),
    _JdsuOnmsiAlarmEventEntryAlarmClearStatus_Type()
)
jdsuOnmsiAlarmEventEntryAlarmClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmClearStatus.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmAckStatus_Type = JdsuOnmsiAlarmAckStatus
_JdsuOnmsiAlarmEventEntryAlarmAckStatus_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmAckStatus = _JdsuOnmsiAlarmEventEntryAlarmAckStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 23),
    _JdsuOnmsiAlarmEventEntryAlarmAckStatus_Type()
)
jdsuOnmsiAlarmEventEntryAlarmAckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmAckStatus.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity = _JdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 24),
    _JdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity_Type()
)
jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmSpecificProblem_Type = DisplayString
_JdsuOnmsiAlarmEventEntryAlarmSpecificProblem_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmSpecificProblem = _JdsuOnmsiAlarmEventEntryAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 25),
    _JdsuOnmsiAlarmEventEntryAlarmSpecificProblem_Type()
)
jdsuOnmsiAlarmEventEntryAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmSpecificProblem.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind_Type = DisplayString
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind = _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 26),
    _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey = _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 27),
    _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName = _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 28),
    _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid = _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 29),
    _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmSystemDN_Type = DisplayString
_JdsuOnmsiAlarmEventEntryAlarmSystemDN_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmSystemDN = _JdsuOnmsiAlarmEventEntryAlarmSystemDN_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 30),
    _JdsuOnmsiAlarmEventEntryAlarmSystemDN_Type()
)
jdsuOnmsiAlarmEventEntryAlarmSystemDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmSystemDN.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmProbableCause_Type = IANAItuProbableCause
_JdsuOnmsiAlarmEventEntryAlarmProbableCause_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmProbableCause = _JdsuOnmsiAlarmEventEntryAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 31),
    _JdsuOnmsiAlarmEventEntryAlarmProbableCause_Type()
)
jdsuOnmsiAlarmEventEntryAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmProbableCause.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmAdditionalText_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmAdditionalText_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmAdditionalText = _JdsuOnmsiAlarmEventEntryAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 32),
    _JdsuOnmsiAlarmEventEntryAlarmAdditionalText_Type()
)
jdsuOnmsiAlarmEventEntryAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmAdditionalText.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 33),
    _JdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 34),
    _JdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 35),
    _JdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 36),
    _JdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 37),
    _JdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 38),
    _JdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 39),
    _JdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntity_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmOriginatingEntity_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity = _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 40),
    _JdsuOnmsiAlarmEventEntryAlarmOriginatingEntity_Type()
)
jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos = _JdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 41),
    _JdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 42),
    _JdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventPonSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventPonSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventPonSpecificInfos = _JdsuOnmsiAlarmEventEntryEventPonSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 43),
    _JdsuOnmsiAlarmEventEntryEventPonSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventPonSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventPonSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 44),
    _JdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos = _JdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 45),
    _JdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 46),
    _JdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventStrainSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventStrainSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos = _JdsuOnmsiAlarmEventEntryEventStrainSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 47),
    _JdsuOnmsiAlarmEventEntryEventStrainSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 48),
    _JdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos = _JdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 49),
    _JdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos = _JdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 50),
    _JdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos_Type()
)
jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos.setStatus("current")
_JdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes_Object = MibTableColumn
jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes = _JdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 3, 1, 51),
    _JdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes_Type()
)
jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakTable_Object = MibTable
jdsuOnmsiAlarmSplitterPeakTable = _JdsuOnmsiAlarmSplitterPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4)
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakTable.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntry_Object = MibTableRow
jdsuOnmsiAlarmSplitterPeakEntry = _JdsuOnmsiAlarmSplitterPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1)
)
jdsuOnmsiAlarmSplitterPeakEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntry.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmSplitterPeakEntryInternalKey_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryInternalKey = _JdsuOnmsiAlarmSplitterPeakEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 1),
    _JdsuOnmsiAlarmSplitterPeakEntryInternalKey_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryInternalKey.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmSplitterPeakEntryName_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryName = _JdsuOnmsiAlarmSplitterPeakEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 2),
    _JdsuOnmsiAlarmSplitterPeakEntryName_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryName.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity = _JdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 3),
    _JdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity = _JdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 4),
    _JdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance = _JdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 5),
    _JdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance = _JdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 6),
    _JdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryReferenceLevel_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryReferenceLevel_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel = _JdsuOnmsiAlarmSplitterPeakEntryReferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 7),
    _JdsuOnmsiAlarmSplitterPeakEntryReferenceLevel_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid_Type = TruthValue
_JdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid = _JdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 8),
    _JdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance = _JdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 9),
    _JdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance = _JdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 10),
    _JdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel_Object = MibTableColumn
jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel = _JdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 1, 4, 1, 11),
    _JdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel_Type()
)
jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel.setStatus("current")
_JdsuOnmsiAlarmFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmFunctions = _JdsuOnmsiAlarmFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2)
)
_JdsuOnmsiAlarmAck_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmAck = _JdsuOnmsiAlarmAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 1)
)
_JdsuOnmsiAlarmAckParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmAckParamInternalKey_Object = MibScalar
jdsuOnmsiAlarmAckParamInternalKey = _JdsuOnmsiAlarmAckParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 1, 1),
    _JdsuOnmsiAlarmAckParamInternalKey_Type()
)
jdsuOnmsiAlarmAckParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmAckParamInternalKey.setStatus("current")
_JdsuOnmsiAlarmAckExecute_Type = Integer32
_JdsuOnmsiAlarmAckExecute_Object = MibScalar
jdsuOnmsiAlarmAckExecute = _JdsuOnmsiAlarmAckExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 1, 2),
    _JdsuOnmsiAlarmAckExecute_Type()
)
jdsuOnmsiAlarmAckExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmAckExecute.setStatus("current")
_JdsuOnmsiAlarmAckError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmAckError_Object = MibScalar
jdsuOnmsiAlarmAckError = _JdsuOnmsiAlarmAckError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 1, 3),
    _JdsuOnmsiAlarmAckError_Type()
)
jdsuOnmsiAlarmAckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmAckError.setStatus("current")
_JdsuOnmsiAlarmUnAck_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmUnAck = _JdsuOnmsiAlarmUnAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 2)
)
_JdsuOnmsiAlarmUnAckParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmUnAckParamInternalKey_Object = MibScalar
jdsuOnmsiAlarmUnAckParamInternalKey = _JdsuOnmsiAlarmUnAckParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 2, 1),
    _JdsuOnmsiAlarmUnAckParamInternalKey_Type()
)
jdsuOnmsiAlarmUnAckParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnAckParamInternalKey.setStatus("current")
_JdsuOnmsiAlarmUnAckExecute_Type = Integer32
_JdsuOnmsiAlarmUnAckExecute_Object = MibScalar
jdsuOnmsiAlarmUnAckExecute = _JdsuOnmsiAlarmUnAckExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 2, 2),
    _JdsuOnmsiAlarmUnAckExecute_Type()
)
jdsuOnmsiAlarmUnAckExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnAckExecute.setStatus("current")
_JdsuOnmsiAlarmUnAckError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmUnAckError_Object = MibScalar
jdsuOnmsiAlarmUnAckError = _JdsuOnmsiAlarmUnAckError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 2, 3),
    _JdsuOnmsiAlarmUnAckError_Type()
)
jdsuOnmsiAlarmUnAckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnAckError.setStatus("current")
_JdsuOnmsiAlarmClear_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmClear = _JdsuOnmsiAlarmClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 3)
)
_JdsuOnmsiAlarmClearParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmClearParamInternalKey_Object = MibScalar
jdsuOnmsiAlarmClearParamInternalKey = _JdsuOnmsiAlarmClearParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 3, 1),
    _JdsuOnmsiAlarmClearParamInternalKey_Type()
)
jdsuOnmsiAlarmClearParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmClearParamInternalKey.setStatus("current")
_JdsuOnmsiAlarmClearExecute_Type = Integer32
_JdsuOnmsiAlarmClearExecute_Object = MibScalar
jdsuOnmsiAlarmClearExecute = _JdsuOnmsiAlarmClearExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 3, 2),
    _JdsuOnmsiAlarmClearExecute_Type()
)
jdsuOnmsiAlarmClearExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmClearExecute.setStatus("current")
_JdsuOnmsiAlarmClearError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmClearError_Object = MibScalar
jdsuOnmsiAlarmClearError = _JdsuOnmsiAlarmClearError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 3, 3),
    _JdsuOnmsiAlarmClearError_Type()
)
jdsuOnmsiAlarmClearError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmClearError.setStatus("current")
_JdsuOnmsiAlarmUnClear_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmUnClear = _JdsuOnmsiAlarmUnClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 4)
)
_JdsuOnmsiAlarmUnClearParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmUnClearParamInternalKey_Object = MibScalar
jdsuOnmsiAlarmUnClearParamInternalKey = _JdsuOnmsiAlarmUnClearParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 4, 1),
    _JdsuOnmsiAlarmUnClearParamInternalKey_Type()
)
jdsuOnmsiAlarmUnClearParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnClearParamInternalKey.setStatus("current")
_JdsuOnmsiAlarmUnClearExecute_Type = Integer32
_JdsuOnmsiAlarmUnClearExecute_Object = MibScalar
jdsuOnmsiAlarmUnClearExecute = _JdsuOnmsiAlarmUnClearExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 4, 2),
    _JdsuOnmsiAlarmUnClearExecute_Type()
)
jdsuOnmsiAlarmUnClearExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnClearExecute.setStatus("current")
_JdsuOnmsiAlarmUnClearError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmUnClearError_Object = MibScalar
jdsuOnmsiAlarmUnClearError = _JdsuOnmsiAlarmUnClearError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 4, 3),
    _JdsuOnmsiAlarmUnClearError_Type()
)
jdsuOnmsiAlarmUnClearError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmUnClearError.setStatus("current")
_JdsuOnmsiAlarmResendEvents_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmResendEvents = _JdsuOnmsiAlarmResendEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 5)
)
_JdsuOnmsiAlarmResendEventsParamSequence_Type = Unsigned32
_JdsuOnmsiAlarmResendEventsParamSequence_Object = MibScalar
jdsuOnmsiAlarmResendEventsParamSequence = _JdsuOnmsiAlarmResendEventsParamSequence_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 5, 1),
    _JdsuOnmsiAlarmResendEventsParamSequence_Type()
)
jdsuOnmsiAlarmResendEventsParamSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmResendEventsParamSequence.setStatus("current")
_JdsuOnmsiAlarmResendEventsExecute_Type = Integer32
_JdsuOnmsiAlarmResendEventsExecute_Object = MibScalar
jdsuOnmsiAlarmResendEventsExecute = _JdsuOnmsiAlarmResendEventsExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 5, 2),
    _JdsuOnmsiAlarmResendEventsExecute_Type()
)
jdsuOnmsiAlarmResendEventsExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmResendEventsExecute.setStatus("current")
_JdsuOnmsiAlarmResendEventsError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmResendEventsError_Object = MibScalar
jdsuOnmsiAlarmResendEventsError = _JdsuOnmsiAlarmResendEventsError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 5, 3),
    _JdsuOnmsiAlarmResendEventsError_Type()
)
jdsuOnmsiAlarmResendEventsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmResendEventsError.setStatus("current")
_JdsuOnmsiAlarmResynchronize_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmResynchronize = _JdsuOnmsiAlarmResynchronize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 6)
)
_JdsuOnmsiAlarmResynchronizeExecute_Type = Integer32
_JdsuOnmsiAlarmResynchronizeExecute_Object = MibScalar
jdsuOnmsiAlarmResynchronizeExecute = _JdsuOnmsiAlarmResynchronizeExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 6, 1),
    _JdsuOnmsiAlarmResynchronizeExecute_Type()
)
jdsuOnmsiAlarmResynchronizeExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmResynchronizeExecute.setStatus("current")
_JdsuOnmsiAlarmResynchronizeError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmResynchronizeError_Object = MibScalar
jdsuOnmsiAlarmResynchronizeError = _JdsuOnmsiAlarmResynchronizeError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 6, 2),
    _JdsuOnmsiAlarmResynchronizeError_Type()
)
jdsuOnmsiAlarmResynchronizeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmResynchronizeError.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiAlarmSplitterPeakLoad = _JdsuOnmsiAlarmSplitterPeakLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 7)
)
_JdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey_Object = MibScalar
jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey = _JdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 7, 1),
    _JdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey_Type()
)
jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakLoadExecute_Type = Integer32
_JdsuOnmsiAlarmSplitterPeakLoadExecute_Object = MibScalar
jdsuOnmsiAlarmSplitterPeakLoadExecute = _JdsuOnmsiAlarmSplitterPeakLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 7, 2),
    _JdsuOnmsiAlarmSplitterPeakLoadExecute_Type()
)
jdsuOnmsiAlarmSplitterPeakLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakLoadExecute.setStatus("current")
_JdsuOnmsiAlarmSplitterPeakLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiAlarmSplitterPeakLoadError_Object = MibScalar
jdsuOnmsiAlarmSplitterPeakLoadError = _JdsuOnmsiAlarmSplitterPeakLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 6, 2, 7, 3),
    _JdsuOnmsiAlarmSplitterPeakLoadError_Type()
)
jdsuOnmsiAlarmSplitterPeakLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmSplitterPeakLoadError.setStatus("current")
_JdsuOnmsiOtuService_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuService = _JdsuOnmsiOtuService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7)
)
_JdsuOnmsiOtuData_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuData = _JdsuOnmsiOtuData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1)
)
_JdsuOnmsiOtuTable_Object = MibTable
jdsuOnmsiOtuTable = _JdsuOnmsiOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuTable.setStatus("current")
_JdsuOnmsiOtuEntry_Object = MibTableRow
jdsuOnmsiOtuEntry = _JdsuOnmsiOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1)
)
jdsuOnmsiOtuEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntry.setStatus("current")
_JdsuOnmsiOtuEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuEntryInternalKey_Object = MibTableColumn
jdsuOnmsiOtuEntryInternalKey = _JdsuOnmsiOtuEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 1),
    _JdsuOnmsiOtuEntryInternalKey_Type()
)
jdsuOnmsiOtuEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryInternalKey.setStatus("current")
_JdsuOnmsiOtuEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuEntryName_Object = MibTableColumn
jdsuOnmsiOtuEntryName = _JdsuOnmsiOtuEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 2),
    _JdsuOnmsiOtuEntryName_Type()
)
jdsuOnmsiOtuEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryName.setStatus("current")
_JdsuOnmsiOtuEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuEntryDescription_Object = MibTableColumn
jdsuOnmsiOtuEntryDescription = _JdsuOnmsiOtuEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 3),
    _JdsuOnmsiOtuEntryDescription_Type()
)
jdsuOnmsiOtuEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryDescription.setStatus("current")
_JdsuOnmsiOtuEntryIpAddress_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuEntryIpAddress_Object = MibTableColumn
jdsuOnmsiOtuEntryIpAddress = _JdsuOnmsiOtuEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 4),
    _JdsuOnmsiOtuEntryIpAddress_Type()
)
jdsuOnmsiOtuEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryIpAddress.setStatus("current")
_JdsuOnmsiOtuEntryDeviceName_Type = DisplayString
_JdsuOnmsiOtuEntryDeviceName_Object = MibTableColumn
jdsuOnmsiOtuEntryDeviceName = _JdsuOnmsiOtuEntryDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 5),
    _JdsuOnmsiOtuEntryDeviceName_Type()
)
jdsuOnmsiOtuEntryDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryDeviceName.setStatus("current")
_JdsuOnmsiOtuEntrySerialNumber_Type = DisplayString
_JdsuOnmsiOtuEntrySerialNumber_Object = MibTableColumn
jdsuOnmsiOtuEntrySerialNumber = _JdsuOnmsiOtuEntrySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 6),
    _JdsuOnmsiOtuEntrySerialNumber_Type()
)
jdsuOnmsiOtuEntrySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntrySerialNumber.setStatus("current")
_JdsuOnmsiOtuEntrySoftwareVersion_Type = DisplayString
_JdsuOnmsiOtuEntrySoftwareVersion_Object = MibTableColumn
jdsuOnmsiOtuEntrySoftwareVersion = _JdsuOnmsiOtuEntrySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 7),
    _JdsuOnmsiOtuEntrySoftwareVersion_Type()
)
jdsuOnmsiOtuEntrySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntrySoftwareVersion.setStatus("current")
_JdsuOnmsiOtuEntryCentralOfficeInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuEntryCentralOfficeInternalKey_Object = MibTableColumn
jdsuOnmsiOtuEntryCentralOfficeInternalKey = _JdsuOnmsiOtuEntryCentralOfficeInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 8),
    _JdsuOnmsiOtuEntryCentralOfficeInternalKey_Type()
)
jdsuOnmsiOtuEntryCentralOfficeInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntryCentralOfficeInternalKey.setStatus("current")
_JdsuOnmsiOtuEntrySeverity_Type = JdsuOnmsiSeverity
_JdsuOnmsiOtuEntrySeverity_Object = MibTableColumn
jdsuOnmsiOtuEntrySeverity = _JdsuOnmsiOtuEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 1, 1, 9),
    _JdsuOnmsiOtuEntrySeverity_Type()
)
jdsuOnmsiOtuEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuEntrySeverity.setStatus("current")
_JdsuOnmsiOtuAdditionalAttributeTable_Object = MibTable
jdsuOnmsiOtuAdditionalAttributeTable = _JdsuOnmsiOtuAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiOtuAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiOtuAdditionalAttributeEntry = _JdsuOnmsiOtuAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 2, 1)
)
jdsuOnmsiOtuAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiOtuAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiOtuAdditionalAttributeEntryInternalKey = _JdsuOnmsiOtuAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 2, 1, 1),
    _JdsuOnmsiOtuAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiOtuAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiOtuAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiOtuAdditionalAttributeEntryName = _JdsuOnmsiOtuAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 2, 1, 2),
    _JdsuOnmsiOtuAdditionalAttributeEntryName_Type()
)
jdsuOnmsiOtuAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiOtuAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiOtuAdditionalAttributeEntryValue = _JdsuOnmsiOtuAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 2, 1, 3),
    _JdsuOnmsiOtuAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiOtuAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiOtuAttributeTable_Object = MibTable
jdsuOnmsiOtuAttributeTable = _JdsuOnmsiOtuAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeTable.setStatus("current")
_JdsuOnmsiOtuAttributeEntry_Object = MibTableRow
jdsuOnmsiOtuAttributeEntry = _JdsuOnmsiOtuAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3, 1)
)
jdsuOnmsiOtuAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeEntry.setStatus("current")
_JdsuOnmsiOtuAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuAttributeEntryName_Object = MibTableColumn
jdsuOnmsiOtuAttributeEntryName = _JdsuOnmsiOtuAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3, 1, 1),
    _JdsuOnmsiOtuAttributeEntryName_Type()
)
jdsuOnmsiOtuAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeEntryName.setStatus("current")
_JdsuOnmsiOtuAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiOtuAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiOtuAttributeEntryAdditional = _JdsuOnmsiOtuAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3, 1, 2),
    _JdsuOnmsiOtuAttributeEntryAdditional_Type()
)
jdsuOnmsiOtuAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiOtuAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiOtuAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiOtuAttributeEntryFindable = _JdsuOnmsiOtuAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3, 1, 3),
    _JdsuOnmsiOtuAttributeEntryFindable_Type()
)
jdsuOnmsiOtuAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeEntryFindable.setStatus("current")
_JdsuOnmsiOtuAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiOtuAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiOtuAttributeEntryUpdatable = _JdsuOnmsiOtuAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 3, 1, 4),
    _JdsuOnmsiOtuAttributeEntryUpdatable_Type()
)
jdsuOnmsiOtuAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiOtuOtdrTable_Object = MibTable
jdsuOnmsiOtuOtdrTable = _JdsuOnmsiOtuOtdrTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrTable.setStatus("current")
_JdsuOnmsiOtuOtdrEntry_Object = MibTableRow
jdsuOnmsiOtuOtdrEntry = _JdsuOnmsiOtuOtdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1)
)
jdsuOnmsiOtuOtdrEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntry.setStatus("current")
_JdsuOnmsiOtuOtdrEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuOtdrEntryInternalKey_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntryInternalKey = _JdsuOnmsiOtuOtdrEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 1),
    _JdsuOnmsiOtuOtdrEntryInternalKey_Type()
)
jdsuOnmsiOtuOtdrEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntryInternalKey.setStatus("current")
_JdsuOnmsiOtuOtdrEntryOtuInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuOtdrEntryOtuInternalKey_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntryOtuInternalKey = _JdsuOnmsiOtuOtdrEntryOtuInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 2),
    _JdsuOnmsiOtuOtdrEntryOtuInternalKey_Type()
)
jdsuOnmsiOtuOtdrEntryOtuInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntryOtuInternalKey.setStatus("current")
_JdsuOnmsiOtuOtdrEntryPosition_Type = JdsuOnmsiOtdrPosition
_JdsuOnmsiOtuOtdrEntryPosition_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntryPosition = _JdsuOnmsiOtuOtdrEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 3),
    _JdsuOnmsiOtuOtdrEntryPosition_Type()
)
jdsuOnmsiOtuOtdrEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntryPosition.setStatus("current")
_JdsuOnmsiOtuOtdrEntryType_Type = DisplayString
_JdsuOnmsiOtuOtdrEntryType_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntryType = _JdsuOnmsiOtuOtdrEntryType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 4),
    _JdsuOnmsiOtuOtdrEntryType_Type()
)
jdsuOnmsiOtuOtdrEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntryType.setStatus("current")
_JdsuOnmsiOtuOtdrEntrySerialNumber_Type = DisplayString
_JdsuOnmsiOtuOtdrEntrySerialNumber_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntrySerialNumber = _JdsuOnmsiOtuOtdrEntrySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 5),
    _JdsuOnmsiOtuOtdrEntrySerialNumber_Type()
)
jdsuOnmsiOtuOtdrEntrySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntrySerialNumber.setStatus("current")
_JdsuOnmsiOtuOtdrEntryWavelengths_Type = DisplayString
_JdsuOnmsiOtuOtdrEntryWavelengths_Object = MibTableColumn
jdsuOnmsiOtuOtdrEntryWavelengths = _JdsuOnmsiOtuOtdrEntryWavelengths_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 4, 1, 6),
    _JdsuOnmsiOtuOtdrEntryWavelengths_Type()
)
jdsuOnmsiOtuOtdrEntryWavelengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuOtdrEntryWavelengths.setStatus("current")
_JdsuOnmsiOtuSwitchTable_Object = MibTable
jdsuOnmsiOtuSwitchTable = _JdsuOnmsiOtuSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchTable.setStatus("current")
_JdsuOnmsiOtuSwitchEntry_Object = MibTableRow
jdsuOnmsiOtuSwitchEntry = _JdsuOnmsiOtuSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1)
)
jdsuOnmsiOtuSwitchEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntry.setStatus("current")
_JdsuOnmsiOtuSwitchEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuSwitchEntryInternalKey_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryInternalKey = _JdsuOnmsiOtuSwitchEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 1),
    _JdsuOnmsiOtuSwitchEntryInternalKey_Type()
)
jdsuOnmsiOtuSwitchEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryInternalKey.setStatus("current")
_JdsuOnmsiOtuSwitchEntryOtuInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuSwitchEntryOtuInternalKey_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryOtuInternalKey = _JdsuOnmsiOtuSwitchEntryOtuInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 2),
    _JdsuOnmsiOtuSwitchEntryOtuInternalKey_Type()
)
jdsuOnmsiOtuSwitchEntryOtuInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryOtuInternalKey.setStatus("current")
_JdsuOnmsiOtuSwitchEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuSwitchEntryName_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryName = _JdsuOnmsiOtuSwitchEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 3),
    _JdsuOnmsiOtuSwitchEntryName_Type()
)
jdsuOnmsiOtuSwitchEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryName.setStatus("current")
_JdsuOnmsiOtuSwitchEntryRemote_Type = TruthValue
_JdsuOnmsiOtuSwitchEntryRemote_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryRemote = _JdsuOnmsiOtuSwitchEntryRemote_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 4),
    _JdsuOnmsiOtuSwitchEntryRemote_Type()
)
jdsuOnmsiOtuSwitchEntryRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryRemote.setStatus("current")
_JdsuOnmsiOtuSwitchEntryPosition_Type = Integer32
_JdsuOnmsiOtuSwitchEntryPosition_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryPosition = _JdsuOnmsiOtuSwitchEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 5),
    _JdsuOnmsiOtuSwitchEntryPosition_Type()
)
jdsuOnmsiOtuSwitchEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryPosition.setStatus("current")
_JdsuOnmsiOtuSwitchEntryInputs_Type = Integer32
_JdsuOnmsiOtuSwitchEntryInputs_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryInputs = _JdsuOnmsiOtuSwitchEntryInputs_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 6),
    _JdsuOnmsiOtuSwitchEntryInputs_Type()
)
jdsuOnmsiOtuSwitchEntryInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryInputs.setStatus("current")
_JdsuOnmsiOtuSwitchEntryOutputs_Type = Integer32
_JdsuOnmsiOtuSwitchEntryOutputs_Object = MibTableColumn
jdsuOnmsiOtuSwitchEntryOutputs = _JdsuOnmsiOtuSwitchEntryOutputs_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 5, 1, 7),
    _JdsuOnmsiOtuSwitchEntryOutputs_Type()
)
jdsuOnmsiOtuSwitchEntryOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuSwitchEntryOutputs.setStatus("current")
_JdsuOnmsiOtuPortTable_Object = MibTable
jdsuOnmsiOtuPortTable = _JdsuOnmsiOtuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6)
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortTable.setStatus("current")
_JdsuOnmsiOtuPortEntry_Object = MibTableRow
jdsuOnmsiOtuPortEntry = _JdsuOnmsiOtuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1)
)
jdsuOnmsiOtuPortEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntry.setStatus("current")
_JdsuOnmsiOtuPortEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuPortEntryInternalKey_Object = MibTableColumn
jdsuOnmsiOtuPortEntryInternalKey = _JdsuOnmsiOtuPortEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 1),
    _JdsuOnmsiOtuPortEntryInternalKey_Type()
)
jdsuOnmsiOtuPortEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryInternalKey.setStatus("current")
_JdsuOnmsiOtuPortEntryOtuInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuPortEntryOtuInternalKey_Object = MibTableColumn
jdsuOnmsiOtuPortEntryOtuInternalKey = _JdsuOnmsiOtuPortEntryOtuInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 2),
    _JdsuOnmsiOtuPortEntryOtuInternalKey_Type()
)
jdsuOnmsiOtuPortEntryOtuInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryOtuInternalKey.setStatus("current")
_JdsuOnmsiOtuPortEntryModuleInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuPortEntryModuleInternalKey_Object = MibTableColumn
jdsuOnmsiOtuPortEntryModuleInternalKey = _JdsuOnmsiOtuPortEntryModuleInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 3),
    _JdsuOnmsiOtuPortEntryModuleInternalKey_Type()
)
jdsuOnmsiOtuPortEntryModuleInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryModuleInternalKey.setStatus("current")
_JdsuOnmsiOtuPortEntryPosition_Type = Integer32
_JdsuOnmsiOtuPortEntryPosition_Object = MibTableColumn
jdsuOnmsiOtuPortEntryPosition = _JdsuOnmsiOtuPortEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 4),
    _JdsuOnmsiOtuPortEntryPosition_Type()
)
jdsuOnmsiOtuPortEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryPosition.setStatus("current")
_JdsuOnmsiOtuPortEntryPonInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuPortEntryPonInternalKey_Object = MibTableColumn
jdsuOnmsiOtuPortEntryPonInternalKey = _JdsuOnmsiOtuPortEntryPonInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 5),
    _JdsuOnmsiOtuPortEntryPonInternalKey_Type()
)
jdsuOnmsiOtuPortEntryPonInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryPonInternalKey.setStatus("current")
_JdsuOnmsiOtuPortEntryLinkInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuPortEntryLinkInternalKey_Object = MibTableColumn
jdsuOnmsiOtuPortEntryLinkInternalKey = _JdsuOnmsiOtuPortEntryLinkInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 1, 6, 1, 6),
    _JdsuOnmsiOtuPortEntryLinkInternalKey_Type()
)
jdsuOnmsiOtuPortEntryLinkInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuPortEntryLinkInternalKey.setStatus("current")
_JdsuOnmsiOtuFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuFunctions = _JdsuOnmsiOtuFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2)
)
_JdsuOnmsiOtuGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuGet = _JdsuOnmsiOtuGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 1)
)
_JdsuOnmsiOtuGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuGetParamInternalKey_Object = MibScalar
jdsuOnmsiOtuGetParamInternalKey = _JdsuOnmsiOtuGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 1, 1),
    _JdsuOnmsiOtuGetParamInternalKey_Type()
)
jdsuOnmsiOtuGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetParamInternalKey.setStatus("current")
_JdsuOnmsiOtuGetExecute_Type = Integer32
_JdsuOnmsiOtuGetExecute_Object = MibScalar
jdsuOnmsiOtuGetExecute = _JdsuOnmsiOtuGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 1, 2),
    _JdsuOnmsiOtuGetExecute_Type()
)
jdsuOnmsiOtuGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetExecute.setStatus("current")
_JdsuOnmsiOtuGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuGetError_Object = MibScalar
jdsuOnmsiOtuGetError = _JdsuOnmsiOtuGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 1, 3),
    _JdsuOnmsiOtuGetError_Type()
)
jdsuOnmsiOtuGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetError.setStatus("current")
_JdsuOnmsiOtuFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuFind = _JdsuOnmsiOtuFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 2)
)
_JdsuOnmsiOtuFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuFindParamAttribute_Object = MibScalar
jdsuOnmsiOtuFindParamAttribute = _JdsuOnmsiOtuFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 2, 1),
    _JdsuOnmsiOtuFindParamAttribute_Type()
)
jdsuOnmsiOtuFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuFindParamAttribute.setStatus("current")
_JdsuOnmsiOtuFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuFindParamValue_Object = MibScalar
jdsuOnmsiOtuFindParamValue = _JdsuOnmsiOtuFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 2, 2),
    _JdsuOnmsiOtuFindParamValue_Type()
)
jdsuOnmsiOtuFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuFindParamValue.setStatus("current")
_JdsuOnmsiOtuFindExecute_Type = Integer32
_JdsuOnmsiOtuFindExecute_Object = MibScalar
jdsuOnmsiOtuFindExecute = _JdsuOnmsiOtuFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 2, 3),
    _JdsuOnmsiOtuFindExecute_Type()
)
jdsuOnmsiOtuFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuFindExecute.setStatus("current")
_JdsuOnmsiOtuFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuFindError_Object = MibScalar
jdsuOnmsiOtuFindError = _JdsuOnmsiOtuFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 2, 4),
    _JdsuOnmsiOtuFindError_Type()
)
jdsuOnmsiOtuFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuFindError.setStatus("current")
_JdsuOnmsiOtuAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuAttributeLoad = _JdsuOnmsiOtuAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 3)
)
_JdsuOnmsiOtuAttributeLoadExecute_Type = Integer32
_JdsuOnmsiOtuAttributeLoadExecute_Object = MibScalar
jdsuOnmsiOtuAttributeLoadExecute = _JdsuOnmsiOtuAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 3, 1),
    _JdsuOnmsiOtuAttributeLoadExecute_Type()
)
jdsuOnmsiOtuAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeLoadExecute.setStatus("current")
_JdsuOnmsiOtuAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuAttributeLoadError_Object = MibScalar
jdsuOnmsiOtuAttributeLoadError = _JdsuOnmsiOtuAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 3, 2),
    _JdsuOnmsiOtuAttributeLoadError_Type()
)
jdsuOnmsiOtuAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuAttributeLoadError.setStatus("current")
_JdsuOnmsiOtuGetPorts_ObjectIdentity = ObjectIdentity
jdsuOnmsiOtuGetPorts = _JdsuOnmsiOtuGetPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 4)
)
_JdsuOnmsiOtuGetPortsParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiOtuGetPortsParamInternalKey_Object = MibScalar
jdsuOnmsiOtuGetPortsParamInternalKey = _JdsuOnmsiOtuGetPortsParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 4, 1),
    _JdsuOnmsiOtuGetPortsParamInternalKey_Type()
)
jdsuOnmsiOtuGetPortsParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetPortsParamInternalKey.setStatus("current")
_JdsuOnmsiOtuGetPortsExecute_Type = Integer32
_JdsuOnmsiOtuGetPortsExecute_Object = MibScalar
jdsuOnmsiOtuGetPortsExecute = _JdsuOnmsiOtuGetPortsExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 4, 2),
    _JdsuOnmsiOtuGetPortsExecute_Type()
)
jdsuOnmsiOtuGetPortsExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetPortsExecute.setStatus("current")
_JdsuOnmsiOtuGetPortsError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiOtuGetPortsError_Object = MibScalar
jdsuOnmsiOtuGetPortsError = _JdsuOnmsiOtuGetPortsError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 7, 2, 4, 3),
    _JdsuOnmsiOtuGetPortsError_Type()
)
jdsuOnmsiOtuGetPortsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiOtuGetPortsError.setStatus("current")
_JdsuOnmsiCentralOfficeService_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeService = _JdsuOnmsiCentralOfficeService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8)
)
_JdsuOnmsiCentralOfficeData_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeData = _JdsuOnmsiCentralOfficeData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1)
)
_JdsuOnmsiCentralOfficeTable_Object = MibTable
jdsuOnmsiCentralOfficeTable = _JdsuOnmsiCentralOfficeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeTable.setStatus("current")
_JdsuOnmsiCentralOfficeEntry_Object = MibTableRow
jdsuOnmsiCentralOfficeEntry = _JdsuOnmsiCentralOfficeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 1, 1)
)
jdsuOnmsiCentralOfficeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeEntryInternalKey"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeEntry.setStatus("current")
_JdsuOnmsiCentralOfficeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiCentralOfficeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiCentralOfficeEntryInternalKey = _JdsuOnmsiCentralOfficeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 1, 1, 1),
    _JdsuOnmsiCentralOfficeEntryInternalKey_Type()
)
jdsuOnmsiCentralOfficeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeEntryInternalKey.setStatus("current")
_JdsuOnmsiCentralOfficeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeEntryName_Object = MibTableColumn
jdsuOnmsiCentralOfficeEntryName = _JdsuOnmsiCentralOfficeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 1, 1, 2),
    _JdsuOnmsiCentralOfficeEntryName_Type()
)
jdsuOnmsiCentralOfficeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeEntryName.setStatus("current")
_JdsuOnmsiCentralOfficeEntryDescription_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeEntryDescription_Object = MibTableColumn
jdsuOnmsiCentralOfficeEntryDescription = _JdsuOnmsiCentralOfficeEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 1, 1, 3),
    _JdsuOnmsiCentralOfficeEntryDescription_Type()
)
jdsuOnmsiCentralOfficeEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeEntryDescription.setStatus("current")
_JdsuOnmsiCentralOfficeAdditionalAttributeTable_Object = MibTable
jdsuOnmsiCentralOfficeAdditionalAttributeTable = _JdsuOnmsiCentralOfficeAdditionalAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAdditionalAttributeTable.setStatus("current")
_JdsuOnmsiCentralOfficeAdditionalAttributeEntry_Object = MibTableRow
jdsuOnmsiCentralOfficeAdditionalAttributeEntry = _JdsuOnmsiCentralOfficeAdditionalAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 2, 1)
)
jdsuOnmsiCentralOfficeAdditionalAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey"),
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAdditionalAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAdditionalAttributeEntry.setStatus("current")
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey_Object = MibTableColumn
jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey = _JdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 2, 1, 1),
    _JdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey_Type()
)
jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey.setStatus("current")
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryName_Object = MibTableColumn
jdsuOnmsiCentralOfficeAdditionalAttributeEntryName = _JdsuOnmsiCentralOfficeAdditionalAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 2, 1, 2),
    _JdsuOnmsiCentralOfficeAdditionalAttributeEntryName_Type()
)
jdsuOnmsiCentralOfficeAdditionalAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAdditionalAttributeEntryName.setStatus("current")
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeAdditionalAttributeEntryValue_Object = MibTableColumn
jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue = _JdsuOnmsiCentralOfficeAdditionalAttributeEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 2, 1, 3),
    _JdsuOnmsiCentralOfficeAdditionalAttributeEntryValue_Type()
)
jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeTable_Object = MibTable
jdsuOnmsiCentralOfficeAttributeTable = _JdsuOnmsiCentralOfficeAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3)
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeTable.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeEntry_Object = MibTableRow
jdsuOnmsiCentralOfficeAttributeEntry = _JdsuOnmsiCentralOfficeAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3, 1)
)
jdsuOnmsiCentralOfficeAttributeEntry.setIndexNames(
    (0, "JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeEntryName"),
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeEntry.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeEntryName_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeAttributeEntryName_Object = MibTableColumn
jdsuOnmsiCentralOfficeAttributeEntryName = _JdsuOnmsiCentralOfficeAttributeEntryName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3, 1, 1),
    _JdsuOnmsiCentralOfficeAttributeEntryName_Type()
)
jdsuOnmsiCentralOfficeAttributeEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeEntryName.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeEntryAdditional_Type = TruthValue
_JdsuOnmsiCentralOfficeAttributeEntryAdditional_Object = MibTableColumn
jdsuOnmsiCentralOfficeAttributeEntryAdditional = _JdsuOnmsiCentralOfficeAttributeEntryAdditional_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3, 1, 2),
    _JdsuOnmsiCentralOfficeAttributeEntryAdditional_Type()
)
jdsuOnmsiCentralOfficeAttributeEntryAdditional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeEntryAdditional.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeEntryFindable_Type = TruthValue
_JdsuOnmsiCentralOfficeAttributeEntryFindable_Object = MibTableColumn
jdsuOnmsiCentralOfficeAttributeEntryFindable = _JdsuOnmsiCentralOfficeAttributeEntryFindable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3, 1, 3),
    _JdsuOnmsiCentralOfficeAttributeEntryFindable_Type()
)
jdsuOnmsiCentralOfficeAttributeEntryFindable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeEntryFindable.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeEntryUpdatable_Type = TruthValue
_JdsuOnmsiCentralOfficeAttributeEntryUpdatable_Object = MibTableColumn
jdsuOnmsiCentralOfficeAttributeEntryUpdatable = _JdsuOnmsiCentralOfficeAttributeEntryUpdatable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 1, 3, 1, 4),
    _JdsuOnmsiCentralOfficeAttributeEntryUpdatable_Type()
)
jdsuOnmsiCentralOfficeAttributeEntryUpdatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeEntryUpdatable.setStatus("current")
_JdsuOnmsiCentralOfficeFunctions_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeFunctions = _JdsuOnmsiCentralOfficeFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2)
)
_JdsuOnmsiCentralOfficeGet_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeGet = _JdsuOnmsiCentralOfficeGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 1)
)
_JdsuOnmsiCentralOfficeGetParamInternalKey_Type = JdsuOnmsiInternalKey
_JdsuOnmsiCentralOfficeGetParamInternalKey_Object = MibScalar
jdsuOnmsiCentralOfficeGetParamInternalKey = _JdsuOnmsiCentralOfficeGetParamInternalKey_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 1, 1),
    _JdsuOnmsiCentralOfficeGetParamInternalKey_Type()
)
jdsuOnmsiCentralOfficeGetParamInternalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeGetParamInternalKey.setStatus("current")
_JdsuOnmsiCentralOfficeGetExecute_Type = Integer32
_JdsuOnmsiCentralOfficeGetExecute_Object = MibScalar
jdsuOnmsiCentralOfficeGetExecute = _JdsuOnmsiCentralOfficeGetExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 1, 2),
    _JdsuOnmsiCentralOfficeGetExecute_Type()
)
jdsuOnmsiCentralOfficeGetExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeGetExecute.setStatus("current")
_JdsuOnmsiCentralOfficeGetError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeGetError_Object = MibScalar
jdsuOnmsiCentralOfficeGetError = _JdsuOnmsiCentralOfficeGetError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 1, 3),
    _JdsuOnmsiCentralOfficeGetError_Type()
)
jdsuOnmsiCentralOfficeGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeGetError.setStatus("current")
_JdsuOnmsiCentralOfficeFind_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeFind = _JdsuOnmsiCentralOfficeFind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 2)
)
_JdsuOnmsiCentralOfficeFindParamAttribute_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeFindParamAttribute_Object = MibScalar
jdsuOnmsiCentralOfficeFindParamAttribute = _JdsuOnmsiCentralOfficeFindParamAttribute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 2, 1),
    _JdsuOnmsiCentralOfficeFindParamAttribute_Type()
)
jdsuOnmsiCentralOfficeFindParamAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeFindParamAttribute.setStatus("current")
_JdsuOnmsiCentralOfficeFindParamValue_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeFindParamValue_Object = MibScalar
jdsuOnmsiCentralOfficeFindParamValue = _JdsuOnmsiCentralOfficeFindParamValue_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 2, 2),
    _JdsuOnmsiCentralOfficeFindParamValue_Type()
)
jdsuOnmsiCentralOfficeFindParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeFindParamValue.setStatus("current")
_JdsuOnmsiCentralOfficeFindExecute_Type = Integer32
_JdsuOnmsiCentralOfficeFindExecute_Object = MibScalar
jdsuOnmsiCentralOfficeFindExecute = _JdsuOnmsiCentralOfficeFindExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 2, 3),
    _JdsuOnmsiCentralOfficeFindExecute_Type()
)
jdsuOnmsiCentralOfficeFindExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeFindExecute.setStatus("current")
_JdsuOnmsiCentralOfficeFindError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeFindError_Object = MibScalar
jdsuOnmsiCentralOfficeFindError = _JdsuOnmsiCentralOfficeFindError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 2, 4),
    _JdsuOnmsiCentralOfficeFindError_Type()
)
jdsuOnmsiCentralOfficeFindError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeFindError.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeLoad_ObjectIdentity = ObjectIdentity
jdsuOnmsiCentralOfficeAttributeLoad = _JdsuOnmsiCentralOfficeAttributeLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 3)
)
_JdsuOnmsiCentralOfficeAttributeLoadExecute_Type = Integer32
_JdsuOnmsiCentralOfficeAttributeLoadExecute_Object = MibScalar
jdsuOnmsiCentralOfficeAttributeLoadExecute = _JdsuOnmsiCentralOfficeAttributeLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 3, 1),
    _JdsuOnmsiCentralOfficeAttributeLoadExecute_Type()
)
jdsuOnmsiCentralOfficeAttributeLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeLoadExecute.setStatus("current")
_JdsuOnmsiCentralOfficeAttributeLoadError_Type = JdsuOnmsiUtf8String
_JdsuOnmsiCentralOfficeAttributeLoadError_Object = MibScalar
jdsuOnmsiCentralOfficeAttributeLoadError = _JdsuOnmsiCentralOfficeAttributeLoadError_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 3, 8, 2, 3, 2),
    _JdsuOnmsiCentralOfficeAttributeLoadError_Type()
)
jdsuOnmsiCentralOfficeAttributeLoadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeAttributeLoadError.setStatus("current")
_JdsuOnmsiEvents_ObjectIdentity = ObjectIdentity
jdsuOnmsiEvents = _JdsuOnmsiEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4)
)
_JdsuOnmsiConf_ObjectIdentity = ObjectIdentity
jdsuOnmsiConf = _JdsuOnmsiConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5)
)
_JdsOnmsiAdministrationConfGroups_ObjectIdentity = ObjectIdentity
jdsOnmsiAdministrationConfGroups = _JdsOnmsiAdministrationConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 2)
)
_JdsuOnmsiServicesConfGroups_ObjectIdentity = ObjectIdentity
jdsuOnmsiServicesConfGroups = _JdsuOnmsiServicesConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3)
)

# Managed Objects groups

jdsuOnmsiProductGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 1)
)
jdsuOnmsiProductGroups.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiProductDescr"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiProductObjectID"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiProductContact"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiProductName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiProductLocation"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiProductGroups.setStatus("current")

jdsuOnmsiSnmpConfigConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 2, 1)
)
jdsuOnmsiSnmpConfigConfGroup.setObjects(
    ("JDSU-ONMSI-MIB", "jdsuOnmsiSnmpConfigurationReload")
)
if mibBuilder.loadTexts:
    jdsuOnmsiSnmpConfigConfGroup.setStatus("current")

jdsuOnmsiImAliveConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 2, 2)
)
jdsuOnmsiImAliveConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiImAlivePeriodMin"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiImAliveText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiImAliveAlarmEventSequence"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiImAliveConfGroup.setStatus("current")

jdsuOnmsiHomeTerminationTypeConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 1)
)
jdsuOnmsiHomeTerminationTypeConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTerminationTypeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTerminationTypeConfGroup.setStatus("current")

jdsuOnmsiHomeConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 2)
)
jdsuOnmsiHomeConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryHomeIdentifier"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryPonInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryVip"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeStartTestParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeStartTestExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeAttributeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeConfGroup.setStatus("current")

jdsuOnmsiPonConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 3)
)
jdsuOnmsiPonConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryLatestTestInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryPortInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntrySeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntrySchedulingConfiguration"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonStartTestParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonStartTestExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonAttributeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonConfGroup.setStatus("current")

jdsuOnmsiPeakConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 4)
)
jdsuOnmsiPeakConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryTestInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryDate"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryIsAReference"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryLevel"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryPower"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryIsPowerMeasured"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntrySeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryRefDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryRefLevel"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryRefPower"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryRefIsPowerMeasured"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryRefDate"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakEntryHomeInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPeakFindError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiPeakConfGroup.setStatus("current")

jdsuOnmsiLinkServiceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 5)
)
jdsuOnmsiLinkServiceConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryMeasureEnabled"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkEntrySeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkUpdateParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkUpdateExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkUpdateError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiLinkAttributeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiLinkServiceConfGroup.setStatus("current")

jdsuOnmsiMonitoringTestServiceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 6)
)
jdsuOnmsiMonitoringTestServiceConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryLinkInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryDisplayOrder"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntrySeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryDetectionConfiguration"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryLocalizationConfiguration"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntrySchedulingConfiguration"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestStartTestParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestStartTestExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestAttributeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestServiceConfGroup.setStatus("current")

jdsuOnmsiAlarmServiceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 7)
)
jdsuOnmsiAlarmServiceConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmTypeName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSpecificProblemName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntrySequence"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventClearStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAckStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPerceivedSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventProbableCause"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAdditionalText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventUserIdentifier"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPonSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmRaisedTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmChangedTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmClearStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAckStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSpecificProblem"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSystemDN"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmProbableCause"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAdditionalText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmAckExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmAckParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmAckError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnAckParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnAckExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnAckError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmClearParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmClearExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmClearError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnClearParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnClearExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmUnClearError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmResendEventsParamSequence"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmResendEventsExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmResendEventsError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmResynchronizeExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmResynchronizeError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmSplitterPeakLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmServiceConfGroup.setStatus("current")

jdsuOnmsiOtuConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 8)
)
jdsuOnmsiOtuConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryIpAddress"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryDeviceName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntrySerialNumber"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntrySoftwareVersion"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntryCentralOfficeInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuEntrySeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryPosition"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntrySerialNumber"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuOtdrEntryWavelengths"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryRemote"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryPosition"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryInputs"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuSwitchEntryOutputs"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryModuleInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryPosition"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryPonInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuPortEntryLinkInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuAttributeLoadError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetPortsParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetPortsExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiOtuGetPortsError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiOtuConfGroup.setStatus("current")

jdsuOnmsiCentralOfficeConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 3, 9)
)
jdsuOnmsiCentralOfficeConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAdditionalAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeEntryAdditional"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeEntryFindable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeEntryUpdatable"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeGetParamInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeGetExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeGetError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeFindParamAttribute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeFindParamValue"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeFindExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeFindError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeLoadExecute"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiCentralOfficeAttributeLoadError"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiCentralOfficeConfGroup.setStatus("current")


# Notification objects

jdsuOnmsiImAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4, 1)
)
jdsuOnmsiImAliveTrap.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiImAliveText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiImAliveAlarmEventSequence"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiImAliveTrap.setStatus(
        "current"
    )

jdsuOnmsiHomeTestResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4, 2)
)
jdsuOnmsiHomeTestResultTrap.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiHomeStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryHomeIdentifier"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryPonInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeEntryLatestPeakStatus"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiHomeTestResultTrap.setStatus(
        "current"
    )

jdsuOnmsiPonTestResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4, 3)
)
jdsuOnmsiPonTestResultTrap.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiPonStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryDescription"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryLatestTestInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryOtuInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntryPortInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonEntrySeverity"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiPonTestResultTrap.setStatus(
        "current"
    )

jdsuOnmsiMonitoringTestResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4, 4)
)
jdsuOnmsiMonitoringTestResultTrap.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestStartTestError"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestEntryInternalKey"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiMonitoringTestResultTrap.setStatus(
        "current"
    )

jdsuOnmsiAlarmEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 4, 5)
)
jdsuOnmsiAlarmEventTrap.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntrySequence"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventClearStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAckStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPerceivedSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventProbableCause"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAdditionalText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventUserIdentifier"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventPonSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmType"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmRaisedTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmChangedTime"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmClearStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAckStatus"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSpecificProblem"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSystemDN"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmProbableCause"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAdditionalText"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiAlarmEventTrap.setStatus(
        "current"
    )


# Notifications groups

jdsuOnmsiEventsConfGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1, 1, 5, 4)
)
jdsuOnmsiEventsConfGroup.setObjects(
      *(("JDSU-ONMSI-MIB", "jdsuOnmsiImAliveTrap"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiHomeTestResultTrap"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiPonTestResultTrap"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiMonitoringTestResultTrap"),
        ("JDSU-ONMSI-MIB", "jdsuOnmsiAlarmEventTrap"))
)
if mibBuilder.loadTexts:
    jdsuOnmsiEventsConfGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JDSU-ONMSI-MIB",
    **{"JdsuOnmsiAlarmAckStatus": JdsuOnmsiAlarmAckStatus,
       "JdsuOnmsiAlarmClearStatus": JdsuOnmsiAlarmClearStatus,
       "JdsuOnmsiAlarmEventType": JdsuOnmsiAlarmEventType,
       "JdsuOnmsiInternalKey": JdsuOnmsiInternalKey,
       "JdsuOnmsiOtdrPosition": JdsuOnmsiOtdrPosition,
       "JdsuOnmsiPeakStatus": JdsuOnmsiPeakStatus,
       "JdsuOnmsiPeakType": JdsuOnmsiPeakType,
       "JdsuOnmsiSeverity": JdsuOnmsiSeverity,
       "JdsuOnmsiUtf8String": JdsuOnmsiUtf8String,
       "jdsuOnmsiMib": jdsuOnmsiMib,
       "jdsuOnmsiProduct": jdsuOnmsiProduct,
       "jdsuOnmsiProductDescr": jdsuOnmsiProductDescr,
       "jdsuOnmsiProductObjectID": jdsuOnmsiProductObjectID,
       "jdsuOnmsiProductContact": jdsuOnmsiProductContact,
       "jdsuOnmsiProductName": jdsuOnmsiProductName,
       "jdsuOnmsiProductLocation": jdsuOnmsiProductLocation,
       "jdsuOnmsiAdministration": jdsuOnmsiAdministration,
       "jdsuOnmsiSnmpConfig": jdsuOnmsiSnmpConfig,
       "jdsuOnmsiSnmpConfigurationReload": jdsuOnmsiSnmpConfigurationReload,
       "jdsuOnmsiImAlive": jdsuOnmsiImAlive,
       "jdsuOnmsiImAlivePeriodMin": jdsuOnmsiImAlivePeriodMin,
       "jdsuOnmsiImAliveText": jdsuOnmsiImAliveText,
       "jdsuOnmsiImAliveAlarmEventSequence": jdsuOnmsiImAliveAlarmEventSequence,
       "jdsuOnmsiServices": jdsuOnmsiServices,
       "jdsuOnmsiHomeService": jdsuOnmsiHomeService,
       "jdsuOnmsiHomeData": jdsuOnmsiHomeData,
       "jdsuOnmsiHomeTable": jdsuOnmsiHomeTable,
       "jdsuOnmsiHomeEntry": jdsuOnmsiHomeEntry,
       "jdsuOnmsiHomeEntryInternalKey": jdsuOnmsiHomeEntryInternalKey,
       "jdsuOnmsiHomeEntryHomeIdentifier": jdsuOnmsiHomeEntryHomeIdentifier,
       "jdsuOnmsiHomeEntryName": jdsuOnmsiHomeEntryName,
       "jdsuOnmsiHomeEntryDescription": jdsuOnmsiHomeEntryDescription,
       "jdsuOnmsiHomeEntryPonInternalKey": jdsuOnmsiHomeEntryPonInternalKey,
       "jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey": jdsuOnmsiHomeEntryHomeTerminationTypeInternalKey,
       "jdsuOnmsiHomeEntryLatestPeakInternalKey": jdsuOnmsiHomeEntryLatestPeakInternalKey,
       "jdsuOnmsiHomeEntryLatestPeakSeverity": jdsuOnmsiHomeEntryLatestPeakSeverity,
       "jdsuOnmsiHomeEntryLatestPeakStatus": jdsuOnmsiHomeEntryLatestPeakStatus,
       "jdsuOnmsiHomeEntryVip": jdsuOnmsiHomeEntryVip,
       "jdsuOnmsiHomeAdditionalAttributeTable": jdsuOnmsiHomeAdditionalAttributeTable,
       "jdsuOnmsiHomeAdditionalAttributeEntry": jdsuOnmsiHomeAdditionalAttributeEntry,
       "jdsuOnmsiHomeAdditionalAttributeEntryInternalKey": jdsuOnmsiHomeAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiHomeAdditionalAttributeEntryName": jdsuOnmsiHomeAdditionalAttributeEntryName,
       "jdsuOnmsiHomeAdditionalAttributeEntryValue": jdsuOnmsiHomeAdditionalAttributeEntryValue,
       "jdsuOnmsiHomeTerminationTypeTable": jdsuOnmsiHomeTerminationTypeTable,
       "jdsuOnmsiHomeTerminationTypeEntry": jdsuOnmsiHomeTerminationTypeEntry,
       "jdsuOnmsiHomeTerminationTypeEntryInternalKey": jdsuOnmsiHomeTerminationTypeEntryInternalKey,
       "jdsuOnmsiHomeTerminationTypeEntryName": jdsuOnmsiHomeTerminationTypeEntryName,
       "jdsuOnmsiHomeTerminationTypeEntryDescription": jdsuOnmsiHomeTerminationTypeEntryDescription,
       "jdsuOnmsiHomeAttributeTable": jdsuOnmsiHomeAttributeTable,
       "jdsuOnmsiHomeAttributeEntry": jdsuOnmsiHomeAttributeEntry,
       "jdsuOnmsiHomeAttributeEntryName": jdsuOnmsiHomeAttributeEntryName,
       "jdsuOnmsiHomeAttributeEntryAdditional": jdsuOnmsiHomeAttributeEntryAdditional,
       "jdsuOnmsiHomeAttributeEntryFindable": jdsuOnmsiHomeAttributeEntryFindable,
       "jdsuOnmsiHomeAttributeEntryUpdatable": jdsuOnmsiHomeAttributeEntryUpdatable,
       "jdsuOnmsiHomeFunctions": jdsuOnmsiHomeFunctions,
       "jdsuOnmsiHomeTerminationTypeLoad": jdsuOnmsiHomeTerminationTypeLoad,
       "jdsuOnmsiHomeTerminationTypeLoadExecute": jdsuOnmsiHomeTerminationTypeLoadExecute,
       "jdsuOnmsiHomeTerminationTypeLoadError": jdsuOnmsiHomeTerminationTypeLoadError,
       "jdsuOnmsiHomeGet": jdsuOnmsiHomeGet,
       "jdsuOnmsiHomeGetParamInternalKey": jdsuOnmsiHomeGetParamInternalKey,
       "jdsuOnmsiHomeGetExecute": jdsuOnmsiHomeGetExecute,
       "jdsuOnmsiHomeGetError": jdsuOnmsiHomeGetError,
       "jdsuOnmsiHomeFind": jdsuOnmsiHomeFind,
       "jdsuOnmsiHomeFindParamAttribute": jdsuOnmsiHomeFindParamAttribute,
       "jdsuOnmsiHomeFindParamValue": jdsuOnmsiHomeFindParamValue,
       "jdsuOnmsiHomeFindExecute": jdsuOnmsiHomeFindExecute,
       "jdsuOnmsiHomeFindError": jdsuOnmsiHomeFindError,
       "jdsuOnmsiHomeStartTest": jdsuOnmsiHomeStartTest,
       "jdsuOnmsiHomeStartTestParamInternalKey": jdsuOnmsiHomeStartTestParamInternalKey,
       "jdsuOnmsiHomeStartTestExecute": jdsuOnmsiHomeStartTestExecute,
       "jdsuOnmsiHomeStartTestError": jdsuOnmsiHomeStartTestError,
       "jdsuOnmsiHomeAttributeLoad": jdsuOnmsiHomeAttributeLoad,
       "jdsuOnmsiHomeAttributeLoadExecute": jdsuOnmsiHomeAttributeLoadExecute,
       "jdsuOnmsiHomeAttributeLoadError": jdsuOnmsiHomeAttributeLoadError,
       "jdsuOnmsiPonService": jdsuOnmsiPonService,
       "jdsuOnmsiPonData": jdsuOnmsiPonData,
       "jdsuOnmsiPonTable": jdsuOnmsiPonTable,
       "jdsuOnmsiPonEntry": jdsuOnmsiPonEntry,
       "jdsuOnmsiPonEntryInternalKey": jdsuOnmsiPonEntryInternalKey,
       "jdsuOnmsiPonEntryName": jdsuOnmsiPonEntryName,
       "jdsuOnmsiPonEntryDescription": jdsuOnmsiPonEntryDescription,
       "jdsuOnmsiPonEntryLatestTestInternalKey": jdsuOnmsiPonEntryLatestTestInternalKey,
       "jdsuOnmsiPonEntryOtuInternalKey": jdsuOnmsiPonEntryOtuInternalKey,
       "jdsuOnmsiPonEntryPortInternalKey": jdsuOnmsiPonEntryPortInternalKey,
       "jdsuOnmsiPonEntrySeverity": jdsuOnmsiPonEntrySeverity,
       "jdsuOnmsiPonEntrySchedulingConfiguration": jdsuOnmsiPonEntrySchedulingConfiguration,
       "jdsuOnmsiPonAdditionalAttributeTable": jdsuOnmsiPonAdditionalAttributeTable,
       "jdsuOnmsiPonAdditionalAttributeEntry": jdsuOnmsiPonAdditionalAttributeEntry,
       "jdsuOnmsiPonAdditionalAttributeEntryInternalKey": jdsuOnmsiPonAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiPonAdditionalAttributeEntryName": jdsuOnmsiPonAdditionalAttributeEntryName,
       "jdsuOnmsiPonAdditionalAttributeEntryValue": jdsuOnmsiPonAdditionalAttributeEntryValue,
       "jdsuOnmsiPonAttributeTable": jdsuOnmsiPonAttributeTable,
       "jdsuOnmsiPonAttributeEntry": jdsuOnmsiPonAttributeEntry,
       "jdsuOnmsiPonAttributeEntryName": jdsuOnmsiPonAttributeEntryName,
       "jdsuOnmsiPonAttributeEntryAdditional": jdsuOnmsiPonAttributeEntryAdditional,
       "jdsuOnmsiPonAttributeEntryFindable": jdsuOnmsiPonAttributeEntryFindable,
       "jdsuOnmsiPonAttributeEntryUpdatable": jdsuOnmsiPonAttributeEntryUpdatable,
       "jdsuOnmsiPonFunctions": jdsuOnmsiPonFunctions,
       "jdsuOnmsiPonGet": jdsuOnmsiPonGet,
       "jdsuOnmsiPonGetParamInternalKey": jdsuOnmsiPonGetParamInternalKey,
       "jdsuOnmsiPonGetExecute": jdsuOnmsiPonGetExecute,
       "jdsuOnmsiPonGetError": jdsuOnmsiPonGetError,
       "jdsuOnmsiPonFind": jdsuOnmsiPonFind,
       "jdsuOnmsiPonFindParamAttribute": jdsuOnmsiPonFindParamAttribute,
       "jdsuOnmsiPonFindParamValue": jdsuOnmsiPonFindParamValue,
       "jdsuOnmsiPonFindExecute": jdsuOnmsiPonFindExecute,
       "jdsuOnmsiPonFindError": jdsuOnmsiPonFindError,
       "jdsuOnmsiPonStartTest": jdsuOnmsiPonStartTest,
       "jdsuOnmsiPonStartTestParamInternalKey": jdsuOnmsiPonStartTestParamInternalKey,
       "jdsuOnmsiPonStartTestExecute": jdsuOnmsiPonStartTestExecute,
       "jdsuOnmsiPonStartTestError": jdsuOnmsiPonStartTestError,
       "jdsuOnmsiPonAttributeLoad": jdsuOnmsiPonAttributeLoad,
       "jdsuOnmsiPonAttributeLoadExecute": jdsuOnmsiPonAttributeLoadExecute,
       "jdsuOnmsiPonAttributeLoadError": jdsuOnmsiPonAttributeLoadError,
       "jdsuOnmsiPeakService": jdsuOnmsiPeakService,
       "jdsuOnmsiPeakData": jdsuOnmsiPeakData,
       "jdsuOnmsiPeakTable": jdsuOnmsiPeakTable,
       "jdsuOnmsiPeakEntry": jdsuOnmsiPeakEntry,
       "jdsuOnmsiPeakEntryInternalKey": jdsuOnmsiPeakEntryInternalKey,
       "jdsuOnmsiPeakEntryTestInternalKey": jdsuOnmsiPeakEntryTestInternalKey,
       "jdsuOnmsiPeakEntryDate": jdsuOnmsiPeakEntryDate,
       "jdsuOnmsiPeakEntryIsAReference": jdsuOnmsiPeakEntryIsAReference,
       "jdsuOnmsiPeakEntryDistance": jdsuOnmsiPeakEntryDistance,
       "jdsuOnmsiPeakEntryLevel": jdsuOnmsiPeakEntryLevel,
       "jdsuOnmsiPeakEntryPower": jdsuOnmsiPeakEntryPower,
       "jdsuOnmsiPeakEntryIsPowerMeasured": jdsuOnmsiPeakEntryIsPowerMeasured,
       "jdsuOnmsiPeakEntrySeverity": jdsuOnmsiPeakEntrySeverity,
       "jdsuOnmsiPeakEntryStatus": jdsuOnmsiPeakEntryStatus,
       "jdsuOnmsiPeakEntryRefDistance": jdsuOnmsiPeakEntryRefDistance,
       "jdsuOnmsiPeakEntryRefLevel": jdsuOnmsiPeakEntryRefLevel,
       "jdsuOnmsiPeakEntryRefPower": jdsuOnmsiPeakEntryRefPower,
       "jdsuOnmsiPeakEntryRefIsPowerMeasured": jdsuOnmsiPeakEntryRefIsPowerMeasured,
       "jdsuOnmsiPeakEntryRefDate": jdsuOnmsiPeakEntryRefDate,
       "jdsuOnmsiPeakEntryType": jdsuOnmsiPeakEntryType,
       "jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey": jdsuOnmsiPeakEntryHomeTerminationTypeInternalKey,
       "jdsuOnmsiPeakEntryHomeInternalKey": jdsuOnmsiPeakEntryHomeInternalKey,
       "jdsuOnmsiPeakFunctions": jdsuOnmsiPeakFunctions,
       "jdsuOnmsiPeakGet": jdsuOnmsiPeakGet,
       "jdsuOnmsiPeakGetParamInternalKey": jdsuOnmsiPeakGetParamInternalKey,
       "jdsuOnmsiPeakGetExecute": jdsuOnmsiPeakGetExecute,
       "jdsuOnmsiPeakGetError": jdsuOnmsiPeakGetError,
       "jdsuOnmsiPeakFind": jdsuOnmsiPeakFind,
       "jdsuOnmsiPeakFindParamAttribute": jdsuOnmsiPeakFindParamAttribute,
       "jdsuOnmsiPeakFindParamValue": jdsuOnmsiPeakFindParamValue,
       "jdsuOnmsiPeakFindExecute": jdsuOnmsiPeakFindExecute,
       "jdsuOnmsiPeakFindError": jdsuOnmsiPeakFindError,
       "jdsuOnmsiLinkService": jdsuOnmsiLinkService,
       "jdsuOnmsiLinkData": jdsuOnmsiLinkData,
       "jdsuOnmsiLinkTable": jdsuOnmsiLinkTable,
       "jdsuOnmsiLinkEntry": jdsuOnmsiLinkEntry,
       "jdsuOnmsiLinkEntryInternalKey": jdsuOnmsiLinkEntryInternalKey,
       "jdsuOnmsiLinkEntryName": jdsuOnmsiLinkEntryName,
       "jdsuOnmsiLinkEntryDescription": jdsuOnmsiLinkEntryDescription,
       "jdsuOnmsiLinkEntryMeasureEnabled": jdsuOnmsiLinkEntryMeasureEnabled,
       "jdsuOnmsiLinkEntryOtuInternalKey": jdsuOnmsiLinkEntryOtuInternalKey,
       "jdsuOnmsiLinkEntrySeverity": jdsuOnmsiLinkEntrySeverity,
       "jdsuOnmsiLinkAdditionalAttributeTable": jdsuOnmsiLinkAdditionalAttributeTable,
       "jdsuOnmsiLinkAdditionalAttributeEntry": jdsuOnmsiLinkAdditionalAttributeEntry,
       "jdsuOnmsiLinkAdditionalAttributeEntryInternalKey": jdsuOnmsiLinkAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiLinkAdditionalAttributeEntryName": jdsuOnmsiLinkAdditionalAttributeEntryName,
       "jdsuOnmsiLinkAdditionalAttributeEntryValue": jdsuOnmsiLinkAdditionalAttributeEntryValue,
       "jdsuOnmsiLinkAttributeTable": jdsuOnmsiLinkAttributeTable,
       "jdsuOnmsiLinkAttributeEntry": jdsuOnmsiLinkAttributeEntry,
       "jdsuOnmsiLinkAttributeEntryName": jdsuOnmsiLinkAttributeEntryName,
       "jdsuOnmsiLinkAttributeEntryAdditional": jdsuOnmsiLinkAttributeEntryAdditional,
       "jdsuOnmsiLinkAttributeEntryFindable": jdsuOnmsiLinkAttributeEntryFindable,
       "jdsuOnmsiLinkAttributeEntryUpdatable": jdsuOnmsiLinkAttributeEntryUpdatable,
       "jdsuOnmsiLinkFunctions": jdsuOnmsiLinkFunctions,
       "jdsuOnmsiLinkGet": jdsuOnmsiLinkGet,
       "jdsuOnmsiLinkGetParamInternalKey": jdsuOnmsiLinkGetParamInternalKey,
       "jdsuOnmsiLinkGetExecute": jdsuOnmsiLinkGetExecute,
       "jdsuOnmsiLinkGetError": jdsuOnmsiLinkGetError,
       "jdsuOnmsiLinkFind": jdsuOnmsiLinkFind,
       "jdsuOnmsiLinkFindParamAttribute": jdsuOnmsiLinkFindParamAttribute,
       "jdsuOnmsiLinkFindParamValue": jdsuOnmsiLinkFindParamValue,
       "jdsuOnmsiLinkFindExecute": jdsuOnmsiLinkFindExecute,
       "jdsuOnmsiLinkFindError": jdsuOnmsiLinkFindError,
       "jdsuOnmsiLinkUpdate": jdsuOnmsiLinkUpdate,
       "jdsuOnmsiLinkUpdateParamInternalKey": jdsuOnmsiLinkUpdateParamInternalKey,
       "jdsuOnmsiLinkUpdateExecute": jdsuOnmsiLinkUpdateExecute,
       "jdsuOnmsiLinkUpdateError": jdsuOnmsiLinkUpdateError,
       "jdsuOnmsiLinkAttributeLoad": jdsuOnmsiLinkAttributeLoad,
       "jdsuOnmsiLinkAttributeLoadExecute": jdsuOnmsiLinkAttributeLoadExecute,
       "jdsuOnmsiLinkAttributeLoadError": jdsuOnmsiLinkAttributeLoadError,
       "jdsuOnmsiMonitoringTestService": jdsuOnmsiMonitoringTestService,
       "jdsuOnmsiMonitoringTestData": jdsuOnmsiMonitoringTestData,
       "jdsuOnmsiMonitoringTestTable": jdsuOnmsiMonitoringTestTable,
       "jdsuOnmsiMonitoringTestEntry": jdsuOnmsiMonitoringTestEntry,
       "jdsuOnmsiMonitoringTestEntryInternalKey": jdsuOnmsiMonitoringTestEntryInternalKey,
       "jdsuOnmsiMonitoringTestEntryName": jdsuOnmsiMonitoringTestEntryName,
       "jdsuOnmsiMonitoringTestEntryDescription": jdsuOnmsiMonitoringTestEntryDescription,
       "jdsuOnmsiMonitoringTestEntryLinkInternalKey": jdsuOnmsiMonitoringTestEntryLinkInternalKey,
       "jdsuOnmsiMonitoringTestEntryDisplayOrder": jdsuOnmsiMonitoringTestEntryDisplayOrder,
       "jdsuOnmsiMonitoringTestEntrySeverity": jdsuOnmsiMonitoringTestEntrySeverity,
       "jdsuOnmsiMonitoringTestEntryDetectionConfiguration": jdsuOnmsiMonitoringTestEntryDetectionConfiguration,
       "jdsuOnmsiMonitoringTestEntryLocalizationConfiguration": jdsuOnmsiMonitoringTestEntryLocalizationConfiguration,
       "jdsuOnmsiMonitoringTestEntrySchedulingConfiguration": jdsuOnmsiMonitoringTestEntrySchedulingConfiguration,
       "jdsuOnmsiMonitoringTestAdditionalAttributeTable": jdsuOnmsiMonitoringTestAdditionalAttributeTable,
       "jdsuOnmsiMonitoringTestAdditionalAttributeEntry": jdsuOnmsiMonitoringTestAdditionalAttributeEntry,
       "jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey": jdsuOnmsiMonitoringTestAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiMonitoringTestAdditionalAttributeEntryName": jdsuOnmsiMonitoringTestAdditionalAttributeEntryName,
       "jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue": jdsuOnmsiMonitoringTestAdditionalAttributeEntryValue,
       "jdsuOnmsiMonitoringTestAttributeTable": jdsuOnmsiMonitoringTestAttributeTable,
       "jdsuOnmsiMonitoringTestAttributeEntry": jdsuOnmsiMonitoringTestAttributeEntry,
       "jdsuOnmsiMonitoringTestAttributeEntryName": jdsuOnmsiMonitoringTestAttributeEntryName,
       "jdsuOnmsiMonitoringTestAttributeEntryAdditional": jdsuOnmsiMonitoringTestAttributeEntryAdditional,
       "jdsuOnmsiMonitoringTestAttributeEntryFindable": jdsuOnmsiMonitoringTestAttributeEntryFindable,
       "jdsuOnmsiMonitoringTestAttributeEntryUpdatable": jdsuOnmsiMonitoringTestAttributeEntryUpdatable,
       "jdsuOnmsiMonitoringTestFunctions": jdsuOnmsiMonitoringTestFunctions,
       "jdsuOnmsiMonitoringTestGet": jdsuOnmsiMonitoringTestGet,
       "jdsuOnmsiMonitoringTestGetParamInternalKey": jdsuOnmsiMonitoringTestGetParamInternalKey,
       "jdsuOnmsiMonitoringTestGetExecute": jdsuOnmsiMonitoringTestGetExecute,
       "jdsuOnmsiMonitoringTestGetError": jdsuOnmsiMonitoringTestGetError,
       "jdsuOnmsiMonitoringTestFind": jdsuOnmsiMonitoringTestFind,
       "jdsuOnmsiMonitoringTestFindParamAttribute": jdsuOnmsiMonitoringTestFindParamAttribute,
       "jdsuOnmsiMonitoringTestFindParamValue": jdsuOnmsiMonitoringTestFindParamValue,
       "jdsuOnmsiMonitoringTestFindExecute": jdsuOnmsiMonitoringTestFindExecute,
       "jdsuOnmsiMonitoringTestFindError": jdsuOnmsiMonitoringTestFindError,
       "jdsuOnmsiMonitoringTestStartTest": jdsuOnmsiMonitoringTestStartTest,
       "jdsuOnmsiMonitoringTestStartTestParamInternalKey": jdsuOnmsiMonitoringTestStartTestParamInternalKey,
       "jdsuOnmsiMonitoringTestStartTestExecute": jdsuOnmsiMonitoringTestStartTestExecute,
       "jdsuOnmsiMonitoringTestStartTestError": jdsuOnmsiMonitoringTestStartTestError,
       "jdsuOnmsiMonitoringTestAttributeLoad": jdsuOnmsiMonitoringTestAttributeLoad,
       "jdsuOnmsiMonitoringTestAttributeLoadExecute": jdsuOnmsiMonitoringTestAttributeLoadExecute,
       "jdsuOnmsiMonitoringTestAttributeLoadError": jdsuOnmsiMonitoringTestAttributeLoadError,
       "jdsuOnmsiAlarmService": jdsuOnmsiAlarmService,
       "jdsuOnmsiAlarmData": jdsuOnmsiAlarmData,
       "jdsuOnmsiAlarmTypesTable": jdsuOnmsiAlarmTypesTable,
       "jdsuOnmsiAlarmTypesEntry": jdsuOnmsiAlarmTypesEntry,
       "jdsuOnmsiAlarmTypeName": jdsuOnmsiAlarmTypeName,
       "jdsuOnmsiAlarmSpecificProblemsTable": jdsuOnmsiAlarmSpecificProblemsTable,
       "jdsuOnmsiAlarmSpecificProblemsEntry": jdsuOnmsiAlarmSpecificProblemsEntry,
       "jdsuOnmsiAlarmSpecificProblemName": jdsuOnmsiAlarmSpecificProblemName,
       "jdsuOnmsiAlarmEventTable": jdsuOnmsiAlarmEventTable,
       "jdsuOnmsiAlarmEventEntry": jdsuOnmsiAlarmEventEntry,
       "jdsuOnmsiAlarmEventEntrySequence": jdsuOnmsiAlarmEventEntrySequence,
       "jdsuOnmsiAlarmEventEntryEventInternalKey": jdsuOnmsiAlarmEventEntryEventInternalKey,
       "jdsuOnmsiAlarmEventEntryEventType": jdsuOnmsiAlarmEventEntryEventType,
       "jdsuOnmsiAlarmEventEntryEventTime": jdsuOnmsiAlarmEventEntryEventTime,
       "jdsuOnmsiAlarmEventEntryEventClearStatus": jdsuOnmsiAlarmEventEntryEventClearStatus,
       "jdsuOnmsiAlarmEventEntryEventAckStatus": jdsuOnmsiAlarmEventEntryEventAckStatus,
       "jdsuOnmsiAlarmEventEntryEventPerceivedSeverity": jdsuOnmsiAlarmEventEntryEventPerceivedSeverity,
       "jdsuOnmsiAlarmEventEntryEventProbableCause": jdsuOnmsiAlarmEventEntryEventProbableCause,
       "jdsuOnmsiAlarmEventEntryEventAdditionalText": jdsuOnmsiAlarmEventEntryEventAdditionalText,
       "jdsuOnmsiAlarmEventEntryEventUserIdentifier": jdsuOnmsiAlarmEventEntryEventUserIdentifier,
       "jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos": jdsuOnmsiAlarmEventEntryEventMonitoringTestSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos": jdsuOnmsiAlarmEventEntryEventPointToPointSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos": jdsuOnmsiAlarmEventEntryEventAttenuationSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos": jdsuOnmsiAlarmEventEntryEventPeakSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos": jdsuOnmsiAlarmEventEntryEventOrlSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos": jdsuOnmsiAlarmEventEntryEventFiberLengthExtensionSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos": jdsuOnmsiAlarmEventEntryEventLocalizationSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmInternalKey": jdsuOnmsiAlarmEventEntryAlarmInternalKey,
       "jdsuOnmsiAlarmEventEntryAlarmType": jdsuOnmsiAlarmEventEntryAlarmType,
       "jdsuOnmsiAlarmEventEntryAlarmRaisedTime": jdsuOnmsiAlarmEventEntryAlarmRaisedTime,
       "jdsuOnmsiAlarmEventEntryAlarmChangedTime": jdsuOnmsiAlarmEventEntryAlarmChangedTime,
       "jdsuOnmsiAlarmEventEntryAlarmClearStatus": jdsuOnmsiAlarmEventEntryAlarmClearStatus,
       "jdsuOnmsiAlarmEventEntryAlarmAckStatus": jdsuOnmsiAlarmEventEntryAlarmAckStatus,
       "jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity": jdsuOnmsiAlarmEventEntryAlarmPerceivedSeverity,
       "jdsuOnmsiAlarmEventEntryAlarmSpecificProblem": jdsuOnmsiAlarmEventEntryAlarmSpecificProblem,
       "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind": jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityKind,
       "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey": jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityInternalKey,
       "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName": jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityName,
       "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid": jdsuOnmsiAlarmEventEntryAlarmOriginatingEntityOid,
       "jdsuOnmsiAlarmEventEntryAlarmSystemDN": jdsuOnmsiAlarmEventEntryAlarmSystemDN,
       "jdsuOnmsiAlarmEventEntryAlarmProbableCause": jdsuOnmsiAlarmEventEntryAlarmProbableCause,
       "jdsuOnmsiAlarmEventEntryAlarmAdditionalText": jdsuOnmsiAlarmEventEntryAlarmAdditionalText,
       "jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmMonitoringTestSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmPointToPointSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmAttenuationSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmPeakSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmOrlSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmFiberLengthExtensionSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmLocalizationSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity": jdsuOnmsiAlarmEventEntryAlarmOriginatingEntity,
       "jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos": jdsuOnmsiAlarmEventEntryEventGpsCoordinatesSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmGpsCoordinatesSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventPonSpecificInfos": jdsuOnmsiAlarmEventEntryEventPonSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmPonSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos": jdsuOnmsiAlarmEventEntryEventSplitterSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmSplitterSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos": jdsuOnmsiAlarmEventEntryEventStrainSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmStrainSpecificInfos,
       "jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos": jdsuOnmsiAlarmEventEntryEventTemperatureSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos": jdsuOnmsiAlarmEventEntryAlarmTemperatureSpecificInfos,
       "jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes": jdsuOnmsiAlarmEventEntryAlarmAdditionalAttributes,
       "jdsuOnmsiAlarmSplitterPeakTable": jdsuOnmsiAlarmSplitterPeakTable,
       "jdsuOnmsiAlarmSplitterPeakEntry": jdsuOnmsiAlarmSplitterPeakEntry,
       "jdsuOnmsiAlarmSplitterPeakEntryInternalKey": jdsuOnmsiAlarmSplitterPeakEntryInternalKey,
       "jdsuOnmsiAlarmSplitterPeakEntryName": jdsuOnmsiAlarmSplitterPeakEntryName,
       "jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity": jdsuOnmsiAlarmSplitterPeakEntryPerceivedSeverity,
       "jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity": jdsuOnmsiAlarmSplitterPeakEntryPreviousSeverity,
       "jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance": jdsuOnmsiAlarmSplitterPeakEntryReferenceBottomDistance,
       "jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance": jdsuOnmsiAlarmSplitterPeakEntryReferenceTopDistance,
       "jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel": jdsuOnmsiAlarmSplitterPeakEntryReferenceLevel,
       "jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid": jdsuOnmsiAlarmSplitterPeakEntryPeakMeasurementValid,
       "jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance": jdsuOnmsiAlarmSplitterPeakEntryMeasuredBottomDistance,
       "jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance": jdsuOnmsiAlarmSplitterPeakEntryMeasuredTopDistance,
       "jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel": jdsuOnmsiAlarmSplitterPeakEntryMeasuredLevel,
       "jdsuOnmsiAlarmFunctions": jdsuOnmsiAlarmFunctions,
       "jdsuOnmsiAlarmAck": jdsuOnmsiAlarmAck,
       "jdsuOnmsiAlarmAckParamInternalKey": jdsuOnmsiAlarmAckParamInternalKey,
       "jdsuOnmsiAlarmAckExecute": jdsuOnmsiAlarmAckExecute,
       "jdsuOnmsiAlarmAckError": jdsuOnmsiAlarmAckError,
       "jdsuOnmsiAlarmUnAck": jdsuOnmsiAlarmUnAck,
       "jdsuOnmsiAlarmUnAckParamInternalKey": jdsuOnmsiAlarmUnAckParamInternalKey,
       "jdsuOnmsiAlarmUnAckExecute": jdsuOnmsiAlarmUnAckExecute,
       "jdsuOnmsiAlarmUnAckError": jdsuOnmsiAlarmUnAckError,
       "jdsuOnmsiAlarmClear": jdsuOnmsiAlarmClear,
       "jdsuOnmsiAlarmClearParamInternalKey": jdsuOnmsiAlarmClearParamInternalKey,
       "jdsuOnmsiAlarmClearExecute": jdsuOnmsiAlarmClearExecute,
       "jdsuOnmsiAlarmClearError": jdsuOnmsiAlarmClearError,
       "jdsuOnmsiAlarmUnClear": jdsuOnmsiAlarmUnClear,
       "jdsuOnmsiAlarmUnClearParamInternalKey": jdsuOnmsiAlarmUnClearParamInternalKey,
       "jdsuOnmsiAlarmUnClearExecute": jdsuOnmsiAlarmUnClearExecute,
       "jdsuOnmsiAlarmUnClearError": jdsuOnmsiAlarmUnClearError,
       "jdsuOnmsiAlarmResendEvents": jdsuOnmsiAlarmResendEvents,
       "jdsuOnmsiAlarmResendEventsParamSequence": jdsuOnmsiAlarmResendEventsParamSequence,
       "jdsuOnmsiAlarmResendEventsExecute": jdsuOnmsiAlarmResendEventsExecute,
       "jdsuOnmsiAlarmResendEventsError": jdsuOnmsiAlarmResendEventsError,
       "jdsuOnmsiAlarmResynchronize": jdsuOnmsiAlarmResynchronize,
       "jdsuOnmsiAlarmResynchronizeExecute": jdsuOnmsiAlarmResynchronizeExecute,
       "jdsuOnmsiAlarmResynchronizeError": jdsuOnmsiAlarmResynchronizeError,
       "jdsuOnmsiAlarmSplitterPeakLoad": jdsuOnmsiAlarmSplitterPeakLoad,
       "jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey": jdsuOnmsiAlarmSplitterPeakLoadParamEventInternalKey,
       "jdsuOnmsiAlarmSplitterPeakLoadExecute": jdsuOnmsiAlarmSplitterPeakLoadExecute,
       "jdsuOnmsiAlarmSplitterPeakLoadError": jdsuOnmsiAlarmSplitterPeakLoadError,
       "jdsuOnmsiOtuService": jdsuOnmsiOtuService,
       "jdsuOnmsiOtuData": jdsuOnmsiOtuData,
       "jdsuOnmsiOtuTable": jdsuOnmsiOtuTable,
       "jdsuOnmsiOtuEntry": jdsuOnmsiOtuEntry,
       "jdsuOnmsiOtuEntryInternalKey": jdsuOnmsiOtuEntryInternalKey,
       "jdsuOnmsiOtuEntryName": jdsuOnmsiOtuEntryName,
       "jdsuOnmsiOtuEntryDescription": jdsuOnmsiOtuEntryDescription,
       "jdsuOnmsiOtuEntryIpAddress": jdsuOnmsiOtuEntryIpAddress,
       "jdsuOnmsiOtuEntryDeviceName": jdsuOnmsiOtuEntryDeviceName,
       "jdsuOnmsiOtuEntrySerialNumber": jdsuOnmsiOtuEntrySerialNumber,
       "jdsuOnmsiOtuEntrySoftwareVersion": jdsuOnmsiOtuEntrySoftwareVersion,
       "jdsuOnmsiOtuEntryCentralOfficeInternalKey": jdsuOnmsiOtuEntryCentralOfficeInternalKey,
       "jdsuOnmsiOtuEntrySeverity": jdsuOnmsiOtuEntrySeverity,
       "jdsuOnmsiOtuAdditionalAttributeTable": jdsuOnmsiOtuAdditionalAttributeTable,
       "jdsuOnmsiOtuAdditionalAttributeEntry": jdsuOnmsiOtuAdditionalAttributeEntry,
       "jdsuOnmsiOtuAdditionalAttributeEntryInternalKey": jdsuOnmsiOtuAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiOtuAdditionalAttributeEntryName": jdsuOnmsiOtuAdditionalAttributeEntryName,
       "jdsuOnmsiOtuAdditionalAttributeEntryValue": jdsuOnmsiOtuAdditionalAttributeEntryValue,
       "jdsuOnmsiOtuAttributeTable": jdsuOnmsiOtuAttributeTable,
       "jdsuOnmsiOtuAttributeEntry": jdsuOnmsiOtuAttributeEntry,
       "jdsuOnmsiOtuAttributeEntryName": jdsuOnmsiOtuAttributeEntryName,
       "jdsuOnmsiOtuAttributeEntryAdditional": jdsuOnmsiOtuAttributeEntryAdditional,
       "jdsuOnmsiOtuAttributeEntryFindable": jdsuOnmsiOtuAttributeEntryFindable,
       "jdsuOnmsiOtuAttributeEntryUpdatable": jdsuOnmsiOtuAttributeEntryUpdatable,
       "jdsuOnmsiOtuOtdrTable": jdsuOnmsiOtuOtdrTable,
       "jdsuOnmsiOtuOtdrEntry": jdsuOnmsiOtuOtdrEntry,
       "jdsuOnmsiOtuOtdrEntryInternalKey": jdsuOnmsiOtuOtdrEntryInternalKey,
       "jdsuOnmsiOtuOtdrEntryOtuInternalKey": jdsuOnmsiOtuOtdrEntryOtuInternalKey,
       "jdsuOnmsiOtuOtdrEntryPosition": jdsuOnmsiOtuOtdrEntryPosition,
       "jdsuOnmsiOtuOtdrEntryType": jdsuOnmsiOtuOtdrEntryType,
       "jdsuOnmsiOtuOtdrEntrySerialNumber": jdsuOnmsiOtuOtdrEntrySerialNumber,
       "jdsuOnmsiOtuOtdrEntryWavelengths": jdsuOnmsiOtuOtdrEntryWavelengths,
       "jdsuOnmsiOtuSwitchTable": jdsuOnmsiOtuSwitchTable,
       "jdsuOnmsiOtuSwitchEntry": jdsuOnmsiOtuSwitchEntry,
       "jdsuOnmsiOtuSwitchEntryInternalKey": jdsuOnmsiOtuSwitchEntryInternalKey,
       "jdsuOnmsiOtuSwitchEntryOtuInternalKey": jdsuOnmsiOtuSwitchEntryOtuInternalKey,
       "jdsuOnmsiOtuSwitchEntryName": jdsuOnmsiOtuSwitchEntryName,
       "jdsuOnmsiOtuSwitchEntryRemote": jdsuOnmsiOtuSwitchEntryRemote,
       "jdsuOnmsiOtuSwitchEntryPosition": jdsuOnmsiOtuSwitchEntryPosition,
       "jdsuOnmsiOtuSwitchEntryInputs": jdsuOnmsiOtuSwitchEntryInputs,
       "jdsuOnmsiOtuSwitchEntryOutputs": jdsuOnmsiOtuSwitchEntryOutputs,
       "jdsuOnmsiOtuPortTable": jdsuOnmsiOtuPortTable,
       "jdsuOnmsiOtuPortEntry": jdsuOnmsiOtuPortEntry,
       "jdsuOnmsiOtuPortEntryInternalKey": jdsuOnmsiOtuPortEntryInternalKey,
       "jdsuOnmsiOtuPortEntryOtuInternalKey": jdsuOnmsiOtuPortEntryOtuInternalKey,
       "jdsuOnmsiOtuPortEntryModuleInternalKey": jdsuOnmsiOtuPortEntryModuleInternalKey,
       "jdsuOnmsiOtuPortEntryPosition": jdsuOnmsiOtuPortEntryPosition,
       "jdsuOnmsiOtuPortEntryPonInternalKey": jdsuOnmsiOtuPortEntryPonInternalKey,
       "jdsuOnmsiOtuPortEntryLinkInternalKey": jdsuOnmsiOtuPortEntryLinkInternalKey,
       "jdsuOnmsiOtuFunctions": jdsuOnmsiOtuFunctions,
       "jdsuOnmsiOtuGet": jdsuOnmsiOtuGet,
       "jdsuOnmsiOtuGetParamInternalKey": jdsuOnmsiOtuGetParamInternalKey,
       "jdsuOnmsiOtuGetExecute": jdsuOnmsiOtuGetExecute,
       "jdsuOnmsiOtuGetError": jdsuOnmsiOtuGetError,
       "jdsuOnmsiOtuFind": jdsuOnmsiOtuFind,
       "jdsuOnmsiOtuFindParamAttribute": jdsuOnmsiOtuFindParamAttribute,
       "jdsuOnmsiOtuFindParamValue": jdsuOnmsiOtuFindParamValue,
       "jdsuOnmsiOtuFindExecute": jdsuOnmsiOtuFindExecute,
       "jdsuOnmsiOtuFindError": jdsuOnmsiOtuFindError,
       "jdsuOnmsiOtuAttributeLoad": jdsuOnmsiOtuAttributeLoad,
       "jdsuOnmsiOtuAttributeLoadExecute": jdsuOnmsiOtuAttributeLoadExecute,
       "jdsuOnmsiOtuAttributeLoadError": jdsuOnmsiOtuAttributeLoadError,
       "jdsuOnmsiOtuGetPorts": jdsuOnmsiOtuGetPorts,
       "jdsuOnmsiOtuGetPortsParamInternalKey": jdsuOnmsiOtuGetPortsParamInternalKey,
       "jdsuOnmsiOtuGetPortsExecute": jdsuOnmsiOtuGetPortsExecute,
       "jdsuOnmsiOtuGetPortsError": jdsuOnmsiOtuGetPortsError,
       "jdsuOnmsiCentralOfficeService": jdsuOnmsiCentralOfficeService,
       "jdsuOnmsiCentralOfficeData": jdsuOnmsiCentralOfficeData,
       "jdsuOnmsiCentralOfficeTable": jdsuOnmsiCentralOfficeTable,
       "jdsuOnmsiCentralOfficeEntry": jdsuOnmsiCentralOfficeEntry,
       "jdsuOnmsiCentralOfficeEntryInternalKey": jdsuOnmsiCentralOfficeEntryInternalKey,
       "jdsuOnmsiCentralOfficeEntryName": jdsuOnmsiCentralOfficeEntryName,
       "jdsuOnmsiCentralOfficeEntryDescription": jdsuOnmsiCentralOfficeEntryDescription,
       "jdsuOnmsiCentralOfficeAdditionalAttributeTable": jdsuOnmsiCentralOfficeAdditionalAttributeTable,
       "jdsuOnmsiCentralOfficeAdditionalAttributeEntry": jdsuOnmsiCentralOfficeAdditionalAttributeEntry,
       "jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey": jdsuOnmsiCentralOfficeAdditionalAttributeEntryInternalKey,
       "jdsuOnmsiCentralOfficeAdditionalAttributeEntryName": jdsuOnmsiCentralOfficeAdditionalAttributeEntryName,
       "jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue": jdsuOnmsiCentralOfficeAdditionalAttributeEntryValue,
       "jdsuOnmsiCentralOfficeAttributeTable": jdsuOnmsiCentralOfficeAttributeTable,
       "jdsuOnmsiCentralOfficeAttributeEntry": jdsuOnmsiCentralOfficeAttributeEntry,
       "jdsuOnmsiCentralOfficeAttributeEntryName": jdsuOnmsiCentralOfficeAttributeEntryName,
       "jdsuOnmsiCentralOfficeAttributeEntryAdditional": jdsuOnmsiCentralOfficeAttributeEntryAdditional,
       "jdsuOnmsiCentralOfficeAttributeEntryFindable": jdsuOnmsiCentralOfficeAttributeEntryFindable,
       "jdsuOnmsiCentralOfficeAttributeEntryUpdatable": jdsuOnmsiCentralOfficeAttributeEntryUpdatable,
       "jdsuOnmsiCentralOfficeFunctions": jdsuOnmsiCentralOfficeFunctions,
       "jdsuOnmsiCentralOfficeGet": jdsuOnmsiCentralOfficeGet,
       "jdsuOnmsiCentralOfficeGetParamInternalKey": jdsuOnmsiCentralOfficeGetParamInternalKey,
       "jdsuOnmsiCentralOfficeGetExecute": jdsuOnmsiCentralOfficeGetExecute,
       "jdsuOnmsiCentralOfficeGetError": jdsuOnmsiCentralOfficeGetError,
       "jdsuOnmsiCentralOfficeFind": jdsuOnmsiCentralOfficeFind,
       "jdsuOnmsiCentralOfficeFindParamAttribute": jdsuOnmsiCentralOfficeFindParamAttribute,
       "jdsuOnmsiCentralOfficeFindParamValue": jdsuOnmsiCentralOfficeFindParamValue,
       "jdsuOnmsiCentralOfficeFindExecute": jdsuOnmsiCentralOfficeFindExecute,
       "jdsuOnmsiCentralOfficeFindError": jdsuOnmsiCentralOfficeFindError,
       "jdsuOnmsiCentralOfficeAttributeLoad": jdsuOnmsiCentralOfficeAttributeLoad,
       "jdsuOnmsiCentralOfficeAttributeLoadExecute": jdsuOnmsiCentralOfficeAttributeLoadExecute,
       "jdsuOnmsiCentralOfficeAttributeLoadError": jdsuOnmsiCentralOfficeAttributeLoadError,
       "jdsuOnmsiEvents": jdsuOnmsiEvents,
       "jdsuOnmsiImAliveTrap": jdsuOnmsiImAliveTrap,
       "jdsuOnmsiHomeTestResultTrap": jdsuOnmsiHomeTestResultTrap,
       "jdsuOnmsiPonTestResultTrap": jdsuOnmsiPonTestResultTrap,
       "jdsuOnmsiMonitoringTestResultTrap": jdsuOnmsiMonitoringTestResultTrap,
       "jdsuOnmsiAlarmEventTrap": jdsuOnmsiAlarmEventTrap,
       "jdsuOnmsiConf": jdsuOnmsiConf,
       "jdsuOnmsiProductGroups": jdsuOnmsiProductGroups,
       "jdsOnmsiAdministrationConfGroups": jdsOnmsiAdministrationConfGroups,
       "jdsuOnmsiSnmpConfigConfGroup": jdsuOnmsiSnmpConfigConfGroup,
       "jdsuOnmsiImAliveConfGroup": jdsuOnmsiImAliveConfGroup,
       "jdsuOnmsiServicesConfGroups": jdsuOnmsiServicesConfGroups,
       "jdsuOnmsiHomeTerminationTypeConfGroup": jdsuOnmsiHomeTerminationTypeConfGroup,
       "jdsuOnmsiHomeConfGroup": jdsuOnmsiHomeConfGroup,
       "jdsuOnmsiPonConfGroup": jdsuOnmsiPonConfGroup,
       "jdsuOnmsiPeakConfGroup": jdsuOnmsiPeakConfGroup,
       "jdsuOnmsiLinkServiceConfGroup": jdsuOnmsiLinkServiceConfGroup,
       "jdsuOnmsiMonitoringTestServiceConfGroup": jdsuOnmsiMonitoringTestServiceConfGroup,
       "jdsuOnmsiAlarmServiceConfGroup": jdsuOnmsiAlarmServiceConfGroup,
       "jdsuOnmsiOtuConfGroup": jdsuOnmsiOtuConfGroup,
       "jdsuOnmsiCentralOfficeConfGroup": jdsuOnmsiCentralOfficeConfGroup,
       "jdsuOnmsiEventsConfGroup": jdsuOnmsiEventsConfGroup}
)
