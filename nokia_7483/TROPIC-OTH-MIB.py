# SNMP MIB module (TROPIC-OTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-OTH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnOthMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnOthMIB",
    "tnPortModules")

(ApsK1K2,) = mibBuilder.importSymbols(
    "TROPIC-L1SERVICE-MIB",
    "ApsK1K2")

(AluWdmDMInfoCurrentStatus,
 AluWdmEnabledDisabled,
 AluWdmOdukStatus,
 AluWdmOthOdukCurrentStatusBits,
 AluWdmOthOdukRate,
 AluWdmOthOdukXcRate,
 AluWdmTimDetMode,
 AluWdmTtiStatus,
 TnCommand,
 TropicOperationalCapabilityType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmDMInfoCurrentStatus",
    "AluWdmEnabledDisabled",
    "AluWdmOdukStatus",
    "AluWdmOthOdukCurrentStatusBits",
    "AluWdmOthOdukRate",
    "AluWdmOthOdukXcRate",
    "AluWdmTimDetMode",
    "AluWdmTtiStatus",
    "TnCommand",
    "TropicOperationalCapabilityType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnOthMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tnOthMibModule.setRevisions(
        ("2012-03-16 12:00",
         "2012-09-28 12:00",
         "2012-10-12 12:00",
         "2012-11-05 12:00",
         "2012-11-06 12:00",
         "2013-01-24 12:00",
         "2013-04-01 12:00",
         "2013-04-16 12:00",
         "2013-06-21 12:00",
         "2013-08-05 12:00",
         "2013-08-16 12:00",
         "2013-09-11 12:00",
         "2013-11-13 12:00",
         "2014-01-07 12:00",
         "2014-02-26 12:00",
         "2014-11-13 12:00",
         "2014-12-12 12:00",
         "2015-02-06 12:00",
         "2015-03-26 12:00",
         "2015-05-15 12:00",
         "2015-05-18 12:00",
         "2015-05-26 12:00",
         "2015-06-02 12:00",
         "2015-08-06 12:00",
         "2016-02-19 12:00",
         "2016-02-26 12:00",
         "2016-04-05 12:00",
         "2016-04-08 12:00",
         "2016-04-18 12:00",
         "2016-04-27 12:00",
         "2016-05-21 12:00",
         "2016-05-25 12:00",
         "2016-07-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnOthConf_ObjectIdentity = ObjectIdentity
tnOthConf = _TnOthConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1)
)
_TnOthGroups_ObjectIdentity = ObjectIdentity
tnOthGroups = _TnOthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1)
)
_TnOthCompliances_ObjectIdentity = ObjectIdentity
tnOthCompliances = _TnOthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 2)
)
_TnOthObjs_ObjectIdentity = ObjectIdentity
tnOthObjs = _TnOthObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2)
)
_TnOthBasics_ObjectIdentity = ObjectIdentity
tnOthBasics = _TnOthBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1)
)
_TnOthOdukAttributeTotal_Type = Integer32
_TnOthOdukAttributeTotal_Object = MibScalar
tnOthOdukAttributeTotal = _TnOthOdukAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 1),
    _TnOthOdukAttributeTotal_Type()
)
tnOthOdukAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukAttributeTotal.setStatus("current")
_TnOthOdukTable_Object = MibTable
tnOthOdukTable = _TnOthOdukTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnOthOdukTable.setStatus("current")
_TnOthOdukEntry_Object = MibTableRow
tnOthOdukEntry = _TnOthOdukEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1)
)
tnOthOdukEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukEntry.setStatus("current")
_TnOthIfIndex_Type = Unsigned32
_TnOthIfIndex_Object = MibTableColumn
tnOthIfIndex = _TnOthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 1),
    _TnOthIfIndex_Type()
)
tnOthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthIfIndex.setStatus("current")
_TnOthIfIndexLo_Type = Unsigned32
_TnOthIfIndexLo_Object = MibTableColumn
tnOthIfIndexLo = _TnOthIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 2),
    _TnOthIfIndexLo_Type()
)
tnOthIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthIfIndexLo.setStatus("current")


class _TnOthOdukDirectionality_Type(Integer32):
    """Custom type tnOthOdukDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sink", 1),
          ("source", 2),
          ("bidirectional", 3))
    )


_TnOthOdukDirectionality_Type.__name__ = "Integer32"
_TnOthOdukDirectionality_Object = MibTableColumn
tnOthOdukDirectionality = _TnOthOdukDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 3),
    _TnOthOdukDirectionality_Type()
)
tnOthOdukDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukDirectionality.setStatus("current")
_TnOthOdukRate_Type = AluWdmOthOdukRate
_TnOthOdukRate_Object = MibTableColumn
tnOthOdukRate = _TnOthOdukRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 4),
    _TnOthOdukRate_Type()
)
tnOthOdukRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRate.setStatus("current")


class _TnOthOdukTcmFieldsInUse_Type(Bits):
    """Custom type tnOthOdukTcmFieldsInUse based on Bits"""
    namedValues = NamedValues(
        *(("tcmField1-am-nim", 0),
          ("tcmField1-am-ttp", 1),
          ("tcmField1-bm-nim", 2),
          ("tcmField1-bm-ttp", 3),
          ("tcmField2-am-nim", 4),
          ("tcmField2-am-ttp", 5),
          ("tcmField2-bm-nim", 6),
          ("tcmField2-bm-ttp", 7),
          ("tcmField3-am-nim", 8),
          ("tcmField3-am-ttp", 9),
          ("tcmField3-bm-nim", 10),
          ("tcmField3-bm-ttp", 11),
          ("tcmField4-am-nim", 12),
          ("tcmField4-am-ttp", 13),
          ("tcmField4-bm-nim", 14),
          ("tcmField4-bm-ttp", 15),
          ("tcmField5-am-nim", 16),
          ("tcmField5-am-ttp", 17),
          ("tcmField5-bm-nim", 18),
          ("tcmField5-bm-ttp", 19),
          ("tcmField6-am-nim", 20),
          ("tcmField6-am-ttp", 21),
          ("tcmField6-bm-nim", 22),
          ("tcmField6-bm-ttp", 23))
    )

_TnOthOdukTcmFieldsInUse_Type.__name__ = "Bits"
_TnOthOdukTcmFieldsInUse_Object = MibTableColumn
tnOthOdukTcmFieldsInUse = _TnOthOdukTcmFieldsInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 5),
    _TnOthOdukTcmFieldsInUse_Type()
)
tnOthOdukTcmFieldsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmFieldsInUse.setStatus("current")
_TnOthOdukTtpPresent_Type = TruthValue
_TnOthOdukTtpPresent_Object = MibTableColumn
tnOthOdukTtpPresent = _TnOthOdukTtpPresent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 6),
    _TnOthOdukTtpPresent_Type()
)
tnOthOdukTtpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpPresent.setStatus("current")
_TnOthOdukAdminStatus_Type = AluWdmOdukStatus
_TnOthOdukAdminStatus_Object = MibTableColumn
tnOthOdukAdminStatus = _TnOthOdukAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 7),
    _TnOthOdukAdminStatus_Type()
)
tnOthOdukAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukAdminStatus.setStatus("current")
_TnOthOdukStateAINS_Type = TruthValue
_TnOthOdukStateAINS_Object = MibTableColumn
tnOthOdukStateAINS = _TnOthOdukStateAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 8),
    _TnOthOdukStateAINS_Type()
)
tnOthOdukStateAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukStateAINS.setStatus("current")
_TnOthOdukOperStatus_Type = AluWdmOdukStatus
_TnOthOdukOperStatus_Object = MibTableColumn
tnOthOdukOperStatus = _TnOthOdukOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 9),
    _TnOthOdukOperStatus_Type()
)
tnOthOdukOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukOperStatus.setStatus("current")
_TnOthOdukStateQualifier_Type = TropicStateQualifierType
_TnOthOdukStateQualifier_Object = MibTableColumn
tnOthOdukStateQualifier = _TnOthOdukStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 10),
    _TnOthOdukStateQualifier_Type()
)
tnOthOdukStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukStateQualifier.setStatus("current")
_TnOthOdukOperationalCapability_Type = TropicOperationalCapabilityType
_TnOthOdukOperationalCapability_Object = MibTableColumn
tnOthOdukOperationalCapability = _TnOthOdukOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 11),
    _TnOthOdukOperationalCapability_Type()
)
tnOthOdukOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukOperationalCapability.setStatus("current")
_TnOthOdukAINSDebounceTime_Type = Integer32
_TnOthOdukAINSDebounceTime_Object = MibTableColumn
tnOthOdukAINSDebounceTime = _TnOthOdukAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 12),
    _TnOthOdukAINSDebounceTime_Type()
)
tnOthOdukAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukAINSDebounceTime.setUnits("Seconds")
_TnOthOdukUsingSysAINSDebounceTime_Type = TruthValue
_TnOthOdukUsingSysAINSDebounceTime_Object = MibTableColumn
tnOthOdukUsingSysAINSDebounceTime = _TnOthOdukUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 13),
    _TnOthOdukUsingSysAINSDebounceTime_Type()
)
tnOthOdukUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukUsingSysAINSDebounceTime.setStatus("current")
_TnOthOdukAINSDebounceTimeRemaining_Type = Unsigned32
_TnOthOdukAINSDebounceTimeRemaining_Object = MibTableColumn
tnOthOdukAINSDebounceTimeRemaining = _TnOthOdukAINSDebounceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 14),
    _TnOthOdukAINSDebounceTimeRemaining_Type()
)
tnOthOdukAINSDebounceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukAINSDebounceTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukAINSDebounceTimeRemaining.setUnits("Seconds")
_TnOthOdukForceAdminStatus_Type = TnCommand
_TnOthOdukForceAdminStatus_Object = MibTableColumn
tnOthOdukForceAdminStatus = _TnOthOdukForceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 15),
    _TnOthOdukForceAdminStatus_Type()
)
tnOthOdukForceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukForceAdminStatus.setStatus("current")


class _TnOthOdukMgracd_Type(Integer32):
    """Custom type tnOthOdukMgracd based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("cp", 2),
          ("mgnpln", 3),
          ("cpmgnpln", 4))
    )


_TnOthOdukMgracd_Type.__name__ = "Integer32"
_TnOthOdukMgracd_Object = MibTableColumn
tnOthOdukMgracd = _TnOthOdukMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 16),
    _TnOthOdukMgracd_Type()
)
tnOthOdukMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukMgracd.setStatus("current")
_TnOthOdukAlmProfName_Type = OctetString
_TnOthOdukAlmProfName_Object = MibTableColumn
tnOthOdukAlmProfName = _TnOthOdukAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 17),
    _TnOthOdukAlmProfName_Type()
)
tnOthOdukAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukAlmProfName.setStatus("current")


class _TnOthOdukFlexType_Type(Integer32):
    """Custom type tnOthOdukFlexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("oduflexGfp", 2),
          ("oduflexCBR", 3))
    )


_TnOthOdukFlexType_Type.__name__ = "Integer32"
_TnOthOdukFlexType_Object = MibTableColumn
tnOthOdukFlexType = _TnOthOdukFlexType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 18),
    _TnOthOdukFlexType_Type()
)
tnOthOdukFlexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukFlexType.setStatus("current")


class _TnOthOdukFlexClientType_Type(Integer32):
    """Custom type tnOthOdukFlexClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fC400", 2),
          ("fC800", 3),
          ("fC1600", 4),
          ("g3SDI18", 5),
          ("iBSDR", 6),
          ("iBDDR", 7),
          ("iBQDR", 8),
          ("g3SDI19", 9))
    )


_TnOthOdukFlexClientType_Type.__name__ = "Integer32"
_TnOthOdukFlexClientType_Object = MibTableColumn
tnOthOdukFlexClientType = _TnOthOdukFlexClientType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 19),
    _TnOthOdukFlexClientType_Type()
)
tnOthOdukFlexClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukFlexClientType.setStatus("current")


class _TnOthOdukFlexGfpSize_Type(Unsigned32):
    """Custom type tnOthOdukFlexGfpSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_TnOthOdukFlexGfpSize_Type.__name__ = "Unsigned32"
_TnOthOdukFlexGfpSize_Object = MibTableColumn
tnOthOdukFlexGfpSize = _TnOthOdukFlexGfpSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 2, 1, 20),
    _TnOthOdukFlexGfpSize_Type()
)
tnOthOdukFlexGfpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukFlexGfpSize.setStatus("current")
_TnOthOdukTtpAttributeTotal_Type = Integer32
_TnOthOdukTtpAttributeTotal_Object = MibScalar
tnOthOdukTtpAttributeTotal = _TnOthOdukTtpAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 3),
    _TnOthOdukTtpAttributeTotal_Type()
)
tnOthOdukTtpAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpAttributeTotal.setStatus("current")
_TnOthOdukTtpTable_Object = MibTable
tnOthOdukTtpTable = _TnOthOdukTtpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnOthOdukTtpTable.setStatus("current")
_TnOthOdukTtpEntry_Object = MibTableRow
tnOthOdukTtpEntry = _TnOthOdukTtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1)
)
tnOthOdukTtpEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukTtpEntry.setStatus("current")


class _TnOthOdukTtpSapiTransmitted_Type(OctetString):
    """Custom type tnOthOdukTtpSapiTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnOthOdukTtpSapiTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTtpSapiTransmitted_Object = MibTableColumn
tnOthOdukTtpSapiTransmitted = _TnOthOdukTtpSapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 1),
    _TnOthOdukTtpSapiTransmitted_Type()
)
tnOthOdukTtpSapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpSapiTransmitted.setStatus("current")


class _TnOthOdukTtpDapiExpected_Type(OctetString):
    """Custom type tnOthOdukTtpDapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTtpDapiExpected_Type.__name__ = "OctetString"
_TnOthOdukTtpDapiExpected_Object = MibTableColumn
tnOthOdukTtpDapiExpected = _TnOthOdukTtpDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 2),
    _TnOthOdukTtpDapiExpected_Type()
)
tnOthOdukTtpDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpDapiExpected.setStatus("current")


class _TnOthOdukTtpSapiExpected_Type(OctetString):
    """Custom type tnOthOdukTtpSapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnOthOdukTtpSapiExpected_Type.__name__ = "OctetString"
_TnOthOdukTtpSapiExpected_Object = MibTableColumn
tnOthOdukTtpSapiExpected = _TnOthOdukTtpSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 3),
    _TnOthOdukTtpSapiExpected_Type()
)
tnOthOdukTtpSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpSapiExpected.setStatus("current")


class _TnOthOdukTtpTraceIdentifierAccepted_Type(OctetString):
    """Custom type tnOthOdukTtpTraceIdentifierAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_TnOthOdukTtpTraceIdentifierAccepted_Type.__name__ = "OctetString"
_TnOthOdukTtpTraceIdentifierAccepted_Object = MibTableColumn
tnOthOdukTtpTraceIdentifierAccepted = _TnOthOdukTtpTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 4),
    _TnOthOdukTtpTraceIdentifierAccepted_Type()
)
tnOthOdukTtpTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpTraceIdentifierAccepted.setStatus("current")


class _TnOthOdukTtpTimDetMode_Type(AluWdmTimDetMode):
    """Custom type tnOthOdukTtpTimDetMode based on AluWdmTimDetMode"""
    defaultValue = 1


_TnOthOdukTtpTimDetMode_Type.__name__ = "AluWdmTimDetMode"
_TnOthOdukTtpTimDetMode_Object = MibTableColumn
tnOthOdukTtpTimDetMode = _TnOthOdukTtpTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 5),
    _TnOthOdukTtpTimDetMode_Type()
)
tnOthOdukTtpTimDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpTimDetMode.setStatus("current")
_TnOthOdukTtpTimActEnabled_Type = TruthValue
_TnOthOdukTtpTimActEnabled_Object = MibTableColumn
tnOthOdukTtpTimActEnabled = _TnOthOdukTtpTimActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 6),
    _TnOthOdukTtpTimActEnabled_Type()
)
tnOthOdukTtpTimActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpTimActEnabled.setStatus("current")
_TnOthOdukTtpTtiStatus_Type = AluWdmTtiStatus
_TnOthOdukTtpTtiStatus_Object = MibTableColumn
tnOthOdukTtpTtiStatus = _TnOthOdukTtpTtiStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 7),
    _TnOthOdukTtpTtiStatus_Type()
)
tnOthOdukTtpTtiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpTtiStatus.setStatus("current")
_TnOthOdukTtpDegThr_Type = Unsigned32
_TnOthOdukTtpDegThr_Object = MibTableColumn
tnOthOdukTtpDegThr = _TnOthOdukTtpDegThr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 8),
    _TnOthOdukTtpDegThr_Type()
)
tnOthOdukTtpDegThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpDegThr.setStatus("current")
_TnOthOdukTtpDegM_Type = Unsigned32
_TnOthOdukTtpDegM_Object = MibTableColumn
tnOthOdukTtpDegM = _TnOthOdukTtpDegM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 9),
    _TnOthOdukTtpDegM_Type()
)
tnOthOdukTtpDegM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpDegM.setStatus("current")


class _TnOthOdukPayloadType_Type(Unsigned32):
    """Custom type tnOthOdukPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnOthOdukPayloadType_Type.__name__ = "Unsigned32"
_TnOthOdukPayloadType_Object = MibTableColumn
tnOthOdukPayloadType = _TnOthOdukPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 10),
    _TnOthOdukPayloadType_Type()
)
tnOthOdukPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukPayloadType.setStatus("current")
_TnOthOdukRxPayloadType_Type = Unsigned32
_TnOthOdukRxPayloadType_Object = MibTableColumn
tnOthOdukRxPayloadType = _TnOthOdukRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 11),
    _TnOthOdukRxPayloadType_Type()
)
tnOthOdukRxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRxPayloadType.setStatus("current")
_TnOthOdukPlmConsequenceAction_Type = TruthValue
_TnOthOdukPlmConsequenceAction_Object = MibTableColumn
tnOthOdukPlmConsequenceAction = _TnOthOdukPlmConsequenceAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 12),
    _TnOthOdukPlmConsequenceAction_Type()
)
tnOthOdukPlmConsequenceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukPlmConsequenceAction.setStatus("current")


class _TnOthOdukTxOduStruct_Type(SnmpAdminString):
    """Custom type tnOthOdukTxOduStruct based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_TnOthOdukTxOduStruct_Type.__name__ = "SnmpAdminString"
_TnOthOdukTxOduStruct_Object = MibTableColumn
tnOthOdukTxOduStruct = _TnOthOdukTxOduStruct_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 13),
    _TnOthOdukTxOduStruct_Type()
)
tnOthOdukTxOduStruct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTxOduStruct.setStatus("current")


class _TnOthOdukRxOduStruct_Type(SnmpAdminString):
    """Custom type tnOthOdukRxOduStruct based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOthOdukRxOduStruct_Type.__name__ = "SnmpAdminString"
_TnOthOdukRxOduStruct_Object = MibTableColumn
tnOthOdukRxOduStruct = _TnOthOdukRxOduStruct_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 14),
    _TnOthOdukRxOduStruct_Type()
)
tnOthOdukRxOduStruct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRxOduStruct.setStatus("current")
_TnOthOdukTtpCurrentStatus_Type = AluWdmOthOdukCurrentStatusBits
_TnOthOdukTtpCurrentStatus_Object = MibTableColumn
tnOthOdukTtpCurrentStatus = _TnOthOdukTtpCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 15),
    _TnOthOdukTtpCurrentStatus_Type()
)
tnOthOdukTtpCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpCurrentStatus.setStatus("current")
_TnOthOdukOdu0Interwk_Type = AluWdmEnabledDisabled
_TnOthOdukOdu0Interwk_Object = MibTableColumn
tnOthOdukOdu0Interwk = _TnOthOdukOdu0Interwk_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 16),
    _TnOthOdukOdu0Interwk_Type()
)
tnOthOdukOdu0Interwk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukOdu0Interwk.setStatus("current")


class _TnOthOdukTtpDapiAccepted_Type(OctetString):
    """Custom type tnOthOdukTtpDapiAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTtpDapiAccepted_Type.__name__ = "OctetString"
_TnOthOdukTtpDapiAccepted_Object = MibTableColumn
tnOthOdukTtpDapiAccepted = _TnOthOdukTtpDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 17),
    _TnOthOdukTtpDapiAccepted_Type()
)
tnOthOdukTtpDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpDapiAccepted.setStatus("current")


class _TnOthOdukTtpDapiTransmitted_Type(OctetString):
    """Custom type tnOthOdukTtpDapiTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTtpDapiTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTtpDapiTransmitted_Object = MibTableColumn
tnOthOdukTtpDapiTransmitted = _TnOthOdukTtpDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 18),
    _TnOthOdukTtpDapiTransmitted_Type()
)
tnOthOdukTtpDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpDapiTransmitted.setStatus("current")


class _TnOthOdukTtpOsAccepted_Type(OctetString):
    """Custom type tnOthOdukTtpOsAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOthOdukTtpOsAccepted_Type.__name__ = "OctetString"
_TnOthOdukTtpOsAccepted_Object = MibTableColumn
tnOthOdukTtpOsAccepted = _TnOthOdukTtpOsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 19),
    _TnOthOdukTtpOsAccepted_Type()
)
tnOthOdukTtpOsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTtpOsAccepted.setStatus("current")


class _TnOthOdukTtpOsTransmitted_Type(OctetString):
    """Custom type tnOthOdukTtpOsTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOthOdukTtpOsTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTtpOsTransmitted_Object = MibTableColumn
tnOthOdukTtpOsTransmitted = _TnOthOdukTtpOsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 20),
    _TnOthOdukTtpOsTransmitted_Type()
)
tnOthOdukTtpOsTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpOsTransmitted.setStatus("current")
_TnOthOdukRxMSI_Type = OctetString
_TnOthOdukRxMSI_Object = MibTableColumn
tnOthOdukRxMSI = _TnOthOdukRxMSI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 21),
    _TnOthOdukRxMSI_Type()
)
tnOthOdukRxMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukRxMSI.setStatus("current")


class _TnOthOdukTtpCndRes_Type(Integer32):
    """Custom type tnOthOdukTtpCndRes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c1d", 1),
          ("c8d", 2))
    )


_TnOthOdukTtpCndRes_Type.__name__ = "Integer32"
_TnOthOdukTtpCndRes_Object = MibTableColumn
tnOthOdukTtpCndRes = _TnOthOdukTtpCndRes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 22),
    _TnOthOdukTtpCndRes_Type()
)
tnOthOdukTtpCndRes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpCndRes.setStatus("current")


class _TnOthOdukTtpCmEmphasis_Type(Integer32):
    """Custom type tnOthOdukTtpCmEmphasis based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TnOthOdukTtpCmEmphasis_Type.__name__ = "Integer32"
_TnOthOdukTtpCmEmphasis_Object = MibTableColumn
tnOthOdukTtpCmEmphasis = _TnOthOdukTtpCmEmphasis_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 23),
    _TnOthOdukTtpCmEmphasis_Type()
)
tnOthOdukTtpCmEmphasis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpCmEmphasis.setStatus("current")


class _TnOthOdukTtpManualOduPtf_Type(Integer32):
    """Custom type tnOthOdukTtpManualOduPtf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("create", 2),
          ("delete", 3))
    )


_TnOthOdukTtpManualOduPtf_Type.__name__ = "Integer32"
_TnOthOdukTtpManualOduPtf_Object = MibTableColumn
tnOthOdukTtpManualOduPtf = _TnOthOdukTtpManualOduPtf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 24),
    _TnOthOdukTtpManualOduPtf_Type()
)
tnOthOdukTtpManualOduPtf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpManualOduPtf.setStatus("current")


class _TnOthOdukTtpCsfType_Type(Integer32):
    """Custom type tnOthOdukTtpCsfType based on Integer32"""
    defaultValue = 3

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
        *(("unused", 1),
          ("lcs", 2),
          ("lccs", 3),
          ("unknown", 4))
    )


_TnOthOdukTtpCsfType_Type.__name__ = "Integer32"
_TnOthOdukTtpCsfType_Object = MibTableColumn
tnOthOdukTtpCsfType = _TnOthOdukTtpCsfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 4, 1, 25),
    _TnOthOdukTtpCsfType_Type()
)
tnOthOdukTtpCsfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTtpCsfType.setStatus("current")
_TnOthOdukNimAttributeTotal_Type = Integer32
_TnOthOdukNimAttributeTotal_Object = MibScalar
tnOthOdukNimAttributeTotal = _TnOthOdukNimAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 5),
    _TnOthOdukNimAttributeTotal_Type()
)
tnOthOdukNimAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukNimAttributeTotal.setStatus("current")
_TnOthOdukNimTable_Object = MibTable
tnOthOdukNimTable = _TnOthOdukNimTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnOthOdukNimTable.setStatus("current")
_TnOthOdukNimEntry_Object = MibTableRow
tnOthOdukNimEntry = _TnOthOdukNimEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1)
)
tnOthOdukNimEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukNimDirectionality"),
)
if mibBuilder.loadTexts:
    tnOthOdukNimEntry.setStatus("current")


class _TnOthOdukNimDirectionality_Type(Integer32):
    """Custom type tnOthOdukNimDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sink", 1),
          ("source", 2))
    )


_TnOthOdukNimDirectionality_Type.__name__ = "Integer32"
_TnOthOdukNimDirectionality_Object = MibTableColumn
tnOthOdukNimDirectionality = _TnOthOdukNimDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 1),
    _TnOthOdukNimDirectionality_Type()
)
tnOthOdukNimDirectionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukNimDirectionality.setStatus("current")


class _TnOthOdukNimDapiExpected_Type(OctetString):
    """Custom type tnOthOdukNimDapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukNimDapiExpected_Type.__name__ = "OctetString"
_TnOthOdukNimDapiExpected_Object = MibTableColumn
tnOthOdukNimDapiExpected = _TnOthOdukNimDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 2),
    _TnOthOdukNimDapiExpected_Type()
)
tnOthOdukNimDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimDapiExpected.setStatus("current")


class _TnOthOdukNimSapiExpected_Type(OctetString):
    """Custom type tnOthOdukNimSapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnOthOdukNimSapiExpected_Type.__name__ = "OctetString"
_TnOthOdukNimSapiExpected_Object = MibTableColumn
tnOthOdukNimSapiExpected = _TnOthOdukNimSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 3),
    _TnOthOdukNimSapiExpected_Type()
)
tnOthOdukNimSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimSapiExpected.setStatus("current")


class _TnOthOdukNimTraceIdentifierAccepted_Type(OctetString):
    """Custom type tnOthOdukNimTraceIdentifierAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_TnOthOdukNimTraceIdentifierAccepted_Type.__name__ = "OctetString"
_TnOthOdukNimTraceIdentifierAccepted_Object = MibTableColumn
tnOthOdukNimTraceIdentifierAccepted = _TnOthOdukNimTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 4),
    _TnOthOdukNimTraceIdentifierAccepted_Type()
)
tnOthOdukNimTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukNimTraceIdentifierAccepted.setStatus("current")
_TnOthOdukNimTimDetMode_Type = AluWdmTimDetMode
_TnOthOdukNimTimDetMode_Object = MibTableColumn
tnOthOdukNimTimDetMode = _TnOthOdukNimTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 5),
    _TnOthOdukNimTimDetMode_Type()
)
tnOthOdukNimTimDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimTimDetMode.setStatus("current")
_TnOthOdukNimTimActEnabled_Type = TruthValue
_TnOthOdukNimTimActEnabled_Object = MibTableColumn
tnOthOdukNimTimActEnabled = _TnOthOdukNimTimActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 6),
    _TnOthOdukNimTimActEnabled_Type()
)
tnOthOdukNimTimActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimTimActEnabled.setStatus("current")
_TnOthOdukNimTtiStatus_Type = AluWdmTtiStatus
_TnOthOdukNimTtiStatus_Object = MibTableColumn
tnOthOdukNimTtiStatus = _TnOthOdukNimTtiStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 7),
    _TnOthOdukNimTtiStatus_Type()
)
tnOthOdukNimTtiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukNimTtiStatus.setStatus("current")
_TnOthOdukNimDegThr_Type = Unsigned32
_TnOthOdukNimDegThr_Object = MibTableColumn
tnOthOdukNimDegThr = _TnOthOdukNimDegThr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 8),
    _TnOthOdukNimDegThr_Type()
)
tnOthOdukNimDegThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimDegThr.setStatus("current")
_TnOthOdukNimDegM_Type = Unsigned32
_TnOthOdukNimDegM_Object = MibTableColumn
tnOthOdukNimDegM = _TnOthOdukNimDegM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 9),
    _TnOthOdukNimDegM_Type()
)
tnOthOdukNimDegM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimDegM.setStatus("current")
_TnOthOdukNimPom_Type = TruthValue
_TnOthOdukNimPom_Object = MibTableColumn
tnOthOdukNimPom = _TnOthOdukNimPom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 11),
    _TnOthOdukNimPom_Type()
)
tnOthOdukNimPom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukNimPom.setStatus("current")


class _TnOthOdukNimDapiAccepted_Type(OctetString):
    """Custom type tnOthOdukNimDapiAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukNimDapiAccepted_Type.__name__ = "OctetString"
_TnOthOdukNimDapiAccepted_Object = MibTableColumn
tnOthOdukNimDapiAccepted = _TnOthOdukNimDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 12),
    _TnOthOdukNimDapiAccepted_Type()
)
tnOthOdukNimDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukNimDapiAccepted.setStatus("current")


class _TnOthOdukNimOsAccepted_Type(OctetString):
    """Custom type tnOthOdukNimOsAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOthOdukNimOsAccepted_Type.__name__ = "OctetString"
_TnOthOdukNimOsAccepted_Object = MibTableColumn
tnOthOdukNimOsAccepted = _TnOthOdukNimOsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 6, 1, 13),
    _TnOthOdukNimOsAccepted_Type()
)
tnOthOdukNimOsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukNimOsAccepted.setStatus("current")
_TnOthGcc12AttributeTotal_Type = Integer32
_TnOthGcc12AttributeTotal_Object = MibScalar
tnOthGcc12AttributeTotal = _TnOthGcc12AttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 7),
    _TnOthGcc12AttributeTotal_Type()
)
tnOthGcc12AttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthGcc12AttributeTotal.setStatus("current")
_TnOthGcc12Table_Object = MibTable
tnOthGcc12Table = _TnOthGcc12Table_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnOthGcc12Table.setStatus("current")
_TnOthGcc12Entry_Object = MibTableRow
tnOthGcc12Entry = _TnOthGcc12Entry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1)
)
tnOthGcc12Entry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
    (0, "TROPIC-OTH-MIB", "tnOthGcc12Codirectional"),
    (0, "TROPIC-OTH-MIB", "tnOthGcc12GccAccess"),
)
if mibBuilder.loadTexts:
    tnOthGcc12Entry.setStatus("current")
_TnOthGcc12Codirectional_Type = TruthValue
_TnOthGcc12Codirectional_Object = MibTableColumn
tnOthGcc12Codirectional = _TnOthGcc12Codirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1, 1),
    _TnOthGcc12Codirectional_Type()
)
tnOthGcc12Codirectional.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthGcc12Codirectional.setStatus("current")


class _TnOthGcc12GccAccess_Type(Integer32):
    """Custom type tnOthGcc12GccAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gcc1", 1),
          ("gcc2", 2),
          ("gcc1and2", 3))
    )


_TnOthGcc12GccAccess_Type.__name__ = "Integer32"
_TnOthGcc12GccAccess_Object = MibTableColumn
tnOthGcc12GccAccess = _TnOthGcc12GccAccess_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1, 2),
    _TnOthGcc12GccAccess_Type()
)
tnOthGcc12GccAccess.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthGcc12GccAccess.setStatus("current")
_TnOthGcc12RowStatus_Type = RowStatus
_TnOthGcc12RowStatus_Object = MibTableColumn
tnOthGcc12RowStatus = _TnOthGcc12RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1, 3),
    _TnOthGcc12RowStatus_Type()
)
tnOthGcc12RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthGcc12RowStatus.setStatus("current")
_TnOthGcc12GccPassThrough_Type = TruthValue
_TnOthGcc12GccPassThrough_Object = MibTableColumn
tnOthGcc12GccPassThrough = _TnOthGcc12GccPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1, 4),
    _TnOthGcc12GccPassThrough_Type()
)
tnOthGcc12GccPassThrough.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthGcc12GccPassThrough.setStatus("current")


class _TnOthGcc12Application_Type(OctetString):
    """Custom type tnOthGcc12Application based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOthGcc12Application_Type.__name__ = "OctetString"
_TnOthGcc12Application_Object = MibTableColumn
tnOthGcc12Application = _TnOthGcc12Application_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 8, 1, 5),
    _TnOthGcc12Application_Type()
)
tnOthGcc12Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthGcc12Application.setStatus("current")
_TnOthOdukTAttributeTotal_Type = Integer32
_TnOthOdukTAttributeTotal_Object = MibScalar
tnOthOdukTAttributeTotal = _TnOthOdukTAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 9),
    _TnOthOdukTAttributeTotal_Type()
)
tnOthOdukTAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTAttributeTotal.setStatus("current")
_TnOthOdukTTable_Object = MibTable
tnOthOdukTTable = _TnOthOdukTTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnOthOdukTTable.setStatus("current")
_TnOthOdukTEntry_Object = MibTableRow
tnOthOdukTEntry = _TnOthOdukTEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1)
)
tnOthOdukTEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukTcmIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukTEntry.setStatus("current")
_TnOthOdukTRowStatus_Type = RowStatus
_TnOthOdukTRowStatus_Object = MibTableColumn
tnOthOdukTRowStatus = _TnOthOdukTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 3),
    _TnOthOdukTRowStatus_Type()
)
tnOthOdukTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTRowStatus.setStatus("current")


class _TnOthOdukTTcmMode_Type(Integer32):
    """Custom type tnOthOdukTTcmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("termination", 1),
          ("nonIntrusive", 2))
    )


_TnOthOdukTTcmMode_Type.__name__ = "Integer32"
_TnOthOdukTTcmMode_Object = MibTableColumn
tnOthOdukTTcmMode = _TnOthOdukTTcmMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 4),
    _TnOthOdukTTcmMode_Type()
)
tnOthOdukTTcmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTTcmMode.setStatus("current")


class _TnOthOdukTPosSeq_Type(Unsigned32):
    """Custom type tnOthOdukTPosSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TnOthOdukTPosSeq_Type.__name__ = "Unsigned32"
_TnOthOdukTPosSeq_Object = MibTableColumn
tnOthOdukTPosSeq = _TnOthOdukTPosSeq_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 5),
    _TnOthOdukTPosSeq_Type()
)
tnOthOdukTPosSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTPosSeq.setStatus("current")
_TnOthOdukTAdminStatus_Type = AluWdmOdukStatus
_TnOthOdukTAdminStatus_Object = MibTableColumn
tnOthOdukTAdminStatus = _TnOthOdukTAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 6),
    _TnOthOdukTAdminStatus_Type()
)
tnOthOdukTAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTAdminStatus.setStatus("current")


class _TnOthOdukTSapiTransmitted_Type(OctetString):
    """Custom type tnOthOdukTSapiTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnOthOdukTSapiTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTSapiTransmitted_Object = MibTableColumn
tnOthOdukTSapiTransmitted = _TnOthOdukTSapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 7),
    _TnOthOdukTSapiTransmitted_Type()
)
tnOthOdukTSapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTSapiTransmitted.setStatus("current")


class _TnOthOdukTSapiExpected_Type(OctetString):
    """Custom type tnOthOdukTSapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnOthOdukTSapiExpected_Type.__name__ = "OctetString"
_TnOthOdukTSapiExpected_Object = MibTableColumn
tnOthOdukTSapiExpected = _TnOthOdukTSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 8),
    _TnOthOdukTSapiExpected_Type()
)
tnOthOdukTSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTSapiExpected.setStatus("current")


class _TnOthOdukTTraceIdentifierAccepted_Type(OctetString):
    """Custom type tnOthOdukTTraceIdentifierAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_TnOthOdukTTraceIdentifierAccepted_Type.__name__ = "OctetString"
_TnOthOdukTTraceIdentifierAccepted_Object = MibTableColumn
tnOthOdukTTraceIdentifierAccepted = _TnOthOdukTTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 9),
    _TnOthOdukTTraceIdentifierAccepted_Type()
)
tnOthOdukTTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTTraceIdentifierAccepted.setStatus("current")


class _TnOthOdukTTimDetMode_Type(AluWdmTimDetMode):
    """Custom type tnOthOdukTTimDetMode based on AluWdmTimDetMode"""
    defaultValue = 1


_TnOthOdukTTimDetMode_Type.__name__ = "AluWdmTimDetMode"
_TnOthOdukTTimDetMode_Object = MibTableColumn
tnOthOdukTTimDetMode = _TnOthOdukTTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 10),
    _TnOthOdukTTimDetMode_Type()
)
tnOthOdukTTimDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTTimDetMode.setStatus("current")


class _TnOthOdukTTimActEnabled_Type(TruthValue):
    """Custom type tnOthOdukTTimActEnabled based on TruthValue"""
    defaultValue = 2


_TnOthOdukTTimActEnabled_Type.__name__ = "TruthValue"
_TnOthOdukTTimActEnabled_Object = MibTableColumn
tnOthOdukTTimActEnabled = _TnOthOdukTTimActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 11),
    _TnOthOdukTTimActEnabled_Type()
)
tnOthOdukTTimActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTTimActEnabled.setStatus("current")
_TnOthOdukTTtpTtiStatus_Type = AluWdmTtiStatus
_TnOthOdukTTtpTtiStatus_Object = MibTableColumn
tnOthOdukTTtpTtiStatus = _TnOthOdukTTtpTtiStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 12),
    _TnOthOdukTTtpTtiStatus_Type()
)
tnOthOdukTTtpTtiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTTtpTtiStatus.setStatus("current")


class _TnOthOdukTAisOnDef_Type(Integer32):
    """Custom type tnOthOdukTAisOnDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukTAisOnDef_Type.__name__ = "Integer32"
_TnOthOdukTAisOnDef_Object = MibTableColumn
tnOthOdukTAisOnDef = _TnOthOdukTAisOnDef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 13),
    _TnOthOdukTAisOnDef_Type()
)
tnOthOdukTAisOnDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTAisOnDef.setStatus("current")


class _TnOthOdukTLtcResp_Type(Integer32):
    """Custom type tnOthOdukTLtcResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukTLtcResp_Type.__name__ = "Integer32"
_TnOthOdukTLtcResp_Object = MibTableColumn
tnOthOdukTLtcResp = _TnOthOdukTLtcResp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 14),
    _TnOthOdukTLtcResp_Type()
)
tnOthOdukTLtcResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTLtcResp.setStatus("current")
_TnOthOdukTOhAdd_Type = TruthValue
_TnOthOdukTOhAdd_Object = MibTableColumn
tnOthOdukTOhAdd = _TnOthOdukTOhAdd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 15),
    _TnOthOdukTOhAdd_Type()
)
tnOthOdukTOhAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTOhAdd.setStatus("current")
_TnOthOdukTOhRmv_Type = TruthValue
_TnOthOdukTOhRmv_Object = MibTableColumn
tnOthOdukTOhRmv = _TnOthOdukTOhRmv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 16),
    _TnOthOdukTOhRmv_Type()
)
tnOthOdukTOhRmv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTOhRmv.setStatus("current")
_TnOthOdukTcmIfIndex_Type = Unsigned32
_TnOthOdukTcmIfIndex_Object = MibTableColumn
tnOthOdukTcmIfIndex = _TnOthOdukTcmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 17),
    _TnOthOdukTcmIfIndex_Type()
)
tnOthOdukTcmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukTcmIfIndex.setStatus("current")
_TnOthOdukTcmIfIndexLo_Type = Unsigned32
_TnOthOdukTcmIfIndexLo_Object = MibTableColumn
tnOthOdukTcmIfIndexLo = _TnOthOdukTcmIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 18),
    _TnOthOdukTcmIfIndexLo_Type()
)
tnOthOdukTcmIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukTcmIfIndexLo.setStatus("current")
_TnOthOdukTDegThr_Type = Unsigned32
_TnOthOdukTDegThr_Object = MibTableColumn
tnOthOdukTDegThr = _TnOthOdukTDegThr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 19),
    _TnOthOdukTDegThr_Type()
)
tnOthOdukTDegThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTDegThr.setStatus("current")
_TnOthOdukTDegM_Type = Unsigned32
_TnOthOdukTDegM_Object = MibTableColumn
tnOthOdukTDegM = _TnOthOdukTDegM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 20),
    _TnOthOdukTDegM_Type()
)
tnOthOdukTDegM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTDegM.setStatus("current")


class _TnOthOdukTDapiAccepted_Type(OctetString):
    """Custom type tnOthOdukTDapiAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTDapiAccepted_Type.__name__ = "OctetString"
_TnOthOdukTDapiAccepted_Object = MibTableColumn
tnOthOdukTDapiAccepted = _TnOthOdukTDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 21),
    _TnOthOdukTDapiAccepted_Type()
)
tnOthOdukTDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTDapiAccepted.setStatus("current")


class _TnOthOdukTDapiExpected_Type(OctetString):
    """Custom type tnOthOdukTDapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTDapiExpected_Type.__name__ = "OctetString"
_TnOthOdukTDapiExpected_Object = MibTableColumn
tnOthOdukTDapiExpected = _TnOthOdukTDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 22),
    _TnOthOdukTDapiExpected_Type()
)
tnOthOdukTDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTDapiExpected.setStatus("current")


class _TnOthOdukTDapiTransmitted_Type(OctetString):
    """Custom type tnOthOdukTDapiTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOthOdukTDapiTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTDapiTransmitted_Object = MibTableColumn
tnOthOdukTDapiTransmitted = _TnOthOdukTDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 23),
    _TnOthOdukTDapiTransmitted_Type()
)
tnOthOdukTDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTDapiTransmitted.setStatus("current")


class _TnOthOdukTOsAccepted_Type(OctetString):
    """Custom type tnOthOdukTOsAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOthOdukTOsAccepted_Type.__name__ = "OctetString"
_TnOthOdukTOsAccepted_Object = MibTableColumn
tnOthOdukTOsAccepted = _TnOthOdukTOsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 24),
    _TnOthOdukTOsAccepted_Type()
)
tnOthOdukTOsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTOsAccepted.setStatus("current")


class _TnOthOdukTOsTransmitted_Type(OctetString):
    """Custom type tnOthOdukTOsTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOthOdukTOsTransmitted_Type.__name__ = "OctetString"
_TnOthOdukTOsTransmitted_Object = MibTableColumn
tnOthOdukTOsTransmitted = _TnOthOdukTOsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 25),
    _TnOthOdukTOsTransmitted_Type()
)
tnOthOdukTOsTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTOsTransmitted.setStatus("current")
_TnOthOdukTTcmAlmProfName_Type = OctetString
_TnOthOdukTTcmAlmProfName_Object = MibTableColumn
tnOthOdukTTcmAlmProfName = _TnOthOdukTTcmAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 26),
    _TnOthOdukTTcmAlmProfName_Type()
)
tnOthOdukTTcmAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTTcmAlmProfName.setStatus("current")


class _TnOthOdukTcmOperStatus_Type(Integer32):
    """Custom type tnOthOdukTcmOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("down", 2),
          ("up", 3))
    )


_TnOthOdukTcmOperStatus_Type.__name__ = "Integer32"
_TnOthOdukTcmOperStatus_Object = MibTableColumn
tnOthOdukTcmOperStatus = _TnOthOdukTcmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 27),
    _TnOthOdukTcmOperStatus_Type()
)
tnOthOdukTcmOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTcmOperStatus.setStatus("current")


class _TnOthOdukTcmMgracd_Type(Integer32):
    """Custom type tnOthOdukTcmMgracd based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("cp", 2),
          ("mgnpln", 3),
          ("cpmgnpln", 4))
    )


_TnOthOdukTcmMgracd_Type.__name__ = "Integer32"
_TnOthOdukTcmMgracd_Object = MibTableColumn
tnOthOdukTcmMgracd = _TnOthOdukTcmMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 28),
    _TnOthOdukTcmMgracd_Type()
)
tnOthOdukTcmMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukTcmMgracd.setStatus("current")


class _TnOthOdukTcmincstat_Type(Unsigned32):
    """Custom type tnOthOdukTcmincstat based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnOthOdukTcmincstat_Type.__name__ = "Unsigned32"
_TnOthOdukTcmincstat_Object = MibTableColumn
tnOthOdukTcmincstat = _TnOthOdukTcmincstat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 29),
    _TnOthOdukTcmincstat_Type()
)
tnOthOdukTcmincstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmincstat.setStatus("current")


class _TnOthOdukTcmOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnOthOdukTcmOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnOthOdukTcmOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnOthOdukTcmOperationalCapability_Object = MibTableColumn
tnOthOdukTcmOperationalCapability = _TnOthOdukTcmOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 30),
    _TnOthOdukTcmOperationalCapability_Type()
)
tnOthOdukTcmOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmOperationalCapability.setStatus("current")
_TnOthOdukTcmStateQualifier_Type = TropicStateQualifierType
_TnOthOdukTcmStateQualifier_Object = MibTableColumn
tnOthOdukTcmStateQualifier = _TnOthOdukTcmStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 10, 1, 31),
    _TnOthOdukTcmStateQualifier_Type()
)
tnOthOdukTcmStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukTcmStateQualifier.setStatus("current")
_TnOthOdukXcAttributeTotal_Type = Integer32
_TnOthOdukXcAttributeTotal_Object = MibScalar
tnOthOdukXcAttributeTotal = _TnOthOdukXcAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 13),
    _TnOthOdukXcAttributeTotal_Type()
)
tnOthOdukXcAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukXcAttributeTotal.setStatus("current")
_TnOthOdukXcTable_Object = MibTable
tnOthOdukXcTable = _TnOthOdukXcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnOthOdukXcTable.setStatus("current")
_TnOthOdukXcEntry_Object = MibTableRow
tnOthOdukXcEntry = _TnOthOdukXcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1)
)
tnOthOdukXcEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukXcSrcIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukXcSrcIfIndexLo"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukXcDestIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukXcDestIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukXcEntry.setStatus("current")
_TnOthOdukXcSrcIfIndex_Type = Integer32
_TnOthOdukXcSrcIfIndex_Object = MibTableColumn
tnOthOdukXcSrcIfIndex = _TnOthOdukXcSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 1),
    _TnOthOdukXcSrcIfIndex_Type()
)
tnOthOdukXcSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukXcSrcIfIndex.setStatus("current")
_TnOthOdukXcSrcIfIndexLo_Type = Integer32
_TnOthOdukXcSrcIfIndexLo_Object = MibTableColumn
tnOthOdukXcSrcIfIndexLo = _TnOthOdukXcSrcIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 2),
    _TnOthOdukXcSrcIfIndexLo_Type()
)
tnOthOdukXcSrcIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukXcSrcIfIndexLo.setStatus("current")
_TnOthOdukXcDestIfIndex_Type = Integer32
_TnOthOdukXcDestIfIndex_Object = MibTableColumn
tnOthOdukXcDestIfIndex = _TnOthOdukXcDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 3),
    _TnOthOdukXcDestIfIndex_Type()
)
tnOthOdukXcDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukXcDestIfIndex.setStatus("current")
_TnOthOdukXcDestIfIndexLo_Type = Integer32
_TnOthOdukXcDestIfIndexLo_Object = MibTableColumn
tnOthOdukXcDestIfIndexLo = _TnOthOdukXcDestIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 4),
    _TnOthOdukXcDestIfIndexLo_Type()
)
tnOthOdukXcDestIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukXcDestIfIndexLo.setStatus("current")
_TnOthOdukXcRowStatus_Type = RowStatus
_TnOthOdukXcRowStatus_Object = MibTableColumn
tnOthOdukXcRowStatus = _TnOthOdukXcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 5),
    _TnOthOdukXcRowStatus_Type()
)
tnOthOdukXcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukXcRowStatus.setStatus("current")
_TnOthOdukXcId_Type = Unsigned32
_TnOthOdukXcId_Object = MibTableColumn
tnOthOdukXcId = _TnOthOdukXcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 6),
    _TnOthOdukXcId_Type()
)
tnOthOdukXcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukXcId.setStatus("current")
_TnOthOdukXcRate_Type = AluWdmOthOdukXcRate
_TnOthOdukXcRate_Object = MibTableColumn
tnOthOdukXcRate = _TnOthOdukXcRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 7),
    _TnOthOdukXcRate_Type()
)
tnOthOdukXcRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukXcRate.setStatus("current")
_TnOthOdukXcBidirectional_Type = TruthValue
_TnOthOdukXcBidirectional_Object = MibTableColumn
tnOthOdukXcBidirectional = _TnOthOdukXcBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 8),
    _TnOthOdukXcBidirectional_Type()
)
tnOthOdukXcBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukXcBidirectional.setStatus("current")


class _TnOthOdukXcName_Type(SnmpAdminString):
    """Custom type tnOthOdukXcName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOthOdukXcName_Type.__name__ = "SnmpAdminString"
_TnOthOdukXcName_Object = MibTableColumn
tnOthOdukXcName = _TnOthOdukXcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 9),
    _TnOthOdukXcName_Type()
)
tnOthOdukXcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukXcName.setStatus("current")


class _TnOthOdukXcProtectionState_Type(Integer32):
    """Custom type tnOthOdukXcProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("protection", 2),
          ("working", 3))
    )


_TnOthOdukXcProtectionState_Type.__name__ = "Integer32"
_TnOthOdukXcProtectionState_Object = MibTableColumn
tnOthOdukXcProtectionState = _TnOthOdukXcProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 10),
    _TnOthOdukXcProtectionState_Type()
)
tnOthOdukXcProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukXcProtectionState.setStatus("current")


class _TnOthOdukXcTopology_Type(OctetString):
    """Custom type tnOthOdukXcTopology based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_TnOthOdukXcTopology_Type.__name__ = "OctetString"
_TnOthOdukXcTopology_Object = MibTableColumn
tnOthOdukXcTopology = _TnOthOdukXcTopology_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 14, 1, 11),
    _TnOthOdukXcTopology_Type()
)
tnOthOdukXcTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukXcTopology.setStatus("current")
_TnOthOdukApsGroupAttributeTotal_Type = Integer32
_TnOthOdukApsGroupAttributeTotal_Object = MibScalar
tnOthOdukApsGroupAttributeTotal = _TnOthOdukApsGroupAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 15),
    _TnOthOdukApsGroupAttributeTotal_Type()
)
tnOthOdukApsGroupAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupAttributeTotal.setStatus("current")
_TnOthOdukApsGroupTable_Object = MibTable
tnOthOdukApsGroupTable = _TnOthOdukApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16)
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupTable.setStatus("current")
_TnOthOdukApsGroupEntry_Object = MibTableRow
tnOthOdukApsGroupEntry = _TnOthOdukApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1)
)
tnOthOdukApsGroupEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsToIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsToIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupEntry.setStatus("current")
_TnOthOdukApsToIfIndex_Type = Integer32
_TnOthOdukApsToIfIndex_Object = MibTableColumn
tnOthOdukApsToIfIndex = _TnOthOdukApsToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 1),
    _TnOthOdukApsToIfIndex_Type()
)
tnOthOdukApsToIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukApsToIfIndex.setStatus("current")
_TnOthOdukApsToIfIndexLo_Type = Integer32
_TnOthOdukApsToIfIndexLo_Object = MibTableColumn
tnOthOdukApsToIfIndexLo = _TnOthOdukApsToIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 2),
    _TnOthOdukApsToIfIndexLo_Type()
)
tnOthOdukApsToIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukApsToIfIndexLo.setStatus("current")
_TnOthOdukApsFromedIfIndex_Type = Integer32
_TnOthOdukApsFromedIfIndex_Object = MibTableColumn
tnOthOdukApsFromedIfIndex = _TnOthOdukApsFromedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 3),
    _TnOthOdukApsFromedIfIndex_Type()
)
tnOthOdukApsFromedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsFromedIfIndex.setStatus("current")
_TnOthOdukApsFromedIfIndexLo_Type = Integer32
_TnOthOdukApsFromedIfIndexLo_Object = MibTableColumn
tnOthOdukApsFromedIfIndexLo = _TnOthOdukApsFromedIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 4),
    _TnOthOdukApsFromedIfIndexLo_Type()
)
tnOthOdukApsFromedIfIndexLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsFromedIfIndexLo.setStatus("current")
_TnOthOdukApsFromingIfIndex_Type = Integer32
_TnOthOdukApsFromingIfIndex_Object = MibTableColumn
tnOthOdukApsFromingIfIndex = _TnOthOdukApsFromingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 5),
    _TnOthOdukApsFromingIfIndex_Type()
)
tnOthOdukApsFromingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsFromingIfIndex.setStatus("current")
_TnOthOdukApsFromingIfIndexLo_Type = Integer32
_TnOthOdukApsFromingIfIndexLo_Object = MibTableColumn
tnOthOdukApsFromingIfIndexLo = _TnOthOdukApsFromingIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 6),
    _TnOthOdukApsFromingIfIndexLo_Type()
)
tnOthOdukApsFromingIfIndexLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsFromingIfIndexLo.setStatus("current")


class _TnOthOdukApsAction_Type(Integer32):
    """Custom type tnOthOdukApsAction based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("update", 3),
          ("convertToProt", 4),
          ("convertToUnprot", 5),
          ("noCommand", 6),
          ("convertToUnprotFroming", 7))
    )


_TnOthOdukApsAction_Type.__name__ = "Integer32"
_TnOthOdukApsAction_Object = MibTableColumn
tnOthOdukApsAction = _TnOthOdukApsAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 7),
    _TnOthOdukApsAction_Type()
)
tnOthOdukApsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsAction.setStatus("current")


class _TnOthOdukApsDescr_Type(SnmpAdminString):
    """Custom type tnOthOdukApsDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOthOdukApsDescr_Type.__name__ = "SnmpAdminString"
_TnOthOdukApsDescr_Object = MibTableColumn
tnOthOdukApsDescr = _TnOthOdukApsDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 8),
    _TnOthOdukApsDescr_Type()
)
tnOthOdukApsDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsDescr.setStatus("current")


class _TnOthOdukApsMode_Type(Integer32):
    """Custom type tnOthOdukApsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sncn", 1),
          ("sncnc", 2),
          ("snci", 3))
    )


_TnOthOdukApsMode_Type.__name__ = "Integer32"
_TnOthOdukApsMode_Object = MibTableColumn
tnOthOdukApsMode = _TnOthOdukApsMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 9),
    _TnOthOdukApsMode_Type()
)
tnOthOdukApsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsMode.setStatus("current")


class _TnOthOdukApsRevert_Type(Integer32):
    """Custom type tnOthOdukApsRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_TnOthOdukApsRevert_Type.__name__ = "Integer32"
_TnOthOdukApsRevert_Object = MibTableColumn
tnOthOdukApsRevert = _TnOthOdukApsRevert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 10),
    _TnOthOdukApsRevert_Type()
)
tnOthOdukApsRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsRevert.setStatus("current")


class _TnOthOdukApsDirection_Type(Integer32):
    """Custom type tnOthOdukApsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_TnOthOdukApsDirection_Type.__name__ = "Integer32"
_TnOthOdukApsDirection_Object = MibTableColumn
tnOthOdukApsDirection = _TnOthOdukApsDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 11),
    _TnOthOdukApsDirection_Type()
)
tnOthOdukApsDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsDirection.setStatus("current")


class _TnOthOdukApsXcBidirectional_Type(Integer32):
    """Custom type tnOthOdukApsXcBidirectional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWaySNCP", 1),
          ("twoWaySNCP", 2))
    )


_TnOthOdukApsXcBidirectional_Type.__name__ = "Integer32"
_TnOthOdukApsXcBidirectional_Object = MibTableColumn
tnOthOdukApsXcBidirectional = _TnOthOdukApsXcBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 12),
    _TnOthOdukApsXcBidirectional_Type()
)
tnOthOdukApsXcBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsXcBidirectional.setStatus("current")


class _TnOthOdukApsWaitToRestore_Type(Unsigned32):
    """Custom type tnOthOdukApsWaitToRestore based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnOthOdukApsWaitToRestore_Type.__name__ = "Unsigned32"
_TnOthOdukApsWaitToRestore_Object = MibTableColumn
tnOthOdukApsWaitToRestore = _TnOthOdukApsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 13),
    _TnOthOdukApsWaitToRestore_Type()
)
tnOthOdukApsWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsWaitToRestore.setStatus("current")


class _TnOthOdukApsHoldOffTimer_Type(Unsigned32):
    """Custom type tnOthOdukApsHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnOthOdukApsHoldOffTimer_Type.__name__ = "Unsigned32"
_TnOthOdukApsHoldOffTimer_Object = MibTableColumn
tnOthOdukApsHoldOffTimer = _TnOthOdukApsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 14),
    _TnOthOdukApsHoldOffTimer_Type()
)
tnOthOdukApsHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnOthOdukApsHoldOffTimer.setUnits("milli-seconds")
_TnOthOdukApsGroupK1K2Trans_Type = ApsK1K2
_TnOthOdukApsGroupK1K2Trans_Object = MibTableColumn
tnOthOdukApsGroupK1K2Trans = _TnOthOdukApsGroupK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 15),
    _TnOthOdukApsGroupK1K2Trans_Type()
)
tnOthOdukApsGroupK1K2Trans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupK1K2Trans.setStatus("current")


class _TnOthOdukApsGroupMethod_Type(Integer32):
    """Custom type tnOthOdukApsGroupMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pnim", 1),
          ("tcm1", 2),
          ("tcm2", 3),
          ("tcm3", 4),
          ("tcm4", 5),
          ("tcm5", 6),
          ("tcm6", 7),
          ("padapt", 8))
    )


_TnOthOdukApsGroupMethod_Type.__name__ = "Integer32"
_TnOthOdukApsGroupMethod_Object = MibTableColumn
tnOthOdukApsGroupMethod = _TnOthOdukApsGroupMethod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 16),
    _TnOthOdukApsGroupMethod_Type()
)
tnOthOdukApsGroupMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupMethod.setStatus("current")


class _TnOthOdukApsPingMethod_Type(Integer32):
    """Custom type tnOthOdukApsPingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pnim", 1),
          ("tcm1", 2),
          ("tcm2", 3),
          ("tcm3", 4),
          ("tcm4", 5),
          ("tcm5", 6),
          ("tcm6", 7),
          ("padapt", 8))
    )


_TnOthOdukApsPingMethod_Type.__name__ = "Integer32"
_TnOthOdukApsPingMethod_Object = MibTableColumn
tnOthOdukApsPingMethod = _TnOthOdukApsPingMethod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 17),
    _TnOthOdukApsPingMethod_Type()
)
tnOthOdukApsPingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsPingMethod.setStatus("current")


class _TnOthOdukApsSdEnable_Type(TruthValue):
    """Custom type tnOthOdukApsSdEnable based on TruthValue"""
    defaultValue = 2


_TnOthOdukApsSdEnable_Type.__name__ = "TruthValue"
_TnOthOdukApsSdEnable_Object = MibTableColumn
tnOthOdukApsSdEnable = _TnOthOdukApsSdEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 18),
    _TnOthOdukApsSdEnable_Type()
)
tnOthOdukApsSdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsSdEnable.setStatus("current")


class _TnOthOdukApsCurrentStatus_Type(Bits):
    """Custom type tnOthOdukApsCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("modeMismatch", 0),
          ("channelMismatch", 1),
          ("psbf", 2),
          ("feplf", 3),
          ("extraTraffic", 4))
    )

_TnOthOdukApsCurrentStatus_Type.__name__ = "Bits"
_TnOthOdukApsCurrentStatus_Object = MibTableColumn
tnOthOdukApsCurrentStatus = _TnOthOdukApsCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 19),
    _TnOthOdukApsCurrentStatus_Type()
)
tnOthOdukApsCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsCurrentStatus.setStatus("current")
_TnOthOdukApsGroupID_Type = Unsigned32
_TnOthOdukApsGroupID_Object = MibTableColumn
tnOthOdukApsGroupID = _TnOthOdukApsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 20),
    _TnOthOdukApsGroupID_Type()
)
tnOthOdukApsGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupID.setStatus("current")
_TnOthOdukApsOduXcRate_Type = AluWdmOthOdukXcRate
_TnOthOdukApsOduXcRate_Object = MibTableColumn
tnOthOdukApsOduXcRate = _TnOthOdukApsOduXcRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 21),
    _TnOthOdukApsOduXcRate_Type()
)
tnOthOdukApsOduXcRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsOduXcRate.setStatus("current")


class _TnOthOdukApsGroupCurrentStatus_Type(Integer32):
    """Custom type tnOthOdukApsGroupCurrentStatus based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("lockoutNe", 1),
          ("frcdNe", 2),
          ("sfNe", 3),
          ("sdNe", 4),
          ("manNe", 5),
          ("wtrNe", 6),
          ("dnr", 7),
          ("nr", 8),
          ("lockoutFe", 9),
          ("frcdFe", 10),
          ("sfFe", 11),
          ("sdFe", 12),
          ("manFe", 13),
          ("wtrFe", 14),
          ("exerNe", 15),
          ("exerFe", 16))
    )


_TnOthOdukApsGroupCurrentStatus_Type.__name__ = "Integer32"
_TnOthOdukApsGroupCurrentStatus_Object = MibTableColumn
tnOthOdukApsGroupCurrentStatus = _TnOthOdukApsGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 22),
    _TnOthOdukApsGroupCurrentStatus_Type()
)
tnOthOdukApsGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupCurrentStatus.setStatus("current")


class _TnOthOdukApsSwitchCmd_Type(Integer32):
    """Custom type tnOthOdukApsSwitchCmd based on Integer32"""
    defaultValue = 1

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
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7))
    )


_TnOthOdukApsSwitchCmd_Type.__name__ = "Integer32"
_TnOthOdukApsSwitchCmd_Object = MibTableColumn
tnOthOdukApsSwitchCmd = _TnOthOdukApsSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 23),
    _TnOthOdukApsSwitchCmd_Type()
)
tnOthOdukApsSwitchCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsSwitchCmd.setStatus("current")


class _TnOthOdukApsActSide_Type(Integer32):
    """Custom type tnOthOdukApsActSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2))
    )


_TnOthOdukApsActSide_Type.__name__ = "Integer32"
_TnOthOdukApsActSide_Object = MibTableColumn
tnOthOdukApsActSide = _TnOthOdukApsActSide_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 24),
    _TnOthOdukApsActSide_Type()
)
tnOthOdukApsActSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsActSide.setStatus("current")


class _TnOthOdukApsFromedSfd_Type(Integer32):
    """Custom type tnOthOdukApsFromedSfd based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("sd", 2),
          ("none", 3))
    )


_TnOthOdukApsFromedSfd_Type.__name__ = "Integer32"
_TnOthOdukApsFromedSfd_Object = MibTableColumn
tnOthOdukApsFromedSfd = _TnOthOdukApsFromedSfd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 25),
    _TnOthOdukApsFromedSfd_Type()
)
tnOthOdukApsFromedSfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsFromedSfd.setStatus("current")


class _TnOthOdukApsFromingSfd_Type(Integer32):
    """Custom type tnOthOdukApsFromingSfd based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("sd", 2),
          ("none", 3))
    )


_TnOthOdukApsFromingSfd_Type.__name__ = "Integer32"
_TnOthOdukApsFromingSfd_Object = MibTableColumn
tnOthOdukApsFromingSfd = _TnOthOdukApsFromingSfd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 16, 1, 26),
    _TnOthOdukApsFromingSfd_Type()
)
tnOthOdukApsFromingSfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsFromingSfd.setStatus("current")
_TnOthOdukMemberAttributeTotal_Type = Integer32
_TnOthOdukMemberAttributeTotal_Object = MibScalar
tnOthOdukMemberAttributeTotal = _TnOthOdukMemberAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 17),
    _TnOthOdukMemberAttributeTotal_Type()
)
tnOthOdukMemberAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukMemberAttributeTotal.setStatus("current")
_TnOthOdukMemberTable_Object = MibTable
tnOthOdukMemberTable = _TnOthOdukMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18)
)
if mibBuilder.loadTexts:
    tnOthOdukMemberTable.setStatus("current")
_TnOthOdukMemberEntry_Object = MibTableRow
tnOthOdukMemberEntry = _TnOthOdukMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1)
)
tnOthOdukMemberEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsToIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsToIfIndexLo"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsMemberIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsMemberIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukMemberEntry.setStatus("current")
_TnOthOdukApsMemberIfIndex_Type = Integer32
_TnOthOdukApsMemberIfIndex_Object = MibTableColumn
tnOthOdukApsMemberIfIndex = _TnOthOdukApsMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 1),
    _TnOthOdukApsMemberIfIndex_Type()
)
tnOthOdukApsMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberIfIndex.setStatus("current")
_TnOthOdukApsMemberIfIndexLo_Type = Integer32
_TnOthOdukApsMemberIfIndexLo_Object = MibTableColumn
tnOthOdukApsMemberIfIndexLo = _TnOthOdukApsMemberIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 2),
    _TnOthOdukApsMemberIfIndexLo_Type()
)
tnOthOdukApsMemberIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberIfIndexLo.setStatus("current")
_TnOthOdukApsMemberRowStatus_Type = RowStatus
_TnOthOdukApsMemberRowStatus_Object = MibTableColumn
tnOthOdukApsMemberRowStatus = _TnOthOdukApsMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 3),
    _TnOthOdukApsMemberRowStatus_Type()
)
tnOthOdukApsMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberRowStatus.setStatus("current")


class _TnOthOdukApsMemberConfigNumber_Type(Integer32):
    """Custom type tnOthOdukApsMemberConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 1),
          ("working", 2))
    )


_TnOthOdukApsMemberConfigNumber_Type.__name__ = "Integer32"
_TnOthOdukApsMemberConfigNumber_Object = MibTableColumn
tnOthOdukApsMemberConfigNumber = _TnOthOdukApsMemberConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 4),
    _TnOthOdukApsMemberConfigNumber_Type()
)
tnOthOdukApsMemberConfigNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberConfigNumber.setStatus("current")


class _TnOthOdukApsMemberSwitch_Type(Integer32):
    """Custom type tnOthOdukApsMemberSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7),
          ("exercise", 8))
    )


_TnOthOdukApsMemberSwitch_Type.__name__ = "Integer32"
_TnOthOdukApsMemberSwitch_Object = MibTableColumn
tnOthOdukApsMemberSwitch = _TnOthOdukApsMemberSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 5),
    _TnOthOdukApsMemberSwitch_Type()
)
tnOthOdukApsMemberSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberSwitch.setStatus("current")


class _TnOthOdukApsMemberCurrentStatus_Type(Bits):
    """Custom type tnOthOdukApsMemberCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3),
          ("txActive", 4),
          ("txStandby", 5),
          ("rxActive", 6),
          ("rxStandby", 7))
    )

_TnOthOdukApsMemberCurrentStatus_Type.__name__ = "Bits"
_TnOthOdukApsMemberCurrentStatus_Object = MibTableColumn
tnOthOdukApsMemberCurrentStatus = _TnOthOdukApsMemberCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 18, 1, 6),
    _TnOthOdukApsMemberCurrentStatus_Type()
)
tnOthOdukApsMemberCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsMemberCurrentStatus.setStatus("current")
_TnOthOdukApsGroupIdAttributeTotal_Type = Integer32
_TnOthOdukApsGroupIdAttributeTotal_Object = MibScalar
tnOthOdukApsGroupIdAttributeTotal = _TnOthOdukApsGroupIdAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 19),
    _TnOthOdukApsGroupIdAttributeTotal_Type()
)
tnOthOdukApsGroupIdAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdAttributeTotal.setStatus("current")
_TnOthOdukApsGroupIdTable_Object = MibTable
tnOthOdukApsGroupIdTable = _TnOthOdukApsGroupIdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 20)
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdTable.setStatus("current")
_TnOthOdukApsGroupIdEntry_Object = MibTableRow
tnOthOdukApsGroupIdEntry = _TnOthOdukApsGroupIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 20, 1)
)
tnOthOdukApsGroupIdEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthOdukApsGroupID"),
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdEntry.setStatus("current")
_TnOthOdukApsGroupIdToIfIndex_Type = Integer32
_TnOthOdukApsGroupIdToIfIndex_Object = MibTableColumn
tnOthOdukApsGroupIdToIfIndex = _TnOthOdukApsGroupIdToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 20, 1, 1),
    _TnOthOdukApsGroupIdToIfIndex_Type()
)
tnOthOdukApsGroupIdToIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdToIfIndex.setStatus("current")
_TnOthOdukApsGroupIdToIfIndexLo_Type = Integer32
_TnOthOdukApsGroupIdToIfIndexLo_Object = MibTableColumn
tnOthOdukApsGroupIdToIfIndexLo = _TnOthOdukApsGroupIdToIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 20, 1, 2),
    _TnOthOdukApsGroupIdToIfIndexLo_Type()
)
tnOthOdukApsGroupIdToIfIndexLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdToIfIndexLo.setStatus("current")
_TnOthOdukOptsgAttributeTotal_Type = Integer32
_TnOthOdukOptsgAttributeTotal_Object = MibScalar
tnOthOdukOptsgAttributeTotal = _TnOthOdukOptsgAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 21),
    _TnOthOdukOptsgAttributeTotal_Type()
)
tnOthOdukOptsgAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukOptsgAttributeTotal.setStatus("current")
_TnOthOdukOptsgTable_Object = MibTable
tnOthOdukOptsgTable = _TnOthOdukOptsgTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 22)
)
if mibBuilder.loadTexts:
    tnOthOdukOptsgTable.setStatus("current")
_TnOthOdukOptsgEntry_Object = MibTableRow
tnOthOdukOptsgEntry = _TnOthOdukOptsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 22, 1)
)
tnOthOdukOptsgEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukOptsgEntry.setStatus("current")


class _TnOptsgStruct_Type(SnmpAdminString):
    """Custom type tnOptsgStruct based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOptsgStruct_Type.__name__ = "SnmpAdminString"
_TnOptsgStruct_Object = MibTableColumn
tnOptsgStruct = _TnOptsgStruct_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 22, 1, 1),
    _TnOptsgStruct_Type()
)
tnOptsgStruct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOptsgStruct.setStatus("current")


class _TnIncOptsgStruct_Type(SnmpAdminString):
    """Custom type tnIncOptsgStruct based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnIncOptsgStruct_Type.__name__ = "SnmpAdminString"
_TnIncOptsgStruct_Object = MibTableColumn
tnIncOptsgStruct = _TnIncOptsgStruct_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 22, 1, 2),
    _TnIncOptsgStruct_Type()
)
tnIncOptsgStruct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIncOptsgStruct.setStatus("current")
_TnOthOdukDMConfigAttributeTotal_Type = Integer32
_TnOthOdukDMConfigAttributeTotal_Object = MibScalar
tnOthOdukDMConfigAttributeTotal = _TnOthOdukDMConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 23),
    _TnOthOdukDMConfigAttributeTotal_Type()
)
tnOthOdukDMConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukDMConfigAttributeTotal.setStatus("current")
_TnOthOdukDMConfigTable_Object = MibTable
tnOthOdukDMConfigTable = _TnOthOdukDMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 24)
)
if mibBuilder.loadTexts:
    tnOthOdukDMConfigTable.setStatus("current")
_TnOthOdukDMConfigEntry_Object = MibTableRow
tnOthOdukDMConfigEntry = _TnOthOdukDMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 24, 1)
)
tnOthOdukDMConfigEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukDMConfigEntry.setStatus("current")


class _TnOthOdukDMConfigCMEPMode_Type(Integer32):
    """Custom type tnOthOdukDMConfigCMEPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 1),
          ("source", 2),
          ("destination", 3))
    )


_TnOthOdukDMConfigCMEPMode_Type.__name__ = "Integer32"
_TnOthOdukDMConfigCMEPMode_Object = MibTableColumn
tnOthOdukDMConfigCMEPMode = _TnOthOdukDMConfigCMEPMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 24, 1, 1),
    _TnOthOdukDMConfigCMEPMode_Type()
)
tnOthOdukDMConfigCMEPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukDMConfigCMEPMode.setStatus("current")


class _TnOthOdukDMConfigEnable_Type(Integer32):
    """Custom type tnOthOdukDMConfigEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnOthOdukDMConfigEnable_Type.__name__ = "Integer32"
_TnOthOdukDMConfigEnable_Object = MibTableColumn
tnOthOdukDMConfigEnable = _TnOthOdukDMConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 24, 1, 2),
    _TnOthOdukDMConfigEnable_Type()
)
tnOthOdukDMConfigEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOthOdukDMConfigEnable.setStatus("current")
_TnOthOdukDMInfoAttributeTotal_Type = Integer32
_TnOthOdukDMInfoAttributeTotal_Object = MibScalar
tnOthOdukDMInfoAttributeTotal = _TnOthOdukDMInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 25),
    _TnOthOdukDMInfoAttributeTotal_Type()
)
tnOthOdukDMInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukDMInfoAttributeTotal.setStatus("current")
_TnOthOdukDMInfoTable_Object = MibTable
tnOthOdukDMInfoTable = _TnOthOdukDMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 26)
)
if mibBuilder.loadTexts:
    tnOthOdukDMInfoTable.setStatus("current")
_TnOthOdukDMInfoEntry_Object = MibTableRow
tnOthOdukDMInfoEntry = _TnOthOdukDMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 26, 1)
)
tnOthOdukDMInfoEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukDMInfoEntry.setStatus("current")
_TnOthOdukDMInfoCurrentStatus_Type = AluWdmDMInfoCurrentStatus
_TnOthOdukDMInfoCurrentStatus_Object = MibTableColumn
tnOthOdukDMInfoCurrentStatus = _TnOthOdukDMInfoCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 26, 1, 1),
    _TnOthOdukDMInfoCurrentStatus_Type()
)
tnOthOdukDMInfoCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukDMInfoCurrentStatus.setStatus("current")
_TnOthOdukDMInfoCurrentValue_Type = Unsigned32
_TnOthOdukDMInfoCurrentValue_Object = MibTableColumn
tnOthOdukDMInfoCurrentValue = _TnOthOdukDMInfoCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 26, 1, 2),
    _TnOthOdukDMInfoCurrentValue_Type()
)
tnOthOdukDMInfoCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukDMInfoCurrentValue.setStatus("current")
_TnOthOdukIncFtflInfoAttributeTotal_Type = Integer32
_TnOthOdukIncFtflInfoAttributeTotal_Object = MibScalar
tnOthOdukIncFtflInfoAttributeTotal = _TnOthOdukIncFtflInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 27),
    _TnOthOdukIncFtflInfoAttributeTotal_Type()
)
tnOthOdukIncFtflInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflInfoAttributeTotal.setStatus("current")
_TnOthOdukIncFtflInfoTable_Object = MibTable
tnOthOdukIncFtflInfoTable = _TnOthOdukIncFtflInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28)
)
if mibBuilder.loadTexts:
    tnOthOdukIncFtflInfoTable.setStatus("current")
_TnOthOdukIncFtflInfoEntry_Object = MibTableRow
tnOthOdukIncFtflInfoEntry = _TnOthOdukIncFtflInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1)
)
tnOthOdukIncFtflInfoEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnOthOdukIncFtflInfoEntry.setStatus("current")
_TnOthOdukIncFtflFwTypeID_Type = OctetString
_TnOthOdukIncFtflFwTypeID_Object = MibTableColumn
tnOthOdukIncFtflFwTypeID = _TnOthOdukIncFtflFwTypeID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1, 1),
    _TnOthOdukIncFtflFwTypeID_Type()
)
tnOthOdukIncFtflFwTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflFwTypeID.setStatus("current")
_TnOthOdukIncFtflFwOperID_Type = OctetString
_TnOthOdukIncFtflFwOperID_Object = MibTableColumn
tnOthOdukIncFtflFwOperID = _TnOthOdukIncFtflFwOperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1, 2),
    _TnOthOdukIncFtflFwOperID_Type()
)
tnOthOdukIncFtflFwOperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflFwOperID.setStatus("current")
_TnOthOdukIncFtflBwTypeID_Type = OctetString
_TnOthOdukIncFtflBwTypeID_Object = MibTableColumn
tnOthOdukIncFtflBwTypeID = _TnOthOdukIncFtflBwTypeID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1, 3),
    _TnOthOdukIncFtflBwTypeID_Type()
)
tnOthOdukIncFtflBwTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflBwTypeID.setStatus("current")
_TnOthOdukIncFtflBwOperID_Type = OctetString
_TnOthOdukIncFtflBwOperID_Object = MibTableColumn
tnOthOdukIncFtflBwOperID = _TnOthOdukIncFtflBwOperID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1, 4),
    _TnOthOdukIncFtflBwOperID_Type()
)
tnOthOdukIncFtflBwOperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflBwOperID.setStatus("current")
_TnOthOdukIncFtflExp_Type = OctetString
_TnOthOdukIncFtflExp_Object = MibTableColumn
tnOthOdukIncFtflExp = _TnOthOdukIncFtflExp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 2, 1, 28, 1, 5),
    _TnOthOdukIncFtflExp_Type()
)
tnOthOdukIncFtflExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOthOdukIncFtflExp.setStatus("current")

# Managed Objects groups

tnOthOdukScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 1)
)
tnOthOdukScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukScalarsGroup.setStatus("current")

tnOthOdukGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 2)
)
tnOthOdukGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukDirectionality"),
        ("TROPIC-OTH-MIB", "tnOthOdukRate"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmFieldsInUse"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpPresent"),
        ("TROPIC-OTH-MIB", "tnOthOdukAdminStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukStateAINS"),
        ("TROPIC-OTH-MIB", "tnOthOdukOperStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukStateQualifier"),
        ("TROPIC-OTH-MIB", "tnOthOdukOperationalCapability"),
        ("TROPIC-OTH-MIB", "tnOthOdukAINSDebounceTime"),
        ("TROPIC-OTH-MIB", "tnOthOdukUsingSysAINSDebounceTime"),
        ("TROPIC-OTH-MIB", "tnOthOdukAINSDebounceTimeRemaining"),
        ("TROPIC-OTH-MIB", "tnOthOdukForceAdminStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukMgracd"),
        ("TROPIC-OTH-MIB", "tnOthOdukAlmProfName"),
        ("TROPIC-OTH-MIB", "tnOthOdukFlexType"),
        ("TROPIC-OTH-MIB", "tnOthOdukFlexClientType"),
        ("TROPIC-OTH-MIB", "tnOthOdukFlexGfpSize"))
)
if mibBuilder.loadTexts:
    tnOthOdukGroup.setStatus("current")

tnOthOdukTtpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 3)
)
tnOthOdukTtpScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukTtpAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukTtpScalarsGroup.setStatus("current")

tnOthOdukTtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 4)
)
tnOthOdukTtpGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukTtpSapiTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpDapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpSapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpTraceIdentifierAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpTimDetMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpTimActEnabled"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpTtiStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpDegThr"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpDegM"),
        ("TROPIC-OTH-MIB", "tnOthOdukPayloadType"),
        ("TROPIC-OTH-MIB", "tnOthOdukRxPayloadType"),
        ("TROPIC-OTH-MIB", "tnOthOdukPlmConsequenceAction"),
        ("TROPIC-OTH-MIB", "tnOthOdukTxOduStruct"),
        ("TROPIC-OTH-MIB", "tnOthOdukRxOduStruct"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpCurrentStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukOdu0Interwk"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpDapiAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpDapiTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpOsAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpOsTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukRxMSI"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpCndRes"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpCmEmphasis"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpManualOduPtf"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpCsfType"))
)
if mibBuilder.loadTexts:
    tnOthOdukTtpGroup.setStatus("current")

tnOthOdukNimScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 5)
)
tnOthOdukNimScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukNimAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukNimScalarsGroup.setStatus("current")

tnOthOdukNimGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 6)
)
tnOthOdukNimGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukNimDapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimSapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimTraceIdentifierAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimTimDetMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimTimActEnabled"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimTtiStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimDegThr"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimDegM"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimPom"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimDapiAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimOsAccepted"))
)
if mibBuilder.loadTexts:
    tnOthOdukNimGroup.setStatus("current")

tnOthGcc12ScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 7)
)
tnOthGcc12ScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthGcc12AttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthGcc12ScalarsGroup.setStatus("current")

tnOthGcc12Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 8)
)
tnOthGcc12Group.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthGcc12RowStatus"),
        ("TROPIC-OTH-MIB", "tnOthGcc12GccPassThrough"),
        ("TROPIC-OTH-MIB", "tnOthGcc12Application"))
)
if mibBuilder.loadTexts:
    tnOthGcc12Group.setStatus("current")

tnOthOdukTScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 9)
)
tnOthOdukTScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukTAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukTScalarsGroup.setStatus("current")

tnOthOdukTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 10)
)
tnOthOdukTGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukTRowStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTcmMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukTPosSeq"),
        ("TROPIC-OTH-MIB", "tnOthOdukTAdminStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukTSapiTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTSapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTraceIdentifierAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTimDetMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTimActEnabled"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTtpTtiStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukTAisOnDef"),
        ("TROPIC-OTH-MIB", "tnOthOdukTLtcResp"),
        ("TROPIC-OTH-MIB", "tnOthOdukTOhAdd"),
        ("TROPIC-OTH-MIB", "tnOthOdukTOhRmv"),
        ("TROPIC-OTH-MIB", "tnOthOdukTDegThr"),
        ("TROPIC-OTH-MIB", "tnOthOdukTDegM"),
        ("TROPIC-OTH-MIB", "tnOthOdukTDapiAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTDapiExpected"),
        ("TROPIC-OTH-MIB", "tnOthOdukTDapiTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTOsAccepted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTOsTransmitted"),
        ("TROPIC-OTH-MIB", "tnOthOdukTTcmAlmProfName"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmOperStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmMgracd"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmincstat"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmOperationalCapability"),
        ("TROPIC-OTH-MIB", "tnOthOdukTcmStateQualifier"))
)
if mibBuilder.loadTexts:
    tnOthOdukTGroup.setStatus("current")

tnOthOdukXcScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 13)
)
tnOthOdukXcScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukXcAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukXcScalarsGroup.setStatus("current")

tnOthOdukXcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 14)
)
tnOthOdukXcGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukXcRowStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcId"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcRate"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcBidirectional"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcName"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcProtectionState"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcTopology"))
)
if mibBuilder.loadTexts:
    tnOthOdukXcGroup.setStatus("current")

tnOthOdukApsScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 15)
)
tnOthOdukApsScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukApsGroupAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukApsScalarsGroup.setStatus("current")

tnOthOdukApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 16)
)
tnOthOdukApsGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukApsAction"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsDescr"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsRevert"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsDirection"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsXcBidirectional"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsWaitToRestore"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsHoldOffTimer"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupK1K2Trans"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupMethod"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsPingMethod"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsSdEnable"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsCurrentStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupID"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsOduXcRate"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupCurrentStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsSwitchCmd"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsActSide"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsFromedSfd"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsFromingSfd"))
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroup.setStatus("current")

tnOthOdukMemberScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 17)
)
tnOthOdukMemberScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukMemberAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukMemberScalarsGroup.setStatus("current")

tnOthOdukMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 18)
)
tnOthOdukMemberGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukApsMemberRowStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsMemberConfigNumber"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsMemberSwitch"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsMemberCurrentStatus"))
)
if mibBuilder.loadTexts:
    tnOthOdukMemberGroup.setStatus("current")

tnOthOdukApsGroupIdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 19)
)
tnOthOdukApsGroupIdScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukApsGroupIdAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdScalarsGroup.setStatus("current")

tnOthOdukApsGroupIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 20)
)
tnOthOdukApsGroupIdGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukApsGroupIdToIfIndex"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupIdToIfIndexLo"))
)
if mibBuilder.loadTexts:
    tnOthOdukApsGroupIdGroup.setStatus("current")

tnOthOdukOptsgScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 21)
)
tnOthOdukOptsgScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukOptsgAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukOptsgScalarsGroup.setStatus("current")

tnOthOdukOptsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 22)
)
tnOthOdukOptsgGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOptsgStruct"),
        ("TROPIC-OTH-MIB", "tnIncOptsgStruct"))
)
if mibBuilder.loadTexts:
    tnOthOdukOptsgGroup.setStatus("current")

tnOthOdukDMConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 23)
)
tnOthOdukDMConfigScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukDMConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukDMConfigScalarsGroup.setStatus("current")

tnOthOdukDMConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 24)
)
tnOthOdukDMConfigGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukDMConfigCMEPMode"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMConfigEnable"))
)
if mibBuilder.loadTexts:
    tnOthOdukDMConfigGroup.setStatus("current")

tnOthOdukDMInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 25)
)
tnOthOdukDMInfoScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukDMInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukDMInfoScalarsGroup.setStatus("current")

tnOthOdukDMInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 26)
)
tnOthOdukDMInfoGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukDMInfoCurrentStatus"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMInfoCurrentValue"))
)
if mibBuilder.loadTexts:
    tnOthOdukDMInfoGroup.setStatus("current")

tnOthOdukIncFtflInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 27)
)
tnOthOdukIncFtflInfoScalarsGroup.setObjects(
    ("TROPIC-OTH-MIB", "tnOthOdukIncFtflInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnOthOdukIncFtflInfoScalarsGroup.setStatus("current")

tnOthOdukIncFtflInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 1, 28)
)
tnOthOdukIncFtflInfoGroup.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukIncFtflFwTypeID"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflFwOperID"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflBwTypeID"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflBwOperID"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflExp"))
)
if mibBuilder.loadTexts:
    tnOthOdukIncFtflInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10, 1, 2, 1)
)
tnOthCompliance.setObjects(
      *(("TROPIC-OTH-MIB", "tnOthOdukScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukTtpGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukNimGroup"),
        ("TROPIC-OTH-MIB", "tnOthGcc12ScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthGcc12Group"),
        ("TROPIC-OTH-MIB", "tnOthOdukTScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukTGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukXcGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukMemberScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukMemberGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupIdScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukApsGroupIdGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukOptsgScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukOptsgGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMConfigScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMConfigGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMInfoScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukDMInfoGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflInfoScalarsGroup"),
        ("TROPIC-OTH-MIB", "tnOthOdukIncFtflInfoGroup"))
)
if mibBuilder.loadTexts:
    tnOthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OTH-MIB",
    **{"tnOthMibModule": tnOthMibModule,
       "tnOthConf": tnOthConf,
       "tnOthGroups": tnOthGroups,
       "tnOthOdukScalarsGroup": tnOthOdukScalarsGroup,
       "tnOthOdukGroup": tnOthOdukGroup,
       "tnOthOdukTtpScalarsGroup": tnOthOdukTtpScalarsGroup,
       "tnOthOdukTtpGroup": tnOthOdukTtpGroup,
       "tnOthOdukNimScalarsGroup": tnOthOdukNimScalarsGroup,
       "tnOthOdukNimGroup": tnOthOdukNimGroup,
       "tnOthGcc12ScalarsGroup": tnOthGcc12ScalarsGroup,
       "tnOthGcc12Group": tnOthGcc12Group,
       "tnOthOdukTScalarsGroup": tnOthOdukTScalarsGroup,
       "tnOthOdukTGroup": tnOthOdukTGroup,
       "tnOthOdukXcScalarsGroup": tnOthOdukXcScalarsGroup,
       "tnOthOdukXcGroup": tnOthOdukXcGroup,
       "tnOthOdukApsScalarsGroup": tnOthOdukApsScalarsGroup,
       "tnOthOdukApsGroup": tnOthOdukApsGroup,
       "tnOthOdukMemberScalarsGroup": tnOthOdukMemberScalarsGroup,
       "tnOthOdukMemberGroup": tnOthOdukMemberGroup,
       "tnOthOdukApsGroupIdScalarsGroup": tnOthOdukApsGroupIdScalarsGroup,
       "tnOthOdukApsGroupIdGroup": tnOthOdukApsGroupIdGroup,
       "tnOthOdukOptsgScalarsGroup": tnOthOdukOptsgScalarsGroup,
       "tnOthOdukOptsgGroup": tnOthOdukOptsgGroup,
       "tnOthOdukDMConfigScalarsGroup": tnOthOdukDMConfigScalarsGroup,
       "tnOthOdukDMConfigGroup": tnOthOdukDMConfigGroup,
       "tnOthOdukDMInfoScalarsGroup": tnOthOdukDMInfoScalarsGroup,
       "tnOthOdukDMInfoGroup": tnOthOdukDMInfoGroup,
       "tnOthOdukIncFtflInfoScalarsGroup": tnOthOdukIncFtflInfoScalarsGroup,
       "tnOthOdukIncFtflInfoGroup": tnOthOdukIncFtflInfoGroup,
       "tnOthCompliances": tnOthCompliances,
       "tnOthCompliance": tnOthCompliance,
       "tnOthObjs": tnOthObjs,
       "tnOthBasics": tnOthBasics,
       "tnOthOdukAttributeTotal": tnOthOdukAttributeTotal,
       "tnOthOdukTable": tnOthOdukTable,
       "tnOthOdukEntry": tnOthOdukEntry,
       "tnOthIfIndex": tnOthIfIndex,
       "tnOthIfIndexLo": tnOthIfIndexLo,
       "tnOthOdukDirectionality": tnOthOdukDirectionality,
       "tnOthOdukRate": tnOthOdukRate,
       "tnOthOdukTcmFieldsInUse": tnOthOdukTcmFieldsInUse,
       "tnOthOdukTtpPresent": tnOthOdukTtpPresent,
       "tnOthOdukAdminStatus": tnOthOdukAdminStatus,
       "tnOthOdukStateAINS": tnOthOdukStateAINS,
       "tnOthOdukOperStatus": tnOthOdukOperStatus,
       "tnOthOdukStateQualifier": tnOthOdukStateQualifier,
       "tnOthOdukOperationalCapability": tnOthOdukOperationalCapability,
       "tnOthOdukAINSDebounceTime": tnOthOdukAINSDebounceTime,
       "tnOthOdukUsingSysAINSDebounceTime": tnOthOdukUsingSysAINSDebounceTime,
       "tnOthOdukAINSDebounceTimeRemaining": tnOthOdukAINSDebounceTimeRemaining,
       "tnOthOdukForceAdminStatus": tnOthOdukForceAdminStatus,
       "tnOthOdukMgracd": tnOthOdukMgracd,
       "tnOthOdukAlmProfName": tnOthOdukAlmProfName,
       "tnOthOdukFlexType": tnOthOdukFlexType,
       "tnOthOdukFlexClientType": tnOthOdukFlexClientType,
       "tnOthOdukFlexGfpSize": tnOthOdukFlexGfpSize,
       "tnOthOdukTtpAttributeTotal": tnOthOdukTtpAttributeTotal,
       "tnOthOdukTtpTable": tnOthOdukTtpTable,
       "tnOthOdukTtpEntry": tnOthOdukTtpEntry,
       "tnOthOdukTtpSapiTransmitted": tnOthOdukTtpSapiTransmitted,
       "tnOthOdukTtpDapiExpected": tnOthOdukTtpDapiExpected,
       "tnOthOdukTtpSapiExpected": tnOthOdukTtpSapiExpected,
       "tnOthOdukTtpTraceIdentifierAccepted": tnOthOdukTtpTraceIdentifierAccepted,
       "tnOthOdukTtpTimDetMode": tnOthOdukTtpTimDetMode,
       "tnOthOdukTtpTimActEnabled": tnOthOdukTtpTimActEnabled,
       "tnOthOdukTtpTtiStatus": tnOthOdukTtpTtiStatus,
       "tnOthOdukTtpDegThr": tnOthOdukTtpDegThr,
       "tnOthOdukTtpDegM": tnOthOdukTtpDegM,
       "tnOthOdukPayloadType": tnOthOdukPayloadType,
       "tnOthOdukRxPayloadType": tnOthOdukRxPayloadType,
       "tnOthOdukPlmConsequenceAction": tnOthOdukPlmConsequenceAction,
       "tnOthOdukTxOduStruct": tnOthOdukTxOduStruct,
       "tnOthOdukRxOduStruct": tnOthOdukRxOduStruct,
       "tnOthOdukTtpCurrentStatus": tnOthOdukTtpCurrentStatus,
       "tnOthOdukOdu0Interwk": tnOthOdukOdu0Interwk,
       "tnOthOdukTtpDapiAccepted": tnOthOdukTtpDapiAccepted,
       "tnOthOdukTtpDapiTransmitted": tnOthOdukTtpDapiTransmitted,
       "tnOthOdukTtpOsAccepted": tnOthOdukTtpOsAccepted,
       "tnOthOdukTtpOsTransmitted": tnOthOdukTtpOsTransmitted,
       "tnOthOdukRxMSI": tnOthOdukRxMSI,
       "tnOthOdukTtpCndRes": tnOthOdukTtpCndRes,
       "tnOthOdukTtpCmEmphasis": tnOthOdukTtpCmEmphasis,
       "tnOthOdukTtpManualOduPtf": tnOthOdukTtpManualOduPtf,
       "tnOthOdukTtpCsfType": tnOthOdukTtpCsfType,
       "tnOthOdukNimAttributeTotal": tnOthOdukNimAttributeTotal,
       "tnOthOdukNimTable": tnOthOdukNimTable,
       "tnOthOdukNimEntry": tnOthOdukNimEntry,
       "tnOthOdukNimDirectionality": tnOthOdukNimDirectionality,
       "tnOthOdukNimDapiExpected": tnOthOdukNimDapiExpected,
       "tnOthOdukNimSapiExpected": tnOthOdukNimSapiExpected,
       "tnOthOdukNimTraceIdentifierAccepted": tnOthOdukNimTraceIdentifierAccepted,
       "tnOthOdukNimTimDetMode": tnOthOdukNimTimDetMode,
       "tnOthOdukNimTimActEnabled": tnOthOdukNimTimActEnabled,
       "tnOthOdukNimTtiStatus": tnOthOdukNimTtiStatus,
       "tnOthOdukNimDegThr": tnOthOdukNimDegThr,
       "tnOthOdukNimDegM": tnOthOdukNimDegM,
       "tnOthOdukNimPom": tnOthOdukNimPom,
       "tnOthOdukNimDapiAccepted": tnOthOdukNimDapiAccepted,
       "tnOthOdukNimOsAccepted": tnOthOdukNimOsAccepted,
       "tnOthGcc12AttributeTotal": tnOthGcc12AttributeTotal,
       "tnOthGcc12Table": tnOthGcc12Table,
       "tnOthGcc12Entry": tnOthGcc12Entry,
       "tnOthGcc12Codirectional": tnOthGcc12Codirectional,
       "tnOthGcc12GccAccess": tnOthGcc12GccAccess,
       "tnOthGcc12RowStatus": tnOthGcc12RowStatus,
       "tnOthGcc12GccPassThrough": tnOthGcc12GccPassThrough,
       "tnOthGcc12Application": tnOthGcc12Application,
       "tnOthOdukTAttributeTotal": tnOthOdukTAttributeTotal,
       "tnOthOdukTTable": tnOthOdukTTable,
       "tnOthOdukTEntry": tnOthOdukTEntry,
       "tnOthOdukTRowStatus": tnOthOdukTRowStatus,
       "tnOthOdukTTcmMode": tnOthOdukTTcmMode,
       "tnOthOdukTPosSeq": tnOthOdukTPosSeq,
       "tnOthOdukTAdminStatus": tnOthOdukTAdminStatus,
       "tnOthOdukTSapiTransmitted": tnOthOdukTSapiTransmitted,
       "tnOthOdukTSapiExpected": tnOthOdukTSapiExpected,
       "tnOthOdukTTraceIdentifierAccepted": tnOthOdukTTraceIdentifierAccepted,
       "tnOthOdukTTimDetMode": tnOthOdukTTimDetMode,
       "tnOthOdukTTimActEnabled": tnOthOdukTTimActEnabled,
       "tnOthOdukTTtpTtiStatus": tnOthOdukTTtpTtiStatus,
       "tnOthOdukTAisOnDef": tnOthOdukTAisOnDef,
       "tnOthOdukTLtcResp": tnOthOdukTLtcResp,
       "tnOthOdukTOhAdd": tnOthOdukTOhAdd,
       "tnOthOdukTOhRmv": tnOthOdukTOhRmv,
       "tnOthOdukTcmIfIndex": tnOthOdukTcmIfIndex,
       "tnOthOdukTcmIfIndexLo": tnOthOdukTcmIfIndexLo,
       "tnOthOdukTDegThr": tnOthOdukTDegThr,
       "tnOthOdukTDegM": tnOthOdukTDegM,
       "tnOthOdukTDapiAccepted": tnOthOdukTDapiAccepted,
       "tnOthOdukTDapiExpected": tnOthOdukTDapiExpected,
       "tnOthOdukTDapiTransmitted": tnOthOdukTDapiTransmitted,
       "tnOthOdukTOsAccepted": tnOthOdukTOsAccepted,
       "tnOthOdukTOsTransmitted": tnOthOdukTOsTransmitted,
       "tnOthOdukTTcmAlmProfName": tnOthOdukTTcmAlmProfName,
       "tnOthOdukTcmOperStatus": tnOthOdukTcmOperStatus,
       "tnOthOdukTcmMgracd": tnOthOdukTcmMgracd,
       "tnOthOdukTcmincstat": tnOthOdukTcmincstat,
       "tnOthOdukTcmOperationalCapability": tnOthOdukTcmOperationalCapability,
       "tnOthOdukTcmStateQualifier": tnOthOdukTcmStateQualifier,
       "tnOthOdukXcAttributeTotal": tnOthOdukXcAttributeTotal,
       "tnOthOdukXcTable": tnOthOdukXcTable,
       "tnOthOdukXcEntry": tnOthOdukXcEntry,
       "tnOthOdukXcSrcIfIndex": tnOthOdukXcSrcIfIndex,
       "tnOthOdukXcSrcIfIndexLo": tnOthOdukXcSrcIfIndexLo,
       "tnOthOdukXcDestIfIndex": tnOthOdukXcDestIfIndex,
       "tnOthOdukXcDestIfIndexLo": tnOthOdukXcDestIfIndexLo,
       "tnOthOdukXcRowStatus": tnOthOdukXcRowStatus,
       "tnOthOdukXcId": tnOthOdukXcId,
       "tnOthOdukXcRate": tnOthOdukXcRate,
       "tnOthOdukXcBidirectional": tnOthOdukXcBidirectional,
       "tnOthOdukXcName": tnOthOdukXcName,
       "tnOthOdukXcProtectionState": tnOthOdukXcProtectionState,
       "tnOthOdukXcTopology": tnOthOdukXcTopology,
       "tnOthOdukApsGroupAttributeTotal": tnOthOdukApsGroupAttributeTotal,
       "tnOthOdukApsGroupTable": tnOthOdukApsGroupTable,
       "tnOthOdukApsGroupEntry": tnOthOdukApsGroupEntry,
       "tnOthOdukApsToIfIndex": tnOthOdukApsToIfIndex,
       "tnOthOdukApsToIfIndexLo": tnOthOdukApsToIfIndexLo,
       "tnOthOdukApsFromedIfIndex": tnOthOdukApsFromedIfIndex,
       "tnOthOdukApsFromedIfIndexLo": tnOthOdukApsFromedIfIndexLo,
       "tnOthOdukApsFromingIfIndex": tnOthOdukApsFromingIfIndex,
       "tnOthOdukApsFromingIfIndexLo": tnOthOdukApsFromingIfIndexLo,
       "tnOthOdukApsAction": tnOthOdukApsAction,
       "tnOthOdukApsDescr": tnOthOdukApsDescr,
       "tnOthOdukApsMode": tnOthOdukApsMode,
       "tnOthOdukApsRevert": tnOthOdukApsRevert,
       "tnOthOdukApsDirection": tnOthOdukApsDirection,
       "tnOthOdukApsXcBidirectional": tnOthOdukApsXcBidirectional,
       "tnOthOdukApsWaitToRestore": tnOthOdukApsWaitToRestore,
       "tnOthOdukApsHoldOffTimer": tnOthOdukApsHoldOffTimer,
       "tnOthOdukApsGroupK1K2Trans": tnOthOdukApsGroupK1K2Trans,
       "tnOthOdukApsGroupMethod": tnOthOdukApsGroupMethod,
       "tnOthOdukApsPingMethod": tnOthOdukApsPingMethod,
       "tnOthOdukApsSdEnable": tnOthOdukApsSdEnable,
       "tnOthOdukApsCurrentStatus": tnOthOdukApsCurrentStatus,
       "tnOthOdukApsGroupID": tnOthOdukApsGroupID,
       "tnOthOdukApsOduXcRate": tnOthOdukApsOduXcRate,
       "tnOthOdukApsGroupCurrentStatus": tnOthOdukApsGroupCurrentStatus,
       "tnOthOdukApsSwitchCmd": tnOthOdukApsSwitchCmd,
       "tnOthOdukApsActSide": tnOthOdukApsActSide,
       "tnOthOdukApsFromedSfd": tnOthOdukApsFromedSfd,
       "tnOthOdukApsFromingSfd": tnOthOdukApsFromingSfd,
       "tnOthOdukMemberAttributeTotal": tnOthOdukMemberAttributeTotal,
       "tnOthOdukMemberTable": tnOthOdukMemberTable,
       "tnOthOdukMemberEntry": tnOthOdukMemberEntry,
       "tnOthOdukApsMemberIfIndex": tnOthOdukApsMemberIfIndex,
       "tnOthOdukApsMemberIfIndexLo": tnOthOdukApsMemberIfIndexLo,
       "tnOthOdukApsMemberRowStatus": tnOthOdukApsMemberRowStatus,
       "tnOthOdukApsMemberConfigNumber": tnOthOdukApsMemberConfigNumber,
       "tnOthOdukApsMemberSwitch": tnOthOdukApsMemberSwitch,
       "tnOthOdukApsMemberCurrentStatus": tnOthOdukApsMemberCurrentStatus,
       "tnOthOdukApsGroupIdAttributeTotal": tnOthOdukApsGroupIdAttributeTotal,
       "tnOthOdukApsGroupIdTable": tnOthOdukApsGroupIdTable,
       "tnOthOdukApsGroupIdEntry": tnOthOdukApsGroupIdEntry,
       "tnOthOdukApsGroupIdToIfIndex": tnOthOdukApsGroupIdToIfIndex,
       "tnOthOdukApsGroupIdToIfIndexLo": tnOthOdukApsGroupIdToIfIndexLo,
       "tnOthOdukOptsgAttributeTotal": tnOthOdukOptsgAttributeTotal,
       "tnOthOdukOptsgTable": tnOthOdukOptsgTable,
       "tnOthOdukOptsgEntry": tnOthOdukOptsgEntry,
       "tnOptsgStruct": tnOptsgStruct,
       "tnIncOptsgStruct": tnIncOptsgStruct,
       "tnOthOdukDMConfigAttributeTotal": tnOthOdukDMConfigAttributeTotal,
       "tnOthOdukDMConfigTable": tnOthOdukDMConfigTable,
       "tnOthOdukDMConfigEntry": tnOthOdukDMConfigEntry,
       "tnOthOdukDMConfigCMEPMode": tnOthOdukDMConfigCMEPMode,
       "tnOthOdukDMConfigEnable": tnOthOdukDMConfigEnable,
       "tnOthOdukDMInfoAttributeTotal": tnOthOdukDMInfoAttributeTotal,
       "tnOthOdukDMInfoTable": tnOthOdukDMInfoTable,
       "tnOthOdukDMInfoEntry": tnOthOdukDMInfoEntry,
       "tnOthOdukDMInfoCurrentStatus": tnOthOdukDMInfoCurrentStatus,
       "tnOthOdukDMInfoCurrentValue": tnOthOdukDMInfoCurrentValue,
       "tnOthOdukIncFtflInfoAttributeTotal": tnOthOdukIncFtflInfoAttributeTotal,
       "tnOthOdukIncFtflInfoTable": tnOthOdukIncFtflInfoTable,
       "tnOthOdukIncFtflInfoEntry": tnOthOdukIncFtflInfoEntry,
       "tnOthOdukIncFtflFwTypeID": tnOthOdukIncFtflFwTypeID,
       "tnOthOdukIncFtflFwOperID": tnOthOdukIncFtflFwOperID,
       "tnOthOdukIncFtflBwTypeID": tnOthOdukIncFtflBwTypeID,
       "tnOthOdukIncFtflBwOperID": tnOthOdukIncFtflBwOperID,
       "tnOthOdukIncFtflExp": tnOthOdukIncFtflExp}
)
