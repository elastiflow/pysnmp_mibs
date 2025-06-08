# SNMP MIB module (IEEE8021-AS-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-AS-V2-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:12:19 2025
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

(Float64TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float64TC")

(IEEE8021BridgePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021AsV2TimeSyncMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 33)
)
if mibBuilder.loadTexts:
    ieee8021AsV2TimeSyncMib.setRevisions(
        ("2020-06-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ieee8021AsV2ClockIdentity(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class Ieee8021AsV2GPtpProfileIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class Ieee8021AsV2ClockClassValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58,
              187,
              193,
              248,
              255)
        )
    )
    namedValues = NamedValues(
        *(("primarySync", 6),
          ("primarySyncLost", 7),
          ("applicationSpecificSync", 13),
          ("applicationSpecficSyncLost", 14),
          ("primarySyncAlternativeA", 52),
          ("applicationSpecificAlternativeA", 58),
          ("primarySyncAlternativeB", 187),
          ("applicationSpecficAlternativeB", 193),
          ("defaultClock", 248),
          ("slaveOnlyClock", 255))
    )



class Ieee8021AsV2ClockAccuracyValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254)
        )
    )
    namedValues = NamedValues(
        *(("timeAccurateTo25ns", 32),
          ("timeAccurateTo100ns", 33),
          ("timeAccurateTo250ns", 34),
          ("timeAccurateTo1us", 35),
          ("timeAccurateTo2dot5us", 36),
          ("timeAccurateTo10us", 37),
          ("timeAccurateTo25us", 38),
          ("timeAccurateTo100us", 39),
          ("timeAccurateTo250us", 40),
          ("timeAccurateTo1ms", 41),
          ("timeAccurateTo2dot5ms", 42),
          ("timeAccurateTo10ms", 43),
          ("timeAccurateTo25ms", 44),
          ("timeAccurateTo100ms", 45),
          ("timeAccurateTo250ms", 46),
          ("timeAccurateTo1s", 47),
          ("timeAccurateTo10s", 48),
          ("timeAccurateToGT10s", 49),
          ("timeAccurateToUnknown", 254))
    )



class Ieee8021AsV2TimeSourceValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160))
    )



class Ieee8021ASV2PtpTimeInterval(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class Ieee8021ASV2PtpPortIdentity(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixedLength = 10



class Ieee8021ASV2ScaledNs(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixedLength = 12



class Ieee8021ASV2UScaledNs(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixedLength = 12



class Ieee8021ASV2PTPInstanceIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class Ieee8021ASV2Timestamp(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



# MIB Managed Objects in the order of their OIDs

_Ieee8021AsV2MIBObjects_ObjectIdentity = ObjectIdentity
ieee8021AsV2MIBObjects = _Ieee8021AsV2MIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 33, 1)
)
_Ieee8021AsV2PtpInstanceTable_Object = MibTable
ieee8021AsV2PtpInstanceTable = _Ieee8021AsV2PtpInstanceTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstanceTable.setStatus("current")
_Ieee8021AsV2PtpInstanceEntry_Object = MibTableRow
ieee8021AsV2PtpInstanceEntry = _Ieee8021AsV2PtpInstanceEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 1, 1)
)
ieee8021AsV2PtpInstanceEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstanceEntry.setStatus("current")
_Ieee8021AsV2PtpInstance_Type = Ieee8021ASV2PTPInstanceIdentifier
_Ieee8021AsV2PtpInstance_Object = MibTableColumn
ieee8021AsV2PtpInstance = _Ieee8021AsV2PtpInstance_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 1, 1, 1),
    _Ieee8021AsV2PtpInstance_Type()
)
ieee8021AsV2PtpInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstance.setStatus("current")


class _Ieee8021AsV2PtpInstanceName_Type(SnmpAdminString):
    """Custom type ieee8021AsV2PtpInstanceName based on SnmpAdminString"""
    defaultValue = OctetString("")


_Ieee8021AsV2PtpInstanceName_Type.__name__ = "SnmpAdminString"
_Ieee8021AsV2PtpInstanceName_Object = MibTableColumn
ieee8021AsV2PtpInstanceName = _Ieee8021AsV2PtpInstanceName_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 1, 1, 2),
    _Ieee8021AsV2PtpInstanceName_Type()
)
ieee8021AsV2PtpInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstanceName.setStatus("current")
_Ieee8021AsV2PtpInstanceRowStatus_Type = RowStatus
_Ieee8021AsV2PtpInstanceRowStatus_Object = MibTableColumn
ieee8021AsV2PtpInstanceRowStatus = _Ieee8021AsV2PtpInstanceRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 1, 1, 3),
    _Ieee8021AsV2PtpInstanceRowStatus_Type()
)
ieee8021AsV2PtpInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstanceRowStatus.setStatus("current")
_Ieee8021AsV2DefaultDSTable_Object = MibTable
ieee8021AsV2DefaultDSTable = _Ieee8021AsV2DefaultDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSTable.setStatus("current")
_Ieee8021AsV2DefaultDSEntry_Object = MibTableRow
ieee8021AsV2DefaultDSEntry = _Ieee8021AsV2DefaultDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1)
)
ieee8021AsV2DefaultDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSEntry.setStatus("current")
_Ieee8021AsV2DefaultDSClockIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2DefaultDSClockIdentity_Object = MibTableColumn
ieee8021AsV2DefaultDSClockIdentity = _Ieee8021AsV2DefaultDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 1),
    _Ieee8021AsV2DefaultDSClockIdentity_Type()
)
ieee8021AsV2DefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSClockIdentity.setStatus("current")


class _Ieee8021AsV2DefaultDSNumberPorts_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSNumberPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ieee8021AsV2DefaultDSNumberPorts_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSNumberPorts_Object = MibTableColumn
ieee8021AsV2DefaultDSNumberPorts = _Ieee8021AsV2DefaultDSNumberPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 2),
    _Ieee8021AsV2DefaultDSNumberPorts_Type()
)
ieee8021AsV2DefaultDSNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSNumberPorts.setStatus("current")
_Ieee8021AsV2DefaultDSClockQualityClockClass_Type = Ieee8021AsV2ClockClassValue
_Ieee8021AsV2DefaultDSClockQualityClockClass_Object = MibTableColumn
ieee8021AsV2DefaultDSClockQualityClockClass = _Ieee8021AsV2DefaultDSClockQualityClockClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 3),
    _Ieee8021AsV2DefaultDSClockQualityClockClass_Type()
)
ieee8021AsV2DefaultDSClockQualityClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSClockQualityClockClass.setStatus("current")
_Ieee8021AsV2DefaultDSClockQualityClockAccuracy_Type = Ieee8021AsV2ClockAccuracyValue
_Ieee8021AsV2DefaultDSClockQualityClockAccuracy_Object = MibTableColumn
ieee8021AsV2DefaultDSClockQualityClockAccuracy = _Ieee8021AsV2DefaultDSClockQualityClockAccuracy_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 4),
    _Ieee8021AsV2DefaultDSClockQualityClockAccuracy_Type()
)
ieee8021AsV2DefaultDSClockQualityClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSClockQualityClockAccuracy.setStatus("current")


class _Ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance_Object = MibTableColumn
ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance = _Ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 5),
    _Ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance_Type()
)
ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance.setStatus("current")


class _Ieee8021AsV2DefaultDSPriority1_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2DefaultDSPriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSPriority1_Object = MibTableColumn
ieee8021AsV2DefaultDSPriority1 = _Ieee8021AsV2DefaultDSPriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 6),
    _Ieee8021AsV2DefaultDSPriority1_Type()
)
ieee8021AsV2DefaultDSPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSPriority1.setStatus("current")


class _Ieee8021AsV2DefaultDSPriority2_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSPriority2 based on Unsigned32"""
    defaultValue = 248

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2DefaultDSPriority2_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSPriority2_Object = MibTableColumn
ieee8021AsV2DefaultDSPriority2 = _Ieee8021AsV2DefaultDSPriority2_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 7),
    _Ieee8021AsV2DefaultDSPriority2_Type()
)
ieee8021AsV2DefaultDSPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSPriority2.setStatus("current")
_Ieee8021AsV2DefaultDSGmCapable_Type = TruthValue
_Ieee8021AsV2DefaultDSGmCapable_Object = MibTableColumn
ieee8021AsV2DefaultDSGmCapable = _Ieee8021AsV2DefaultDSGmCapable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 8),
    _Ieee8021AsV2DefaultDSGmCapable_Type()
)
ieee8021AsV2DefaultDSGmCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSGmCapable.setStatus("current")


class _Ieee8021AsV2DefaultDSCurrentUtcOffset_Type(Integer32):
    """Custom type ieee8021AsV2DefaultDSCurrentUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Ieee8021AsV2DefaultDSCurrentUtcOffset_Type.__name__ = "Integer32"
_Ieee8021AsV2DefaultDSCurrentUtcOffset_Object = MibTableColumn
ieee8021AsV2DefaultDSCurrentUtcOffset = _Ieee8021AsV2DefaultDSCurrentUtcOffset_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 9),
    _Ieee8021AsV2DefaultDSCurrentUtcOffset_Type()
)
ieee8021AsV2DefaultDSCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSCurrentUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSCurrentUtcOffset.setUnits("seconds")
_Ieee8021AsV2DefaultDSCurrentUtcOffsetValid_Type = TruthValue
_Ieee8021AsV2DefaultDSCurrentUtcOffsetValid_Object = MibTableColumn
ieee8021AsV2DefaultDSCurrentUtcOffsetValid = _Ieee8021AsV2DefaultDSCurrentUtcOffsetValid_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 10),
    _Ieee8021AsV2DefaultDSCurrentUtcOffsetValid_Type()
)
ieee8021AsV2DefaultDSCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSCurrentUtcOffsetValid.setStatus("current")
_Ieee8021AsV2DefaultDSLeap59_Type = TruthValue
_Ieee8021AsV2DefaultDSLeap59_Object = MibTableColumn
ieee8021AsV2DefaultDSLeap59 = _Ieee8021AsV2DefaultDSLeap59_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 11),
    _Ieee8021AsV2DefaultDSLeap59_Type()
)
ieee8021AsV2DefaultDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSLeap59.setStatus("current")
_Ieee8021AsV2DefaultDSLeap61_Type = TruthValue
_Ieee8021AsV2DefaultDSLeap61_Object = MibTableColumn
ieee8021AsV2DefaultDSLeap61 = _Ieee8021AsV2DefaultDSLeap61_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 12),
    _Ieee8021AsV2DefaultDSLeap61_Type()
)
ieee8021AsV2DefaultDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSLeap61.setStatus("current")
_Ieee8021AsV2DefaultDSTimeTraceable_Type = TruthValue
_Ieee8021AsV2DefaultDSTimeTraceable_Object = MibTableColumn
ieee8021AsV2DefaultDSTimeTraceable = _Ieee8021AsV2DefaultDSTimeTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 13),
    _Ieee8021AsV2DefaultDSTimeTraceable_Type()
)
ieee8021AsV2DefaultDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSTimeTraceable.setStatus("current")
_Ieee8021AsV2DefaultDSFrequencyTraceable_Type = TruthValue
_Ieee8021AsV2DefaultDSFrequencyTraceable_Object = MibTableColumn
ieee8021AsV2DefaultDSFrequencyTraceable = _Ieee8021AsV2DefaultDSFrequencyTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 14),
    _Ieee8021AsV2DefaultDSFrequencyTraceable_Type()
)
ieee8021AsV2DefaultDSFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSFrequencyTraceable.setStatus("current")
_Ieee8021AsV2DefaultDSPtpTimescale_Type = TruthValue
_Ieee8021AsV2DefaultDSPtpTimescale_Object = MibTableColumn
ieee8021AsV2DefaultDSPtpTimescale = _Ieee8021AsV2DefaultDSPtpTimescale_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 15),
    _Ieee8021AsV2DefaultDSPtpTimescale_Type()
)
ieee8021AsV2DefaultDSPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSPtpTimescale.setStatus("current")
_Ieee8021AsV2DefaultDSTimeSource_Type = Ieee8021AsV2TimeSourceValue
_Ieee8021AsV2DefaultDSTimeSource_Object = MibTableColumn
ieee8021AsV2DefaultDSTimeSource = _Ieee8021AsV2DefaultDSTimeSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 16),
    _Ieee8021AsV2DefaultDSTimeSource_Type()
)
ieee8021AsV2DefaultDSTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSTimeSource.setStatus("current")


class _Ieee8021AsV2DefaultDSDomainNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSDomainNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ieee8021AsV2DefaultDSDomainNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSDomainNumber_Object = MibTableColumn
ieee8021AsV2DefaultDSDomainNumber = _Ieee8021AsV2DefaultDSDomainNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 17),
    _Ieee8021AsV2DefaultDSDomainNumber_Type()
)
ieee8021AsV2DefaultDSDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSDomainNumber.setStatus("current")


class _Ieee8021AsV2DefaultDSSdoId_Type(Unsigned32):
    """Custom type ieee8021AsV2DefaultDSSdoId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ieee8021AsV2DefaultDSSdoId_Type.__name__ = "Unsigned32"
_Ieee8021AsV2DefaultDSSdoId_Object = MibTableColumn
ieee8021AsV2DefaultDSSdoId = _Ieee8021AsV2DefaultDSSdoId_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 18),
    _Ieee8021AsV2DefaultDSSdoId_Type()
)
ieee8021AsV2DefaultDSSdoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSSdoId.setStatus("current")
_Ieee8021AsV2DefaultDSExternalPortConfigurationEnabled_Type = TruthValue
_Ieee8021AsV2DefaultDSExternalPortConfigurationEnabled_Object = MibTableColumn
ieee8021AsV2DefaultDSExternalPortConfigurationEnabled = _Ieee8021AsV2DefaultDSExternalPortConfigurationEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 19),
    _Ieee8021AsV2DefaultDSExternalPortConfigurationEnabled_Type()
)
ieee8021AsV2DefaultDSExternalPortConfigurationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSExternalPortConfigurationEnabled.setStatus("current")
_Ieee8021AsV2DefaultDSInstanceEnable_Type = TruthValue
_Ieee8021AsV2DefaultDSInstanceEnable_Object = MibTableColumn
ieee8021AsV2DefaultDSInstanceEnable = _Ieee8021AsV2DefaultDSInstanceEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 2, 1, 20),
    _Ieee8021AsV2DefaultDSInstanceEnable_Type()
)
ieee8021AsV2DefaultDSInstanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSInstanceEnable.setStatus("current")
_Ieee8021AsV2CurrentDSTable_Object = MibTable
ieee8021AsV2CurrentDSTable = _Ieee8021AsV2CurrentDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTable.setStatus("current")
_Ieee8021AsV2CurrentDSEntry_Object = MibTableRow
ieee8021AsV2CurrentDSEntry = _Ieee8021AsV2CurrentDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1)
)
ieee8021AsV2CurrentDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSEntry.setStatus("current")


class _Ieee8021AsV2CurrentDSStepsRemoved_Type(Unsigned32):
    """Custom type ieee8021AsV2CurrentDSStepsRemoved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2CurrentDSStepsRemoved_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CurrentDSStepsRemoved_Object = MibTableColumn
ieee8021AsV2CurrentDSStepsRemoved = _Ieee8021AsV2CurrentDSStepsRemoved_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 1),
    _Ieee8021AsV2CurrentDSStepsRemoved_Type()
)
ieee8021AsV2CurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSStepsRemoved.setStatus("current")
_Ieee8021AsV2CurrentDSOffsetFromMaster_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2CurrentDSOffsetFromMaster_Object = MibTableColumn
ieee8021AsV2CurrentDSOffsetFromMaster = _Ieee8021AsV2CurrentDSOffsetFromMaster_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 2),
    _Ieee8021AsV2CurrentDSOffsetFromMaster_Type()
)
ieee8021AsV2CurrentDSOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSOffsetFromMaster.setStatus("current")
_Ieee8021AsV2CurrentDSLastGmPhaseChange_Type = Ieee8021ASV2ScaledNs
_Ieee8021AsV2CurrentDSLastGmPhaseChange_Object = MibTableColumn
ieee8021AsV2CurrentDSLastGmPhaseChange = _Ieee8021AsV2CurrentDSLastGmPhaseChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 3),
    _Ieee8021AsV2CurrentDSLastGmPhaseChange_Type()
)
ieee8021AsV2CurrentDSLastGmPhaseChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSLastGmPhaseChange.setStatus("current")
_Ieee8021AsV2CurrentDSLastGmFreqChange_Type = Float64TC
_Ieee8021AsV2CurrentDSLastGmFreqChange_Object = MibTableColumn
ieee8021AsV2CurrentDSLastGmFreqChange = _Ieee8021AsV2CurrentDSLastGmFreqChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 4),
    _Ieee8021AsV2CurrentDSLastGmFreqChange_Type()
)
ieee8021AsV2CurrentDSLastGmFreqChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSLastGmFreqChange.setStatus("current")


class _Ieee8021AsV2CurrentDSGmTimebaseIndicator_Type(Unsigned32):
    """Custom type ieee8021AsV2CurrentDSGmTimebaseIndicator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2CurrentDSGmTimebaseIndicator_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CurrentDSGmTimebaseIndicator_Object = MibTableColumn
ieee8021AsV2CurrentDSGmTimebaseIndicator = _Ieee8021AsV2CurrentDSGmTimebaseIndicator_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 5),
    _Ieee8021AsV2CurrentDSGmTimebaseIndicator_Type()
)
ieee8021AsV2CurrentDSGmTimebaseIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSGmTimebaseIndicator.setStatus("current")
_Ieee8021AsV2CurrentDSGmChangeCount_Type = Counter32
_Ieee8021AsV2CurrentDSGmChangeCount_Object = MibTableColumn
ieee8021AsV2CurrentDSGmChangeCount = _Ieee8021AsV2CurrentDSGmChangeCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 6),
    _Ieee8021AsV2CurrentDSGmChangeCount_Type()
)
ieee8021AsV2CurrentDSGmChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSGmChangeCount.setStatus("current")
_Ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent_Type = TimeStamp
_Ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent_Object = MibTableColumn
ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent = _Ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 7),
    _Ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent_Type()
)
ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent_Type = TimeStamp
_Ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent_Object = MibTableColumn
ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent = _Ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 8),
    _Ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent_Type()
)
ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent_Type = TimeStamp
_Ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent_Object = MibTableColumn
ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent = _Ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 3, 1, 9),
    _Ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent_Type()
)
ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent.setUnits("0.01 seconds")
_Ieee8021AsV2ParentDSTable_Object = MibTable
ieee8021AsV2ParentDSTable = _Ieee8021AsV2ParentDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSTable.setStatus("current")
_Ieee8021AsV2ParentDSEntry_Object = MibTableRow
ieee8021AsV2ParentDSEntry = _Ieee8021AsV2ParentDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1)
)
ieee8021AsV2ParentDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSEntry.setStatus("current")
_Ieee8021AsV2ParentDSParentClockIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2ParentDSParentClockIdentity_Object = MibTableColumn
ieee8021AsV2ParentDSParentClockIdentity = _Ieee8021AsV2ParentDSParentClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 1),
    _Ieee8021AsV2ParentDSParentClockIdentity_Type()
)
ieee8021AsV2ParentDSParentClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSParentClockIdentity.setStatus("current")


class _Ieee8021AsV2ParentDSParentPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2ParentDSParentPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2ParentDSParentPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2ParentDSParentPortNumber_Object = MibTableColumn
ieee8021AsV2ParentDSParentPortNumber = _Ieee8021AsV2ParentDSParentPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 2),
    _Ieee8021AsV2ParentDSParentPortNumber_Type()
)
ieee8021AsV2ParentDSParentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSParentPortNumber.setStatus("current")
_Ieee8021AsV2ParentDSCumulativeRateRatio_Type = Integer32
_Ieee8021AsV2ParentDSCumulativeRateRatio_Object = MibTableColumn
ieee8021AsV2ParentDSCumulativeRateRatio = _Ieee8021AsV2ParentDSCumulativeRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 3),
    _Ieee8021AsV2ParentDSCumulativeRateRatio_Type()
)
ieee8021AsV2ParentDSCumulativeRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSCumulativeRateRatio.setStatus("current")
_Ieee8021AsV2ParentDSGrandmasterIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2ParentDSGrandmasterIdentity_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterIdentity = _Ieee8021AsV2ParentDSGrandmasterIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 4),
    _Ieee8021AsV2ParentDSGrandmasterIdentity_Type()
)
ieee8021AsV2ParentDSGrandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterIdentity.setStatus("current")
_Ieee8021AsV2ParentDSGrandmasterClockQualityclockClass_Type = Ieee8021AsV2ClockClassValue
_Ieee8021AsV2ParentDSGrandmasterClockQualityclockClass_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterClockQualityclockClass = _Ieee8021AsV2ParentDSGrandmasterClockQualityclockClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 5),
    _Ieee8021AsV2ParentDSGrandmasterClockQualityclockClass_Type()
)
ieee8021AsV2ParentDSGrandmasterClockQualityclockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterClockQualityclockClass.setStatus("current")
_Ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy_Type = Ieee8021AsV2ClockAccuracyValue
_Ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy = _Ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 6),
    _Ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy_Type()
)
ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy.setStatus("current")


class _Ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar_Type(Unsigned32):
    """Custom type ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar_Type.__name__ = "Unsigned32"
_Ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar = _Ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 7),
    _Ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar_Type()
)
ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar.setStatus("current")


class _Ieee8021AsV2ParentDSGrandmasterPriority1_Type(Unsigned32):
    """Custom type ieee8021AsV2ParentDSGrandmasterPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2ParentDSGrandmasterPriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsV2ParentDSGrandmasterPriority1_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterPriority1 = _Ieee8021AsV2ParentDSGrandmasterPriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 8),
    _Ieee8021AsV2ParentDSGrandmasterPriority1_Type()
)
ieee8021AsV2ParentDSGrandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterPriority1.setStatus("current")


class _Ieee8021AsV2ParentDSGrandmasterPriority2_Type(Unsigned32):
    """Custom type ieee8021AsV2ParentDSGrandmasterPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2ParentDSGrandmasterPriority2_Type.__name__ = "Unsigned32"
_Ieee8021AsV2ParentDSGrandmasterPriority2_Object = MibTableColumn
ieee8021AsV2ParentDSGrandmasterPriority2 = _Ieee8021AsV2ParentDSGrandmasterPriority2_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 4, 1, 9),
    _Ieee8021AsV2ParentDSGrandmasterPriority2_Type()
)
ieee8021AsV2ParentDSGrandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGrandmasterPriority2.setStatus("current")
_Ieee8021AsV2TimePropertiesDSTable_Object = MibTable
ieee8021AsV2TimePropertiesDSTable = _Ieee8021AsV2TimePropertiesDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSTable.setStatus("current")
_Ieee8021AsV2TimePropertiesDSEntry_Object = MibTableRow
ieee8021AsV2TimePropertiesDSEntry = _Ieee8021AsV2TimePropertiesDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1)
)
ieee8021AsV2TimePropertiesDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSEntry.setStatus("current")


class _Ieee8021AsV2TimePropertiesDSCurrentUtcOffset_Type(Integer32):
    """Custom type ieee8021AsV2TimePropertiesDSCurrentUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Ieee8021AsV2TimePropertiesDSCurrentUtcOffset_Type.__name__ = "Integer32"
_Ieee8021AsV2TimePropertiesDSCurrentUtcOffset_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSCurrentUtcOffset = _Ieee8021AsV2TimePropertiesDSCurrentUtcOffset_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 1),
    _Ieee8021AsV2TimePropertiesDSCurrentUtcOffset_Type()
)
ieee8021AsV2TimePropertiesDSCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSCurrentUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSCurrentUtcOffset.setUnits("seconds")
_Ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid = _Ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 2),
    _Ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid_Type()
)
ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid.setStatus("current")
_Ieee8021AsV2TimePropertiesDSLeap59_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSLeap59_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSLeap59 = _Ieee8021AsV2TimePropertiesDSLeap59_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 3),
    _Ieee8021AsV2TimePropertiesDSLeap59_Type()
)
ieee8021AsV2TimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSLeap59.setStatus("current")
_Ieee8021AsV2TimePropertiesDSLeap61_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSLeap61_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSLeap61 = _Ieee8021AsV2TimePropertiesDSLeap61_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 4),
    _Ieee8021AsV2TimePropertiesDSLeap61_Type()
)
ieee8021AsV2TimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSLeap61.setStatus("current")
_Ieee8021AsV2TimePropertiesDSTimeTraceable_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSTimeTraceable_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSTimeTraceable = _Ieee8021AsV2TimePropertiesDSTimeTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 5),
    _Ieee8021AsV2TimePropertiesDSTimeTraceable_Type()
)
ieee8021AsV2TimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSTimeTraceable.setStatus("current")
_Ieee8021AsV2TimePropertiesDSFrequencyTraceable_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSFrequencyTraceable_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSFrequencyTraceable = _Ieee8021AsV2TimePropertiesDSFrequencyTraceable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 6),
    _Ieee8021AsV2TimePropertiesDSFrequencyTraceable_Type()
)
ieee8021AsV2TimePropertiesDSFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSFrequencyTraceable.setStatus("current")
_Ieee8021AsV2TimePropertiesDSPtpTimescale_Type = TruthValue
_Ieee8021AsV2TimePropertiesDSPtpTimescale_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSPtpTimescale = _Ieee8021AsV2TimePropertiesDSPtpTimescale_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 7),
    _Ieee8021AsV2TimePropertiesDSPtpTimescale_Type()
)
ieee8021AsV2TimePropertiesDSPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSPtpTimescale.setStatus("current")
_Ieee8021AsV2TimePropertiesDSTimeSource_Type = Ieee8021AsV2TimeSourceValue
_Ieee8021AsV2TimePropertiesDSTimeSource_Object = MibTableColumn
ieee8021AsV2TimePropertiesDSTimeSource = _Ieee8021AsV2TimePropertiesDSTimeSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 5, 1, 8),
    _Ieee8021AsV2TimePropertiesDSTimeSource_Type()
)
ieee8021AsV2TimePropertiesDSTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSTimeSource.setStatus("current")
_Ieee8021AsV2PathTraceDSTable_Object = MibTable
ieee8021AsV2PathTraceDSTable = _Ieee8021AsV2PathTraceDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSTable.setStatus("current")
_Ieee8021AsV2PathTraceDSEntry_Object = MibTableRow
ieee8021AsV2PathTraceDSEntry = _Ieee8021AsV2PathTraceDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 6, 1)
)
ieee8021AsV2PathTraceDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSEntry.setStatus("current")
_Ieee8021AsV2PathTraceDSEnable_Type = TruthValue
_Ieee8021AsV2PathTraceDSEnable_Object = MibTableColumn
ieee8021AsV2PathTraceDSEnable = _Ieee8021AsV2PathTraceDSEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 6, 1, 2),
    _Ieee8021AsV2PathTraceDSEnable_Type()
)
ieee8021AsV2PathTraceDSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSEnable.setStatus("current")
_Ieee8021AsV2PathTraceDSArrayTable_Object = MibTable
ieee8021AsV2PathTraceDSArrayTable = _Ieee8021AsV2PathTraceDSArrayTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSArrayTable.setStatus("current")
_Ieee8021AsV2PathTraceDSArrayEntry_Object = MibTableRow
ieee8021AsV2PathTraceDSArrayEntry = _Ieee8021AsV2PathTraceDSArrayEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 7, 1)
)
ieee8021AsV2PathTraceDSArrayEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PathTraceDSArrayIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSArrayEntry.setStatus("current")


class _Ieee8021AsV2PathTraceDSArrayIndex_Type(Unsigned32):
    """Custom type ieee8021AsV2PathTraceDSArrayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 179),
    )


_Ieee8021AsV2PathTraceDSArrayIndex_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PathTraceDSArrayIndex_Object = MibTableColumn
ieee8021AsV2PathTraceDSArrayIndex = _Ieee8021AsV2PathTraceDSArrayIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 7, 1, 1),
    _Ieee8021AsV2PathTraceDSArrayIndex_Type()
)
ieee8021AsV2PathTraceDSArrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSArrayIndex.setStatus("current")
_Ieee8021AsV2PathTraceDSArrayList_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2PathTraceDSArrayList_Object = MibTableColumn
ieee8021AsV2PathTraceDSArrayList = _Ieee8021AsV2PathTraceDSArrayList_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 7, 1, 2),
    _Ieee8021AsV2PathTraceDSArrayList_Type()
)
ieee8021AsV2PathTraceDSArrayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSArrayList.setStatus("current")
_Ieee8021AsV2AcceptableMasterTableDSTable_Object = MibTable
ieee8021AsV2AcceptableMasterTableDSTable = _Ieee8021AsV2AcceptableMasterTableDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSTable.setStatus("current")
_Ieee8021AsV2AcceptableMasterTableDSEntry_Object = MibTableRow
ieee8021AsV2AcceptableMasterTableDSEntry = _Ieee8021AsV2AcceptableMasterTableDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 8, 1)
)
ieee8021AsV2AcceptableMasterTableDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSEntry.setStatus("current")


class _Ieee8021AsV2AcceptableMasterTableDSMaxTableSize_Type(Unsigned32):
    """Custom type ieee8021AsV2AcceptableMasterTableDSMaxTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2AcceptableMasterTableDSMaxTableSize_Type.__name__ = "Unsigned32"
_Ieee8021AsV2AcceptableMasterTableDSMaxTableSize_Object = MibTableColumn
ieee8021AsV2AcceptableMasterTableDSMaxTableSize = _Ieee8021AsV2AcceptableMasterTableDSMaxTableSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 8, 1, 1),
    _Ieee8021AsV2AcceptableMasterTableDSMaxTableSize_Type()
)
ieee8021AsV2AcceptableMasterTableDSMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSMaxTableSize.setStatus("current")


class _Ieee8021AsV2AcceptableMasterTableDSActualTableSize_Type(Unsigned32):
    """Custom type ieee8021AsV2AcceptableMasterTableDSActualTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2AcceptableMasterTableDSActualTableSize_Type.__name__ = "Unsigned32"
_Ieee8021AsV2AcceptableMasterTableDSActualTableSize_Object = MibTableColumn
ieee8021AsV2AcceptableMasterTableDSActualTableSize = _Ieee8021AsV2AcceptableMasterTableDSActualTableSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 8, 1, 2),
    _Ieee8021AsV2AcceptableMasterTableDSActualTableSize_Type()
)
ieee8021AsV2AcceptableMasterTableDSActualTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSActualTableSize.setStatus("current")
_Ieee8021AsV2AcceptableMasterTableDSArrayTable_Object = MibTable
ieee8021AsV2AcceptableMasterTableDSArrayTable = _Ieee8021AsV2AcceptableMasterTableDSArrayTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 9)
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayTable.setStatus("current")
_Ieee8021AsV2AcceptableMasterTableDSArrayEntry_Object = MibTableRow
ieee8021AsV2AcceptableMasterTableDSArrayEntry = _Ieee8021AsV2AcceptableMasterTableDSArrayEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 9, 1)
)
ieee8021AsV2AcceptableMasterTableDSArrayEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSArrayIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayEntry.setStatus("current")


class _Ieee8021AsV2AcceptableMasterTableDSArrayIndex_Type(Unsigned32):
    """Custom type ieee8021AsV2AcceptableMasterTableDSArrayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2AcceptableMasterTableDSArrayIndex_Type.__name__ = "Unsigned32"
_Ieee8021AsV2AcceptableMasterTableDSArrayIndex_Object = MibTableColumn
ieee8021AsV2AcceptableMasterTableDSArrayIndex = _Ieee8021AsV2AcceptableMasterTableDSArrayIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 9, 1, 1),
    _Ieee8021AsV2AcceptableMasterTableDSArrayIndex_Type()
)
ieee8021AsV2AcceptableMasterTableDSArrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayIndex.setStatus("current")
_Ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity_Type = Ieee8021ASV2PtpPortIdentity
_Ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity_Object = MibTableColumn
ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity = _Ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 9, 1, 2),
    _Ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity_Type()
)
ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity.setStatus("current")


class _Ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1_Type(Unsigned32):
    """Custom type ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1_Type.__name__ = "Unsigned32"
_Ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1_Object = MibTableColumn
ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1 = _Ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 9, 1, 3),
    _Ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1_Type()
)
ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1.setStatus("current")
_Ieee8021AsV2PortDSTable_Object = MibTable
ieee8021AsV2PortDSTable = _Ieee8021AsV2PortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSTable.setStatus("current")
_Ieee8021AsV2PortDSEntry_Object = MibTableRow
ieee8021AsV2PortDSEntry = _Ieee8021AsV2PortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1)
)
ieee8021AsV2PortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSEntry.setStatus("current")
_Ieee8021AsV2BridgeBasePort_Type = IEEE8021BridgePortNumber
_Ieee8021AsV2BridgeBasePort_Object = MibTableColumn
ieee8021AsV2BridgeBasePort = _Ieee8021AsV2BridgeBasePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 1),
    _Ieee8021AsV2BridgeBasePort_Type()
)
ieee8021AsV2BridgeBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2BridgeBasePort.setStatus("current")
_Ieee8021AsV2PortDSIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2PortDSIndex_Object = MibTableColumn
ieee8021AsV2PortDSIndex = _Ieee8021AsV2PortDSIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 2),
    _Ieee8021AsV2PortDSIndex_Type()
)
ieee8021AsV2PortDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSIndex.setStatus("current")
_Ieee8021AsV2PortDSClockIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2PortDSClockIdentity_Object = MibTableColumn
ieee8021AsV2PortDSClockIdentity = _Ieee8021AsV2PortDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 3),
    _Ieee8021AsV2PortDSClockIdentity_Type()
)
ieee8021AsV2PortDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSClockIdentity.setStatus("current")


class _Ieee8021AsV2PortDSPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2PortDSPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSPortNumber_Object = MibTableColumn
ieee8021AsV2PortDSPortNumber = _Ieee8021AsV2PortDSPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 4),
    _Ieee8021AsV2PortDSPortNumber_Type()
)
ieee8021AsV2PortDSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPortNumber.setStatus("current")


class _Ieee8021AsV2PortDSPortState_Type(Integer32):
    """Custom type ieee8021AsV2PortDSPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 3),
          ("masterPort", 6),
          ("passivePort", 7),
          ("slavePort", 9))
    )


_Ieee8021AsV2PortDSPortState_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSPortState_Object = MibTableColumn
ieee8021AsV2PortDSPortState = _Ieee8021AsV2PortDSPortState_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 5),
    _Ieee8021AsV2PortDSPortState_Type()
)
ieee8021AsV2PortDSPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPortState.setStatus("current")
_Ieee8021AsV2PortDSPtpPortEnabled_Type = TruthValue
_Ieee8021AsV2PortDSPtpPortEnabled_Object = MibTableColumn
ieee8021AsV2PortDSPtpPortEnabled = _Ieee8021AsV2PortDSPtpPortEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 6),
    _Ieee8021AsV2PortDSPtpPortEnabled_Type()
)
ieee8021AsV2PortDSPtpPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPtpPortEnabled.setStatus("current")


class _Ieee8021AsV2PortDSDelayMechanism_Type(Integer32):
    """Custom type ieee8021AsV2PortDSDelayMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 2),
          ("commonp2p", 3),
          ("special", 4))
    )


_Ieee8021AsV2PortDSDelayMechanism_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSDelayMechanism_Object = MibTableColumn
ieee8021AsV2PortDSDelayMechanism = _Ieee8021AsV2PortDSDelayMechanism_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 7),
    _Ieee8021AsV2PortDSDelayMechanism_Type()
)
ieee8021AsV2PortDSDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSDelayMechanism.setStatus("current")
_Ieee8021AsV2PortDSIsMeasuringDelay_Type = TruthValue
_Ieee8021AsV2PortDSIsMeasuringDelay_Object = MibTableColumn
ieee8021AsV2PortDSIsMeasuringDelay = _Ieee8021AsV2PortDSIsMeasuringDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 8),
    _Ieee8021AsV2PortDSIsMeasuringDelay_Type()
)
ieee8021AsV2PortDSIsMeasuringDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSIsMeasuringDelay.setStatus("current")
_Ieee8021AsV2PortDSAsCapable_Type = TruthValue
_Ieee8021AsV2PortDSAsCapable_Object = MibTableColumn
ieee8021AsV2PortDSAsCapable = _Ieee8021AsV2PortDSAsCapable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 9),
    _Ieee8021AsV2PortDSAsCapable_Type()
)
ieee8021AsV2PortDSAsCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSAsCapable.setStatus("current")
_Ieee8021AsV2PortDSMeanLinkDelay_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2PortDSMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2PortDSMeanLinkDelay = _Ieee8021AsV2PortDSMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 10),
    _Ieee8021AsV2PortDSMeanLinkDelay_Type()
)
ieee8021AsV2PortDSMeanLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMeanLinkDelay.setStatus("current")
_Ieee8021AsV2PortDSMeanLinkDelayThresh_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2PortDSMeanLinkDelayThresh_Object = MibTableColumn
ieee8021AsV2PortDSMeanLinkDelayThresh = _Ieee8021AsV2PortDSMeanLinkDelayThresh_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 11),
    _Ieee8021AsV2PortDSMeanLinkDelayThresh_Type()
)
ieee8021AsV2PortDSMeanLinkDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMeanLinkDelayThresh.setStatus("current")
_Ieee8021AsV2PortDSDelayAsym_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2PortDSDelayAsym_Object = MibTableColumn
ieee8021AsV2PortDSDelayAsym = _Ieee8021AsV2PortDSDelayAsym_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 12),
    _Ieee8021AsV2PortDSDelayAsym_Type()
)
ieee8021AsV2PortDSDelayAsym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSDelayAsym.setStatus("current")
_Ieee8021AsV2PortDSNbrRateRatio_Type = Integer32
_Ieee8021AsV2PortDSNbrRateRatio_Object = MibTableColumn
ieee8021AsV2PortDSNbrRateRatio = _Ieee8021AsV2PortDSNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 13),
    _Ieee8021AsV2PortDSNbrRateRatio_Type()
)
ieee8021AsV2PortDSNbrRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSNbrRateRatio.setStatus("current")


class _Ieee8021AsV2PortDSInitialLogAnnounceInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSInitialLogAnnounceInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSInitialLogAnnounceInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSInitialLogAnnounceInterval_Object = MibTableColumn
ieee8021AsV2PortDSInitialLogAnnounceInterval = _Ieee8021AsV2PortDSInitialLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 14),
    _Ieee8021AsV2PortDSInitialLogAnnounceInterval_Type()
)
ieee8021AsV2PortDSInitialLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialLogAnnounceInterval.setStatus("current")


class _Ieee8021AsV2PortDSCurrentLogAnnounceInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSCurrentLogAnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSCurrentLogAnnounceInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSCurrentLogAnnounceInterval_Object = MibTableColumn
ieee8021AsV2PortDSCurrentLogAnnounceInterval = _Ieee8021AsV2PortDSCurrentLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 15),
    _Ieee8021AsV2PortDSCurrentLogAnnounceInterval_Type()
)
ieee8021AsV2PortDSCurrentLogAnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentLogAnnounceInterval.setStatus("current")
_Ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval_Type = TruthValue
_Ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval = _Ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 16),
    _Ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval_Type()
)
ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval.setStatus("current")


class _Ieee8021AsV2PortDSMgtSettableLogAnnounceInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSMgtSettableLogAnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSMgtSettableLogAnnounceInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSMgtSettableLogAnnounceInterval_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableLogAnnounceInterval = _Ieee8021AsV2PortDSMgtSettableLogAnnounceInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 17),
    _Ieee8021AsV2PortDSMgtSettableLogAnnounceInterval_Type()
)
ieee8021AsV2PortDSMgtSettableLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableLogAnnounceInterval.setStatus("current")


class _Ieee8021AsV2PortDSAnnounceReceiptTimeout_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSAnnounceReceiptTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2PortDSAnnounceReceiptTimeout_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSAnnounceReceiptTimeout_Object = MibTableColumn
ieee8021AsV2PortDSAnnounceReceiptTimeout = _Ieee8021AsV2PortDSAnnounceReceiptTimeout_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 18),
    _Ieee8021AsV2PortDSAnnounceReceiptTimeout_Type()
)
ieee8021AsV2PortDSAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSAnnounceReceiptTimeout.setStatus("current")


class _Ieee8021AsV2PortDSInitialLogSyncInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSInitialLogSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSInitialLogSyncInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSInitialLogSyncInterval_Object = MibTableColumn
ieee8021AsV2PortDSInitialLogSyncInterval = _Ieee8021AsV2PortDSInitialLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 19),
    _Ieee8021AsV2PortDSInitialLogSyncInterval_Type()
)
ieee8021AsV2PortDSInitialLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialLogSyncInterval.setStatus("current")


class _Ieee8021AsV2PortDSCurrentLogSyncInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSCurrentLogSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSCurrentLogSyncInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSCurrentLogSyncInterval_Object = MibTableColumn
ieee8021AsV2PortDSCurrentLogSyncInterval = _Ieee8021AsV2PortDSCurrentLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 20),
    _Ieee8021AsV2PortDSCurrentLogSyncInterval_Type()
)
ieee8021AsV2PortDSCurrentLogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentLogSyncInterval.setStatus("current")
_Ieee8021AsV2PortDSUseMgtSettableLogSyncInterval_Type = TruthValue
_Ieee8021AsV2PortDSUseMgtSettableLogSyncInterval_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableLogSyncInterval = _Ieee8021AsV2PortDSUseMgtSettableLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 21),
    _Ieee8021AsV2PortDSUseMgtSettableLogSyncInterval_Type()
)
ieee8021AsV2PortDSUseMgtSettableLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableLogSyncInterval.setStatus("current")


class _Ieee8021AsV2PortDSMgtSettableLogSyncInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSMgtSettableLogSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSMgtSettableLogSyncInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSMgtSettableLogSyncInterval_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableLogSyncInterval = _Ieee8021AsV2PortDSMgtSettableLogSyncInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 22),
    _Ieee8021AsV2PortDSMgtSettableLogSyncInterval_Type()
)
ieee8021AsV2PortDSMgtSettableLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableLogSyncInterval.setStatus("current")


class _Ieee8021AsV2PortDSSyncReceiptTimeout_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSSyncReceiptTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021AsV2PortDSSyncReceiptTimeout_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSSyncReceiptTimeout_Object = MibTableColumn
ieee8021AsV2PortDSSyncReceiptTimeout = _Ieee8021AsV2PortDSSyncReceiptTimeout_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 23),
    _Ieee8021AsV2PortDSSyncReceiptTimeout_Type()
)
ieee8021AsV2PortDSSyncReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSSyncReceiptTimeout.setStatus("current")
_Ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval_Type = Ieee8021ASV2UScaledNs
_Ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval_Object = MibTableColumn
ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval = _Ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 24),
    _Ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval_Type()
)
ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval.setUnits("2**-16 ns")


class _Ieee8021AsV2PortDSInitialLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSInitialLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSInitialLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSInitialLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2PortDSInitialLogPdelayReqInterval = _Ieee8021AsV2PortDSInitialLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 25),
    _Ieee8021AsV2PortDSInitialLogPdelayReqInterval_Type()
)
ieee8021AsV2PortDSInitialLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2PortDSCurrentLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSCurrentLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSCurrentLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSCurrentLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2PortDSCurrentLogPdelayReqInterval = _Ieee8021AsV2PortDSCurrentLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 26),
    _Ieee8021AsV2PortDSCurrentLogPdelayReqInterval_Type()
)
ieee8021AsV2PortDSCurrentLogPdelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval = _Ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 27),
    _Ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval_Type()
)
ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval = _Ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 28),
    _Ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval_Type()
)
ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval_Object = MibTableColumn
ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval = _Ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 29),
    _Ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval_Type()
)
ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval.setStatus("current")


class _Ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval_Object = MibTableColumn
ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval = _Ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 30),
    _Ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval_Type()
)
ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval.setStatus("current")


class _Ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval = _Ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 31),
    _Ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval_Type()
)
ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval.setStatus("current")


class _Ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval_Type(Integer32):
    """Custom type ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval = _Ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 32),
    _Ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval_Type()
)
ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval.setStatus("current")
_Ieee8021AsV2PortDSInitialComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2PortDSInitialComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2PortDSInitialComputeNbrRateRatio = _Ieee8021AsV2PortDSInitialComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 33),
    _Ieee8021AsV2PortDSInitialComputeNbrRateRatio_Type()
)
ieee8021AsV2PortDSInitialComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2PortDSCurrentComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2PortDSCurrentComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2PortDSCurrentComputeNbrRateRatio = _Ieee8021AsV2PortDSCurrentComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 34),
    _Ieee8021AsV2PortDSCurrentComputeNbrRateRatio_Type()
)
ieee8021AsV2PortDSCurrentComputeNbrRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentComputeNbrRateRatio.setStatus("current")


class _Ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio = _Ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 35),
    _Ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio_Type()
)
ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio = _Ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 36),
    _Ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio_Type()
)
ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2PortDSInitialComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2PortDSInitialComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2PortDSInitialComputeMeanLinkDelay = _Ieee8021AsV2PortDSInitialComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 37),
    _Ieee8021AsV2PortDSInitialComputeMeanLinkDelay_Type()
)
ieee8021AsV2PortDSInitialComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialComputeMeanLinkDelay.setStatus("current")
_Ieee8021AsV2PortDSCurrentComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2PortDSCurrentComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2PortDSCurrentComputeMeanLinkDelay = _Ieee8021AsV2PortDSCurrentComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 38),
    _Ieee8021AsV2PortDSCurrentComputeMeanLinkDelay_Type()
)
ieee8021AsV2PortDSCurrentComputeMeanLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentComputeMeanLinkDelay.setStatus("current")


class _Ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay = _Ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 39),
    _Ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay_Type()
)
ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay.setStatus("current")
_Ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay = _Ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 40),
    _Ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay_Type()
)
ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay.setStatus("current")


class _Ieee8021AsV2PortDSAllowedLostRsp_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSAllowedLostRsp based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ieee8021AsV2PortDSAllowedLostRsp_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSAllowedLostRsp_Object = MibTableColumn
ieee8021AsV2PortDSAllowedLostRsp = _Ieee8021AsV2PortDSAllowedLostRsp_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 41),
    _Ieee8021AsV2PortDSAllowedLostRsp_Type()
)
ieee8021AsV2PortDSAllowedLostRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSAllowedLostRsp.setStatus("current")


class _Ieee8021AsV2PortDSAllowedFaults_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSAllowedFaults based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ieee8021AsV2PortDSAllowedFaults_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSAllowedFaults_Object = MibTableColumn
ieee8021AsV2PortDSAllowedFaults = _Ieee8021AsV2PortDSAllowedFaults_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 42),
    _Ieee8021AsV2PortDSAllowedFaults_Type()
)
ieee8021AsV2PortDSAllowedFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSAllowedFaults.setStatus("current")


class _Ieee8021AsV2PortDSGPtpCapableReceiptTimeout_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSGPtpCapableReceiptTimeout based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ieee8021AsV2PortDSGPtpCapableReceiptTimeout_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSGPtpCapableReceiptTimeout_Object = MibTableColumn
ieee8021AsV2PortDSGPtpCapableReceiptTimeout = _Ieee8021AsV2PortDSGPtpCapableReceiptTimeout_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 43),
    _Ieee8021AsV2PortDSGPtpCapableReceiptTimeout_Type()
)
ieee8021AsV2PortDSGPtpCapableReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSGPtpCapableReceiptTimeout.setStatus("current")


class _Ieee8021AsV2PortDSVersionNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSVersionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ieee8021AsV2PortDSVersionNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSVersionNumber_Object = MibTableColumn
ieee8021AsV2PortDSVersionNumber = _Ieee8021AsV2PortDSVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 44),
    _Ieee8021AsV2PortDSVersionNumber_Type()
)
ieee8021AsV2PortDSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSVersionNumber.setStatus("current")
_Ieee8021AsV2PortDSNup_Type = Float64TC
_Ieee8021AsV2PortDSNup_Object = MibTableColumn
ieee8021AsV2PortDSNup = _Ieee8021AsV2PortDSNup_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 45),
    _Ieee8021AsV2PortDSNup_Type()
)
ieee8021AsV2PortDSNup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSNup.setStatus("current")
_Ieee8021AsV2PortDSNdown_Type = Float64TC
_Ieee8021AsV2PortDSNdown_Object = MibTableColumn
ieee8021AsV2PortDSNdown = _Ieee8021AsV2PortDSNdown_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 46),
    _Ieee8021AsV2PortDSNdown_Type()
)
ieee8021AsV2PortDSNdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSNdown.setStatus("current")
_Ieee8021AsV2PortDSOneStepTxOper_Type = TruthValue
_Ieee8021AsV2PortDSOneStepTxOper_Object = MibTableColumn
ieee8021AsV2PortDSOneStepTxOper = _Ieee8021AsV2PortDSOneStepTxOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 47),
    _Ieee8021AsV2PortDSOneStepTxOper_Type()
)
ieee8021AsV2PortDSOneStepTxOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSOneStepTxOper.setStatus("current")
_Ieee8021AsV2PortDSOneStepReceive_Type = TruthValue
_Ieee8021AsV2PortDSOneStepReceive_Object = MibTableColumn
ieee8021AsV2PortDSOneStepReceive = _Ieee8021AsV2PortDSOneStepReceive_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 48),
    _Ieee8021AsV2PortDSOneStepReceive_Type()
)
ieee8021AsV2PortDSOneStepReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSOneStepReceive.setStatus("current")
_Ieee8021AsV2PortDSOneStepTransmit_Type = TruthValue
_Ieee8021AsV2PortDSOneStepTransmit_Object = MibTableColumn
ieee8021AsV2PortDSOneStepTransmit = _Ieee8021AsV2PortDSOneStepTransmit_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 49),
    _Ieee8021AsV2PortDSOneStepTransmit_Type()
)
ieee8021AsV2PortDSOneStepTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSOneStepTransmit.setStatus("current")


class _Ieee8021AsV2PortDSInitialOneStepTxOper_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSInitialOneStepTxOper based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2PortDSInitialOneStepTxOper_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSInitialOneStepTxOper_Object = MibTableColumn
ieee8021AsV2PortDSInitialOneStepTxOper = _Ieee8021AsV2PortDSInitialOneStepTxOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 50),
    _Ieee8021AsV2PortDSInitialOneStepTxOper_Type()
)
ieee8021AsV2PortDSInitialOneStepTxOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSInitialOneStepTxOper.setStatus("current")
_Ieee8021AsV2PortDSCurrentOneStepTxOper_Type = TruthValue
_Ieee8021AsV2PortDSCurrentOneStepTxOper_Object = MibTableColumn
ieee8021AsV2PortDSCurrentOneStepTxOper = _Ieee8021AsV2PortDSCurrentOneStepTxOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 51),
    _Ieee8021AsV2PortDSCurrentOneStepTxOper_Type()
)
ieee8021AsV2PortDSCurrentOneStepTxOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSCurrentOneStepTxOper.setStatus("current")


class _Ieee8021AsV2PortDSUseMgtSettableOneStepTxOper_Type(TruthValue):
    """Custom type ieee8021AsV2PortDSUseMgtSettableOneStepTxOper based on TruthValue"""
    defaultValue = 1


_Ieee8021AsV2PortDSUseMgtSettableOneStepTxOper_Type.__name__ = "TruthValue"
_Ieee8021AsV2PortDSUseMgtSettableOneStepTxOper_Object = MibTableColumn
ieee8021AsV2PortDSUseMgtSettableOneStepTxOper = _Ieee8021AsV2PortDSUseMgtSettableOneStepTxOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 52),
    _Ieee8021AsV2PortDSUseMgtSettableOneStepTxOper_Type()
)
ieee8021AsV2PortDSUseMgtSettableOneStepTxOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSUseMgtSettableOneStepTxOper.setStatus("current")
_Ieee8021AsV2PortDSMgtSettableOneStepTxOper_Type = TruthValue
_Ieee8021AsV2PortDSMgtSettableOneStepTxOper_Object = MibTableColumn
ieee8021AsV2PortDSMgtSettableOneStepTxOper = _Ieee8021AsV2PortDSMgtSettableOneStepTxOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 53),
    _Ieee8021AsV2PortDSMgtSettableOneStepTxOper_Type()
)
ieee8021AsV2PortDSMgtSettableOneStepTxOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMgtSettableOneStepTxOper.setStatus("current")
_Ieee8021AsV2PortDSSyncLocked_Type = TruthValue
_Ieee8021AsV2PortDSSyncLocked_Object = MibTableColumn
ieee8021AsV2PortDSSyncLocked = _Ieee8021AsV2PortDSSyncLocked_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 54),
    _Ieee8021AsV2PortDSSyncLocked_Type()
)
ieee8021AsV2PortDSSyncLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSSyncLocked.setStatus("current")
_Ieee8021AsV2PortDSPdelayTruncTST1_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2PortDSPdelayTruncTST1_Object = MibTableColumn
ieee8021AsV2PortDSPdelayTruncTST1 = _Ieee8021AsV2PortDSPdelayTruncTST1_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 55),
    _Ieee8021AsV2PortDSPdelayTruncTST1_Type()
)
ieee8021AsV2PortDSPdelayTruncTST1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPdelayTruncTST1.setStatus("current")
_Ieee8021AsV2PortDSPdelayTruncTST2_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2PortDSPdelayTruncTST2_Object = MibTableColumn
ieee8021AsV2PortDSPdelayTruncTST2 = _Ieee8021AsV2PortDSPdelayTruncTST2_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 56),
    _Ieee8021AsV2PortDSPdelayTruncTST2_Type()
)
ieee8021AsV2PortDSPdelayTruncTST2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPdelayTruncTST2.setStatus("current")
_Ieee8021AsV2PortDSPdelayTruncTST3_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2PortDSPdelayTruncTST3_Object = MibTableColumn
ieee8021AsV2PortDSPdelayTruncTST3 = _Ieee8021AsV2PortDSPdelayTruncTST3_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 57),
    _Ieee8021AsV2PortDSPdelayTruncTST3_Type()
)
ieee8021AsV2PortDSPdelayTruncTST3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPdelayTruncTST3.setStatus("current")
_Ieee8021AsV2PortDSPdelayTruncTST4_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2PortDSPdelayTruncTST4_Object = MibTableColumn
ieee8021AsV2PortDSPdelayTruncTST4 = _Ieee8021AsV2PortDSPdelayTruncTST4_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 58),
    _Ieee8021AsV2PortDSPdelayTruncTST4_Type()
)
ieee8021AsV2PortDSPdelayTruncTST4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSPdelayTruncTST4.setStatus("current")


class _Ieee8021AsV2PortDSMinorVersionNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2PortDSMinorVersionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021AsV2PortDSMinorVersionNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2PortDSMinorVersionNumber_Object = MibTableColumn
ieee8021AsV2PortDSMinorVersionNumber = _Ieee8021AsV2PortDSMinorVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 10, 1, 59),
    _Ieee8021AsV2PortDSMinorVersionNumber_Type()
)
ieee8021AsV2PortDSMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSMinorVersionNumber.setStatus("current")
_Ieee8021AsV2DescriptionPortDSTable_Object = MibTable
ieee8021AsV2DescriptionPortDSTable = _Ieee8021AsV2DescriptionPortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 11)
)
if mibBuilder.loadTexts:
    ieee8021AsV2DescriptionPortDSTable.setStatus("current")
_Ieee8021AsV2DescriptionPortDSEntry_Object = MibTableRow
ieee8021AsV2DescriptionPortDSEntry = _Ieee8021AsV2DescriptionPortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 11, 1)
)
ieee8021AsV2DescriptionPortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2DescriptionPortDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2DescriptionPortDSEntry.setStatus("current")
_Ieee8021AsV2DescriptionPortDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2DescriptionPortDSAsIndex_Object = MibTableColumn
ieee8021AsV2DescriptionPortDSAsIndex = _Ieee8021AsV2DescriptionPortDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 11, 1, 1),
    _Ieee8021AsV2DescriptionPortDSAsIndex_Type()
)
ieee8021AsV2DescriptionPortDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2DescriptionPortDSAsIndex.setStatus("current")
_Ieee8021AsV2DescriptionPortDSProfileIdentifier_Type = Ieee8021AsV2GPtpProfileIdentifier
_Ieee8021AsV2DescriptionPortDSProfileIdentifier_Object = MibTableColumn
ieee8021AsV2DescriptionPortDSProfileIdentifier = _Ieee8021AsV2DescriptionPortDSProfileIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 11, 1, 2),
    _Ieee8021AsV2DescriptionPortDSProfileIdentifier_Type()
)
ieee8021AsV2DescriptionPortDSProfileIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2DescriptionPortDSProfileIdentifier.setStatus("current")
_Ieee8021AsV2PortStatDSTable_Object = MibTable
ieee8021AsV2PortStatDSTable = _Ieee8021AsV2PortStatDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12)
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatDSTable.setStatus("current")
_Ieee8021AsV2PortStatDSEntry_Object = MibTableRow
ieee8021AsV2PortStatDSEntry = _Ieee8021AsV2PortStatDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1)
)
ieee8021AsV2PortStatDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatDSEntry.setStatus("current")
_Ieee8021AsV2PortStatRxSyncCount_Type = Counter32
_Ieee8021AsV2PortStatRxSyncCount_Object = MibTableColumn
ieee8021AsV2PortStatRxSyncCount = _Ieee8021AsV2PortStatRxSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 1),
    _Ieee8021AsV2PortStatRxSyncCount_Type()
)
ieee8021AsV2PortStatRxSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxSyncCount.setStatus("current")
_Ieee8021AsV2PortStatRxOneStepSyncCount_Type = Counter32
_Ieee8021AsV2PortStatRxOneStepSyncCount_Object = MibTableColumn
ieee8021AsV2PortStatRxOneStepSyncCount = _Ieee8021AsV2PortStatRxOneStepSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 2),
    _Ieee8021AsV2PortStatRxOneStepSyncCount_Type()
)
ieee8021AsV2PortStatRxOneStepSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxOneStepSyncCount.setStatus("current")
_Ieee8021AsV2PortStatRxFollowUpCount_Type = Counter32
_Ieee8021AsV2PortStatRxFollowUpCount_Object = MibTableColumn
ieee8021AsV2PortStatRxFollowUpCount = _Ieee8021AsV2PortStatRxFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 3),
    _Ieee8021AsV2PortStatRxFollowUpCount_Type()
)
ieee8021AsV2PortStatRxFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxFollowUpCount.setStatus("current")
_Ieee8021AsV2PortStatRxPdelayRequestCount_Type = Counter32
_Ieee8021AsV2PortStatRxPdelayRequestCount_Object = MibTableColumn
ieee8021AsV2PortStatRxPdelayRequestCount = _Ieee8021AsV2PortStatRxPdelayRequestCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 4),
    _Ieee8021AsV2PortStatRxPdelayRequestCount_Type()
)
ieee8021AsV2PortStatRxPdelayRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxPdelayRequestCount.setStatus("current")
_Ieee8021AsV2PortStatRxPdelayRspCount_Type = Counter32
_Ieee8021AsV2PortStatRxPdelayRspCount_Object = MibTableColumn
ieee8021AsV2PortStatRxPdelayRspCount = _Ieee8021AsV2PortStatRxPdelayRspCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 5),
    _Ieee8021AsV2PortStatRxPdelayRspCount_Type()
)
ieee8021AsV2PortStatRxPdelayRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxPdelayRspCount.setStatus("current")
_Ieee8021AsV2PortStatRxPdelayRspFollowUpCount_Type = Counter32
_Ieee8021AsV2PortStatRxPdelayRspFollowUpCount_Object = MibTableColumn
ieee8021AsV2PortStatRxPdelayRspFollowUpCount = _Ieee8021AsV2PortStatRxPdelayRspFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 6),
    _Ieee8021AsV2PortStatRxPdelayRspFollowUpCount_Type()
)
ieee8021AsV2PortStatRxPdelayRspFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxPdelayRspFollowUpCount.setStatus("current")
_Ieee8021AsV2PortStatRxAnnounceCount_Type = Counter32
_Ieee8021AsV2PortStatRxAnnounceCount_Object = MibTableColumn
ieee8021AsV2PortStatRxAnnounceCount = _Ieee8021AsV2PortStatRxAnnounceCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 7),
    _Ieee8021AsV2PortStatRxAnnounceCount_Type()
)
ieee8021AsV2PortStatRxAnnounceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxAnnounceCount.setStatus("current")
_Ieee8021AsV2PortStatRxPtpPacketDiscardCount_Type = Counter32
_Ieee8021AsV2PortStatRxPtpPacketDiscardCount_Object = MibTableColumn
ieee8021AsV2PortStatRxPtpPacketDiscardCount = _Ieee8021AsV2PortStatRxPtpPacketDiscardCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 8),
    _Ieee8021AsV2PortStatRxPtpPacketDiscardCount_Type()
)
ieee8021AsV2PortStatRxPtpPacketDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatRxPtpPacketDiscardCount.setStatus("current")
_Ieee8021AsV2PortStatSyncReceiptTimeoutCount_Type = Counter32
_Ieee8021AsV2PortStatSyncReceiptTimeoutCount_Object = MibTableColumn
ieee8021AsV2PortStatSyncReceiptTimeoutCount = _Ieee8021AsV2PortStatSyncReceiptTimeoutCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 9),
    _Ieee8021AsV2PortStatSyncReceiptTimeoutCount_Type()
)
ieee8021AsV2PortStatSyncReceiptTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatSyncReceiptTimeoutCount.setStatus("current")
_Ieee8021AsV2PortStatAnnounceReceiptTimeoutCount_Type = Counter32
_Ieee8021AsV2PortStatAnnounceReceiptTimeoutCount_Object = MibTableColumn
ieee8021AsV2PortStatAnnounceReceiptTimeoutCount = _Ieee8021AsV2PortStatAnnounceReceiptTimeoutCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 10),
    _Ieee8021AsV2PortStatAnnounceReceiptTimeoutCount_Type()
)
ieee8021AsV2PortStatAnnounceReceiptTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatAnnounceReceiptTimeoutCount.setStatus("current")
_Ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount_Type = Counter32
_Ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount_Object = MibTableColumn
ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount = _Ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 11),
    _Ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount_Type()
)
ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount.setStatus("current")
_Ieee8021AsV2PortStatTxSyncCount_Type = Counter32
_Ieee8021AsV2PortStatTxSyncCount_Object = MibTableColumn
ieee8021AsV2PortStatTxSyncCount = _Ieee8021AsV2PortStatTxSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 12),
    _Ieee8021AsV2PortStatTxSyncCount_Type()
)
ieee8021AsV2PortStatTxSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxSyncCount.setStatus("current")
_Ieee8021AsV2PortStatTxOneStepSyncCount_Type = Counter32
_Ieee8021AsV2PortStatTxOneStepSyncCount_Object = MibTableColumn
ieee8021AsV2PortStatTxOneStepSyncCount = _Ieee8021AsV2PortStatTxOneStepSyncCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 13),
    _Ieee8021AsV2PortStatTxOneStepSyncCount_Type()
)
ieee8021AsV2PortStatTxOneStepSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxOneStepSyncCount.setStatus("current")
_Ieee8021AsV2PortStatTxFollowUpCount_Type = Counter32
_Ieee8021AsV2PortStatTxFollowUpCount_Object = MibTableColumn
ieee8021AsV2PortStatTxFollowUpCount = _Ieee8021AsV2PortStatTxFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 14),
    _Ieee8021AsV2PortStatTxFollowUpCount_Type()
)
ieee8021AsV2PortStatTxFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxFollowUpCount.setStatus("current")
_Ieee8021AsV2PortStatTxPdelayRequestCount_Type = Counter32
_Ieee8021AsV2PortStatTxPdelayRequestCount_Object = MibTableColumn
ieee8021AsV2PortStatTxPdelayRequestCount = _Ieee8021AsV2PortStatTxPdelayRequestCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 15),
    _Ieee8021AsV2PortStatTxPdelayRequestCount_Type()
)
ieee8021AsV2PortStatTxPdelayRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxPdelayRequestCount.setStatus("current")
_Ieee8021AsV2PortStatTxPdelayRspCount_Type = Counter32
_Ieee8021AsV2PortStatTxPdelayRspCount_Object = MibTableColumn
ieee8021AsV2PortStatTxPdelayRspCount = _Ieee8021AsV2PortStatTxPdelayRspCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 16),
    _Ieee8021AsV2PortStatTxPdelayRspCount_Type()
)
ieee8021AsV2PortStatTxPdelayRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxPdelayRspCount.setStatus("current")
_Ieee8021AsV2PortStatTxPdelayRspFollowUpCount_Type = Counter32
_Ieee8021AsV2PortStatTxPdelayRspFollowUpCount_Object = MibTableColumn
ieee8021AsV2PortStatTxPdelayRspFollowUpCount = _Ieee8021AsV2PortStatTxPdelayRspFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 17),
    _Ieee8021AsV2PortStatTxPdelayRspFollowUpCount_Type()
)
ieee8021AsV2PortStatTxPdelayRspFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxPdelayRspFollowUpCount.setStatus("current")
_Ieee8021AsV2PortStatTxAnnounceCount_Type = Counter32
_Ieee8021AsV2PortStatTxAnnounceCount_Object = MibTableColumn
ieee8021AsV2PortStatTxAnnounceCount = _Ieee8021AsV2PortStatTxAnnounceCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 12, 1, 18),
    _Ieee8021AsV2PortStatTxAnnounceCount_Type()
)
ieee8021AsV2PortStatTxAnnounceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatTxAnnounceCount.setStatus("current")
_Ieee8021AsV2AcceptableMasterPortDSTable_Object = MibTable
ieee8021AsV2AcceptableMasterPortDSTable = _Ieee8021AsV2AcceptableMasterPortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 13)
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterPortDSTable.setStatus("current")
_Ieee8021AsV2AcceptableMasterPortDSEntry_Object = MibTableRow
ieee8021AsV2AcceptableMasterPortDSEntry = _Ieee8021AsV2AcceptableMasterPortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 13, 1)
)
ieee8021AsV2AcceptableMasterPortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterPortDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterPortDSEntry.setStatus("current")
_Ieee8021AsV2AcceptableMasterPortDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2AcceptableMasterPortDSAsIndex_Object = MibTableColumn
ieee8021AsV2AcceptableMasterPortDSAsIndex = _Ieee8021AsV2AcceptableMasterPortDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 13, 1, 1),
    _Ieee8021AsV2AcceptableMasterPortDSAsIndex_Type()
)
ieee8021AsV2AcceptableMasterPortDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterPortDSAsIndex.setStatus("current")
_Ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled_Type = TruthValue
_Ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled_Object = MibTableColumn
ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled = _Ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 13, 1, 2),
    _Ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled_Type()
)
ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled.setStatus("current")
_Ieee8021AsV2ExternalPortConfigurationPortDSTable_Object = MibTable
ieee8021AsV2ExternalPortConfigurationPortDSTable = _Ieee8021AsV2ExternalPortConfigurationPortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 14)
)
if mibBuilder.loadTexts:
    ieee8021AsV2ExternalPortConfigurationPortDSTable.setStatus("current")
_Ieee8021AsV2ExternalPortConfigurationPortDSEntry_Object = MibTableRow
ieee8021AsV2ExternalPortConfigurationPortDSEntry = _Ieee8021AsV2ExternalPortConfigurationPortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 14, 1)
)
ieee8021AsV2ExternalPortConfigurationPortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2ExternalPortConfigurationPortDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2ExternalPortConfigurationPortDSEntry.setStatus("current")
_Ieee8021AsV2ExternalPortConfigurationPortDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2ExternalPortConfigurationPortDSAsIndex_Object = MibTableColumn
ieee8021AsV2ExternalPortConfigurationPortDSAsIndex = _Ieee8021AsV2ExternalPortConfigurationPortDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 14, 1, 1),
    _Ieee8021AsV2ExternalPortConfigurationPortDSAsIndex_Type()
)
ieee8021AsV2ExternalPortConfigurationPortDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2ExternalPortConfigurationPortDSAsIndex.setStatus("current")


class _Ieee8021AsV2ExternalPortConfigurationPortDSDesiredState_Type(Integer32):
    """Custom type ieee8021AsV2ExternalPortConfigurationPortDSDesiredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 3),
          ("masterPort", 6),
          ("passivePort", 7),
          ("slavePort", 9))
    )


_Ieee8021AsV2ExternalPortConfigurationPortDSDesiredState_Type.__name__ = "Integer32"
_Ieee8021AsV2ExternalPortConfigurationPortDSDesiredState_Object = MibTableColumn
ieee8021AsV2ExternalPortConfigurationPortDSDesiredState = _Ieee8021AsV2ExternalPortConfigurationPortDSDesiredState_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 14, 1, 2),
    _Ieee8021AsV2ExternalPortConfigurationPortDSDesiredState_Type()
)
ieee8021AsV2ExternalPortConfigurationPortDSDesiredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2ExternalPortConfigurationPortDSDesiredState.setStatus("current")
_Ieee8021AsV2AsymMeasurementModeDSTable_Object = MibTable
ieee8021AsV2AsymMeasurementModeDSTable = _Ieee8021AsV2AsymMeasurementModeDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 15)
)
if mibBuilder.loadTexts:
    ieee8021AsV2AsymMeasurementModeDSTable.setStatus("current")
_Ieee8021AsV2AsymMeasurementModeDSEntry_Object = MibTableRow
ieee8021AsV2AsymMeasurementModeDSEntry = _Ieee8021AsV2AsymMeasurementModeDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 15, 1)
)
ieee8021AsV2AsymMeasurementModeDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2AsymMeasurementModeDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2AsymMeasurementModeDSEntry.setStatus("current")
_Ieee8021AsV2AsymMeasurementModeDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2AsymMeasurementModeDSAsIndex_Object = MibTableColumn
ieee8021AsV2AsymMeasurementModeDSAsIndex = _Ieee8021AsV2AsymMeasurementModeDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 15, 1, 1),
    _Ieee8021AsV2AsymMeasurementModeDSAsIndex_Type()
)
ieee8021AsV2AsymMeasurementModeDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2AsymMeasurementModeDSAsIndex.setStatus("current")
_Ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode_Type = TruthValue
_Ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode_Object = MibTableColumn
ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode = _Ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 15, 1, 2),
    _Ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode_Type()
)
ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode.setStatus("current")
_Ieee8021AsV2CommonServicesPortDSTable_Object = MibTable
ieee8021AsV2CommonServicesPortDSTable = _Ieee8021AsV2CommonServicesPortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 16)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonServicesPortDSTable.setStatus("current")
_Ieee8021AsV2CommonServicesPortDSEntry_Object = MibTableRow
ieee8021AsV2CommonServicesPortDSEntry = _Ieee8021AsV2CommonServicesPortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 16, 1)
)
ieee8021AsV2CommonServicesPortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstance"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonServicesPortDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonServicesPortDSEntry.setStatus("current")
_Ieee8021AsV2CommonServicesPortDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2CommonServicesPortDSAsIndex_Object = MibTableColumn
ieee8021AsV2CommonServicesPortDSAsIndex = _Ieee8021AsV2CommonServicesPortDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 16, 1, 1),
    _Ieee8021AsV2CommonServicesPortDSAsIndex_Type()
)
ieee8021AsV2CommonServicesPortDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2CommonServicesPortDSAsIndex.setStatus("current")


class _Ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber_Object = MibTableColumn
ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber = _Ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 16, 1, 2),
    _Ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber_Type()
)
ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable_Object = MibTable
ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable = _Ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 17)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry_Object = MibTableRow
ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry = _Ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 17, 1)
)
ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsDefaultDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry.setStatus("current")
_Ieee8021AsV2CmldsDefaultDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2CmldsDefaultDSAsIndex_Object = MibTableColumn
ieee8021AsV2CmldsDefaultDSAsIndex = _Ieee8021AsV2CmldsDefaultDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 17, 1, 1),
    _Ieee8021AsV2CmldsDefaultDSAsIndex_Type()
)
ieee8021AsV2CmldsDefaultDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsDefaultDSAsIndex.setStatus("current")
_Ieee8021AsV2CmldsDefaultDSClockIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2CmldsDefaultDSClockIdentity_Object = MibTableColumn
ieee8021AsV2CmldsDefaultDSClockIdentity = _Ieee8021AsV2CmldsDefaultDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 17, 1, 2),
    _Ieee8021AsV2CmldsDefaultDSClockIdentity_Type()
)
ieee8021AsV2CmldsDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsDefaultDSClockIdentity.setStatus("current")


class _Ieee8021AsV2CmldsDefaultDSNumberLinkPorts_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsDefaultDSNumberLinkPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2CmldsDefaultDSNumberLinkPorts_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsDefaultDSNumberLinkPorts_Object = MibTableColumn
ieee8021AsV2CmldsDefaultDSNumberLinkPorts = _Ieee8021AsV2CmldsDefaultDSNumberLinkPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 17, 1, 3),
    _Ieee8021AsV2CmldsDefaultDSNumberLinkPorts_Type()
)
ieee8021AsV2CmldsDefaultDSNumberLinkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsDefaultDSNumberLinkPorts.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable_Object = MibTable
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable = _Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry_Object = MibTableRow
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry = _Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1)
)
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2BridgeBasePort"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2CmldsLinkPortDSAsIndex_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSAsIndex = _Ieee8021AsV2CmldsLinkPortDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 1),
    _Ieee8021AsV2CmldsLinkPortDSAsIndex_Type()
)
ieee8021AsV2CmldsLinkPortDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSAsIndex.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSClockIdentity_Type = Ieee8021AsV2ClockIdentity
_Ieee8021AsV2CmldsLinkPortDSClockIdentity_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSClockIdentity = _Ieee8021AsV2CmldsLinkPortDSClockIdentity_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 2),
    _Ieee8021AsV2CmldsLinkPortDSClockIdentity_Type()
)
ieee8021AsV2CmldsLinkPortDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSClockIdentity.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSPortNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsLinkPortDSPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AsV2CmldsLinkPortDSPortNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsLinkPortDSPortNumber_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSPortNumber = _Ieee8021AsV2CmldsLinkPortDSPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 3),
    _Ieee8021AsV2CmldsLinkPortDSPortNumber_Type()
)
ieee8021AsV2CmldsLinkPortDSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSPortNumber.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled = _Ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 4),
    _Ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled_Type()
)
ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay = _Ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 5),
    _Ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains = _Ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 6),
    _Ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains_Type()
)
ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSMeanLinkDelay_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2CmldsLinkPortDSMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMeanLinkDelay = _Ieee8021AsV2CmldsLinkPortDSMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 7),
    _Ieee8021AsV2CmldsLinkPortDSMeanLinkDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSMeanLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMeanLinkDelay.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh = _Ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 8),
    _Ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh_Type()
)
ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSDelayAsym_Type = Ieee8021ASV2PtpTimeInterval
_Ieee8021AsV2CmldsLinkPortDSDelayAsym_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSDelayAsym = _Ieee8021AsV2CmldsLinkPortDSDelayAsym_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 9),
    _Ieee8021AsV2CmldsLinkPortDSDelayAsym_Type()
)
ieee8021AsV2CmldsLinkPortDSDelayAsym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSDelayAsym.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSNbrRateRatio_Type = Integer32
_Ieee8021AsV2CmldsLinkPortDSNbrRateRatio_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSNbrRateRatio = _Ieee8021AsV2CmldsLinkPortDSNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 10),
    _Ieee8021AsV2CmldsLinkPortDSNbrRateRatio_Type()
)
ieee8021AsV2CmldsLinkPortDSNbrRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSNbrRateRatio.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval = _Ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 11),
    _Ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval_Type()
)
ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval = _Ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 12),
    _Ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval_Type()
)
ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval_Type(TruthValue):
    """Custom type ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval_Type.__name__ = "TruthValue"
_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval = _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 13),
    _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval_Type()
)
ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval_Type(Integer32):
    """Custom type ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval_Type.__name__ = "Integer32"
_Ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval = _Ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 14),
    _Ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval_Type()
)
ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio = _Ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 15),
    _Ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio_Type()
)
ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio = _Ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 16),
    _Ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio_Type()
)
ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio_Type(TruthValue):
    """Custom type ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio_Type.__name__ = "TruthValue"
_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio = _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 17),
    _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio_Type()
)
ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio = _Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 18),
    _Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio_Type()
)
ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay = _Ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 19),
    _Ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay = _Ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 20),
    _Ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay_Type(TruthValue):
    """Custom type ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay based on TruthValue"""
    defaultValue = 2


_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay_Type.__name__ = "TruthValue"
_Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay = _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 21),
    _Ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay_Type = TruthValue
_Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay = _Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 22),
    _Ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay_Type()
)
ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSAllowedLostRsp_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsLinkPortDSAllowedLostRsp based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ieee8021AsV2CmldsLinkPortDSAllowedLostRsp_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsLinkPortDSAllowedLostRsp_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSAllowedLostRsp = _Ieee8021AsV2CmldsLinkPortDSAllowedLostRsp_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 23),
    _Ieee8021AsV2CmldsLinkPortDSAllowedLostRsp_Type()
)
ieee8021AsV2CmldsLinkPortDSAllowedLostRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSAllowedLostRsp.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSAllowedFaults_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsLinkPortDSAllowedFaults based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ieee8021AsV2CmldsLinkPortDSAllowedFaults_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsLinkPortDSAllowedFaults_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSAllowedFaults = _Ieee8021AsV2CmldsLinkPortDSAllowedFaults_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 24),
    _Ieee8021AsV2CmldsLinkPortDSAllowedFaults_Type()
)
ieee8021AsV2CmldsLinkPortDSAllowedFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSAllowedFaults.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSVersionNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsLinkPortDSVersionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021AsV2CmldsLinkPortDSVersionNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsLinkPortDSVersionNumber_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSVersionNumber = _Ieee8021AsV2CmldsLinkPortDSVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 25),
    _Ieee8021AsV2CmldsLinkPortDSVersionNumber_Type()
)
ieee8021AsV2CmldsLinkPortDSVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSVersionNumber.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1 = _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 26),
    _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1_Type()
)
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2 = _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 27),
    _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2_Type()
)
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3 = _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 28),
    _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3_Type()
)
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3.setStatus("current")
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4_Type = Ieee8021ASV2Timestamp
_Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4 = _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 29),
    _Ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4_Type()
)
ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4.setStatus("current")


class _Ieee8021AsV2CmldsLinkPortDSMinorVersionNumber_Type(Unsigned32):
    """Custom type ieee8021AsV2CmldsLinkPortDSMinorVersionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021AsV2CmldsLinkPortDSMinorVersionNumber_Type.__name__ = "Unsigned32"
_Ieee8021AsV2CmldsLinkPortDSMinorVersionNumber_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortDSMinorVersionNumber = _Ieee8021AsV2CmldsLinkPortDSMinorVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 18, 1, 30),
    _Ieee8021AsV2CmldsLinkPortDSMinorVersionNumber_Type()
)
ieee8021AsV2CmldsLinkPortDSMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortDSMinorVersionNumber.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable_Object = MibTable
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable = _Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry_Object = MibTableRow
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry = _Ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1)
)
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2BridgeBasePort"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2CmldsLinkPortStatDSIndex_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSIndex = _Ieee8021AsV2CmldsLinkPortStatDSIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 1),
    _Ieee8021AsV2CmldsLinkPortStatDSIndex_Type()
)
ieee8021AsV2CmldsLinkPortStatDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSIndex.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount = _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 2),
    _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount = _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 3),
    _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount = _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 4),
    _Ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount = _Ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 5),
    _Ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount = _Ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 6),
    _Ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount = _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 7),
    _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount = _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 8),
    _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount.setStatus("current")
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount_Type = Counter32
_Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount_Object = MibTableColumn
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount = _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 19, 1, 9),
    _Ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount_Type()
)
ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable_Object = MibTable
ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable = _Ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 20)
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable.setStatus("current")
_Ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry_Object = MibTableRow
ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry = _Ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 20, 1)
)
ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry.setIndexNames(
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2BridgeBasePort"),
    (0, "IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry.setStatus("current")
_Ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex_Type = InterfaceIndexOrZero
_Ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex_Object = MibTableColumn
ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex = _Ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 20, 1, 1),
    _Ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex_Type()
)
ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex.setStatus("current")
_Ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode_Type = TruthValue
_Ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode_Object = MibTableColumn
ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode = _Ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 33, 1, 20, 1, 2),
    _Ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode_Type()
)
ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode.setStatus("current")
_Ieee8021AsV2Conformance_ObjectIdentity = ObjectIdentity
ieee8021AsV2Conformance = _Ieee8021AsV2Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 33, 2)
)
_Ieee8021AsV2Groups_ObjectIdentity = ObjectIdentity
ieee8021AsV2Groups = _Ieee8021AsV2Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1)
)
_Ieee8021AsV2Compliances_ObjectIdentity = ObjectIdentity
ieee8021AsV2Compliances = _Ieee8021AsV2Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 2)
)

# Managed Objects groups

ieee8021AsV2PtpInstanceGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 1)
)
ieee8021AsV2PtpInstanceGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstanceName"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2PtpInstanceGroup.setStatus("current")

ieee8021AsV2DefaultDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 2)
)
ieee8021AsV2DefaultDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSClockIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSNumberPorts"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSClockQualityClockClass"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSClockQualityClockAccuracy"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSPriority1"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSPriority2"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSGmCapable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSCurrentUtcOffset"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSCurrentUtcOffsetValid"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSLeap59"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSLeap61"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSTimeTraceable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSFrequencyTraceable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSPtpTimescale"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSTimeSource"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSDomainNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSSdoId"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSExternalPortConfigurationEnabled"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSInstanceEnable"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2DefaultDSGroup.setStatus("current")

ieee8021AsV2CurrentDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 3)
)
ieee8021AsV2CurrentDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSStepsRemoved"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSOffsetFromMaster"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSLastGmPhaseChange"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSLastGmFreqChange"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSGmTimebaseIndicator"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSGmChangeCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2CurrentDSGroup.setStatus("current")

ieee8021AsV2ParentDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 4)
)
ieee8021AsV2ParentDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSParentClockIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSParentPortNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSCumulativeRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterClockQualityclockClass"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterPriority1"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGrandmasterPriority2"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2ParentDSGroup.setStatus("current")

ieee8021AsV2TimePropertiesDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 5)
)
ieee8021AsV2TimePropertiesDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSCurrentUtcOffset"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSLeap59"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSLeap61"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSTimeTraceable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSFrequencyTraceable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSPtpTimescale"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSTimeSource"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2TimePropertiesDSGroup.setStatus("current")

ieee8021AsV2PathTraceDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 6)
)
ieee8021AsV2PathTraceDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PathTraceDSEnable")
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSGroup.setStatus("current")

ieee8021AsV2PathTraceDSArrayTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 7)
)
ieee8021AsV2PathTraceDSArrayTableGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PathTraceDSArrayList")
)
if mibBuilder.loadTexts:
    ieee8021AsV2PathTraceDSArrayTableGroup.setStatus("current")

ieee8021AsV2AcceptableMasterTableDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 8)
)
ieee8021AsV2AcceptableMasterTableDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSMaxTableSize"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSActualTableSize"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSGroup.setStatus("current")

ieee8021AsV2AcceptableMasterTableDSArrayGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 9)
)
ieee8021AsV2AcceptableMasterTableDSArrayGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterTableDSArrayGroup.setStatus("current")

ieee8021AsV2PortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 10)
)
ieee8021AsV2PortDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSClockIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPortNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPortState"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPtpPortEnabled"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSDelayMechanism"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSIsMeasuringDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSAsCapable"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMeanLinkDelayThresh"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSDelayAsym"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialLogAnnounceInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentLogAnnounceInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableLogAnnounceInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSAnnounceReceiptTimeout"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialLogSyncInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentLogSyncInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableLogSyncInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableLogSyncInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSSyncReceiptTimeout"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSAllowedLostRsp"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSAllowedFaults"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSGPtpCapableReceiptTimeout"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSVersionNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSNup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSNdown"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSOneStepTxOper"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSOneStepReceive"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSOneStepTransmit"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSInitialOneStepTxOper"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSCurrentOneStepTxOper"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSUseMgtSettableOneStepTxOper"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMgtSettableOneStepTxOper"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSSyncLocked"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPdelayTruncTST1"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPdelayTruncTST2"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPdelayTruncTST3"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSPdelayTruncTST4"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSMinorVersionNumber"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortDSGroup.setStatus("current")

ieee8021AsV2DescriptionPortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 11)
)
ieee8021AsV2DescriptionPortDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DescriptionPortDSProfileIdentifier")
)
if mibBuilder.loadTexts:
    ieee8021AsV2DescriptionPortDSGroup.setStatus("current")

ieee8021AsV2PortStatIfGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 12)
)
ieee8021AsV2PortStatIfGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxSyncCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxOneStepSyncCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxFollowUpCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxPdelayRequestCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxPdelayRspCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxPdelayRspFollowUpCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxAnnounceCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatRxPtpPacketDiscardCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatSyncReceiptTimeoutCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatAnnounceReceiptTimeoutCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxSyncCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxOneStepSyncCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxFollowUpCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxPdelayRequestCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxPdelayRspCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxPdelayRspFollowUpCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatTxAnnounceCount"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2PortStatIfGroup.setStatus("current")

ieee8021AsV2AcceptableMasterPortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 13)
)
ieee8021AsV2AcceptableMasterPortDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled")
)
if mibBuilder.loadTexts:
    ieee8021AsV2AcceptableMasterPortDSGroup.setStatus("current")

ieee8021AsV2ExternalPortConfigurationPortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 14)
)
ieee8021AsV2ExternalPortConfigurationPortDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ExternalPortConfigurationPortDSDesiredState")
)
if mibBuilder.loadTexts:
    ieee8021AsV2ExternalPortConfigurationPortDSGroup.setStatus("current")

ieee8021AsV2AsymMeasurementModeDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 15)
)
ieee8021AsV2AsymMeasurementModeDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode")
)
if mibBuilder.loadTexts:
    ieee8021AsV2AsymMeasurementModeDSGroup.setStatus("current")

ieee8021AsV2CommonServicesPortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 16)
)
ieee8021AsV2CommonServicesPortDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber")
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonServicesPortDSGroup.setStatus("current")

ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 17)
)
ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsDefaultDSClockIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsDefaultDSNumberLinkPorts"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup.setStatus("current")

ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 18)
)
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSClockIdentity"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSPortNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSDelayAsym"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSAllowedLostRsp"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSAllowedFaults"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSVersionNumber"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortDSMinorVersionNumber"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup.setStatus("current")

ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 19)
)
ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup.setStatus("current")

ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 1, 20)
)
ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup.setObjects(
    ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode")
)
if mibBuilder.loadTexts:
    ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021AsV2Compliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 33, 2, 2, 1)
)
ieee8021AsV2Compliance.setObjects(
      *(("IEEE8021-AS-V2-MIB", "ieee8021AsV2PtpInstanceGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DefaultDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CurrentDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ParentDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2TimePropertiesDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PathTraceDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PathTraceDSArrayTableGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterTableDSArrayGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2DescriptionPortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2PortStatIfGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AcceptableMasterPortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2ExternalPortConfigurationPortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2AsymMeasurementModeDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonServicesPortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup"),
        ("IEEE8021-AS-V2-MIB", "ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup"))
)
if mibBuilder.loadTexts:
    ieee8021AsV2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-AS-V2-MIB",
    **{"Ieee8021AsV2ClockIdentity": Ieee8021AsV2ClockIdentity,
       "Ieee8021AsV2GPtpProfileIdentifier": Ieee8021AsV2GPtpProfileIdentifier,
       "Ieee8021AsV2ClockClassValue": Ieee8021AsV2ClockClassValue,
       "Ieee8021AsV2ClockAccuracyValue": Ieee8021AsV2ClockAccuracyValue,
       "Ieee8021AsV2TimeSourceValue": Ieee8021AsV2TimeSourceValue,
       "Ieee8021ASV2PtpTimeInterval": Ieee8021ASV2PtpTimeInterval,
       "Ieee8021ASV2PtpPortIdentity": Ieee8021ASV2PtpPortIdentity,
       "Ieee8021ASV2ScaledNs": Ieee8021ASV2ScaledNs,
       "Ieee8021ASV2UScaledNs": Ieee8021ASV2UScaledNs,
       "Ieee8021ASV2PTPInstanceIdentifier": Ieee8021ASV2PTPInstanceIdentifier,
       "Ieee8021ASV2Timestamp": Ieee8021ASV2Timestamp,
       "ieee8021AsV2TimeSyncMib": ieee8021AsV2TimeSyncMib,
       "ieee8021AsV2MIBObjects": ieee8021AsV2MIBObjects,
       "ieee8021AsV2PtpInstanceTable": ieee8021AsV2PtpInstanceTable,
       "ieee8021AsV2PtpInstanceEntry": ieee8021AsV2PtpInstanceEntry,
       "ieee8021AsV2PtpInstance": ieee8021AsV2PtpInstance,
       "ieee8021AsV2PtpInstanceName": ieee8021AsV2PtpInstanceName,
       "ieee8021AsV2PtpInstanceRowStatus": ieee8021AsV2PtpInstanceRowStatus,
       "ieee8021AsV2DefaultDSTable": ieee8021AsV2DefaultDSTable,
       "ieee8021AsV2DefaultDSEntry": ieee8021AsV2DefaultDSEntry,
       "ieee8021AsV2DefaultDSClockIdentity": ieee8021AsV2DefaultDSClockIdentity,
       "ieee8021AsV2DefaultDSNumberPorts": ieee8021AsV2DefaultDSNumberPorts,
       "ieee8021AsV2DefaultDSClockQualityClockClass": ieee8021AsV2DefaultDSClockQualityClockClass,
       "ieee8021AsV2DefaultDSClockQualityClockAccuracy": ieee8021AsV2DefaultDSClockQualityClockAccuracy,
       "ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance": ieee8021AsV2DefaultDSClockQualityOffsetScaledLogVariance,
       "ieee8021AsV2DefaultDSPriority1": ieee8021AsV2DefaultDSPriority1,
       "ieee8021AsV2DefaultDSPriority2": ieee8021AsV2DefaultDSPriority2,
       "ieee8021AsV2DefaultDSGmCapable": ieee8021AsV2DefaultDSGmCapable,
       "ieee8021AsV2DefaultDSCurrentUtcOffset": ieee8021AsV2DefaultDSCurrentUtcOffset,
       "ieee8021AsV2DefaultDSCurrentUtcOffsetValid": ieee8021AsV2DefaultDSCurrentUtcOffsetValid,
       "ieee8021AsV2DefaultDSLeap59": ieee8021AsV2DefaultDSLeap59,
       "ieee8021AsV2DefaultDSLeap61": ieee8021AsV2DefaultDSLeap61,
       "ieee8021AsV2DefaultDSTimeTraceable": ieee8021AsV2DefaultDSTimeTraceable,
       "ieee8021AsV2DefaultDSFrequencyTraceable": ieee8021AsV2DefaultDSFrequencyTraceable,
       "ieee8021AsV2DefaultDSPtpTimescale": ieee8021AsV2DefaultDSPtpTimescale,
       "ieee8021AsV2DefaultDSTimeSource": ieee8021AsV2DefaultDSTimeSource,
       "ieee8021AsV2DefaultDSDomainNumber": ieee8021AsV2DefaultDSDomainNumber,
       "ieee8021AsV2DefaultDSSdoId": ieee8021AsV2DefaultDSSdoId,
       "ieee8021AsV2DefaultDSExternalPortConfigurationEnabled": ieee8021AsV2DefaultDSExternalPortConfigurationEnabled,
       "ieee8021AsV2DefaultDSInstanceEnable": ieee8021AsV2DefaultDSInstanceEnable,
       "ieee8021AsV2CurrentDSTable": ieee8021AsV2CurrentDSTable,
       "ieee8021AsV2CurrentDSEntry": ieee8021AsV2CurrentDSEntry,
       "ieee8021AsV2CurrentDSStepsRemoved": ieee8021AsV2CurrentDSStepsRemoved,
       "ieee8021AsV2CurrentDSOffsetFromMaster": ieee8021AsV2CurrentDSOffsetFromMaster,
       "ieee8021AsV2CurrentDSLastGmPhaseChange": ieee8021AsV2CurrentDSLastGmPhaseChange,
       "ieee8021AsV2CurrentDSLastGmFreqChange": ieee8021AsV2CurrentDSLastGmFreqChange,
       "ieee8021AsV2CurrentDSGmTimebaseIndicator": ieee8021AsV2CurrentDSGmTimebaseIndicator,
       "ieee8021AsV2CurrentDSGmChangeCount": ieee8021AsV2CurrentDSGmChangeCount,
       "ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent": ieee8021AsV2CurrentDSTimeOfLastGmChangeEvent,
       "ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent": ieee8021AsV2CurrentDSTimeOfLastGmPhaseChangeEvent,
       "ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent": ieee8021AsV2CurrentDSTimeOfLastGmFreqChangeEvent,
       "ieee8021AsV2ParentDSTable": ieee8021AsV2ParentDSTable,
       "ieee8021AsV2ParentDSEntry": ieee8021AsV2ParentDSEntry,
       "ieee8021AsV2ParentDSParentClockIdentity": ieee8021AsV2ParentDSParentClockIdentity,
       "ieee8021AsV2ParentDSParentPortNumber": ieee8021AsV2ParentDSParentPortNumber,
       "ieee8021AsV2ParentDSCumulativeRateRatio": ieee8021AsV2ParentDSCumulativeRateRatio,
       "ieee8021AsV2ParentDSGrandmasterIdentity": ieee8021AsV2ParentDSGrandmasterIdentity,
       "ieee8021AsV2ParentDSGrandmasterClockQualityclockClass": ieee8021AsV2ParentDSGrandmasterClockQualityclockClass,
       "ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy": ieee8021AsV2ParentDSGrandmasterClockQualityclockAccuracy,
       "ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar": ieee8021AsV2ParentDSGrandmasterClockQualityoffsetScaledLogVar,
       "ieee8021AsV2ParentDSGrandmasterPriority1": ieee8021AsV2ParentDSGrandmasterPriority1,
       "ieee8021AsV2ParentDSGrandmasterPriority2": ieee8021AsV2ParentDSGrandmasterPriority2,
       "ieee8021AsV2TimePropertiesDSTable": ieee8021AsV2TimePropertiesDSTable,
       "ieee8021AsV2TimePropertiesDSEntry": ieee8021AsV2TimePropertiesDSEntry,
       "ieee8021AsV2TimePropertiesDSCurrentUtcOffset": ieee8021AsV2TimePropertiesDSCurrentUtcOffset,
       "ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid": ieee8021AsV2TimePropertiesDSCurrentUtcOffsetValid,
       "ieee8021AsV2TimePropertiesDSLeap59": ieee8021AsV2TimePropertiesDSLeap59,
       "ieee8021AsV2TimePropertiesDSLeap61": ieee8021AsV2TimePropertiesDSLeap61,
       "ieee8021AsV2TimePropertiesDSTimeTraceable": ieee8021AsV2TimePropertiesDSTimeTraceable,
       "ieee8021AsV2TimePropertiesDSFrequencyTraceable": ieee8021AsV2TimePropertiesDSFrequencyTraceable,
       "ieee8021AsV2TimePropertiesDSPtpTimescale": ieee8021AsV2TimePropertiesDSPtpTimescale,
       "ieee8021AsV2TimePropertiesDSTimeSource": ieee8021AsV2TimePropertiesDSTimeSource,
       "ieee8021AsV2PathTraceDSTable": ieee8021AsV2PathTraceDSTable,
       "ieee8021AsV2PathTraceDSEntry": ieee8021AsV2PathTraceDSEntry,
       "ieee8021AsV2PathTraceDSEnable": ieee8021AsV2PathTraceDSEnable,
       "ieee8021AsV2PathTraceDSArrayTable": ieee8021AsV2PathTraceDSArrayTable,
       "ieee8021AsV2PathTraceDSArrayEntry": ieee8021AsV2PathTraceDSArrayEntry,
       "ieee8021AsV2PathTraceDSArrayIndex": ieee8021AsV2PathTraceDSArrayIndex,
       "ieee8021AsV2PathTraceDSArrayList": ieee8021AsV2PathTraceDSArrayList,
       "ieee8021AsV2AcceptableMasterTableDSTable": ieee8021AsV2AcceptableMasterTableDSTable,
       "ieee8021AsV2AcceptableMasterTableDSEntry": ieee8021AsV2AcceptableMasterTableDSEntry,
       "ieee8021AsV2AcceptableMasterTableDSMaxTableSize": ieee8021AsV2AcceptableMasterTableDSMaxTableSize,
       "ieee8021AsV2AcceptableMasterTableDSActualTableSize": ieee8021AsV2AcceptableMasterTableDSActualTableSize,
       "ieee8021AsV2AcceptableMasterTableDSArrayTable": ieee8021AsV2AcceptableMasterTableDSArrayTable,
       "ieee8021AsV2AcceptableMasterTableDSArrayEntry": ieee8021AsV2AcceptableMasterTableDSArrayEntry,
       "ieee8021AsV2AcceptableMasterTableDSArrayIndex": ieee8021AsV2AcceptableMasterTableDSArrayIndex,
       "ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity": ieee8021AsV2AcceptableMasterTableDSArrayPortIdentity,
       "ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1": ieee8021AsV2AcceptableMasterTableDSArrayAlternatePriority1,
       "ieee8021AsV2PortDSTable": ieee8021AsV2PortDSTable,
       "ieee8021AsV2PortDSEntry": ieee8021AsV2PortDSEntry,
       "ieee8021AsV2BridgeBasePort": ieee8021AsV2BridgeBasePort,
       "ieee8021AsV2PortDSIndex": ieee8021AsV2PortDSIndex,
       "ieee8021AsV2PortDSClockIdentity": ieee8021AsV2PortDSClockIdentity,
       "ieee8021AsV2PortDSPortNumber": ieee8021AsV2PortDSPortNumber,
       "ieee8021AsV2PortDSPortState": ieee8021AsV2PortDSPortState,
       "ieee8021AsV2PortDSPtpPortEnabled": ieee8021AsV2PortDSPtpPortEnabled,
       "ieee8021AsV2PortDSDelayMechanism": ieee8021AsV2PortDSDelayMechanism,
       "ieee8021AsV2PortDSIsMeasuringDelay": ieee8021AsV2PortDSIsMeasuringDelay,
       "ieee8021AsV2PortDSAsCapable": ieee8021AsV2PortDSAsCapable,
       "ieee8021AsV2PortDSMeanLinkDelay": ieee8021AsV2PortDSMeanLinkDelay,
       "ieee8021AsV2PortDSMeanLinkDelayThresh": ieee8021AsV2PortDSMeanLinkDelayThresh,
       "ieee8021AsV2PortDSDelayAsym": ieee8021AsV2PortDSDelayAsym,
       "ieee8021AsV2PortDSNbrRateRatio": ieee8021AsV2PortDSNbrRateRatio,
       "ieee8021AsV2PortDSInitialLogAnnounceInterval": ieee8021AsV2PortDSInitialLogAnnounceInterval,
       "ieee8021AsV2PortDSCurrentLogAnnounceInterval": ieee8021AsV2PortDSCurrentLogAnnounceInterval,
       "ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval": ieee8021AsV2PortDSUseMgtSettableLogAnnounceInterval,
       "ieee8021AsV2PortDSMgtSettableLogAnnounceInterval": ieee8021AsV2PortDSMgtSettableLogAnnounceInterval,
       "ieee8021AsV2PortDSAnnounceReceiptTimeout": ieee8021AsV2PortDSAnnounceReceiptTimeout,
       "ieee8021AsV2PortDSInitialLogSyncInterval": ieee8021AsV2PortDSInitialLogSyncInterval,
       "ieee8021AsV2PortDSCurrentLogSyncInterval": ieee8021AsV2PortDSCurrentLogSyncInterval,
       "ieee8021AsV2PortDSUseMgtSettableLogSyncInterval": ieee8021AsV2PortDSUseMgtSettableLogSyncInterval,
       "ieee8021AsV2PortDSMgtSettableLogSyncInterval": ieee8021AsV2PortDSMgtSettableLogSyncInterval,
       "ieee8021AsV2PortDSSyncReceiptTimeout": ieee8021AsV2PortDSSyncReceiptTimeout,
       "ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval": ieee8021AsV2PortDSSyncReceiptTimeoutTimeInterval,
       "ieee8021AsV2PortDSInitialLogPdelayReqInterval": ieee8021AsV2PortDSInitialLogPdelayReqInterval,
       "ieee8021AsV2PortDSCurrentLogPdelayReqInterval": ieee8021AsV2PortDSCurrentLogPdelayReqInterval,
       "ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval": ieee8021AsV2PortDSUseMgtSettableLogPdelayReqInterval,
       "ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval": ieee8021AsV2PortDSMgtSettableLogPdelayReqInterval,
       "ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval": ieee8021AsV2PortDSInitialLogGptpCapableMessageInterval,
       "ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval": ieee8021AsV2PortDSCurrentLogGptpCapableMessageInterval,
       "ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval": ieee8021AsV2PortDSUseMgtSettableLogGptpCapableMessageInterval,
       "ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval": ieee8021AsV2PortDSMgtSettableLogGptpCapableMessageInterval,
       "ieee8021AsV2PortDSInitialComputeNbrRateRatio": ieee8021AsV2PortDSInitialComputeNbrRateRatio,
       "ieee8021AsV2PortDSCurrentComputeNbrRateRatio": ieee8021AsV2PortDSCurrentComputeNbrRateRatio,
       "ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio": ieee8021AsV2PortDSUseMgtSettableComputeNbrRateRatio,
       "ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio": ieee8021AsV2PortDSMgtSettableComputeNbrRateRatio,
       "ieee8021AsV2PortDSInitialComputeMeanLinkDelay": ieee8021AsV2PortDSInitialComputeMeanLinkDelay,
       "ieee8021AsV2PortDSCurrentComputeMeanLinkDelay": ieee8021AsV2PortDSCurrentComputeMeanLinkDelay,
       "ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay": ieee8021AsV2PortDSUseMgtSettableComputeMeanLinkDelay,
       "ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay": ieee8021AsV2PortDSMgtSettableComputeMeanLinkDelay,
       "ieee8021AsV2PortDSAllowedLostRsp": ieee8021AsV2PortDSAllowedLostRsp,
       "ieee8021AsV2PortDSAllowedFaults": ieee8021AsV2PortDSAllowedFaults,
       "ieee8021AsV2PortDSGPtpCapableReceiptTimeout": ieee8021AsV2PortDSGPtpCapableReceiptTimeout,
       "ieee8021AsV2PortDSVersionNumber": ieee8021AsV2PortDSVersionNumber,
       "ieee8021AsV2PortDSNup": ieee8021AsV2PortDSNup,
       "ieee8021AsV2PortDSNdown": ieee8021AsV2PortDSNdown,
       "ieee8021AsV2PortDSOneStepTxOper": ieee8021AsV2PortDSOneStepTxOper,
       "ieee8021AsV2PortDSOneStepReceive": ieee8021AsV2PortDSOneStepReceive,
       "ieee8021AsV2PortDSOneStepTransmit": ieee8021AsV2PortDSOneStepTransmit,
       "ieee8021AsV2PortDSInitialOneStepTxOper": ieee8021AsV2PortDSInitialOneStepTxOper,
       "ieee8021AsV2PortDSCurrentOneStepTxOper": ieee8021AsV2PortDSCurrentOneStepTxOper,
       "ieee8021AsV2PortDSUseMgtSettableOneStepTxOper": ieee8021AsV2PortDSUseMgtSettableOneStepTxOper,
       "ieee8021AsV2PortDSMgtSettableOneStepTxOper": ieee8021AsV2PortDSMgtSettableOneStepTxOper,
       "ieee8021AsV2PortDSSyncLocked": ieee8021AsV2PortDSSyncLocked,
       "ieee8021AsV2PortDSPdelayTruncTST1": ieee8021AsV2PortDSPdelayTruncTST1,
       "ieee8021AsV2PortDSPdelayTruncTST2": ieee8021AsV2PortDSPdelayTruncTST2,
       "ieee8021AsV2PortDSPdelayTruncTST3": ieee8021AsV2PortDSPdelayTruncTST3,
       "ieee8021AsV2PortDSPdelayTruncTST4": ieee8021AsV2PortDSPdelayTruncTST4,
       "ieee8021AsV2PortDSMinorVersionNumber": ieee8021AsV2PortDSMinorVersionNumber,
       "ieee8021AsV2DescriptionPortDSTable": ieee8021AsV2DescriptionPortDSTable,
       "ieee8021AsV2DescriptionPortDSEntry": ieee8021AsV2DescriptionPortDSEntry,
       "ieee8021AsV2DescriptionPortDSAsIndex": ieee8021AsV2DescriptionPortDSAsIndex,
       "ieee8021AsV2DescriptionPortDSProfileIdentifier": ieee8021AsV2DescriptionPortDSProfileIdentifier,
       "ieee8021AsV2PortStatDSTable": ieee8021AsV2PortStatDSTable,
       "ieee8021AsV2PortStatDSEntry": ieee8021AsV2PortStatDSEntry,
       "ieee8021AsV2PortStatRxSyncCount": ieee8021AsV2PortStatRxSyncCount,
       "ieee8021AsV2PortStatRxOneStepSyncCount": ieee8021AsV2PortStatRxOneStepSyncCount,
       "ieee8021AsV2PortStatRxFollowUpCount": ieee8021AsV2PortStatRxFollowUpCount,
       "ieee8021AsV2PortStatRxPdelayRequestCount": ieee8021AsV2PortStatRxPdelayRequestCount,
       "ieee8021AsV2PortStatRxPdelayRspCount": ieee8021AsV2PortStatRxPdelayRspCount,
       "ieee8021AsV2PortStatRxPdelayRspFollowUpCount": ieee8021AsV2PortStatRxPdelayRspFollowUpCount,
       "ieee8021AsV2PortStatRxAnnounceCount": ieee8021AsV2PortStatRxAnnounceCount,
       "ieee8021AsV2PortStatRxPtpPacketDiscardCount": ieee8021AsV2PortStatRxPtpPacketDiscardCount,
       "ieee8021AsV2PortStatSyncReceiptTimeoutCount": ieee8021AsV2PortStatSyncReceiptTimeoutCount,
       "ieee8021AsV2PortStatAnnounceReceiptTimeoutCount": ieee8021AsV2PortStatAnnounceReceiptTimeoutCount,
       "ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount": ieee8021AsV2PortStatPdelayAllowedLostRspExceededCount,
       "ieee8021AsV2PortStatTxSyncCount": ieee8021AsV2PortStatTxSyncCount,
       "ieee8021AsV2PortStatTxOneStepSyncCount": ieee8021AsV2PortStatTxOneStepSyncCount,
       "ieee8021AsV2PortStatTxFollowUpCount": ieee8021AsV2PortStatTxFollowUpCount,
       "ieee8021AsV2PortStatTxPdelayRequestCount": ieee8021AsV2PortStatTxPdelayRequestCount,
       "ieee8021AsV2PortStatTxPdelayRspCount": ieee8021AsV2PortStatTxPdelayRspCount,
       "ieee8021AsV2PortStatTxPdelayRspFollowUpCount": ieee8021AsV2PortStatTxPdelayRspFollowUpCount,
       "ieee8021AsV2PortStatTxAnnounceCount": ieee8021AsV2PortStatTxAnnounceCount,
       "ieee8021AsV2AcceptableMasterPortDSTable": ieee8021AsV2AcceptableMasterPortDSTable,
       "ieee8021AsV2AcceptableMasterPortDSEntry": ieee8021AsV2AcceptableMasterPortDSEntry,
       "ieee8021AsV2AcceptableMasterPortDSAsIndex": ieee8021AsV2AcceptableMasterPortDSAsIndex,
       "ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled": ieee8021AsV2AcceptableMasterPortDSAcceptableMasterTableEnabled,
       "ieee8021AsV2ExternalPortConfigurationPortDSTable": ieee8021AsV2ExternalPortConfigurationPortDSTable,
       "ieee8021AsV2ExternalPortConfigurationPortDSEntry": ieee8021AsV2ExternalPortConfigurationPortDSEntry,
       "ieee8021AsV2ExternalPortConfigurationPortDSAsIndex": ieee8021AsV2ExternalPortConfigurationPortDSAsIndex,
       "ieee8021AsV2ExternalPortConfigurationPortDSDesiredState": ieee8021AsV2ExternalPortConfigurationPortDSDesiredState,
       "ieee8021AsV2AsymMeasurementModeDSTable": ieee8021AsV2AsymMeasurementModeDSTable,
       "ieee8021AsV2AsymMeasurementModeDSEntry": ieee8021AsV2AsymMeasurementModeDSEntry,
       "ieee8021AsV2AsymMeasurementModeDSAsIndex": ieee8021AsV2AsymMeasurementModeDSAsIndex,
       "ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode": ieee8021AsV2AsymMeasurementModeDSAsymMeasurementMode,
       "ieee8021AsV2CommonServicesPortDSTable": ieee8021AsV2CommonServicesPortDSTable,
       "ieee8021AsV2CommonServicesPortDSEntry": ieee8021AsV2CommonServicesPortDSEntry,
       "ieee8021AsV2CommonServicesPortDSAsIndex": ieee8021AsV2CommonServicesPortDSAsIndex,
       "ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber": ieee8021AsV2CommonServicesPortDSCmldsLinkPortPortNumber,
       "ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable": ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSTable,
       "ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry": ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSEntry,
       "ieee8021AsV2CmldsDefaultDSAsIndex": ieee8021AsV2CmldsDefaultDSAsIndex,
       "ieee8021AsV2CmldsDefaultDSClockIdentity": ieee8021AsV2CmldsDefaultDSClockIdentity,
       "ieee8021AsV2CmldsDefaultDSNumberLinkPorts": ieee8021AsV2CmldsDefaultDSNumberLinkPorts,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSTable,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSEntry,
       "ieee8021AsV2CmldsLinkPortDSAsIndex": ieee8021AsV2CmldsLinkPortDSAsIndex,
       "ieee8021AsV2CmldsLinkPortDSClockIdentity": ieee8021AsV2CmldsLinkPortDSClockIdentity,
       "ieee8021AsV2CmldsLinkPortDSPortNumber": ieee8021AsV2CmldsLinkPortDSPortNumber,
       "ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled": ieee8021AsV2CmldsLinkPortDSCmldsLinkPortEnabled,
       "ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay": ieee8021AsV2CmldsLinkPortDSIsMeasuringDelay,
       "ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains": ieee8021AsV2CmldsLinkPortDSAsCapableAcrossDomains,
       "ieee8021AsV2CmldsLinkPortDSMeanLinkDelay": ieee8021AsV2CmldsLinkPortDSMeanLinkDelay,
       "ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh": ieee8021AsV2CmldsLinkPortDSMeanLinkDelayThresh,
       "ieee8021AsV2CmldsLinkPortDSDelayAsym": ieee8021AsV2CmldsLinkPortDSDelayAsym,
       "ieee8021AsV2CmldsLinkPortDSNbrRateRatio": ieee8021AsV2CmldsLinkPortDSNbrRateRatio,
       "ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval": ieee8021AsV2CmldsLinkPortDSInitialLogPdelayReqInterval,
       "ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval": ieee8021AsV2CmldsLinkPortDSCurrentLogPdelayReqInterval,
       "ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval": ieee8021AsV2CmldsLinkPortDSUseMgtSettableLogPdelayReqInterval,
       "ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval": ieee8021AsV2CmldsLinkPortDSMgtSettableLogPdelayReqInterval,
       "ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio": ieee8021AsV2CmldsLinkPortDSInitialComputeNbrRateRatio,
       "ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio": ieee8021AsV2CmldsLinkPortDSCurrentComputeNbrRateRatio,
       "ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio": ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeNbrRateRatio,
       "ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio": ieee8021AsV2CmldsLinkPortDSMgtSettableComputeNbrRateRatio,
       "ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay": ieee8021AsV2CmldsLinkPortDSInitialComputeMeanLinkDelay,
       "ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay": ieee8021AsV2CmldsLinkPortDSCurrentComputeMeanLinkDelay,
       "ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay": ieee8021AsV2CmldsLinkPortDSUseMgtSettableComputeMeanLinkDelay,
       "ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay": ieee8021AsV2CmldsLinkPortDSMgtSettableComputeMeanLinkDelay,
       "ieee8021AsV2CmldsLinkPortDSAllowedLostRsp": ieee8021AsV2CmldsLinkPortDSAllowedLostRsp,
       "ieee8021AsV2CmldsLinkPortDSAllowedFaults": ieee8021AsV2CmldsLinkPortDSAllowedFaults,
       "ieee8021AsV2CmldsLinkPortDSVersionNumber": ieee8021AsV2CmldsLinkPortDSVersionNumber,
       "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1": ieee8021AsV2CmldsLinkPortDSPdelayTruncTST1,
       "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2": ieee8021AsV2CmldsLinkPortDSPdelayTruncTST2,
       "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3": ieee8021AsV2CmldsLinkPortDSPdelayTruncTST3,
       "ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4": ieee8021AsV2CmldsLinkPortDSPdelayTruncTST4,
       "ieee8021AsV2CmldsLinkPortDSMinorVersionNumber": ieee8021AsV2CmldsLinkPortDSMinorVersionNumber,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSTable,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSEntry,
       "ieee8021AsV2CmldsLinkPortStatDSIndex": ieee8021AsV2CmldsLinkPortStatDSIndex,
       "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount": ieee8021AsV2CmldsLinkPortStatDSRxPdelayRequestCount,
       "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount": ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspCount,
       "ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount": ieee8021AsV2CmldsLinkPortStatDSRxPdelayRspFollowUpCount,
       "ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount": ieee8021AsV2CmldsLinkPortStatDSRxPtpPacketDiscardCount,
       "ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount": ieee8021AsV2CmldsLinkPortStatDSPdelayAllowedLostRspExceededCount,
       "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount": ieee8021AsV2CmldsLinkPortStatDSTxPdelayRequestCount,
       "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount": ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspCount,
       "ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount": ieee8021AsV2CmldsLinkPortStatDSTxPdelayRspFollowUpCount,
       "ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable": ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSTable,
       "ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry": ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSEntry,
       "ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex": ieee8021AsV2CmldsAsymMeasurementModeDSAsIndex,
       "ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode": ieee8021AsV2CmldsAsymMeasurementModeDSAsymMeasurementMode,
       "ieee8021AsV2Conformance": ieee8021AsV2Conformance,
       "ieee8021AsV2Groups": ieee8021AsV2Groups,
       "ieee8021AsV2PtpInstanceGroup": ieee8021AsV2PtpInstanceGroup,
       "ieee8021AsV2DefaultDSGroup": ieee8021AsV2DefaultDSGroup,
       "ieee8021AsV2CurrentDSGroup": ieee8021AsV2CurrentDSGroup,
       "ieee8021AsV2ParentDSGroup": ieee8021AsV2ParentDSGroup,
       "ieee8021AsV2TimePropertiesDSGroup": ieee8021AsV2TimePropertiesDSGroup,
       "ieee8021AsV2PathTraceDSGroup": ieee8021AsV2PathTraceDSGroup,
       "ieee8021AsV2PathTraceDSArrayTableGroup": ieee8021AsV2PathTraceDSArrayTableGroup,
       "ieee8021AsV2AcceptableMasterTableDSGroup": ieee8021AsV2AcceptableMasterTableDSGroup,
       "ieee8021AsV2AcceptableMasterTableDSArrayGroup": ieee8021AsV2AcceptableMasterTableDSArrayGroup,
       "ieee8021AsV2PortDSGroup": ieee8021AsV2PortDSGroup,
       "ieee8021AsV2DescriptionPortDSGroup": ieee8021AsV2DescriptionPortDSGroup,
       "ieee8021AsV2PortStatIfGroup": ieee8021AsV2PortStatIfGroup,
       "ieee8021AsV2AcceptableMasterPortDSGroup": ieee8021AsV2AcceptableMasterPortDSGroup,
       "ieee8021AsV2ExternalPortConfigurationPortDSGroup": ieee8021AsV2ExternalPortConfigurationPortDSGroup,
       "ieee8021AsV2AsymMeasurementModeDSGroup": ieee8021AsV2AsymMeasurementModeDSGroup,
       "ieee8021AsV2CommonServicesPortDSGroup": ieee8021AsV2CommonServicesPortDSGroup,
       "ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup": ieee8021AsV2CommonMeanLinkDelayServiceDefaultDSGroup,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortDSGroup,
       "ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup": ieee8021AsV2CommonMeanLinkDelayServiceLinkPortStatDSGroup,
       "ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup": ieee8021AsV2CommonMeanLinkDelayServiceAsymMeasurementModeDSGroup,
       "ieee8021AsV2Compliances": ieee8021AsV2Compliances,
       "ieee8021AsV2Compliance": ieee8021AsV2Compliance}
)
