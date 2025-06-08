# SNMP MIB module (BELAIR-CABLE-MODEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-CABLE-MODEM.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairApplications,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairApplications")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairCableModemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4)
)
if mibBuilder.loadTexts:
    belairCableModemMib.setRevisions(
        ("2009-09-28 15:50",
         "2008-07-29 14:40",
         "2006-04-26 16:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class TenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_BelairCmObjects_ObjectIdentity = ObjectIdentity
belairCmObjects = _BelairCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1)
)
_BelairCmStatusTable_Object = MibTable
belairCmStatusTable = _BelairCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    belairCmStatusTable.setStatus("current")
_BelairCmStatusEntry_Object = MibTableRow
belairCmStatusEntry = _BelairCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1)
)
belairCmStatusEntry.setIndexNames(
    (0, "BELAIR-CABLE-MODEM", "belairCmStatusIndex"),
)
if mibBuilder.loadTexts:
    belairCmStatusEntry.setStatus("current")


class _BelairCmStatusIndex_Type(Integer32):
    """Custom type belairCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_BelairCmStatusIndex_Type.__name__ = "Integer32"
_BelairCmStatusIndex_Object = MibTableColumn
belairCmStatusIndex = _BelairCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 1),
    _BelairCmStatusIndex_Type()
)
belairCmStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCmStatusIndex.setStatus("current")


class _BelairCmStatusValue_Type(Integer32):
    """Custom type belairCmStatusValue based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("notReady", 2),
          ("notSynchronized", 3),
          ("phySynchronized", 4),
          ("usParametersAcquired", 5),
          ("rangingComplete", 6),
          ("ipComplete", 7),
          ("todEstablished", 8),
          ("securityEstablished", 9),
          ("paramTransferComplete", 10),
          ("registrationComplete", 11),
          ("operational", 12),
          ("accessDenied", 13))
    )


_BelairCmStatusValue_Type.__name__ = "Integer32"
_BelairCmStatusValue_Object = MibTableColumn
belairCmStatusValue = _BelairCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 2),
    _BelairCmStatusValue_Type()
)
belairCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmStatusValue.setStatus("current")
_BelairCmIpAddress_Type = IpAddress
_BelairCmIpAddress_Object = MibTableColumn
belairCmIpAddress = _BelairCmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 3),
    _BelairCmIpAddress_Type()
)
belairCmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmIpAddress.setStatus("current")
_BelairCmMacAddress_Type = MacAddress
_BelairCmMacAddress_Object = MibTableColumn
belairCmMacAddress = _BelairCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 4),
    _BelairCmMacAddress_Type()
)
belairCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmMacAddress.setStatus("current")


class _BelairCmSwCurrentVersion_Type(OctetString):
    """Custom type belairCmSwCurrentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairCmSwCurrentVersion_Type.__name__ = "OctetString"
_BelairCmSwCurrentVersion_Object = MibTableColumn
belairCmSwCurrentVersion = _BelairCmSwCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 5),
    _BelairCmSwCurrentVersion_Type()
)
belairCmSwCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmSwCurrentVersion.setStatus("current")
_BelairCmDownstreamFrequency_Type = Integer32
_BelairCmDownstreamFrequency_Object = MibTableColumn
belairCmDownstreamFrequency = _BelairCmDownstreamFrequency_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 6),
    _BelairCmDownstreamFrequency_Type()
)
belairCmDownstreamFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmDownstreamFrequency.setStatus("current")
if mibBuilder.loadTexts:
    belairCmDownstreamFrequency.setUnits("Hz")
_BelairCmTimingOffset_Type = Integer32
_BelairCmTimingOffset_Object = MibTableColumn
belairCmTimingOffset = _BelairCmTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 7),
    _BelairCmTimingOffset_Type()
)
belairCmTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmTimingOffset.setStatus("current")
if mibBuilder.loadTexts:
    belairCmTimingOffset.setUnits("ppm")
_BelairCmCarrierFrequencyOffset_Type = Integer32
_BelairCmCarrierFrequencyOffset_Object = MibTableColumn
belairCmCarrierFrequencyOffset = _BelairCmCarrierFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 8),
    _BelairCmCarrierFrequencyOffset_Type()
)
belairCmCarrierFrequencyOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmCarrierFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    belairCmCarrierFrequencyOffset.setUnits("hz")
_BelairCmUpstreamPower_Type = TenthdBmV
_BelairCmUpstreamPower_Object = MibTableColumn
belairCmUpstreamPower = _BelairCmUpstreamPower_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 9),
    _BelairCmUpstreamPower_Type()
)
belairCmUpstreamPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmUpstreamPower.setStatus("current")
if mibBuilder.loadTexts:
    belairCmUpstreamPower.setUnits("dBmV/10")
_BelairCmDownstreamPower_Type = TenthdBmV
_BelairCmDownstreamPower_Object = MibTableColumn
belairCmDownstreamPower = _BelairCmDownstreamPower_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 10),
    _BelairCmDownstreamPower_Type()
)
belairCmDownstreamPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmDownstreamPower.setStatus("current")
if mibBuilder.loadTexts:
    belairCmDownstreamPower.setUnits("dBmV/10")
_BelairCmDownstreamSnr_Type = TenthdB
_BelairCmDownstreamSnr_Object = MibTableColumn
belairCmDownstreamSnr = _BelairCmDownstreamSnr_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 11),
    _BelairCmDownstreamSnr_Type()
)
belairCmDownstreamSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmDownstreamSnr.setStatus("current")
if mibBuilder.loadTexts:
    belairCmDownstreamSnr.setUnits("dB/10")


class _BelairCmQamModulationMode_Type(Integer32):
    """Custom type belairCmQamModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(256, 256),
    )


_BelairCmQamModulationMode_Type.__name__ = "Integer32"
_BelairCmQamModulationMode_Object = MibTableColumn
belairCmQamModulationMode = _BelairCmQamModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 12),
    _BelairCmQamModulationMode_Type()
)
belairCmQamModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmQamModulationMode.setStatus("current")
_BelairCmStatusQamLock_Type = TruthValue
_BelairCmStatusQamLock_Object = MibTableColumn
belairCmStatusQamLock = _BelairCmStatusQamLock_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 13),
    _BelairCmStatusQamLock_Type()
)
belairCmStatusQamLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmStatusQamLock.setStatus("current")
_BelairCmStatusFecSync_Type = TruthValue
_BelairCmStatusFecSync_Object = MibTableColumn
belairCmStatusFecSync = _BelairCmStatusFecSync_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 14),
    _BelairCmStatusFecSync_Type()
)
belairCmStatusFecSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmStatusFecSync.setStatus("current")
_BelairCmStatusMpegSync_Type = TruthValue
_BelairCmStatusMpegSync_Object = MibTableColumn
belairCmStatusMpegSync = _BelairCmStatusMpegSync_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 15),
    _BelairCmStatusMpegSync_Type()
)
belairCmStatusMpegSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmStatusMpegSync.setStatus("current")
_BelairCmStatusWeakSignal_Type = TruthValue
_BelairCmStatusWeakSignal_Object = MibTableColumn
belairCmStatusWeakSignal = _BelairCmStatusWeakSignal_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 1, 1, 16),
    _BelairCmStatusWeakSignal_Type()
)
belairCmStatusWeakSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmStatusWeakSignal.setStatus("current")
_BelairCmCurrentTable_Object = MibTable
belairCmCurrentTable = _BelairCmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    belairCmCurrentTable.setStatus("current")
_BelairCmCurrentEntry_Object = MibTableRow
belairCmCurrentEntry = _BelairCmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 2, 1)
)
belairCmCurrentEntry.setIndexNames(
    (0, "BELAIR-CABLE-MODEM", "belairCmStatusIndex"),
)
if mibBuilder.loadTexts:
    belairCmCurrentEntry.setStatus("current")
_BelairCmCurrentUASs_Type = PerfCurrentCount
_BelairCmCurrentUASs_Object = MibTableColumn
belairCmCurrentUASs = _BelairCmCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 2, 1, 1),
    _BelairCmCurrentUASs_Type()
)
belairCmCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmCurrentUASs.setStatus("current")
_BelairCmIntervalTable_Object = MibTable
belairCmIntervalTable = _BelairCmIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    belairCmIntervalTable.setStatus("current")
_BelairCmIntervalEntry_Object = MibTableRow
belairCmIntervalEntry = _BelairCmIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 3, 1)
)
belairCmIntervalEntry.setIndexNames(
    (0, "BELAIR-CABLE-MODEM", "belairCmStatusIndex"),
    (0, "BELAIR-CABLE-MODEM", "belairCmIntervalIndex"),
)
if mibBuilder.loadTexts:
    belairCmIntervalEntry.setStatus("current")


class _BelairCmIntervalIndex_Type(Integer32):
    """Custom type belairCmIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BelairCmIntervalIndex_Type.__name__ = "Integer32"
_BelairCmIntervalIndex_Object = MibTableColumn
belairCmIntervalIndex = _BelairCmIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 3, 1, 1),
    _BelairCmIntervalIndex_Type()
)
belairCmIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCmIntervalIndex.setStatus("current")
_BelairCmIntervalUASs_Type = PerfIntervalCount
_BelairCmIntervalUASs_Object = MibTableColumn
belairCmIntervalUASs = _BelairCmIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 3, 1, 2),
    _BelairCmIntervalUASs_Type()
)
belairCmIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmIntervalUASs.setStatus("current")
_BelairCmTotalTable_Object = MibTable
belairCmTotalTable = _BelairCmTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    belairCmTotalTable.setStatus("current")
_BelairCmTotalEntry_Object = MibTableRow
belairCmTotalEntry = _BelairCmTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 4, 1)
)
belairCmTotalEntry.setIndexNames(
    (0, "BELAIR-CABLE-MODEM", "belairCmStatusIndex"),
)
if mibBuilder.loadTexts:
    belairCmTotalEntry.setStatus("current")
_BelairCmTotalUASs_Type = PerfTotalCount
_BelairCmTotalUASs_Object = MibTableColumn
belairCmTotalUASs = _BelairCmTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 4, 1, 1),
    _BelairCmTotalUASs_Type()
)
belairCmTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCmTotalUASs.setStatus("current")
_BelairCm24HrIntervalTable_Object = MibTable
belairCm24HrIntervalTable = _BelairCm24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 5)
)
if mibBuilder.loadTexts:
    belairCm24HrIntervalTable.setStatus("current")
_BelairCm24HrIntervalEntry_Object = MibTableRow
belairCm24HrIntervalEntry = _BelairCm24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 5, 1)
)
belairCm24HrIntervalEntry.setIndexNames(
    (0, "BELAIR-CABLE-MODEM", "belairCmStatusIndex"),
    (0, "BELAIR-CABLE-MODEM", "belairCm24HrIntervalIndex"),
)
if mibBuilder.loadTexts:
    belairCm24HrIntervalEntry.setStatus("current")


class _BelairCm24HrIntervalIndex_Type(Integer32):
    """Custom type belairCm24HrIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_BelairCm24HrIntervalIndex_Type.__name__ = "Integer32"
_BelairCm24HrIntervalIndex_Object = MibTableColumn
belairCm24HrIntervalIndex = _BelairCm24HrIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 5, 1, 1),
    _BelairCm24HrIntervalIndex_Type()
)
belairCm24HrIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCm24HrIntervalIndex.setStatus("current")
_BelairCm24HrIntervalUASs_Type = Gauge32
_BelairCm24HrIntervalUASs_Object = MibTableColumn
belairCm24HrIntervalUASs = _BelairCm24HrIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 1, 5, 1, 2),
    _BelairCm24HrIntervalUASs_Type()
)
belairCm24HrIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCm24HrIntervalUASs.setStatus("current")
_BelairCmTrapObjects_ObjectIdentity = ObjectIdentity
belairCmTrapObjects = _BelairCmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 2)
)
_BelairCmTrapPrefix_ObjectIdentity = ObjectIdentity
belairCmTrapPrefix = _BelairCmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 2, 0)
)
_BelairCmConformance_ObjectIdentity = ObjectIdentity
belairCmConformance = _BelairCmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 3)
)

# Managed Objects groups

belairCmObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 3, 1)
)
belairCmObjectsGroup.setObjects(
      *(("BELAIR-CABLE-MODEM", "belairCmStatusValue"),
        ("BELAIR-CABLE-MODEM", "belairCmIpAddress"),
        ("BELAIR-CABLE-MODEM", "belairCmMacAddress"),
        ("BELAIR-CABLE-MODEM", "belairCmSwCurrentVersion"),
        ("BELAIR-CABLE-MODEM", "belairCmDownstreamFrequency"),
        ("BELAIR-CABLE-MODEM", "belairCmTimingOffset"),
        ("BELAIR-CABLE-MODEM", "belairCmCarrierFrequencyOffset"),
        ("BELAIR-CABLE-MODEM", "belairCmUpstreamPower"),
        ("BELAIR-CABLE-MODEM", "belairCmDownstreamPower"),
        ("BELAIR-CABLE-MODEM", "belairCmDownstreamSnr"),
        ("BELAIR-CABLE-MODEM", "belairCmQamModulationMode"),
        ("BELAIR-CABLE-MODEM", "belairCmStatusQamLock"),
        ("BELAIR-CABLE-MODEM", "belairCmStatusFecSync"),
        ("BELAIR-CABLE-MODEM", "belairCmStatusMpegSync"),
        ("BELAIR-CABLE-MODEM", "belairCmStatusWeakSignal"),
        ("BELAIR-CABLE-MODEM", "belairCmCurrentUASs"),
        ("BELAIR-CABLE-MODEM", "belairCmIntervalUASs"),
        ("BELAIR-CABLE-MODEM", "belairCmTotalUASs"),
        ("BELAIR-CABLE-MODEM", "belairCm24HrIntervalUASs"))
)
if mibBuilder.loadTexts:
    belairCmObjectsGroup.setStatus("current")


# Notification objects

belairCmIpAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 2, 0, 1)
)
belairCmIpAddressChange.setObjects(
    ("BELAIR-CABLE-MODEM", "belairCmIpAddress")
)
if mibBuilder.loadTexts:
    belairCmIpAddressChange.setStatus(
        "current"
    )


# Notifications groups

belairCmTrapObjectsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 4, 3, 2)
)
belairCmTrapObjectsGroup.setObjects(
    ("BELAIR-CABLE-MODEM", "belairCmIpAddressChange")
)
if mibBuilder.loadTexts:
    belairCmTrapObjectsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-CABLE-MODEM",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "belairCableModemMib": belairCableModemMib,
       "belairCmObjects": belairCmObjects,
       "belairCmStatusTable": belairCmStatusTable,
       "belairCmStatusEntry": belairCmStatusEntry,
       "belairCmStatusIndex": belairCmStatusIndex,
       "belairCmStatusValue": belairCmStatusValue,
       "belairCmIpAddress": belairCmIpAddress,
       "belairCmMacAddress": belairCmMacAddress,
       "belairCmSwCurrentVersion": belairCmSwCurrentVersion,
       "belairCmDownstreamFrequency": belairCmDownstreamFrequency,
       "belairCmTimingOffset": belairCmTimingOffset,
       "belairCmCarrierFrequencyOffset": belairCmCarrierFrequencyOffset,
       "belairCmUpstreamPower": belairCmUpstreamPower,
       "belairCmDownstreamPower": belairCmDownstreamPower,
       "belairCmDownstreamSnr": belairCmDownstreamSnr,
       "belairCmQamModulationMode": belairCmQamModulationMode,
       "belairCmStatusQamLock": belairCmStatusQamLock,
       "belairCmStatusFecSync": belairCmStatusFecSync,
       "belairCmStatusMpegSync": belairCmStatusMpegSync,
       "belairCmStatusWeakSignal": belairCmStatusWeakSignal,
       "belairCmCurrentTable": belairCmCurrentTable,
       "belairCmCurrentEntry": belairCmCurrentEntry,
       "belairCmCurrentUASs": belairCmCurrentUASs,
       "belairCmIntervalTable": belairCmIntervalTable,
       "belairCmIntervalEntry": belairCmIntervalEntry,
       "belairCmIntervalIndex": belairCmIntervalIndex,
       "belairCmIntervalUASs": belairCmIntervalUASs,
       "belairCmTotalTable": belairCmTotalTable,
       "belairCmTotalEntry": belairCmTotalEntry,
       "belairCmTotalUASs": belairCmTotalUASs,
       "belairCm24HrIntervalTable": belairCm24HrIntervalTable,
       "belairCm24HrIntervalEntry": belairCm24HrIntervalEntry,
       "belairCm24HrIntervalIndex": belairCm24HrIntervalIndex,
       "belairCm24HrIntervalUASs": belairCm24HrIntervalUASs,
       "belairCmTrapObjects": belairCmTrapObjects,
       "belairCmTrapPrefix": belairCmTrapPrefix,
       "belairCmIpAddressChange": belairCmIpAddressChange,
       "belairCmConformance": belairCmConformance,
       "belairCmObjectsGroup": belairCmObjectsGroup,
       "belairCmTrapObjectsGroup": belairCmTrapObjectsGroup}
)
