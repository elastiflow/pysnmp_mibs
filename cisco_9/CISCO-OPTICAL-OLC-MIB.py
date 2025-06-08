# SNMP MIB module (CISCO-OPTICAL-OLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-OPTICAL-OLC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
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

(InterfaceIndex,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoOpticalOlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057)
)
if mibBuilder.loadTexts:
    ciscoOpticalOlcMIB.setRevisions(
        ("2022-11-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoOpticalOlcRamanTuningStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("startup", 1),
          ("disabled", 2),
          ("blocked", 3),
          ("failed", 4),
          ("measurementInProgress", 5),
          ("calculationInProgress", 6),
          ("optimizationInProgress", 7),
          ("tuned", 8))
    )



class CiscoOpticalOlcRamanTuningFailReason(TextualConvention, Integer32):
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
        *(("measurement", 1),
          ("calculation", 2),
          ("optimization", 3))
    )



class CiscoOpticalOlcApcBlockReason(TextualConvention, Integer32):
    status = "current"
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
        *(("hw-fail", 1),
          ("edfa-shutdown", 2),
          ("apr-enabled", 3),
          ("user-disabled", 4),
          ("edfa-apr", 5),
          ("gain-estimation-in-progress", 6),
          ("band-failure", 7),
          ("partial-topology", 8),
          ("node-blocked", 9))
    )



class CiscoOpticalOlcPower(TextualConvention, Integer32):
    status = "current"


class CiscoOpticalOlcGainInDb(TextualConvention, Integer32):
    status = "current"


class CiscoOpticalOlcPSDInDbm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 2300),
    )



class CiscoOpticalOlcGainEstStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("blocked", 1),
          ("disabled", 2),
          ("operational", 3),
          ("idle", 4))
    )



class CiscoOpticalOlcApcAgentDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("receive", 2))
    )



class CiscoOpticalOlcApcInternalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("idle", 2),
          ("oor", 3),
          ("discrepancy", 4),
          ("correcting", 5),
          ("channel-startup", 6))
    )



class CiscoOpticalOlcApcManagerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("idle", 2),
          ("blocked", 3),
          ("working", 4),
          ("enable", 5),
          ("paused", 6))
    )



class CiscoOpticalOlcBandStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("active", 2),
          ("failed", 3),
          ("recovering", 4))
    )



class CiscoOpticalOlcBandPSDType(TextualConvention, Integer32):
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
        *(("unknown-band-psd", 1),
          ("single-band-psd", 2),
          ("dual-band-psd", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOpticalOlcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOpticalOlcMIBObjects = _CiscoOpticalOlcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1)
)
_CooOlcData_ObjectIdentity = ObjectIdentity
cooOlcData = _CooOlcData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1)
)
_CooOlcSpanLossTable_Object = MibTable
cooOlcSpanLossTable = _CooOlcSpanLossTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cooOlcSpanLossTable.setStatus("current")
_CooOlcSpanLossEntry_Object = MibTableRow
cooOlcSpanLossEntry = _CooOlcSpanLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1)
)
cooOlcSpanLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcSpanLossEntry.setStatus("current")
_CooOlcRxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcRxSpanLoss_Object = MibTableColumn
cooOlcRxSpanLoss = _CooOlcRxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 1),
    _CooOlcRxSpanLoss_Type()
)
cooOlcRxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcRxSpanLoss.setUnits("1/100 dB")
_CooOlcApparentRxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcApparentRxSpanLoss_Object = MibTableColumn
cooOlcApparentRxSpanLoss = _CooOlcApparentRxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 2),
    _CooOlcApparentRxSpanLoss_Type()
)
cooOlcApparentRxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApparentRxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcApparentRxSpanLoss.setUnits("1/100 dB")
_CooOlcRxSpanLossPumpsOff_Type = CiscoOpticalOlcPower
_CooOlcRxSpanLossPumpsOff_Object = MibTableColumn
cooOlcRxSpanLossPumpsOff = _CooOlcRxSpanLossPumpsOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 3),
    _CooOlcRxSpanLossPumpsOff_Type()
)
cooOlcRxSpanLossPumpsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRxSpanLossPumpsOff.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcRxSpanLossPumpsOff.setUnits("1/100 dB")
_CooOlcRxSpanLossPumpsOffTimeStamp_Type = OctetString
_CooOlcRxSpanLossPumpsOffTimeStamp_Object = MibTableColumn
cooOlcRxSpanLossPumpsOffTimeStamp = _CooOlcRxSpanLossPumpsOffTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 4),
    _CooOlcRxSpanLossPumpsOffTimeStamp_Type()
)
cooOlcRxSpanLossPumpsOffTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRxSpanLossPumpsOffTimeStamp.setStatus("current")
_CooOlcEstimatedRxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcEstimatedRxSpanLoss_Object = MibTableColumn
cooOlcEstimatedRxSpanLoss = _CooOlcEstimatedRxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 5),
    _CooOlcEstimatedRxSpanLoss_Type()
)
cooOlcEstimatedRxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEstimatedRxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcEstimatedRxSpanLoss.setUnits("1/100 dB")
_CooOlcTxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcTxSpanLoss_Object = MibTableColumn
cooOlcTxSpanLoss = _CooOlcTxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 6),
    _CooOlcTxSpanLoss_Type()
)
cooOlcTxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcTxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcTxSpanLoss.setUnits("1/100 dB")
_CooOlcApparentTxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcApparentTxSpanLoss_Object = MibTableColumn
cooOlcApparentTxSpanLoss = _CooOlcApparentTxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 7),
    _CooOlcApparentTxSpanLoss_Type()
)
cooOlcApparentTxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApparentTxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcApparentTxSpanLoss.setUnits("1/100 dB")
_CooOlcTxSpanLossPumpsOff_Type = CiscoOpticalOlcPower
_CooOlcTxSpanLossPumpsOff_Object = MibTableColumn
cooOlcTxSpanLossPumpsOff = _CooOlcTxSpanLossPumpsOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 8),
    _CooOlcTxSpanLossPumpsOff_Type()
)
cooOlcTxSpanLossPumpsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcTxSpanLossPumpsOff.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcTxSpanLossPumpsOff.setUnits("1/100 dB")
_CooOlcTxSpanLossPumpsOffTimeStamp_Type = OctetString
_CooOlcTxSpanLossPumpsOffTimeStamp_Object = MibTableColumn
cooOlcTxSpanLossPumpsOffTimeStamp = _CooOlcTxSpanLossPumpsOffTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 9),
    _CooOlcTxSpanLossPumpsOffTimeStamp_Type()
)
cooOlcTxSpanLossPumpsOffTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcTxSpanLossPumpsOffTimeStamp.setStatus("current")
_CooOlcEstimatedTxSpanLoss_Type = CiscoOpticalOlcPower
_CooOlcEstimatedTxSpanLoss_Object = MibTableColumn
cooOlcEstimatedTxSpanLoss = _CooOlcEstimatedTxSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 10),
    _CooOlcEstimatedTxSpanLoss_Type()
)
cooOlcEstimatedTxSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEstimatedTxSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcEstimatedTxSpanLoss.setUnits("1/100 dB")
_CooOlcRamanTuningTable_Object = MibTable
cooOlcRamanTuningTable = _CooOlcRamanTuningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cooOlcRamanTuningTable.setStatus("current")
_CooOlcRamanTuningEntry_Object = MibTableRow
cooOlcRamanTuningEntry = _CooOlcRamanTuningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1)
)
cooOlcRamanTuningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcRamanTuningEntry.setStatus("current")
_CooOlcRamanTuningStatus_Type = CiscoOpticalOlcRamanTuningStatus
_CooOlcRamanTuningStatus_Object = MibTableColumn
cooOlcRamanTuningStatus = _CooOlcRamanTuningStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 1),
    _CooOlcRamanTuningStatus_Type()
)
cooOlcRamanTuningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRamanTuningStatus.setStatus("current")


class _CooOlcRamanTuningBlockedReason_Type(DisplayString):
    """Custom type cooOlcRamanTuningBlockedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CooOlcRamanTuningBlockedReason_Type.__name__ = "DisplayString"
_CooOlcRamanTuningBlockedReason_Object = MibTableColumn
cooOlcRamanTuningBlockedReason = _CooOlcRamanTuningBlockedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 2),
    _CooOlcRamanTuningBlockedReason_Type()
)
cooOlcRamanTuningBlockedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRamanTuningBlockedReason.setStatus("current")
_CooOlcRamanTuningFailedReason_Type = CiscoOpticalOlcRamanTuningFailReason
_CooOlcRamanTuningFailedReason_Object = MibTableColumn
cooOlcRamanTuningFailedReason = _CooOlcRamanTuningFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 3),
    _CooOlcRamanTuningFailedReason_Type()
)
cooOlcRamanTuningFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRamanTuningFailedReason.setStatus("current")
_CooOlcTuningCompleteTimeStamp_Type = OctetString
_CooOlcTuningCompleteTimeStamp_Object = MibTableColumn
cooOlcTuningCompleteTimeStamp = _CooOlcTuningCompleteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 4),
    _CooOlcTuningCompleteTimeStamp_Type()
)
cooOlcTuningCompleteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcTuningCompleteTimeStamp.setStatus("current")
_CooOlcEstimatedMaxPossibleGain_Type = CiscoOpticalOlcGainInDb
_CooOlcEstimatedMaxPossibleGain_Object = MibTableColumn
cooOlcEstimatedMaxPossibleGain = _CooOlcEstimatedMaxPossibleGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 5),
    _CooOlcEstimatedMaxPossibleGain_Type()
)
cooOlcEstimatedMaxPossibleGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEstimatedMaxPossibleGain.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcEstimatedMaxPossibleGain.setUnits("1/100 dB")
_CooOlcRamanGainTarget_Type = CiscoOpticalOlcGainInDb
_CooOlcRamanGainTarget_Object = MibTableColumn
cooOlcRamanGainTarget = _CooOlcRamanGainTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 6),
    _CooOlcRamanGainTarget_Type()
)
cooOlcRamanGainTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcRamanGainTarget.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcRamanGainTarget.setUnits("1/100 dB")
_CooOlcGainAchievedOnTuningComplete_Type = CiscoOpticalOlcGainInDb
_CooOlcGainAchievedOnTuningComplete_Object = MibTableColumn
cooOlcGainAchievedOnTuningComplete = _CooOlcGainAchievedOnTuningComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 7),
    _CooOlcGainAchievedOnTuningComplete_Type()
)
cooOlcGainAchievedOnTuningComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcGainAchievedOnTuningComplete.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcGainAchievedOnTuningComplete.setUnits("1/100 dB")
_CooOlcGainEstimatorTable_Object = MibTable
cooOlcGainEstimatorTable = _CooOlcGainEstimatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cooOlcGainEstimatorTable.setStatus("current")
_CooOlcGainEstimatorEntry_Object = MibTableRow
cooOlcGainEstimatorEntry = _CooOlcGainEstimatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1)
)
cooOlcGainEstimatorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcGainEstimatorEntry.setStatus("current")
_CooOlcEgressGainEstStatus_Type = CiscoOpticalOlcGainEstStatus
_CooOlcEgressGainEstStatus_Object = MibTableColumn
cooOlcEgressGainEstStatus = _CooOlcEgressGainEstStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 1),
    _CooOlcEgressGainEstStatus_Type()
)
cooOlcEgressGainEstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEgressGainEstStatus.setStatus("current")
_CooOlcEgressEstimatedGain_Type = CiscoOpticalOlcGainInDb
_CooOlcEgressEstimatedGain_Object = MibTableColumn
cooOlcEgressEstimatedGain = _CooOlcEgressEstimatedGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 2),
    _CooOlcEgressEstimatedGain_Type()
)
cooOlcEgressEstimatedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEgressEstimatedGain.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcEgressEstimatedGain.setUnits("1/100 dB")
_CooOlcEgressEstimatedGainMode_Type = OctetString
_CooOlcEgressEstimatedGainMode_Object = MibTableColumn
cooOlcEgressEstimatedGainMode = _CooOlcEgressEstimatedGainMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 3),
    _CooOlcEgressEstimatedGainMode_Type()
)
cooOlcEgressEstimatedGainMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEgressEstimatedGainMode.setStatus("current")
_CooOlcEgressGainEstTimeStamp_Type = OctetString
_CooOlcEgressGainEstTimeStamp_Object = MibTableColumn
cooOlcEgressGainEstTimeStamp = _CooOlcEgressGainEstTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 4),
    _CooOlcEgressGainEstTimeStamp_Type()
)
cooOlcEgressGainEstTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcEgressGainEstTimeStamp.setStatus("current")
_CooOlcIngressGainEstStatus_Type = CiscoOpticalOlcGainEstStatus
_CooOlcIngressGainEstStatus_Object = MibTableColumn
cooOlcIngressGainEstStatus = _CooOlcIngressGainEstStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 5),
    _CooOlcIngressGainEstStatus_Type()
)
cooOlcIngressGainEstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcIngressGainEstStatus.setStatus("current")
_CooOlcIngressEstimatedGain_Type = CiscoOpticalOlcGainInDb
_CooOlcIngressEstimatedGain_Object = MibTableColumn
cooOlcIngressEstimatedGain = _CooOlcIngressEstimatedGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 6),
    _CooOlcIngressEstimatedGain_Type()
)
cooOlcIngressEstimatedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcIngressEstimatedGain.setStatus("current")
if mibBuilder.loadTexts:
    cooOlcIngressEstimatedGain.setUnits("1/100 dB")
_CooOlcIngressEstimatedGainMode_Type = OctetString
_CooOlcIngressEstimatedGainMode_Object = MibTableColumn
cooOlcIngressEstimatedGainMode = _CooOlcIngressEstimatedGainMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 7),
    _CooOlcIngressEstimatedGainMode_Type()
)
cooOlcIngressEstimatedGainMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcIngressEstimatedGainMode.setStatus("current")
_CooOlcIngressGainEstTimeStamp_Type = OctetString
_CooOlcIngressGainEstTimeStamp_Object = MibTableColumn
cooOlcIngressGainEstTimeStamp = _CooOlcIngressGainEstTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 8),
    _CooOlcIngressGainEstTimeStamp_Type()
)
cooOlcIngressGainEstTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcIngressGainEstTimeStamp.setStatus("current")
_CooOlcApcTable_Object = MibTable
cooOlcApcTable = _CooOlcApcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cooOlcApcTable.setStatus("current")
_CooOlcApcEntry_Object = MibTableRow
cooOlcApcEntry = _CooOlcApcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1)
)
cooOlcApcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-OLC-MIB", "cooOlcApcAgentDirection"),
)
if mibBuilder.loadTexts:
    cooOlcApcEntry.setStatus("current")
_CooOlcApcAgentDirection_Type = CiscoOpticalOlcApcAgentDirection
_CooOlcApcAgentDirection_Object = MibTableColumn
cooOlcApcAgentDirection = _CooOlcApcAgentDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 1),
    _CooOlcApcAgentDirection_Type()
)
cooOlcApcAgentDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooOlcApcAgentDirection.setStatus("current")
_CooOlcApcDomainManager_Type = IpAddress
_CooOlcApcDomainManager_Object = MibTableColumn
cooOlcApcDomainManager = _CooOlcApcDomainManager_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 2),
    _CooOlcApcDomainManager_Type()
)
cooOlcApcDomainManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcDomainManager.setStatus("current")
_CooOlcApcDomainManagerState_Type = CiscoOpticalOlcApcManagerState
_CooOlcApcDomainManagerState_Object = MibTableColumn
cooOlcApcDomainManagerState = _CooOlcApcDomainManagerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 3),
    _CooOlcApcDomainManagerState_Type()
)
cooOlcApcDomainManagerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcDomainManagerState.setStatus("current")
_CooOlcApcDomainManagerBlockedReason_Type = CiscoOpticalOlcApcBlockReason
_CooOlcApcDomainManagerBlockedReason_Object = MibTableColumn
cooOlcApcDomainManagerBlockedReason = _CooOlcApcDomainManagerBlockedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 4),
    _CooOlcApcDomainManagerBlockedReason_Type()
)
cooOlcApcDomainManagerBlockedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcDomainManagerBlockedReason.setStatus("current")
_CooOlcApcInternalState_Type = CiscoOpticalOlcApcInternalState
_CooOlcApcInternalState_Object = MibTableColumn
cooOlcApcInternalState = _CooOlcApcInternalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 5),
    _CooOlcApcInternalState_Type()
)
cooOlcApcInternalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcInternalState.setStatus("current")
_CooOlcApcBlockedReason_Type = CiscoOpticalOlcApcBlockReason
_CooOlcApcBlockedReason_Object = MibTableColumn
cooOlcApcBlockedReason = _CooOlcApcBlockedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 6),
    _CooOlcApcBlockedReason_Type()
)
cooOlcApcBlockedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcBlockedReason.setStatus("current")
_CooOlcApcPsdMin_Type = CiscoOpticalOlcPSDInDbm
_CooOlcApcPsdMin_Object = MibTableColumn
cooOlcApcPsdMin = _CooOlcApcPsdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 7),
    _CooOlcApcPsdMin_Type()
)
cooOlcApcPsdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcApcPsdMin.setStatus("current")
_CooOlcApcGainRange_Type = OctetString
_CooOlcApcGainRange_Object = MibTableColumn
cooOlcApcGainRange = _CooOlcApcGainRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 8),
    _CooOlcApcGainRange_Type()
)
cooOlcApcGainRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOlcApcGainRange.setStatus("current")
_CooOlcApcLastCorrectionTimeStamp_Type = OctetString
_CooOlcApcLastCorrectionTimeStamp_Object = MibTableColumn
cooOlcApcLastCorrectionTimeStamp = _CooOlcApcLastCorrectionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 9),
    _CooOlcApcLastCorrectionTimeStamp_Type()
)
cooOlcApcLastCorrectionTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOlcApcLastCorrectionTimeStamp.setStatus("current")
_CooOlcNeighbourTable_Object = MibTable
cooOlcNeighbourTable = _CooOlcNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cooOlcNeighbourTable.setStatus("current")
_CooOlcNeighbourEntry_Object = MibTableRow
cooOlcNeighbourEntry = _CooOlcNeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1)
)
cooOlcNeighbourEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcNeighbourEntry.setStatus("current")
_CooOlcNbrIpAddr_Type = IpAddress
_CooOlcNbrIpAddr_Object = MibTableColumn
cooOlcNbrIpAddr = _CooOlcNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1, 1),
    _CooOlcNbrIpAddr_Type()
)
cooOlcNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcNbrIpAddr.setStatus("current")
_CooOlcNbrInterface_Type = InterfaceIndex
_CooOlcNbrInterface_Object = MibTableColumn
cooOlcNbrInterface = _CooOlcNbrInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1, 2),
    _CooOlcNbrInterface_Type()
)
cooOlcNbrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcNbrInterface.setStatus("current")
_CooOlcPartnerTable_Object = MibTable
cooOlcPartnerTable = _CooOlcPartnerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cooOlcPartnerTable.setStatus("current")
_CooOlcPartnerEntry_Object = MibTableRow
cooOlcPartnerEntry = _CooOlcPartnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1)
)
cooOlcPartnerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcPartnerEntry.setStatus("current")
_CooOlcPartnerIpAddr_Type = IpAddress
_CooOlcPartnerIpAddr_Object = MibTableColumn
cooOlcPartnerIpAddr = _CooOlcPartnerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1, 1),
    _CooOlcPartnerIpAddr_Type()
)
cooOlcPartnerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcPartnerIpAddr.setStatus("current")
_CooOlcPartnerInterface_Type = OctetString
_CooOlcPartnerInterface_Object = MibTableColumn
cooOlcPartnerInterface = _CooOlcPartnerInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1, 2),
    _CooOlcPartnerInterface_Type()
)
cooOlcPartnerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcPartnerInterface.setStatus("current")
_CooOlcPartnerBandLossTable_Object = MibTable
cooOlcPartnerBandLossTable = _CooOlcPartnerBandLossTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cooOlcPartnerBandLossTable.setStatus("current")
_CooOlcPartnerBandLossEntry_Object = MibTableRow
cooOlcPartnerBandLossEntry = _CooOlcPartnerBandLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1)
)
cooOlcPartnerBandLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOlcPartnerBandLossEntry.setStatus("current")
_CooOlcPathLoss_Type = CiscoOpticalOlcPower
_CooOlcPathLoss_Object = MibTableColumn
cooOlcPathLoss = _CooOlcPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 1),
    _CooOlcPathLoss_Type()
)
cooOlcPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcPathLoss.setStatus("current")
_CooOlcPatchcordLoss_Type = CiscoOpticalOlcPower
_CooOlcPatchcordLoss_Object = MibTableColumn
cooOlcPatchcordLoss = _CooOlcPatchcordLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 2),
    _CooOlcPatchcordLoss_Type()
)
cooOlcPatchcordLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcPatchcordLoss.setStatus("current")
_CooOlcLossMeasurementTimeStamp_Type = OctetString
_CooOlcLossMeasurementTimeStamp_Object = MibTableColumn
cooOlcLossMeasurementTimeStamp = _CooOlcLossMeasurementTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 3),
    _CooOlcLossMeasurementTimeStamp_Type()
)
cooOlcLossMeasurementTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOlcLossMeasurementTimeStamp.setStatus("current")
_CooOlcBandStatusTable_Object = MibTable
cooOlcBandStatusTable = _CooOlcBandStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cooOlcBandStatusTable.setStatus("current")
_CooOlcBandStatusEntry_Object = MibTableRow
cooOlcBandStatusEntry = _CooOlcBandStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1)
)
cooOlcBandStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-OLC-MIB", "cooOlcNodeNum"),
)
if mibBuilder.loadTexts:
    cooOlcBandStatusEntry.setStatus("current")
_CooOlcNodeNum_Type = Integer32
_CooOlcNodeNum_Object = MibTableColumn
cooOlcNodeNum = _CooOlcNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 1),
    _CooOlcNodeNum_Type()
)
cooOlcNodeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooOlcNodeNum.setStatus("current")
_CooOlcNodeRID_Type = IpAddress
_CooOlcNodeRID_Object = MibTableColumn
cooOlcNodeRID = _CooOlcNodeRID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 2),
    _CooOlcNodeRID_Type()
)
cooOlcNodeRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcNodeRID.setStatus("current")
_CooOlcBandStatus_Type = CiscoOpticalOlcBandStatus
_CooOlcBandStatus_Object = MibTableColumn
cooOlcBandStatus = _CooOlcBandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 3),
    _CooOlcBandStatus_Type()
)
cooOlcBandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcBandStatus.setStatus("current")
_CooOlcBandPSD_Type = CiscoOpticalOlcBandPSDType
_CooOlcBandPSD_Object = MibTableColumn
cooOlcBandPSD = _CooOlcBandPSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 4),
    _CooOlcBandPSD_Type()
)
cooOlcBandPSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOlcBandPSD.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-OLC-MIB",
    **{"CiscoOpticalOlcRamanTuningStatus": CiscoOpticalOlcRamanTuningStatus,
       "CiscoOpticalOlcRamanTuningFailReason": CiscoOpticalOlcRamanTuningFailReason,
       "CiscoOpticalOlcApcBlockReason": CiscoOpticalOlcApcBlockReason,
       "CiscoOpticalOlcPower": CiscoOpticalOlcPower,
       "CiscoOpticalOlcGainInDb": CiscoOpticalOlcGainInDb,
       "CiscoOpticalOlcPSDInDbm": CiscoOpticalOlcPSDInDbm,
       "CiscoOpticalOlcGainEstStatus": CiscoOpticalOlcGainEstStatus,
       "CiscoOpticalOlcApcAgentDirection": CiscoOpticalOlcApcAgentDirection,
       "CiscoOpticalOlcApcInternalState": CiscoOpticalOlcApcInternalState,
       "CiscoOpticalOlcApcManagerState": CiscoOpticalOlcApcManagerState,
       "CiscoOpticalOlcBandStatus": CiscoOpticalOlcBandStatus,
       "CiscoOpticalOlcBandPSDType": CiscoOpticalOlcBandPSDType,
       "ciscoOpticalOlcMIB": ciscoOpticalOlcMIB,
       "ciscoOpticalOlcMIBObjects": ciscoOpticalOlcMIBObjects,
       "cooOlcData": cooOlcData,
       "cooOlcSpanLossTable": cooOlcSpanLossTable,
       "cooOlcSpanLossEntry": cooOlcSpanLossEntry,
       "cooOlcRxSpanLoss": cooOlcRxSpanLoss,
       "cooOlcApparentRxSpanLoss": cooOlcApparentRxSpanLoss,
       "cooOlcRxSpanLossPumpsOff": cooOlcRxSpanLossPumpsOff,
       "cooOlcRxSpanLossPumpsOffTimeStamp": cooOlcRxSpanLossPumpsOffTimeStamp,
       "cooOlcEstimatedRxSpanLoss": cooOlcEstimatedRxSpanLoss,
       "cooOlcTxSpanLoss": cooOlcTxSpanLoss,
       "cooOlcApparentTxSpanLoss": cooOlcApparentTxSpanLoss,
       "cooOlcTxSpanLossPumpsOff": cooOlcTxSpanLossPumpsOff,
       "cooOlcTxSpanLossPumpsOffTimeStamp": cooOlcTxSpanLossPumpsOffTimeStamp,
       "cooOlcEstimatedTxSpanLoss": cooOlcEstimatedTxSpanLoss,
       "cooOlcRamanTuningTable": cooOlcRamanTuningTable,
       "cooOlcRamanTuningEntry": cooOlcRamanTuningEntry,
       "cooOlcRamanTuningStatus": cooOlcRamanTuningStatus,
       "cooOlcRamanTuningBlockedReason": cooOlcRamanTuningBlockedReason,
       "cooOlcRamanTuningFailedReason": cooOlcRamanTuningFailedReason,
       "cooOlcTuningCompleteTimeStamp": cooOlcTuningCompleteTimeStamp,
       "cooOlcEstimatedMaxPossibleGain": cooOlcEstimatedMaxPossibleGain,
       "cooOlcRamanGainTarget": cooOlcRamanGainTarget,
       "cooOlcGainAchievedOnTuningComplete": cooOlcGainAchievedOnTuningComplete,
       "cooOlcGainEstimatorTable": cooOlcGainEstimatorTable,
       "cooOlcGainEstimatorEntry": cooOlcGainEstimatorEntry,
       "cooOlcEgressGainEstStatus": cooOlcEgressGainEstStatus,
       "cooOlcEgressEstimatedGain": cooOlcEgressEstimatedGain,
       "cooOlcEgressEstimatedGainMode": cooOlcEgressEstimatedGainMode,
       "cooOlcEgressGainEstTimeStamp": cooOlcEgressGainEstTimeStamp,
       "cooOlcIngressGainEstStatus": cooOlcIngressGainEstStatus,
       "cooOlcIngressEstimatedGain": cooOlcIngressEstimatedGain,
       "cooOlcIngressEstimatedGainMode": cooOlcIngressEstimatedGainMode,
       "cooOlcIngressGainEstTimeStamp": cooOlcIngressGainEstTimeStamp,
       "cooOlcApcTable": cooOlcApcTable,
       "cooOlcApcEntry": cooOlcApcEntry,
       "cooOlcApcAgentDirection": cooOlcApcAgentDirection,
       "cooOlcApcDomainManager": cooOlcApcDomainManager,
       "cooOlcApcDomainManagerState": cooOlcApcDomainManagerState,
       "cooOlcApcDomainManagerBlockedReason": cooOlcApcDomainManagerBlockedReason,
       "cooOlcApcInternalState": cooOlcApcInternalState,
       "cooOlcApcBlockedReason": cooOlcApcBlockedReason,
       "cooOlcApcPsdMin": cooOlcApcPsdMin,
       "cooOlcApcGainRange": cooOlcApcGainRange,
       "cooOlcApcLastCorrectionTimeStamp": cooOlcApcLastCorrectionTimeStamp,
       "cooOlcNeighbourTable": cooOlcNeighbourTable,
       "cooOlcNeighbourEntry": cooOlcNeighbourEntry,
       "cooOlcNbrIpAddr": cooOlcNbrIpAddr,
       "cooOlcNbrInterface": cooOlcNbrInterface,
       "cooOlcPartnerTable": cooOlcPartnerTable,
       "cooOlcPartnerEntry": cooOlcPartnerEntry,
       "cooOlcPartnerIpAddr": cooOlcPartnerIpAddr,
       "cooOlcPartnerInterface": cooOlcPartnerInterface,
       "cooOlcPartnerBandLossTable": cooOlcPartnerBandLossTable,
       "cooOlcPartnerBandLossEntry": cooOlcPartnerBandLossEntry,
       "cooOlcPathLoss": cooOlcPathLoss,
       "cooOlcPatchcordLoss": cooOlcPatchcordLoss,
       "cooOlcLossMeasurementTimeStamp": cooOlcLossMeasurementTimeStamp,
       "cooOlcBandStatusTable": cooOlcBandStatusTable,
       "cooOlcBandStatusEntry": cooOlcBandStatusEntry,
       "cooOlcNodeNum": cooOlcNodeNum,
       "cooOlcNodeRID": cooOlcNodeRID,
       "cooOlcBandStatus": cooOlcBandStatus,
       "cooOlcBandPSD": cooOlcBandPSD}
)
