# SNMP MIB module (EFM-CU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IETF/EFM-CU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:24:44 2025
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

(ifIndex,
 ifSpeed) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifSpeed")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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


# MODULE-IDENTITY

efmCuMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 167)
)
if mibBuilder.loadTexts:
    efmCuMIB.setRevisions(
        ("2007-11-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EfmProfileIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class EfmProfileIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EfmProfileIndexList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class EfmTruthValueOrUnknown(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("true", 1),
          ("false", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EfmCuObjects_ObjectIdentity = ObjectIdentity
efmCuObjects = _EfmCuObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1)
)
_EfmCuPort_ObjectIdentity = ObjectIdentity
efmCuPort = _EfmCuPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 1)
)
_EfmCuPortNotifications_ObjectIdentity = ObjectIdentity
efmCuPortNotifications = _EfmCuPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 0)
)
_EfmCuPortConfTable_Object = MibTable
efmCuPortConfTable = _EfmCuPortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efmCuPortConfTable.setStatus("current")
_EfmCuPortConfEntry_Object = MibTableRow
efmCuPortConfEntry = _EfmCuPortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1)
)
efmCuPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortConfEntry.setStatus("current")


class _EfmCuPAFAdminState_Type(Integer32):
    """Custom type efmCuPAFAdminState based on Integer32"""
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


_EfmCuPAFAdminState_Type.__name__ = "Integer32"
_EfmCuPAFAdminState_Object = MibTableColumn
efmCuPAFAdminState = _EfmCuPAFAdminState_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 1),
    _EfmCuPAFAdminState_Type()
)
efmCuPAFAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFAdminState.setStatus("current")


class _EfmCuPAFDiscoveryCode_Type(PhysAddress):
    """Custom type efmCuPAFDiscoveryCode based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_EfmCuPAFDiscoveryCode_Type.__name__ = "PhysAddress"
_EfmCuPAFDiscoveryCode_Object = MibTableColumn
efmCuPAFDiscoveryCode = _EfmCuPAFDiscoveryCode_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 2),
    _EfmCuPAFDiscoveryCode_Type()
)
efmCuPAFDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFDiscoveryCode.setStatus("current")


class _EfmCuAdminProfile_Type(EfmProfileIndexList):
    """Custom type efmCuAdminProfile based on EfmProfileIndexList"""
    defaultHexValue = "01"


_EfmCuAdminProfile_Type.__name__ = "EfmProfileIndexList"
_EfmCuAdminProfile_Object = MibTableColumn
efmCuAdminProfile = _EfmCuAdminProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 3),
    _EfmCuAdminProfile_Type()
)
efmCuAdminProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuAdminProfile.setStatus("current")


class _EfmCuTargetDataRate_Type(Unsigned32):
    """Custom type efmCuTargetDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
        ValueRangeConstraint(999999, 999999),
    )


_EfmCuTargetDataRate_Type.__name__ = "Unsigned32"
_EfmCuTargetDataRate_Object = MibTableColumn
efmCuTargetDataRate = _EfmCuTargetDataRate_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 4),
    _EfmCuTargetDataRate_Type()
)
efmCuTargetDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuTargetDataRate.setUnits("Kbps")


class _EfmCuTargetSnrMgn_Type(Unsigned32):
    """Custom type efmCuTargetSnrMgn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_EfmCuTargetSnrMgn_Type.__name__ = "Unsigned32"
_EfmCuTargetSnrMgn_Object = MibTableColumn
efmCuTargetSnrMgn = _EfmCuTargetSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 5),
    _EfmCuTargetSnrMgn_Type()
)
efmCuTargetSnrMgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuTargetSnrMgn.setUnits("dB")
_EfmCuAdaptiveSpectra_Type = TruthValue
_EfmCuAdaptiveSpectra_Object = MibTableColumn
efmCuAdaptiveSpectra = _EfmCuAdaptiveSpectra_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 6),
    _EfmCuAdaptiveSpectra_Type()
)
efmCuAdaptiveSpectra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuAdaptiveSpectra.setStatus("current")


class _EfmCuThreshLowRate_Type(Unsigned32):
    """Custom type efmCuThreshLowRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_EfmCuThreshLowRate_Type.__name__ = "Unsigned32"
_EfmCuThreshLowRate_Object = MibTableColumn
efmCuThreshLowRate = _EfmCuThreshLowRate_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 7),
    _EfmCuThreshLowRate_Type()
)
efmCuThreshLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuThreshLowRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuThreshLowRate.setUnits("Kbps")
_EfmCuLowRateCrossingEnable_Type = TruthValue
_EfmCuLowRateCrossingEnable_Object = MibTableColumn
efmCuLowRateCrossingEnable = _EfmCuLowRateCrossingEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 1, 1, 8),
    _EfmCuLowRateCrossingEnable_Type()
)
efmCuLowRateCrossingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuLowRateCrossingEnable.setStatus("current")
_EfmCuPortCapabilityTable_Object = MibTable
efmCuPortCapabilityTable = _EfmCuPortCapabilityTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2)
)
if mibBuilder.loadTexts:
    efmCuPortCapabilityTable.setStatus("current")
_EfmCuPortCapabilityEntry_Object = MibTableRow
efmCuPortCapabilityEntry = _EfmCuPortCapabilityEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2, 1)
)
efmCuPortCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortCapabilityEntry.setStatus("current")
_EfmCuPAFSupported_Type = TruthValue
_EfmCuPAFSupported_Object = MibTableColumn
efmCuPAFSupported = _EfmCuPAFSupported_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2, 1, 1),
    _EfmCuPAFSupported_Type()
)
efmCuPAFSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFSupported.setStatus("current")
_EfmCuPeerPAFSupported_Type = EfmTruthValueOrUnknown
_EfmCuPeerPAFSupported_Object = MibTableColumn
efmCuPeerPAFSupported = _EfmCuPeerPAFSupported_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2, 1, 2),
    _EfmCuPeerPAFSupported_Type()
)
efmCuPeerPAFSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPeerPAFSupported.setStatus("current")


class _EfmCuPAFCapacity_Type(Unsigned32):
    """Custom type efmCuPAFCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_EfmCuPAFCapacity_Type.__name__ = "Unsigned32"
_EfmCuPAFCapacity_Object = MibTableColumn
efmCuPAFCapacity = _EfmCuPAFCapacity_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2, 1, 3),
    _EfmCuPAFCapacity_Type()
)
efmCuPAFCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFCapacity.setStatus("current")


class _EfmCuPeerPAFCapacity_Type(Unsigned32):
    """Custom type efmCuPeerPAFCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_EfmCuPeerPAFCapacity_Type.__name__ = "Unsigned32"
_EfmCuPeerPAFCapacity_Object = MibTableColumn
efmCuPeerPAFCapacity = _EfmCuPeerPAFCapacity_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 2, 1, 4),
    _EfmCuPeerPAFCapacity_Type()
)
efmCuPeerPAFCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPeerPAFCapacity.setStatus("current")
_EfmCuPortStatusTable_Object = MibTable
efmCuPortStatusTable = _EfmCuPortStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3)
)
if mibBuilder.loadTexts:
    efmCuPortStatusTable.setStatus("current")
_EfmCuPortStatusEntry_Object = MibTableRow
efmCuPortStatusEntry = _EfmCuPortStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1)
)
efmCuPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortStatusEntry.setStatus("current")


class _EfmCuFltStatus_Type(Bits):
    """Custom type efmCuFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("noPeer", 0),
          ("peerPowerLoss", 1),
          ("pmeSubTypeMismatch", 2),
          ("lowRate", 3))
    )

_EfmCuFltStatus_Type.__name__ = "Bits"
_EfmCuFltStatus_Object = MibTableColumn
efmCuFltStatus = _EfmCuFltStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 1),
    _EfmCuFltStatus_Type()
)
efmCuFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuFltStatus.setStatus("current")


class _EfmCuPortSide_Type(Integer32):
    """Custom type efmCuPortSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("subscriber", 1),
          ("office", 2),
          ("unknown", 3))
    )


_EfmCuPortSide_Type.__name__ = "Integer32"
_EfmCuPortSide_Object = MibTableColumn
efmCuPortSide = _EfmCuPortSide_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 2),
    _EfmCuPortSide_Type()
)
efmCuPortSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPortSide.setStatus("current")


class _EfmCuNumPMEs_Type(Unsigned32):
    """Custom type efmCuNumPMEs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EfmCuNumPMEs_Type.__name__ = "Unsigned32"
_EfmCuNumPMEs_Object = MibTableColumn
efmCuNumPMEs = _EfmCuNumPMEs_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 3),
    _EfmCuNumPMEs_Type()
)
efmCuNumPMEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuNumPMEs.setStatus("current")
_EfmCuPAFInErrors_Type = Counter32
_EfmCuPAFInErrors_Object = MibTableColumn
efmCuPAFInErrors = _EfmCuPAFInErrors_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 4),
    _EfmCuPAFInErrors_Type()
)
efmCuPAFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInErrors.setStatus("current")
_EfmCuPAFInSmallFragments_Type = Counter32
_EfmCuPAFInSmallFragments_Object = MibTableColumn
efmCuPAFInSmallFragments = _EfmCuPAFInSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 5),
    _EfmCuPAFInSmallFragments_Type()
)
efmCuPAFInSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInSmallFragments.setStatus("current")
_EfmCuPAFInLargeFragments_Type = Counter32
_EfmCuPAFInLargeFragments_Object = MibTableColumn
efmCuPAFInLargeFragments = _EfmCuPAFInLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 6),
    _EfmCuPAFInLargeFragments_Type()
)
efmCuPAFInLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLargeFragments.setStatus("current")
_EfmCuPAFInBadFragments_Type = Counter32
_EfmCuPAFInBadFragments_Object = MibTableColumn
efmCuPAFInBadFragments = _EfmCuPAFInBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 7),
    _EfmCuPAFInBadFragments_Type()
)
efmCuPAFInBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInBadFragments.setStatus("current")
_EfmCuPAFInLostFragments_Type = Counter32
_EfmCuPAFInLostFragments_Object = MibTableColumn
efmCuPAFInLostFragments = _EfmCuPAFInLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 8),
    _EfmCuPAFInLostFragments_Type()
)
efmCuPAFInLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostFragments.setStatus("current")
_EfmCuPAFInLostStarts_Type = Counter32
_EfmCuPAFInLostStarts_Object = MibTableColumn
efmCuPAFInLostStarts = _EfmCuPAFInLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 9),
    _EfmCuPAFInLostStarts_Type()
)
efmCuPAFInLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostStarts.setStatus("current")
_EfmCuPAFInLostEnds_Type = Counter32
_EfmCuPAFInLostEnds_Object = MibTableColumn
efmCuPAFInLostEnds = _EfmCuPAFInLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 10),
    _EfmCuPAFInLostEnds_Type()
)
efmCuPAFInLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostEnds.setStatus("current")
_EfmCuPAFInOverflows_Type = Counter32
_EfmCuPAFInOverflows_Object = MibTableColumn
efmCuPAFInOverflows = _EfmCuPAFInOverflows_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 3, 1, 11),
    _EfmCuPAFInOverflows_Type()
)
efmCuPAFInOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInOverflows.setStatus("current")
_EfmCuPme_ObjectIdentity = ObjectIdentity
efmCuPme = _EfmCuPme_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 2)
)
_EfmCuPmeNotifications_ObjectIdentity = ObjectIdentity
efmCuPmeNotifications = _EfmCuPmeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0)
)
_EfmCuPmeConfTable_Object = MibTable
efmCuPmeConfTable = _EfmCuPmeConfTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1)
)
if mibBuilder.loadTexts:
    efmCuPmeConfTable.setStatus("current")
_EfmCuPmeConfEntry_Object = MibTableRow
efmCuPmeConfEntry = _EfmCuPmeConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1)
)
efmCuPmeConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeConfEntry.setStatus("current")


class _EfmCuPmeAdminSubType_Type(Integer32):
    """Custom type efmCuPmeAdminSubType based on Integer32"""
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
        *(("ieee2BaseTLO", 1),
          ("ieee2BaseTLR", 2),
          ("ieee10PassTSO", 3),
          ("ieee10PassTSR", 4),
          ("ieee2BaseTLor10PassTSR", 5),
          ("ieee2BaseTLor10PassTSO", 6),
          ("ieee10PassTSor2BaseTLO", 7))
    )


_EfmCuPmeAdminSubType_Type.__name__ = "Integer32"
_EfmCuPmeAdminSubType_Object = MibTableColumn
efmCuPmeAdminSubType = _EfmCuPmeAdminSubType_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 1),
    _EfmCuPmeAdminSubType_Type()
)
efmCuPmeAdminSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeAdminSubType.setStatus("current")


class _EfmCuPmeAdminProfile_Type(EfmProfileIndexOrZero):
    """Custom type efmCuPmeAdminProfile based on EfmProfileIndexOrZero"""
    defaultValue = 0


_EfmCuPmeAdminProfile_Type.__name__ = "EfmProfileIndexOrZero"
_EfmCuPmeAdminProfile_Object = MibTableColumn
efmCuPmeAdminProfile = _EfmCuPmeAdminProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 2),
    _EfmCuPmeAdminProfile_Type()
)
efmCuPmeAdminProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeAdminProfile.setStatus("current")


class _EfmCuPAFRemoteDiscoveryCode_Type(PhysAddress):
    """Custom type efmCuPAFRemoteDiscoveryCode based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_EfmCuPAFRemoteDiscoveryCode_Type.__name__ = "PhysAddress"
_EfmCuPAFRemoteDiscoveryCode_Object = MibTableColumn
efmCuPAFRemoteDiscoveryCode = _EfmCuPAFRemoteDiscoveryCode_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 3),
    _EfmCuPAFRemoteDiscoveryCode_Type()
)
efmCuPAFRemoteDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFRemoteDiscoveryCode.setStatus("current")


class _EfmCuPmeThreshLineAtn_Type(Integer32):
    """Custom type efmCuPmeThreshLineAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EfmCuPmeThreshLineAtn_Type.__name__ = "Integer32"
_EfmCuPmeThreshLineAtn_Object = MibTableColumn
efmCuPmeThreshLineAtn = _EfmCuPmeThreshLineAtn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 4),
    _EfmCuPmeThreshLineAtn_Type()
)
efmCuPmeThreshLineAtn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeThreshLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeThreshLineAtn.setUnits("dB")


class _EfmCuPmeThreshSnrMgn_Type(Integer32):
    """Custom type efmCuPmeThreshSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EfmCuPmeThreshSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmeThreshSnrMgn_Object = MibTableColumn
efmCuPmeThreshSnrMgn = _EfmCuPmeThreshSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 5),
    _EfmCuPmeThreshSnrMgn_Type()
)
efmCuPmeThreshSnrMgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeThreshSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeThreshSnrMgn.setUnits("dB")
_EfmCuPmeLineAtnCrossingEnable_Type = TruthValue
_EfmCuPmeLineAtnCrossingEnable_Object = MibTableColumn
efmCuPmeLineAtnCrossingEnable = _EfmCuPmeLineAtnCrossingEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 6),
    _EfmCuPmeLineAtnCrossingEnable_Type()
)
efmCuPmeLineAtnCrossingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeLineAtnCrossingEnable.setStatus("current")
_EfmCuPmeSnrMgnCrossingEnable_Type = TruthValue
_EfmCuPmeSnrMgnCrossingEnable_Object = MibTableColumn
efmCuPmeSnrMgnCrossingEnable = _EfmCuPmeSnrMgnCrossingEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 7),
    _EfmCuPmeSnrMgnCrossingEnable_Type()
)
efmCuPmeSnrMgnCrossingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgnCrossingEnable.setStatus("current")
_EfmCuPmeDeviceFaultEnable_Type = TruthValue
_EfmCuPmeDeviceFaultEnable_Object = MibTableColumn
efmCuPmeDeviceFaultEnable = _EfmCuPmeDeviceFaultEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 8),
    _EfmCuPmeDeviceFaultEnable_Type()
)
efmCuPmeDeviceFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeDeviceFaultEnable.setStatus("current")
_EfmCuPmeConfigInitFailEnable_Type = TruthValue
_EfmCuPmeConfigInitFailEnable_Object = MibTableColumn
efmCuPmeConfigInitFailEnable = _EfmCuPmeConfigInitFailEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 9),
    _EfmCuPmeConfigInitFailEnable_Type()
)
efmCuPmeConfigInitFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeConfigInitFailEnable.setStatus("current")
_EfmCuPmeProtocolInitFailEnable_Type = TruthValue
_EfmCuPmeProtocolInitFailEnable_Object = MibTableColumn
efmCuPmeProtocolInitFailEnable = _EfmCuPmeProtocolInitFailEnable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 1, 1, 10),
    _EfmCuPmeProtocolInitFailEnable_Type()
)
efmCuPmeProtocolInitFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeProtocolInitFailEnable.setStatus("current")
_EfmCuPmeCapabilityTable_Object = MibTable
efmCuPmeCapabilityTable = _EfmCuPmeCapabilityTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 2)
)
if mibBuilder.loadTexts:
    efmCuPmeCapabilityTable.setStatus("current")
_EfmCuPmeCapabilityEntry_Object = MibTableRow
efmCuPmeCapabilityEntry = _EfmCuPmeCapabilityEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 2, 1)
)
efmCuPmeCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeCapabilityEntry.setStatus("current")


class _EfmCuPmeSubTypesSupported_Type(Bits):
    """Custom type efmCuPmeSubTypesSupported based on Bits"""
    namedValues = NamedValues(
        *(("ieee2BaseTLO", 0),
          ("ieee2BaseTLR", 1),
          ("ieee10PassTSO", 2),
          ("ieee10PassTSR", 3))
    )

_EfmCuPmeSubTypesSupported_Type.__name__ = "Bits"
_EfmCuPmeSubTypesSupported_Object = MibTableColumn
efmCuPmeSubTypesSupported = _EfmCuPmeSubTypesSupported_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 2, 1, 1),
    _EfmCuPmeSubTypesSupported_Type()
)
efmCuPmeSubTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSubTypesSupported.setStatus("current")
_EfmCuPmeStatusTable_Object = MibTable
efmCuPmeStatusTable = _EfmCuPmeStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3)
)
if mibBuilder.loadTexts:
    efmCuPmeStatusTable.setStatus("current")
_EfmCuPmeStatusEntry_Object = MibTableRow
efmCuPmeStatusEntry = _EfmCuPmeStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1)
)
efmCuPmeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeStatusEntry.setStatus("current")


class _EfmCuPmeOperStatus_Type(Integer32):
    """Custom type efmCuPmeOperStatus based on Integer32"""
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
        *(("up", 1),
          ("downNotReady", 2),
          ("downReady", 3),
          ("init", 4))
    )


_EfmCuPmeOperStatus_Type.__name__ = "Integer32"
_EfmCuPmeOperStatus_Object = MibTableColumn
efmCuPmeOperStatus = _EfmCuPmeOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 1),
    _EfmCuPmeOperStatus_Type()
)
efmCuPmeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperStatus.setStatus("current")


class _EfmCuPmeFltStatus_Type(Bits):
    """Custom type efmCuPmeFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("lossOfFraming", 0),
          ("snrMgnDefect", 1),
          ("lineAtnDefect", 2),
          ("deviceFault", 3),
          ("configInitFailure", 4),
          ("protocolInitFailure", 5))
    )

_EfmCuPmeFltStatus_Type.__name__ = "Bits"
_EfmCuPmeFltStatus_Object = MibTableColumn
efmCuPmeFltStatus = _EfmCuPmeFltStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 2),
    _EfmCuPmeFltStatus_Type()
)
efmCuPmeFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeFltStatus.setStatus("current")


class _EfmCuPmeOperSubType_Type(Integer32):
    """Custom type efmCuPmeOperSubType based on Integer32"""
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
        *(("ieee2BaseTLO", 1),
          ("ieee2BaseTLR", 2),
          ("ieee10PassTSO", 3),
          ("ieee10PassTSR", 4))
    )


_EfmCuPmeOperSubType_Type.__name__ = "Integer32"
_EfmCuPmeOperSubType_Object = MibTableColumn
efmCuPmeOperSubType = _EfmCuPmeOperSubType_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 3),
    _EfmCuPmeOperSubType_Type()
)
efmCuPmeOperSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperSubType.setStatus("current")
_EfmCuPmeOperProfile_Type = EfmProfileIndexOrZero
_EfmCuPmeOperProfile_Object = MibTableColumn
efmCuPmeOperProfile = _EfmCuPmeOperProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 4),
    _EfmCuPmeOperProfile_Type()
)
efmCuPmeOperProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperProfile.setStatus("current")


class _EfmCuPmeSnrMgn_Type(Integer32):
    """Custom type efmCuPmeSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmeSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmeSnrMgn_Object = MibTableColumn
efmCuPmeSnrMgn = _EfmCuPmeSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 5),
    _EfmCuPmeSnrMgn_Type()
)
efmCuPmeSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgn.setUnits("dB")


class _EfmCuPmePeerSnrMgn_Type(Integer32):
    """Custom type efmCuPmePeerSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmePeerSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmePeerSnrMgn_Object = MibTableColumn
efmCuPmePeerSnrMgn = _EfmCuPmePeerSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 6),
    _EfmCuPmePeerSnrMgn_Type()
)
efmCuPmePeerSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmePeerSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmePeerSnrMgn.setUnits("dB")


class _EfmCuPmeLineAtn_Type(Integer32):
    """Custom type efmCuPmeLineAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmeLineAtn_Type.__name__ = "Integer32"
_EfmCuPmeLineAtn_Object = MibTableColumn
efmCuPmeLineAtn = _EfmCuPmeLineAtn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 7),
    _EfmCuPmeLineAtn_Type()
)
efmCuPmeLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeLineAtn.setUnits("dB")


class _EfmCuPmePeerLineAtn_Type(Integer32):
    """Custom type efmCuPmePeerLineAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmePeerLineAtn_Type.__name__ = "Integer32"
_EfmCuPmePeerLineAtn_Object = MibTableColumn
efmCuPmePeerLineAtn = _EfmCuPmePeerLineAtn_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 8),
    _EfmCuPmePeerLineAtn_Type()
)
efmCuPmePeerLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmePeerLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmePeerLineAtn.setUnits("dB")


class _EfmCuPmeEquivalentLength_Type(Unsigned32):
    """Custom type efmCuPmeEquivalentLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmeEquivalentLength_Type.__name__ = "Unsigned32"
_EfmCuPmeEquivalentLength_Object = MibTableColumn
efmCuPmeEquivalentLength = _EfmCuPmeEquivalentLength_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 9),
    _EfmCuPmeEquivalentLength_Type()
)
efmCuPmeEquivalentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeEquivalentLength.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeEquivalentLength.setUnits("m")
_EfmCuPmeTCCodingErrors_Type = Counter32
_EfmCuPmeTCCodingErrors_Object = MibTableColumn
efmCuPmeTCCodingErrors = _EfmCuPmeTCCodingErrors_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 10),
    _EfmCuPmeTCCodingErrors_Type()
)
efmCuPmeTCCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeTCCodingErrors.setStatus("current")
_EfmCuPmeTCCrcErrors_Type = Counter32
_EfmCuPmeTCCrcErrors_Object = MibTableColumn
efmCuPmeTCCrcErrors = _EfmCuPmeTCCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 3, 1, 11),
    _EfmCuPmeTCCrcErrors_Type()
)
efmCuPmeTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeTCCrcErrors.setStatus("current")
_EfmCuPme2B_ObjectIdentity = ObjectIdentity
efmCuPme2B = _EfmCuPme2B_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5)
)
_EfmCuPme2BProfileTable_Object = MibTable
efmCuPme2BProfileTable = _EfmCuPme2BProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileTable.setStatus("current")
_EfmCuPme2BProfileEntry_Object = MibTableRow
efmCuPme2BProfileEntry = _EfmCuPme2BProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1)
)
efmCuPme2BProfileEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme2BProfileIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileEntry.setStatus("current")
_EfmCuPme2BProfileIndex_Type = EfmProfileIndex
_EfmCuPme2BProfileIndex_Object = MibTableColumn
efmCuPme2BProfileIndex = _EfmCuPme2BProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 1),
    _EfmCuPme2BProfileIndex_Type()
)
efmCuPme2BProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme2BProfileIndex.setStatus("current")
_EfmCuPme2BProfileDescr_Type = SnmpAdminString
_EfmCuPme2BProfileDescr_Object = MibTableColumn
efmCuPme2BProfileDescr = _EfmCuPme2BProfileDescr_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 2),
    _EfmCuPme2BProfileDescr_Type()
)
efmCuPme2BProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BProfileDescr.setStatus("current")


class _EfmCuPme2BRegion_Type(Integer32):
    """Custom type efmCuPme2BRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("region1", 1),
          ("region2", 2))
    )


_EfmCuPme2BRegion_Type.__name__ = "Integer32"
_EfmCuPme2BRegion_Object = MibTableColumn
efmCuPme2BRegion = _EfmCuPme2BRegion_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 3),
    _EfmCuPme2BRegion_Type()
)
efmCuPme2BRegion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BRegion.setStatus("current")


class _EfmCuPme2BsMode_Type(EfmProfileIndexOrZero):
    """Custom type efmCuPme2BsMode based on EfmProfileIndexOrZero"""
    defaultValue = 0


_EfmCuPme2BsMode_Type.__name__ = "EfmProfileIndexOrZero"
_EfmCuPme2BsMode_Object = MibTableColumn
efmCuPme2BsMode = _EfmCuPme2BsMode_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 4),
    _EfmCuPme2BsMode_Type()
)
efmCuPme2BsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BsMode.setStatus("current")


class _EfmCuPme2BMinDataRate_Type(Unsigned32):
    """Custom type efmCuPme2BMinDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 5696),
    )


_EfmCuPme2BMinDataRate_Type.__name__ = "Unsigned32"
_EfmCuPme2BMinDataRate_Object = MibTableColumn
efmCuPme2BMinDataRate = _EfmCuPme2BMinDataRate_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 5),
    _EfmCuPme2BMinDataRate_Type()
)
efmCuPme2BMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BMinDataRate.setUnits("Kbps")


class _EfmCuPme2BMaxDataRate_Type(Unsigned32):
    """Custom type efmCuPme2BMaxDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 5696),
    )


_EfmCuPme2BMaxDataRate_Type.__name__ = "Unsigned32"
_EfmCuPme2BMaxDataRate_Object = MibTableColumn
efmCuPme2BMaxDataRate = _EfmCuPme2BMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 6),
    _EfmCuPme2BMaxDataRate_Type()
)
efmCuPme2BMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRate.setUnits("Kbps")


class _EfmCuPme2BPower_Type(Unsigned32):
    """Custom type efmCuPme2BPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 42),
    )


_EfmCuPme2BPower_Type.__name__ = "Unsigned32"
_EfmCuPme2BPower_Object = MibTableColumn
efmCuPme2BPower = _EfmCuPme2BPower_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 7),
    _EfmCuPme2BPower_Type()
)
efmCuPme2BPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BPower.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BPower.setUnits("0.5 dBm")


class _EfmCuPme2BConstellation_Type(Integer32):
    """Custom type efmCuPme2BConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 0),
          ("tcpam16", 1),
          ("tcpam32", 2))
    )


_EfmCuPme2BConstellation_Type.__name__ = "Integer32"
_EfmCuPme2BConstellation_Object = MibTableColumn
efmCuPme2BConstellation = _EfmCuPme2BConstellation_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 8),
    _EfmCuPme2BConstellation_Type()
)
efmCuPme2BConstellation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BConstellation.setStatus("current")
_EfmCuPme2BProfileRowStatus_Type = RowStatus
_EfmCuPme2BProfileRowStatus_Object = MibTableColumn
efmCuPme2BProfileRowStatus = _EfmCuPme2BProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 2, 1, 9),
    _EfmCuPme2BProfileRowStatus_Type()
)
efmCuPme2BProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BProfileRowStatus.setStatus("current")
_EfmCuPme2BsModeTable_Object = MibTable
efmCuPme2BsModeTable = _EfmCuPme2BsModeTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    efmCuPme2BsModeTable.setStatus("current")
_EfmCuPme2BsModeEntry_Object = MibTableRow
efmCuPme2BsModeEntry = _EfmCuPme2BsModeEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 3, 1)
)
efmCuPme2BsModeEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme2BsModeIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme2BsModeEntry.setStatus("current")
_EfmCuPme2BsModeIndex_Type = EfmProfileIndex
_EfmCuPme2BsModeIndex_Object = MibTableColumn
efmCuPme2BsModeIndex = _EfmCuPme2BsModeIndex_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 3, 1, 1),
    _EfmCuPme2BsModeIndex_Type()
)
efmCuPme2BsModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme2BsModeIndex.setStatus("current")
_EfmCuPme2BsModeDescr_Type = SnmpAdminString
_EfmCuPme2BsModeDescr_Object = MibTableColumn
efmCuPme2BsModeDescr = _EfmCuPme2BsModeDescr_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 3, 1, 2),
    _EfmCuPme2BsModeDescr_Type()
)
efmCuPme2BsModeDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BsModeDescr.setStatus("current")
_EfmCuPme2BsModeRowStatus_Type = RowStatus
_EfmCuPme2BsModeRowStatus_Object = MibTableColumn
efmCuPme2BsModeRowStatus = _EfmCuPme2BsModeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 3, 1, 3),
    _EfmCuPme2BsModeRowStatus_Type()
)
efmCuPme2BsModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BsModeRowStatus.setStatus("current")
_EfmCuPme2BReachRateTable_Object = MibTable
efmCuPme2BReachRateTable = _EfmCuPme2BReachRateTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    efmCuPme2BReachRateTable.setStatus("current")
_EfmCuPme2BReachRateEntry_Object = MibTableRow
efmCuPme2BReachRateEntry = _EfmCuPme2BReachRateEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1)
)
efmCuPme2BReachRateEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme2BsModeIndex"),
    (0, "EFM-CU-MIB", "efmCuPme2BReachRateIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme2BReachRateEntry.setStatus("current")
_EfmCuPme2BReachRateIndex_Type = EfmProfileIndex
_EfmCuPme2BReachRateIndex_Object = MibTableColumn
efmCuPme2BReachRateIndex = _EfmCuPme2BReachRateIndex_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1, 1),
    _EfmCuPme2BReachRateIndex_Type()
)
efmCuPme2BReachRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme2BReachRateIndex.setStatus("current")


class _EfmCuPme2BEquivalentLength_Type(Unsigned32):
    """Custom type efmCuPme2BEquivalentLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_EfmCuPme2BEquivalentLength_Type.__name__ = "Unsigned32"
_EfmCuPme2BEquivalentLength_Object = MibTableColumn
efmCuPme2BEquivalentLength = _EfmCuPme2BEquivalentLength_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1, 2),
    _EfmCuPme2BEquivalentLength_Type()
)
efmCuPme2BEquivalentLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BEquivalentLength.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BEquivalentLength.setUnits("m")


class _EfmCuPme2BMaxDataRatePam16_Type(Unsigned32):
    """Custom type efmCuPme2BMaxDataRatePam16 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(192, 5696),
    )


_EfmCuPme2BMaxDataRatePam16_Type.__name__ = "Unsigned32"
_EfmCuPme2BMaxDataRatePam16_Object = MibTableColumn
efmCuPme2BMaxDataRatePam16 = _EfmCuPme2BMaxDataRatePam16_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1, 3),
    _EfmCuPme2BMaxDataRatePam16_Type()
)
efmCuPme2BMaxDataRatePam16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRatePam16.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRatePam16.setUnits("Kbps")


class _EfmCuPme2BMaxDataRatePam32_Type(Unsigned32):
    """Custom type efmCuPme2BMaxDataRatePam32 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(192, 5696),
    )


_EfmCuPme2BMaxDataRatePam32_Type.__name__ = "Unsigned32"
_EfmCuPme2BMaxDataRatePam32_Object = MibTableColumn
efmCuPme2BMaxDataRatePam32 = _EfmCuPme2BMaxDataRatePam32_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1, 4),
    _EfmCuPme2BMaxDataRatePam32_Type()
)
efmCuPme2BMaxDataRatePam32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRatePam32.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BMaxDataRatePam32.setUnits("Kbps")
_EfmCuPme2BReachRateRowStatus_Type = RowStatus
_EfmCuPme2BReachRateRowStatus_Object = MibTableColumn
efmCuPme2BReachRateRowStatus = _EfmCuPme2BReachRateRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 5, 4, 1, 5),
    _EfmCuPme2BReachRateRowStatus_Type()
)
efmCuPme2BReachRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BReachRateRowStatus.setStatus("current")
_EfmCuPme10P_ObjectIdentity = ObjectIdentity
efmCuPme10P = _EfmCuPme10P_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6)
)
_EfmCuPme10PProfileTable_Object = MibTable
efmCuPme10PProfileTable = _EfmCuPme10PProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileTable.setStatus("current")
_EfmCuPme10PProfileEntry_Object = MibTableRow
efmCuPme10PProfileEntry = _EfmCuPme10PProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1)
)
efmCuPme10PProfileEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme10PProfileIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileEntry.setStatus("current")
_EfmCuPme10PProfileIndex_Type = EfmProfileIndex
_EfmCuPme10PProfileIndex_Object = MibTableColumn
efmCuPme10PProfileIndex = _EfmCuPme10PProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 1),
    _EfmCuPme10PProfileIndex_Type()
)
efmCuPme10PProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme10PProfileIndex.setStatus("current")
_EfmCuPme10PProfileDescr_Type = SnmpAdminString
_EfmCuPme10PProfileDescr_Object = MibTableColumn
efmCuPme10PProfileDescr = _EfmCuPme10PProfileDescr_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 2),
    _EfmCuPme10PProfileDescr_Type()
)
efmCuPme10PProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PProfileDescr.setStatus("current")


class _EfmCuPme10PBandplanPSDMskProfile_Type(Integer32):
    """Custom type efmCuPme10PBandplanPSDMskProfile based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9),
          ("profile10", 10),
          ("profile11", 11),
          ("profile12", 12),
          ("profile13", 13),
          ("profile14", 14),
          ("profile15", 15),
          ("profile16", 16),
          ("profile17", 17),
          ("profile18", 18),
          ("profile19", 19),
          ("profile20", 20),
          ("profile21", 21),
          ("profile22", 22),
          ("profile23", 23),
          ("profile24", 24),
          ("profile25", 25),
          ("profile26", 26),
          ("profile27", 27),
          ("profile28", 28),
          ("profile29", 29),
          ("profile30", 30))
    )


_EfmCuPme10PBandplanPSDMskProfile_Type.__name__ = "Integer32"
_EfmCuPme10PBandplanPSDMskProfile_Object = MibTableColumn
efmCuPme10PBandplanPSDMskProfile = _EfmCuPme10PBandplanPSDMskProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 3),
    _EfmCuPme10PBandplanPSDMskProfile_Type()
)
efmCuPme10PBandplanPSDMskProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PBandplanPSDMskProfile.setStatus("current")


class _EfmCuPme10PUPBOReferenceProfile_Type(Integer32):
    """Custom type efmCuPme10PUPBOReferenceProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("profile0", 0),
          ("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9))
    )


_EfmCuPme10PUPBOReferenceProfile_Type.__name__ = "Integer32"
_EfmCuPme10PUPBOReferenceProfile_Object = MibTableColumn
efmCuPme10PUPBOReferenceProfile = _EfmCuPme10PUPBOReferenceProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 4),
    _EfmCuPme10PUPBOReferenceProfile_Type()
)
efmCuPme10PUPBOReferenceProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PUPBOReferenceProfile.setStatus("current")


class _EfmCuPme10PBandNotchProfiles_Type(Bits):
    """Custom type efmCuPme10PBandNotchProfiles based on Bits"""
    namedValues = NamedValues(
        *(("profile0", 0),
          ("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9),
          ("profile10", 10),
          ("profile11", 11))
    )

_EfmCuPme10PBandNotchProfiles_Type.__name__ = "Bits"
_EfmCuPme10PBandNotchProfiles_Object = MibTableColumn
efmCuPme10PBandNotchProfiles = _EfmCuPme10PBandNotchProfiles_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 5),
    _EfmCuPme10PBandNotchProfiles_Type()
)
efmCuPme10PBandNotchProfiles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PBandNotchProfiles.setStatus("current")


class _EfmCuPme10PPayloadDRateProfile_Type(Integer32):
    """Custom type efmCuPme10PPayloadDRateProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              50,
              70,
              100,
              140,
              200)
        )
    )
    namedValues = NamedValues(
        *(("profile5", 5),
          ("profile10", 10),
          ("profile15", 15),
          ("profile20", 20),
          ("profile25", 25),
          ("profile30", 30),
          ("profile50", 50),
          ("profile70", 70),
          ("profile100", 100),
          ("profile140", 140),
          ("profile200", 200))
    )


_EfmCuPme10PPayloadDRateProfile_Type.__name__ = "Integer32"
_EfmCuPme10PPayloadDRateProfile_Object = MibTableColumn
efmCuPme10PPayloadDRateProfile = _EfmCuPme10PPayloadDRateProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 6),
    _EfmCuPme10PPayloadDRateProfile_Type()
)
efmCuPme10PPayloadDRateProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PPayloadDRateProfile.setStatus("current")


class _EfmCuPme10PPayloadURateProfile_Type(Integer32):
    """Custom type efmCuPme10PPayloadURateProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              50,
              70,
              100)
        )
    )
    namedValues = NamedValues(
        *(("profile5", 5),
          ("profile10", 10),
          ("profile15", 15),
          ("profile20", 20),
          ("profile25", 25),
          ("profile30", 30),
          ("profile50", 50),
          ("profile70", 70),
          ("profile100", 100))
    )


_EfmCuPme10PPayloadURateProfile_Type.__name__ = "Integer32"
_EfmCuPme10PPayloadURateProfile_Object = MibTableColumn
efmCuPme10PPayloadURateProfile = _EfmCuPme10PPayloadURateProfile_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 7),
    _EfmCuPme10PPayloadURateProfile_Type()
)
efmCuPme10PPayloadURateProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PPayloadURateProfile.setStatus("current")
_EfmCuPme10PProfileRowStatus_Type = RowStatus
_EfmCuPme10PProfileRowStatus_Object = MibTableColumn
efmCuPme10PProfileRowStatus = _EfmCuPme10PProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 1, 1, 8),
    _EfmCuPme10PProfileRowStatus_Type()
)
efmCuPme10PProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PProfileRowStatus.setStatus("current")
_EfmCuPme10PStatusTable_Object = MibTable
efmCuPme10PStatusTable = _EfmCuPme10PStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusTable.setStatus("current")
_EfmCuPme10PStatusEntry_Object = MibTableRow
efmCuPme10PStatusEntry = _EfmCuPme10PStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 2, 1)
)
efmCuPme10PStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusEntry.setStatus("current")
_EfmCuPme10PFECCorrectedBlocks_Type = Counter32
_EfmCuPme10PFECCorrectedBlocks_Object = MibTableColumn
efmCuPme10PFECCorrectedBlocks = _EfmCuPme10PFECCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 2, 1, 1),
    _EfmCuPme10PFECCorrectedBlocks_Type()
)
efmCuPme10PFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPme10PFECCorrectedBlocks.setStatus("current")
_EfmCuPme10PFECUncorrectedBlocks_Type = Counter32
_EfmCuPme10PFECUncorrectedBlocks_Object = MibTableColumn
efmCuPme10PFECUncorrectedBlocks = _EfmCuPme10PFECUncorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 6, 2, 1, 2),
    _EfmCuPme10PFECUncorrectedBlocks_Type()
)
efmCuPme10PFECUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPme10PFECUncorrectedBlocks.setStatus("current")
_EfmCuConformance_ObjectIdentity = ObjectIdentity
efmCuConformance = _EfmCuConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 2)
)
_EfmCuGroups_ObjectIdentity = ObjectIdentity
efmCuGroups = _EfmCuGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 2, 1)
)
_EfmCuCompliances_ObjectIdentity = ObjectIdentity
efmCuCompliances = _EfmCuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 167, 2, 2)
)

# Managed Objects groups

efmCuBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 1)
)
efmCuBasicGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPAFSupported"),
        ("EFM-CU-MIB", "efmCuAdminProfile"),
        ("EFM-CU-MIB", "efmCuTargetDataRate"),
        ("EFM-CU-MIB", "efmCuTargetSnrMgn"),
        ("EFM-CU-MIB", "efmCuAdaptiveSpectra"),
        ("EFM-CU-MIB", "efmCuPortSide"),
        ("EFM-CU-MIB", "efmCuFltStatus"))
)
if mibBuilder.loadTexts:
    efmCuBasicGroup.setStatus("current")

efmCuPAFGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 2)
)
efmCuPAFGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPeerPAFSupported"),
        ("EFM-CU-MIB", "efmCuPAFCapacity"),
        ("EFM-CU-MIB", "efmCuPeerPAFCapacity"),
        ("EFM-CU-MIB", "efmCuPAFAdminState"),
        ("EFM-CU-MIB", "efmCuPAFDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuPAFRemoteDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuNumPMEs"))
)
if mibBuilder.loadTexts:
    efmCuPAFGroup.setStatus("current")

efmCuPAFErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 3)
)
efmCuPAFErrorsGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPAFInErrors"),
        ("EFM-CU-MIB", "efmCuPAFInSmallFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLargeFragments"),
        ("EFM-CU-MIB", "efmCuPAFInBadFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLostFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLostStarts"),
        ("EFM-CU-MIB", "efmCuPAFInLostEnds"),
        ("EFM-CU-MIB", "efmCuPAFInOverflows"))
)
if mibBuilder.loadTexts:
    efmCuPAFErrorsGroup.setStatus("current")

efmCuPmeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 4)
)
efmCuPmeGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeAdminProfile"),
        ("EFM-CU-MIB", "efmCuPmeOperStatus"),
        ("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuPmeSubTypesSupported"),
        ("EFM-CU-MIB", "efmCuPmeAdminSubType"),
        ("EFM-CU-MIB", "efmCuPmeOperSubType"),
        ("EFM-CU-MIB", "efmCuPAFRemoteDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuPmeOperProfile"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmePeerSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeLineAtn"),
        ("EFM-CU-MIB", "efmCuPmePeerLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeEquivalentLength"),
        ("EFM-CU-MIB", "efmCuPmeTCCodingErrors"),
        ("EFM-CU-MIB", "efmCuPmeTCCrcErrors"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    efmCuPmeGroup.setStatus("current")

efmCuAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 5)
)
efmCuAlarmConfGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuThreshLowRate"),
        ("EFM-CU-MIB", "efmCuLowRateCrossingEnable"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeLineAtnCrossingEnable"),
        ("EFM-CU-MIB", "efmCuPmeThreshSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgnCrossingEnable"),
        ("EFM-CU-MIB", "efmCuPmeDeviceFaultEnable"),
        ("EFM-CU-MIB", "efmCuPmeConfigInitFailEnable"),
        ("EFM-CU-MIB", "efmCuPmeProtocolInitFailEnable"))
)
if mibBuilder.loadTexts:
    efmCuAlarmConfGroup.setStatus("current")

efmCuPme2BProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 7)
)
efmCuPme2BProfileGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme2BProfileDescr"),
        ("EFM-CU-MIB", "efmCuPme2BRegion"),
        ("EFM-CU-MIB", "efmCuPme2BsMode"),
        ("EFM-CU-MIB", "efmCuPme2BMinDataRate"),
        ("EFM-CU-MIB", "efmCuPme2BMaxDataRate"),
        ("EFM-CU-MIB", "efmCuPme2BPower"),
        ("EFM-CU-MIB", "efmCuPme2BConstellation"),
        ("EFM-CU-MIB", "efmCuPme2BProfileRowStatus"),
        ("EFM-CU-MIB", "efmCuPme2BsModeDescr"),
        ("EFM-CU-MIB", "efmCuPme2BsModeRowStatus"),
        ("EFM-CU-MIB", "efmCuPme2BEquivalentLength"),
        ("EFM-CU-MIB", "efmCuPme2BMaxDataRatePam16"),
        ("EFM-CU-MIB", "efmCuPme2BMaxDataRatePam32"),
        ("EFM-CU-MIB", "efmCuPme2BReachRateRowStatus"))
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileGroup.setStatus("current")

efmCuPme10PProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 8)
)
efmCuPme10PProfileGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme10PProfileDescr"),
        ("EFM-CU-MIB", "efmCuPme10PBandplanPSDMskProfile"),
        ("EFM-CU-MIB", "efmCuPme10PUPBOReferenceProfile"),
        ("EFM-CU-MIB", "efmCuPme10PBandNotchProfiles"),
        ("EFM-CU-MIB", "efmCuPme10PPayloadDRateProfile"),
        ("EFM-CU-MIB", "efmCuPme10PPayloadURateProfile"),
        ("EFM-CU-MIB", "efmCuPme10PProfileRowStatus"))
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileGroup.setStatus("current")

efmCuPme10PStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 9)
)
efmCuPme10PStatusGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme10PFECCorrectedBlocks"),
        ("EFM-CU-MIB", "efmCuPme10PFECUncorrectedBlocks"))
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusGroup.setStatus("current")


# Notification objects

efmCuLowRateCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 1, 0, 1)
)
efmCuLowRateCrossing.setObjects(
      *(("IF-MIB", "ifSpeed"),
        ("EFM-CU-MIB", "efmCuThreshLowRate"))
)
if mibBuilder.loadTexts:
    efmCuLowRateCrossing.setStatus(
        "current"
    )

efmCuPmeLineAtnCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0, 1)
)
efmCuPmeLineAtnCrossing.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"))
)
if mibBuilder.loadTexts:
    efmCuPmeLineAtnCrossing.setStatus(
        "current"
    )

efmCuPmeSnrMgnCrossing = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0, 2)
)
efmCuPmeSnrMgnCrossing.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    efmCuPmeSnrMgnCrossing.setStatus(
        "current"
    )

efmCuPmeDeviceFault = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0, 3)
)
efmCuPmeDeviceFault.setObjects(
    ("EFM-CU-MIB", "efmCuPmeFltStatus")
)
if mibBuilder.loadTexts:
    efmCuPmeDeviceFault.setStatus(
        "current"
    )

efmCuPmeConfigInitFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0, 4)
)
efmCuPmeConfigInitFailure.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuAdminProfile"),
        ("EFM-CU-MIB", "efmCuPmeAdminProfile"))
)
if mibBuilder.loadTexts:
    efmCuPmeConfigInitFailure.setStatus(
        "current"
    )

efmCuPmeProtocolInitFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 167, 1, 2, 0, 5)
)
efmCuPmeProtocolInitFailure.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuPmeOperSubType"))
)
if mibBuilder.loadTexts:
    efmCuPmeProtocolInitFailure.setStatus(
        "current"
    )


# Notifications groups

efmCuNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 167, 2, 1, 6)
)
efmCuNotificationGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuLowRateCrossing"),
        ("EFM-CU-MIB", "efmCuPmeLineAtnCrossing"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgnCrossing"),
        ("EFM-CU-MIB", "efmCuPmeDeviceFault"),
        ("EFM-CU-MIB", "efmCuPmeConfigInitFailure"),
        ("EFM-CU-MIB", "efmCuPmeProtocolInitFailure"))
)
if mibBuilder.loadTexts:
    efmCuNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

efmCuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 167, 2, 2, 1)
)
efmCuCompliance.setObjects(
      *(("EFM-CU-MIB", "efmCuBasicGroup"),
        ("EFM-CU-MIB", "efmCuPmeGroup"),
        ("EFM-CU-MIB", "efmCuAlarmConfGroup"),
        ("EFM-CU-MIB", "efmCuNotificationGroup"),
        ("EFM-CU-MIB", "efmCuPme2BProfileGroup"),
        ("EFM-CU-MIB", "efmCuPme10PProfileGroup"),
        ("EFM-CU-MIB", "efmCuPAFGroup"),
        ("EFM-CU-MIB", "efmCuPAFErrorsGroup"),
        ("EFM-CU-MIB", "efmCuPme10PStatusGroup"))
)
if mibBuilder.loadTexts:
    efmCuCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFM-CU-MIB",
    **{"EfmProfileIndex": EfmProfileIndex,
       "EfmProfileIndexOrZero": EfmProfileIndexOrZero,
       "EfmProfileIndexList": EfmProfileIndexList,
       "EfmTruthValueOrUnknown": EfmTruthValueOrUnknown,
       "efmCuMIB": efmCuMIB,
       "efmCuObjects": efmCuObjects,
       "efmCuPort": efmCuPort,
       "efmCuPortNotifications": efmCuPortNotifications,
       "efmCuLowRateCrossing": efmCuLowRateCrossing,
       "efmCuPortConfTable": efmCuPortConfTable,
       "efmCuPortConfEntry": efmCuPortConfEntry,
       "efmCuPAFAdminState": efmCuPAFAdminState,
       "efmCuPAFDiscoveryCode": efmCuPAFDiscoveryCode,
       "efmCuAdminProfile": efmCuAdminProfile,
       "efmCuTargetDataRate": efmCuTargetDataRate,
       "efmCuTargetSnrMgn": efmCuTargetSnrMgn,
       "efmCuAdaptiveSpectra": efmCuAdaptiveSpectra,
       "efmCuThreshLowRate": efmCuThreshLowRate,
       "efmCuLowRateCrossingEnable": efmCuLowRateCrossingEnable,
       "efmCuPortCapabilityTable": efmCuPortCapabilityTable,
       "efmCuPortCapabilityEntry": efmCuPortCapabilityEntry,
       "efmCuPAFSupported": efmCuPAFSupported,
       "efmCuPeerPAFSupported": efmCuPeerPAFSupported,
       "efmCuPAFCapacity": efmCuPAFCapacity,
       "efmCuPeerPAFCapacity": efmCuPeerPAFCapacity,
       "efmCuPortStatusTable": efmCuPortStatusTable,
       "efmCuPortStatusEntry": efmCuPortStatusEntry,
       "efmCuFltStatus": efmCuFltStatus,
       "efmCuPortSide": efmCuPortSide,
       "efmCuNumPMEs": efmCuNumPMEs,
       "efmCuPAFInErrors": efmCuPAFInErrors,
       "efmCuPAFInSmallFragments": efmCuPAFInSmallFragments,
       "efmCuPAFInLargeFragments": efmCuPAFInLargeFragments,
       "efmCuPAFInBadFragments": efmCuPAFInBadFragments,
       "efmCuPAFInLostFragments": efmCuPAFInLostFragments,
       "efmCuPAFInLostStarts": efmCuPAFInLostStarts,
       "efmCuPAFInLostEnds": efmCuPAFInLostEnds,
       "efmCuPAFInOverflows": efmCuPAFInOverflows,
       "efmCuPme": efmCuPme,
       "efmCuPmeNotifications": efmCuPmeNotifications,
       "efmCuPmeLineAtnCrossing": efmCuPmeLineAtnCrossing,
       "efmCuPmeSnrMgnCrossing": efmCuPmeSnrMgnCrossing,
       "efmCuPmeDeviceFault": efmCuPmeDeviceFault,
       "efmCuPmeConfigInitFailure": efmCuPmeConfigInitFailure,
       "efmCuPmeProtocolInitFailure": efmCuPmeProtocolInitFailure,
       "efmCuPmeConfTable": efmCuPmeConfTable,
       "efmCuPmeConfEntry": efmCuPmeConfEntry,
       "efmCuPmeAdminSubType": efmCuPmeAdminSubType,
       "efmCuPmeAdminProfile": efmCuPmeAdminProfile,
       "efmCuPAFRemoteDiscoveryCode": efmCuPAFRemoteDiscoveryCode,
       "efmCuPmeThreshLineAtn": efmCuPmeThreshLineAtn,
       "efmCuPmeThreshSnrMgn": efmCuPmeThreshSnrMgn,
       "efmCuPmeLineAtnCrossingEnable": efmCuPmeLineAtnCrossingEnable,
       "efmCuPmeSnrMgnCrossingEnable": efmCuPmeSnrMgnCrossingEnable,
       "efmCuPmeDeviceFaultEnable": efmCuPmeDeviceFaultEnable,
       "efmCuPmeConfigInitFailEnable": efmCuPmeConfigInitFailEnable,
       "efmCuPmeProtocolInitFailEnable": efmCuPmeProtocolInitFailEnable,
       "efmCuPmeCapabilityTable": efmCuPmeCapabilityTable,
       "efmCuPmeCapabilityEntry": efmCuPmeCapabilityEntry,
       "efmCuPmeSubTypesSupported": efmCuPmeSubTypesSupported,
       "efmCuPmeStatusTable": efmCuPmeStatusTable,
       "efmCuPmeStatusEntry": efmCuPmeStatusEntry,
       "efmCuPmeOperStatus": efmCuPmeOperStatus,
       "efmCuPmeFltStatus": efmCuPmeFltStatus,
       "efmCuPmeOperSubType": efmCuPmeOperSubType,
       "efmCuPmeOperProfile": efmCuPmeOperProfile,
       "efmCuPmeSnrMgn": efmCuPmeSnrMgn,
       "efmCuPmePeerSnrMgn": efmCuPmePeerSnrMgn,
       "efmCuPmeLineAtn": efmCuPmeLineAtn,
       "efmCuPmePeerLineAtn": efmCuPmePeerLineAtn,
       "efmCuPmeEquivalentLength": efmCuPmeEquivalentLength,
       "efmCuPmeTCCodingErrors": efmCuPmeTCCodingErrors,
       "efmCuPmeTCCrcErrors": efmCuPmeTCCrcErrors,
       "efmCuPme2B": efmCuPme2B,
       "efmCuPme2BProfileTable": efmCuPme2BProfileTable,
       "efmCuPme2BProfileEntry": efmCuPme2BProfileEntry,
       "efmCuPme2BProfileIndex": efmCuPme2BProfileIndex,
       "efmCuPme2BProfileDescr": efmCuPme2BProfileDescr,
       "efmCuPme2BRegion": efmCuPme2BRegion,
       "efmCuPme2BsMode": efmCuPme2BsMode,
       "efmCuPme2BMinDataRate": efmCuPme2BMinDataRate,
       "efmCuPme2BMaxDataRate": efmCuPme2BMaxDataRate,
       "efmCuPme2BPower": efmCuPme2BPower,
       "efmCuPme2BConstellation": efmCuPme2BConstellation,
       "efmCuPme2BProfileRowStatus": efmCuPme2BProfileRowStatus,
       "efmCuPme2BsModeTable": efmCuPme2BsModeTable,
       "efmCuPme2BsModeEntry": efmCuPme2BsModeEntry,
       "efmCuPme2BsModeIndex": efmCuPme2BsModeIndex,
       "efmCuPme2BsModeDescr": efmCuPme2BsModeDescr,
       "efmCuPme2BsModeRowStatus": efmCuPme2BsModeRowStatus,
       "efmCuPme2BReachRateTable": efmCuPme2BReachRateTable,
       "efmCuPme2BReachRateEntry": efmCuPme2BReachRateEntry,
       "efmCuPme2BReachRateIndex": efmCuPme2BReachRateIndex,
       "efmCuPme2BEquivalentLength": efmCuPme2BEquivalentLength,
       "efmCuPme2BMaxDataRatePam16": efmCuPme2BMaxDataRatePam16,
       "efmCuPme2BMaxDataRatePam32": efmCuPme2BMaxDataRatePam32,
       "efmCuPme2BReachRateRowStatus": efmCuPme2BReachRateRowStatus,
       "efmCuPme10P": efmCuPme10P,
       "efmCuPme10PProfileTable": efmCuPme10PProfileTable,
       "efmCuPme10PProfileEntry": efmCuPme10PProfileEntry,
       "efmCuPme10PProfileIndex": efmCuPme10PProfileIndex,
       "efmCuPme10PProfileDescr": efmCuPme10PProfileDescr,
       "efmCuPme10PBandplanPSDMskProfile": efmCuPme10PBandplanPSDMskProfile,
       "efmCuPme10PUPBOReferenceProfile": efmCuPme10PUPBOReferenceProfile,
       "efmCuPme10PBandNotchProfiles": efmCuPme10PBandNotchProfiles,
       "efmCuPme10PPayloadDRateProfile": efmCuPme10PPayloadDRateProfile,
       "efmCuPme10PPayloadURateProfile": efmCuPme10PPayloadURateProfile,
       "efmCuPme10PProfileRowStatus": efmCuPme10PProfileRowStatus,
       "efmCuPme10PStatusTable": efmCuPme10PStatusTable,
       "efmCuPme10PStatusEntry": efmCuPme10PStatusEntry,
       "efmCuPme10PFECCorrectedBlocks": efmCuPme10PFECCorrectedBlocks,
       "efmCuPme10PFECUncorrectedBlocks": efmCuPme10PFECUncorrectedBlocks,
       "efmCuConformance": efmCuConformance,
       "efmCuGroups": efmCuGroups,
       "efmCuBasicGroup": efmCuBasicGroup,
       "efmCuPAFGroup": efmCuPAFGroup,
       "efmCuPAFErrorsGroup": efmCuPAFErrorsGroup,
       "efmCuPmeGroup": efmCuPmeGroup,
       "efmCuAlarmConfGroup": efmCuAlarmConfGroup,
       "efmCuNotificationGroup": efmCuNotificationGroup,
       "efmCuPme2BProfileGroup": efmCuPme2BProfileGroup,
       "efmCuPme10PProfileGroup": efmCuPme10PProfileGroup,
       "efmCuPme10PStatusGroup": efmCuPme10PStatusGroup,
       "efmCuCompliances": efmCuCompliances,
       "efmCuCompliance": efmCuCompliance}
)
