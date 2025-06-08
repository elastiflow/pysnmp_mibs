# SNMP MIB module (TIMETRA-RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-RSVP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:23 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLabel")

(rsvpIfEnabled,
 rsvpIfEntry,
 rsvpNbrProtocol) = mibBuilder.importSymbols(
    "RSVP-MIB",
    "rsvpIfEnabled",
    "rsvpIfEntry",
    "rsvpNbrProtocol")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(vRtrPimNgMvpnUMHPEStandbyAddr,
 vRtrPimNgMvpnUMHPEStandbyAdrTyp) = mibBuilder.importSymbols(
    "TIMETRA-PIM-NG-MIB",
    "vRtrPimNgMvpnUMHPEStandbyAddr",
    "vRtrPimNgMvpnUMHPEStandbyAdrTyp")

(TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState,
 TmnxRsvpDSTEClassType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxRsvpDSTEClassType")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraRsvpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    timetraRsvpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxRsvpSessionFailCode(TextualConvention, Integer32):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("admissionControlError", 1),
          ("noSenderTemplate", 2),
          ("conflictingResvStyle", 3),
          ("unknownResvStyle", 4),
          ("conflictingSourcePorts", 5),
          ("unknownClassObject", 6),
          ("unknownCTypeObject", 7),
          ("badERO", 8),
          ("badObjectLength", 9),
          ("badSubobjectLength", 10),
          ("badLabel", 11),
          ("rroRoutingLoop", 12),
          ("rsvpIpTtlMismatch", 13),
          ("integrityError", 14),
          ("missingMandatoryObject", 15),
          ("missingObjectClass", 16),
          ("wrongObjectOrder", 17),
          ("badAdspecParms", 18),
          ("badTspecParms", 19),
          ("badFlowspecParms", 20))
    )



class TmnxRsvpDSTETeClass(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TmnxRsvpDSTEBwPercent(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TmnxRsvpTEThresholdLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TmnxRsvpAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxRsvpConformance_ObjectIdentity = ObjectIdentity
tmnxRsvpConformance = _TmnxRsvpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7)
)
_TmnxRsvpCompliances_ObjectIdentity = ObjectIdentity
tmnxRsvpCompliances = _TmnxRsvpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1)
)
_TmnxRsvpGroups_ObjectIdentity = ObjectIdentity
tmnxRsvpGroups = _TmnxRsvpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2)
)
_TmnxRsvpObjs_ObjectIdentity = ObjectIdentity
tmnxRsvpObjs = _TmnxRsvpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7)
)
_VRtrRsvpGeneralTable_Object = MibTable
vRtrRsvpGeneralTable = _VRtrRsvpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpGeneralTable.setStatus("current")
_VRtrRsvpGeneralEntry_Object = MibTableRow
vRtrRsvpGeneralEntry = _VRtrRsvpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1)
)
vRtrRsvpGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrRsvpGeneralEntry.setStatus("current")
_VRtrRsvpGeneralLastChange_Type = TimeStamp
_VRtrRsvpGeneralLastChange_Object = MibTableColumn
vRtrRsvpGeneralLastChange = _VRtrRsvpGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 1),
    _VRtrRsvpGeneralLastChange_Type()
)
vRtrRsvpGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralLastChange.setStatus("current")


class _VRtrRsvpGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrRsvpGeneralAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrRsvpGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrRsvpGeneralAdminState_Object = MibTableColumn
vRtrRsvpGeneralAdminState = _VRtrRsvpGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 2),
    _VRtrRsvpGeneralAdminState_Type()
)
vRtrRsvpGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralAdminState.setStatus("current")
_VRtrRsvpGeneralOperState_Type = TmnxOperState
_VRtrRsvpGeneralOperState_Object = MibTableColumn
vRtrRsvpGeneralOperState = _VRtrRsvpGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 3),
    _VRtrRsvpGeneralOperState_Type()
)
vRtrRsvpGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralOperState.setStatus("current")


class _VRtrRsvpGeneralKeepMultiplier_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralKeepMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrRsvpGeneralKeepMultiplier_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralKeepMultiplier_Object = MibTableColumn
vRtrRsvpGeneralKeepMultiplier = _VRtrRsvpGeneralKeepMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 4),
    _VRtrRsvpGeneralKeepMultiplier_Type()
)
vRtrRsvpGeneralKeepMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralKeepMultiplier.setStatus("current")


class _VRtrRsvpGeneralRefreshTime_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralRefreshTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrRsvpGeneralRefreshTime_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralRefreshTime_Object = MibTableColumn
vRtrRsvpGeneralRefreshTime = _VRtrRsvpGeneralRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 5),
    _VRtrRsvpGeneralRefreshTime_Type()
)
vRtrRsvpGeneralRefreshTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralRefreshTime.setUnits("seconds")


class _VRtrRsvpGeneralMsgPacing_Type(TruthValue):
    """Custom type vRtrRsvpGeneralMsgPacing based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGeneralMsgPacing_Type.__name__ = "TruthValue"
_VRtrRsvpGeneralMsgPacing_Object = MibTableColumn
vRtrRsvpGeneralMsgPacing = _VRtrRsvpGeneralMsgPacing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 6),
    _VRtrRsvpGeneralMsgPacing_Type()
)
vRtrRsvpGeneralMsgPacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralMsgPacing.setStatus("current")


class _VRtrRsvpGeneralMsgPacingMaxBurst_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralMsgPacingMaxBurst based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VRtrRsvpGeneralMsgPacingMaxBurst_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralMsgPacingMaxBurst_Object = MibTableColumn
vRtrRsvpGeneralMsgPacingMaxBurst = _VRtrRsvpGeneralMsgPacingMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 7),
    _VRtrRsvpGeneralMsgPacingMaxBurst_Type()
)
vRtrRsvpGeneralMsgPacingMaxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralMsgPacingMaxBurst.setStatus("current")


class _VRtrRsvpGeneralMsgPacingPeriod_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralMsgPacingPeriod based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VRtrRsvpGeneralMsgPacingPeriod_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralMsgPacingPeriod_Object = MibTableColumn
vRtrRsvpGeneralMsgPacingPeriod = _VRtrRsvpGeneralMsgPacingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 8),
    _VRtrRsvpGeneralMsgPacingPeriod_Type()
)
vRtrRsvpGeneralMsgPacingPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralMsgPacingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralMsgPacingPeriod.setUnits("milliseconds")


class _VRtrRsvpGeneralRefreshBypass_Type(TruthValue):
    """Custom type vRtrRsvpGeneralRefreshBypass based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGeneralRefreshBypass_Type.__name__ = "TruthValue"
_VRtrRsvpGeneralRefreshBypass_Object = MibTableColumn
vRtrRsvpGeneralRefreshBypass = _VRtrRsvpGeneralRefreshBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 9),
    _VRtrRsvpGeneralRefreshBypass_Type()
)
vRtrRsvpGeneralRefreshBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralRefreshBypass.setStatus("current")


class _VRtrRsvpGenRapidRetransmitTime_Type(Unsigned32):
    """Custom type vRtrRsvpGenRapidRetransmitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrRsvpGenRapidRetransmitTime_Type.__name__ = "Unsigned32"
_VRtrRsvpGenRapidRetransmitTime_Object = MibTableColumn
vRtrRsvpGenRapidRetransmitTime = _VRtrRsvpGenRapidRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 10),
    _VRtrRsvpGenRapidRetransmitTime_Type()
)
vRtrRsvpGenRapidRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenRapidRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGenRapidRetransmitTime.setUnits("hundred-milliseconds")


class _VRtrRsvpGenRapidRetryLimit_Type(Unsigned32):
    """Custom type vRtrRsvpGenRapidRetryLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VRtrRsvpGenRapidRetryLimit_Type.__name__ = "Unsigned32"
_VRtrRsvpGenRapidRetryLimit_Object = MibTableColumn
vRtrRsvpGenRapidRetryLimit = _VRtrRsvpGenRapidRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 11),
    _VRtrRsvpGenRapidRetryLimit_Type()
)
vRtrRsvpGenRapidRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenRapidRetryLimit.setStatus("current")


class _VRtrRsvpGenGracefulShutdown_Type(TruthValue):
    """Custom type vRtrRsvpGenGracefulShutdown based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGenGracefulShutdown_Type.__name__ = "TruthValue"
_VRtrRsvpGenGracefulShutdown_Object = MibTableColumn
vRtrRsvpGenGracefulShutdown = _VRtrRsvpGenGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 12),
    _VRtrRsvpGenGracefulShutdown_Type()
)
vRtrRsvpGenGracefulShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenGracefulShutdown.setStatus("current")


class _VRtrRsvpGenPreemptionTimer_Type(Unsigned32):
    """Custom type vRtrRsvpGenPreemptionTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_VRtrRsvpGenPreemptionTimer_Type.__name__ = "Unsigned32"
_VRtrRsvpGenPreemptionTimer_Object = MibTableColumn
vRtrRsvpGenPreemptionTimer = _VRtrRsvpGenPreemptionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 13),
    _VRtrRsvpGenPreemptionTimer_Type()
)
vRtrRsvpGenPreemptionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenPreemptionTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGenPreemptionTimer.setUnits("seconds")


class _VRtrRsvpGenTEThresholdUpdate_Type(TruthValue):
    """Custom type vRtrRsvpGenTEThresholdUpdate based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGenTEThresholdUpdate_Type.__name__ = "TruthValue"
_VRtrRsvpGenTEThresholdUpdate_Object = MibTableColumn
vRtrRsvpGenTEThresholdUpdate = _VRtrRsvpGenTEThresholdUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 14),
    _VRtrRsvpGenTEThresholdUpdate_Type()
)
vRtrRsvpGenTEThresholdUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdUpdate.setStatus("current")


class _VRtrRsvpGenTEUpdateOnCacFail_Type(TruthValue):
    """Custom type vRtrRsvpGenTEUpdateOnCacFail based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGenTEUpdateOnCacFail_Type.__name__ = "TruthValue"
_VRtrRsvpGenTEUpdateOnCacFail_Object = MibTableColumn
vRtrRsvpGenTEUpdateOnCacFail = _VRtrRsvpGenTEUpdateOnCacFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 15),
    _VRtrRsvpGenTEUpdateOnCacFail_Type()
)
vRtrRsvpGenTEUpdateOnCacFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEUpdateOnCacFail.setStatus("current")


class _VRtrRsvpGenTEUpdateTimer_Type(Unsigned32):
    """Custom type vRtrRsvpGenTEUpdateTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_VRtrRsvpGenTEUpdateTimer_Type.__name__ = "Unsigned32"
_VRtrRsvpGenTEUpdateTimer_Object = MibTableColumn
vRtrRsvpGenTEUpdateTimer = _VRtrRsvpGenTEUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 16),
    _VRtrRsvpGenTEUpdateTimer_Type()
)
vRtrRsvpGenTEUpdateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEUpdateTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEUpdateTimer.setUnits("seconds")


class _VRtrRsvpGenImplicitNull_Type(TruthValue):
    """Custom type vRtrRsvpGenImplicitNull based on TruthValue"""
    defaultValue = 2


_VRtrRsvpGenImplicitNull_Type.__name__ = "TruthValue"
_VRtrRsvpGenImplicitNull_Object = MibTableColumn
vRtrRsvpGenImplicitNull = _VRtrRsvpGenImplicitNull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 17),
    _VRtrRsvpGenImplicitNull_Type()
)
vRtrRsvpGenImplicitNull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenImplicitNull.setStatus("current")


class _VRtrRsvpGenNodeIdInRro_Type(Integer32):
    """Custom type vRtrRsvpGenNodeIdInRro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_VRtrRsvpGenNodeIdInRro_Type.__name__ = "Integer32"
_VRtrRsvpGenNodeIdInRro_Object = MibTableColumn
vRtrRsvpGenNodeIdInRro = _VRtrRsvpGenNodeIdInRro_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 18),
    _VRtrRsvpGenNodeIdInRro_Type()
)
vRtrRsvpGenNodeIdInRro.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenNodeIdInRro.setStatus("current")


class _VRtrRsvpGenP2PMrgPntAbrtTimer_Type(Unsigned32):
    """Custom type vRtrRsvpGenP2PMrgPntAbrtTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrRsvpGenP2PMrgPntAbrtTimer_Type.__name__ = "Unsigned32"
_VRtrRsvpGenP2PMrgPntAbrtTimer_Object = MibTableColumn
vRtrRsvpGenP2PMrgPntAbrtTimer = _VRtrRsvpGenP2PMrgPntAbrtTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 19),
    _VRtrRsvpGenP2PMrgPntAbrtTimer_Type()
)
vRtrRsvpGenP2PMrgPntAbrtTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenP2PMrgPntAbrtTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGenP2PMrgPntAbrtTimer.setUnits("seconds")


class _VRtrRsvpGenP2MPMrgPntAbrtTimer_Type(Unsigned32):
    """Custom type vRtrRsvpGenP2MPMrgPntAbrtTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrRsvpGenP2MPMrgPntAbrtTimer_Type.__name__ = "Unsigned32"
_VRtrRsvpGenP2MPMrgPntAbrtTimer_Object = MibTableColumn
vRtrRsvpGenP2MPMrgPntAbrtTimer = _VRtrRsvpGenP2MPMrgPntAbrtTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 20),
    _VRtrRsvpGenP2MPMrgPntAbrtTimer_Type()
)
vRtrRsvpGenP2MPMrgPntAbrtTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenP2MPMrgPntAbrtTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGenP2MPMrgPntAbrtTimer.setUnits("seconds")


class _VRtrRsvpGeneralGrHlprMaxRcvryTm_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralGrHlprMaxRcvryTm based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_VRtrRsvpGeneralGrHlprMaxRcvryTm_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralGrHlprMaxRcvryTm_Object = MibTableColumn
vRtrRsvpGeneralGrHlprMaxRcvryTm = _VRtrRsvpGeneralGrHlprMaxRcvryTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 21),
    _VRtrRsvpGeneralGrHlprMaxRcvryTm_Type()
)
vRtrRsvpGeneralGrHlprMaxRcvryTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrHlprMaxRcvryTm.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrHlprMaxRcvryTm.setUnits("seconds")


class _VRtrRsvpGeneralGrHlprMaxRstrtTm_Type(Unsigned32):
    """Custom type vRtrRsvpGeneralGrHlprMaxRstrtTm based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_VRtrRsvpGeneralGrHlprMaxRstrtTm_Type.__name__ = "Unsigned32"
_VRtrRsvpGeneralGrHlprMaxRstrtTm_Object = MibTableColumn
vRtrRsvpGeneralGrHlprMaxRstrtTm = _VRtrRsvpGeneralGrHlprMaxRstrtTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 1, 1, 22),
    _VRtrRsvpGeneralGrHlprMaxRstrtTm_Type()
)
vRtrRsvpGeneralGrHlprMaxRstrtTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrHlprMaxRstrtTm.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrHlprMaxRstrtTm.setUnits("seconds")
_VRtrRsvpGeneralStatTable_Object = MibTable
vRtrRsvpGeneralStatTable = _VRtrRsvpGeneralStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    vRtrRsvpGeneralStatTable.setStatus("current")
_VRtrRsvpGeneralStatEntry_Object = MibTableRow
vRtrRsvpGeneralStatEntry = _VRtrRsvpGeneralStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpGeneralStatEntry.setStatus("current")
_VRtrRsvpGeneralPsbTimeouts_Type = Counter32
_VRtrRsvpGeneralPsbTimeouts_Object = MibTableColumn
vRtrRsvpGeneralPsbTimeouts = _VRtrRsvpGeneralPsbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2, 1, 1),
    _VRtrRsvpGeneralPsbTimeouts_Type()
)
vRtrRsvpGeneralPsbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralPsbTimeouts.setStatus("current")
_VRtrRsvpGeneralRsbTimeouts_Type = Counter32
_VRtrRsvpGeneralRsbTimeouts_Object = MibTableColumn
vRtrRsvpGeneralRsbTimeouts = _VRtrRsvpGeneralRsbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2, 1, 2),
    _VRtrRsvpGeneralRsbTimeouts_Type()
)
vRtrRsvpGeneralRsbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralRsbTimeouts.setStatus("current")
_VRtrRsvpGeneralGrhPsbTimeouts_Type = Counter32
_VRtrRsvpGeneralGrhPsbTimeouts_Object = MibTableColumn
vRtrRsvpGeneralGrhPsbTimeouts = _VRtrRsvpGeneralGrhPsbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2, 1, 3),
    _VRtrRsvpGeneralGrhPsbTimeouts_Type()
)
vRtrRsvpGeneralGrhPsbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrhPsbTimeouts.setStatus("current")
_VRtrRsvpGeneralGrhRsbTimeouts_Type = Counter32
_VRtrRsvpGeneralGrhRsbTimeouts_Object = MibTableColumn
vRtrRsvpGeneralGrhRsbTimeouts = _VRtrRsvpGeneralGrhRsbTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 2, 1, 4),
    _VRtrRsvpGeneralGrhRsbTimeouts_Type()
)
vRtrRsvpGeneralGrhRsbTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpGeneralGrhRsbTimeouts.setStatus("current")
_VRtrRsvpIfTable_Object = MibTable
vRtrRsvpIfTable = _VRtrRsvpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfTable.setStatus("current")
_VRtrRsvpIfEntry_Object = MibTableRow
vRtrRsvpIfEntry = _VRtrRsvpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfEntry.setStatus("current")
_VRtrRsvpIfLastEnabledTime_Type = TimeStamp
_VRtrRsvpIfLastEnabledTime_Object = MibTableColumn
vRtrRsvpIfLastEnabledTime = _VRtrRsvpIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 1),
    _VRtrRsvpIfLastEnabledTime_Type()
)
vRtrRsvpIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfLastEnabledTime.setStatus("current")
_VRtrRsvpIfVRtrIfIndex_Type = InterfaceIndex
_VRtrRsvpIfVRtrIfIndex_Object = MibTableColumn
vRtrRsvpIfVRtrIfIndex = _VRtrRsvpIfVRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 2),
    _VRtrRsvpIfVRtrIfIndex_Type()
)
vRtrRsvpIfVRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfVRtrIfIndex.setStatus("current")


class _VRtrRsvpIfAggregate_Type(TruthValue):
    """Custom type vRtrRsvpIfAggregate based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfAggregate_Type.__name__ = "TruthValue"
_VRtrRsvpIfAggregate_Object = MibTableColumn
vRtrRsvpIfAggregate = _VRtrRsvpIfAggregate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 3),
    _VRtrRsvpIfAggregate_Type()
)
vRtrRsvpIfAggregate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfAggregate.setStatus("current")


class _VRtrRsvpIfAuthenticationKey_Type(OctetString):
    """Custom type vRtrRsvpIfAuthenticationKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrRsvpIfAuthenticationKey_Type.__name__ = "OctetString"
_VRtrRsvpIfAuthenticationKey_Object = MibTableColumn
vRtrRsvpIfAuthenticationKey = _VRtrRsvpIfAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 4),
    _VRtrRsvpIfAuthenticationKey_Type()
)
vRtrRsvpIfAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthenticationKey.setStatus("current")


class _VRtrRsvpIfHelloInterval_Type(Unsigned32):
    """Custom type vRtrRsvpIfHelloInterval based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VRtrRsvpIfHelloInterval_Type.__name__ = "Unsigned32"
_VRtrRsvpIfHelloInterval_Object = MibTableColumn
vRtrRsvpIfHelloInterval = _VRtrRsvpIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 5),
    _VRtrRsvpIfHelloInterval_Type()
)
vRtrRsvpIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfHelloInterval.setUnits("milliseconds")


class _VRtrRsvpIfSubscription_Type(Unsigned32):
    """Custom type vRtrRsvpIfSubscription based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VRtrRsvpIfSubscription_Type.__name__ = "Unsigned32"
_VRtrRsvpIfSubscription_Object = MibTableColumn
vRtrRsvpIfSubscription = _VRtrRsvpIfSubscription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 6),
    _VRtrRsvpIfSubscription_Type()
)
vRtrRsvpIfSubscription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfSubscription.setStatus("current")


class _VRtrRsvpIfKeepMultiplier_Type(Unsigned32):
    """Custom type vRtrRsvpIfKeepMultiplier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrRsvpIfKeepMultiplier_Type.__name__ = "Unsigned32"
_VRtrRsvpIfKeepMultiplier_Object = MibTableColumn
vRtrRsvpIfKeepMultiplier = _VRtrRsvpIfKeepMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 7),
    _VRtrRsvpIfKeepMultiplier_Type()
)
vRtrRsvpIfKeepMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfKeepMultiplier.setStatus("obsolete")


class _VRtrRsvpIfRefreshTime_Type(Unsigned32):
    """Custom type vRtrRsvpIfRefreshTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrRsvpIfRefreshTime_Type.__name__ = "Unsigned32"
_VRtrRsvpIfRefreshTime_Object = MibTableColumn
vRtrRsvpIfRefreshTime = _VRtrRsvpIfRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 8),
    _VRtrRsvpIfRefreshTime_Type()
)
vRtrRsvpIfRefreshTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfRefreshTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrRsvpIfRefreshTime.setUnits("seconds")
_VRtrRsvpIfOperState_Type = TmnxOperState
_VRtrRsvpIfOperState_Object = MibTableColumn
vRtrRsvpIfOperState = _VRtrRsvpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 9),
    _VRtrRsvpIfOperState_Type()
)
vRtrRsvpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfOperState.setStatus("current")
_VRtrRsvpIfActiveSessionCount_Type = Counter32
_VRtrRsvpIfActiveSessionCount_Object = MibTableColumn
vRtrRsvpIfActiveSessionCount = _VRtrRsvpIfActiveSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 10),
    _VRtrRsvpIfActiveSessionCount_Type()
)
vRtrRsvpIfActiveSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfActiveSessionCount.setStatus("current")
_VRtrRsvpIfActiveReservationCount_Type = Counter32
_VRtrRsvpIfActiveReservationCount_Object = MibTableColumn
vRtrRsvpIfActiveReservationCount = _VRtrRsvpIfActiveReservationCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 11),
    _VRtrRsvpIfActiveReservationCount_Type()
)
vRtrRsvpIfActiveReservationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfActiveReservationCount.setStatus("current")
_VRtrRsvpIfTotalSessionCount_Type = Counter32
_VRtrRsvpIfTotalSessionCount_Object = MibTableColumn
vRtrRsvpIfTotalSessionCount = _VRtrRsvpIfTotalSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 12),
    _VRtrRsvpIfTotalSessionCount_Type()
)
vRtrRsvpIfTotalSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfTotalSessionCount.setStatus("current")
_VRtrRsvpIfBandwidth_Type = Unsigned32
_VRtrRsvpIfBandwidth_Object = MibTableColumn
vRtrRsvpIfBandwidth = _VRtrRsvpIfBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 13),
    _VRtrRsvpIfBandwidth_Type()
)
vRtrRsvpIfBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfBandwidth.setUnits("mega-bits per second")
_VRtrRsvpIfReservedBandwidth_Type = Unsigned32
_VRtrRsvpIfReservedBandwidth_Object = MibTableColumn
vRtrRsvpIfReservedBandwidth = _VRtrRsvpIfReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 14),
    _VRtrRsvpIfReservedBandwidth_Type()
)
vRtrRsvpIfReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfReservedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfReservedBandwidth.setUnits("mega-bits per second")


class _VRtrRsvpIfAuthentication_Type(TruthValue):
    """Custom type vRtrRsvpIfAuthentication based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfAuthentication_Type.__name__ = "TruthValue"
_VRtrRsvpIfAuthentication_Object = MibTableColumn
vRtrRsvpIfAuthentication = _VRtrRsvpIfAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 15),
    _VRtrRsvpIfAuthentication_Type()
)
vRtrRsvpIfAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthentication.setStatus("current")


class _VRtrRsvpIfAuthChallenge_Type(TruthValue):
    """Custom type vRtrRsvpIfAuthChallenge based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfAuthChallenge_Type.__name__ = "TruthValue"
_VRtrRsvpIfAuthChallenge_Object = MibTableColumn
vRtrRsvpIfAuthChallenge = _VRtrRsvpIfAuthChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 16),
    _VRtrRsvpIfAuthChallenge_Type()
)
vRtrRsvpIfAuthChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthChallenge.setStatus("current")
_VRtrRsvpIfAuthKeyId_Type = Counter64
_VRtrRsvpIfAuthKeyId_Object = MibTableColumn
vRtrRsvpIfAuthKeyId = _VRtrRsvpIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 17),
    _VRtrRsvpIfAuthKeyId_Type()
)
vRtrRsvpIfAuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthKeyId.setStatus("current")
_VRtrRsvpIfAuthRxSeqNum_Type = Counter64
_VRtrRsvpIfAuthRxSeqNum_Object = MibTableColumn
vRtrRsvpIfAuthRxSeqNum = _VRtrRsvpIfAuthRxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 18),
    _VRtrRsvpIfAuthRxSeqNum_Type()
)
vRtrRsvpIfAuthRxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthRxSeqNum.setStatus("current")
_VRtrRsvpIfAuthTxSeqNum_Type = Counter64
_VRtrRsvpIfAuthTxSeqNum_Object = MibTableColumn
vRtrRsvpIfAuthTxSeqNum = _VRtrRsvpIfAuthTxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 19),
    _VRtrRsvpIfAuthTxSeqNum_Type()
)
vRtrRsvpIfAuthTxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthTxSeqNum.setStatus("current")
_VRtrRsvpIfAuthWindowSize_Type = Counter32
_VRtrRsvpIfAuthWindowSize_Object = MibTableColumn
vRtrRsvpIfAuthWindowSize = _VRtrRsvpIfAuthWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 20),
    _VRtrRsvpIfAuthWindowSize_Type()
)
vRtrRsvpIfAuthWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthWindowSize.setStatus("current")


class _VRtrRsvpIfRefreshReduction_Type(TruthValue):
    """Custom type vRtrRsvpIfRefreshReduction based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfRefreshReduction_Type.__name__ = "TruthValue"
_VRtrRsvpIfRefreshReduction_Object = MibTableColumn
vRtrRsvpIfRefreshReduction = _VRtrRsvpIfRefreshReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 21),
    _VRtrRsvpIfRefreshReduction_Type()
)
vRtrRsvpIfRefreshReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfRefreshReduction.setStatus("current")


class _VRtrRsvpIfReliableDelivery_Type(TruthValue):
    """Custom type vRtrRsvpIfReliableDelivery based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfReliableDelivery_Type.__name__ = "TruthValue"
_VRtrRsvpIfReliableDelivery_Object = MibTableColumn
vRtrRsvpIfReliableDelivery = _VRtrRsvpIfReliableDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 22),
    _VRtrRsvpIfReliableDelivery_Type()
)
vRtrRsvpIfReliableDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfReliableDelivery.setStatus("current")


class _VRtrRsvpIfBfdEnabled_Type(TruthValue):
    """Custom type vRtrRsvpIfBfdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfBfdEnabled_Type.__name__ = "TruthValue"
_VRtrRsvpIfBfdEnabled_Object = MibTableColumn
vRtrRsvpIfBfdEnabled = _VRtrRsvpIfBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 23),
    _VRtrRsvpIfBfdEnabled_Type()
)
vRtrRsvpIfBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfBfdEnabled.setStatus("current")


class _VRtrRsvpIfGracefulShutdown_Type(TruthValue):
    """Custom type vRtrRsvpIfGracefulShutdown based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfGracefulShutdown_Type.__name__ = "TruthValue"
_VRtrRsvpIfGracefulShutdown_Object = MibTableColumn
vRtrRsvpIfGracefulShutdown = _VRtrRsvpIfGracefulShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 24),
    _VRtrRsvpIfGracefulShutdown_Type()
)
vRtrRsvpIfGracefulShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfGracefulShutdown.setStatus("current")


class _VRtrRsvpIfDSTECt0BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt0BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt0BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt0BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt0BwPercent = _VRtrRsvpIfDSTECt0BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 25),
    _VRtrRsvpIfDSTECt0BwPercent_Type()
)
vRtrRsvpIfDSTECt0BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt0BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt1BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt1BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt1BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt1BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt1BwPercent = _VRtrRsvpIfDSTECt1BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 26),
    _VRtrRsvpIfDSTECt1BwPercent_Type()
)
vRtrRsvpIfDSTECt1BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt1BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt2BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt2BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt2BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt2BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt2BwPercent = _VRtrRsvpIfDSTECt2BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 27),
    _VRtrRsvpIfDSTECt2BwPercent_Type()
)
vRtrRsvpIfDSTECt2BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt2BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt3BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt3BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt3BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt3BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt3BwPercent = _VRtrRsvpIfDSTECt3BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 28),
    _VRtrRsvpIfDSTECt3BwPercent_Type()
)
vRtrRsvpIfDSTECt3BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt3BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt4BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt4BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt4BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt4BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt4BwPercent = _VRtrRsvpIfDSTECt4BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 29),
    _VRtrRsvpIfDSTECt4BwPercent_Type()
)
vRtrRsvpIfDSTECt4BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt4BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt5BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt5BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt5BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt5BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt5BwPercent = _VRtrRsvpIfDSTECt5BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 30),
    _VRtrRsvpIfDSTECt5BwPercent_Type()
)
vRtrRsvpIfDSTECt5BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt5BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt6BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt6BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt6BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt6BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt6BwPercent = _VRtrRsvpIfDSTECt6BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 31),
    _VRtrRsvpIfDSTECt6BwPercent_Type()
)
vRtrRsvpIfDSTECt6BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt6BwPercent.setStatus("current")


class _VRtrRsvpIfDSTECt7BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpIfDSTECt7BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpIfDSTECt7BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpIfDSTECt7BwPercent_Object = MibTableColumn
vRtrRsvpIfDSTECt7BwPercent = _VRtrRsvpIfDSTECt7BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 32),
    _VRtrRsvpIfDSTECt7BwPercent_Type()
)
vRtrRsvpIfDSTECt7BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTECt7BwPercent.setStatus("current")


class _VRtrRsvpIfInheritance_Type(Unsigned32):
    """Custom type vRtrRsvpIfInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrRsvpIfInheritance_Type.__name__ = "Unsigned32"
_VRtrRsvpIfInheritance_Object = MibTableColumn
vRtrRsvpIfInheritance = _VRtrRsvpIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 33),
    _VRtrRsvpIfInheritance_Type()
)
vRtrRsvpIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfInheritance.setStatus("current")
_VRtrRsvpIfDSTEBC0Bw_Type = Counter64
_VRtrRsvpIfDSTEBC0Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC0Bw = _VRtrRsvpIfDSTEBC0Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 34),
    _VRtrRsvpIfDSTEBC0Bw_Type()
)
vRtrRsvpIfDSTEBC0Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC0Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC0Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC1Bw_Type = Counter64
_VRtrRsvpIfDSTEBC1Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC1Bw = _VRtrRsvpIfDSTEBC1Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 35),
    _VRtrRsvpIfDSTEBC1Bw_Type()
)
vRtrRsvpIfDSTEBC1Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC1Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC1Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC2Bw_Type = Counter64
_VRtrRsvpIfDSTEBC2Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC2Bw = _VRtrRsvpIfDSTEBC2Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 36),
    _VRtrRsvpIfDSTEBC2Bw_Type()
)
vRtrRsvpIfDSTEBC2Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC2Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC2Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC3Bw_Type = Counter64
_VRtrRsvpIfDSTEBC3Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC3Bw = _VRtrRsvpIfDSTEBC3Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 37),
    _VRtrRsvpIfDSTEBC3Bw_Type()
)
vRtrRsvpIfDSTEBC3Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC3Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC3Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC4Bw_Type = Counter64
_VRtrRsvpIfDSTEBC4Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC4Bw = _VRtrRsvpIfDSTEBC4Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 38),
    _VRtrRsvpIfDSTEBC4Bw_Type()
)
vRtrRsvpIfDSTEBC4Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC4Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC4Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC5Bw_Type = Counter64
_VRtrRsvpIfDSTEBC5Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC5Bw = _VRtrRsvpIfDSTEBC5Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 39),
    _VRtrRsvpIfDSTEBC5Bw_Type()
)
vRtrRsvpIfDSTEBC5Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC5Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC5Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC6Bw_Type = Counter64
_VRtrRsvpIfDSTEBC6Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC6Bw = _VRtrRsvpIfDSTEBC6Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 40),
    _VRtrRsvpIfDSTEBC6Bw_Type()
)
vRtrRsvpIfDSTEBC6Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC6Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC6Bw.setUnits("Kbps")
_VRtrRsvpIfDSTEBC7Bw_Type = Counter64
_VRtrRsvpIfDSTEBC7Bw_Object = MibTableColumn
vRtrRsvpIfDSTEBC7Bw = _VRtrRsvpIfDSTEBC7Bw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 41),
    _VRtrRsvpIfDSTEBC7Bw_Type()
)
vRtrRsvpIfDSTEBC7Bw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC7Bw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEBC7Bw.setUnits("Kbps")


class _VRtrRsvpIfImplicitNull_Type(TruthValue):
    """Custom type vRtrRsvpIfImplicitNull based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfImplicitNull_Type.__name__ = "TruthValue"
_VRtrRsvpIfImplicitNull_Object = MibTableColumn
vRtrRsvpIfImplicitNull = _VRtrRsvpIfImplicitNull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 42),
    _VRtrRsvpIfImplicitNull_Type()
)
vRtrRsvpIfImplicitNull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfImplicitNull.setStatus("current")
_VRtrRsvpIfIgpUpdatePending_Type = TruthValue
_VRtrRsvpIfIgpUpdatePending_Object = MibTableColumn
vRtrRsvpIfIgpUpdatePending = _VRtrRsvpIfIgpUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 43),
    _VRtrRsvpIfIgpUpdatePending_Type()
)
vRtrRsvpIfIgpUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfIgpUpdatePending.setStatus("current")
_VRtrRsvpIfIgpNextUpdate_Type = Unsigned32
_VRtrRsvpIfIgpNextUpdate_Object = MibTableColumn
vRtrRsvpIfIgpNextUpdate = _VRtrRsvpIfIgpNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 44),
    _VRtrRsvpIfIgpNextUpdate_Type()
)
vRtrRsvpIfIgpNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfIgpNextUpdate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfIgpNextUpdate.setUnits("seconds")


class _VRtrRsvpIfGraceHelper_Type(TruthValue):
    """Custom type vRtrRsvpIfGraceHelper based on TruthValue"""
    defaultValue = 2


_VRtrRsvpIfGraceHelper_Type.__name__ = "TruthValue"
_VRtrRsvpIfGraceHelper_Object = MibTableColumn
vRtrRsvpIfGraceHelper = _VRtrRsvpIfGraceHelper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 45),
    _VRtrRsvpIfGraceHelper_Type()
)
vRtrRsvpIfGraceHelper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfGraceHelper.setStatus("current")
_VRtrRsvpIfMaxResvBandwidth_Type = Unsigned32
_VRtrRsvpIfMaxResvBandwidth_Object = MibTableColumn
vRtrRsvpIfMaxResvBandwidth = _VRtrRsvpIfMaxResvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 46),
    _VRtrRsvpIfMaxResvBandwidth_Type()
)
vRtrRsvpIfMaxResvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfMaxResvBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfMaxResvBandwidth.setUnits("mega-bits per second")


class _VRtrRsvpIfAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type vRtrRsvpIfAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrRsvpIfAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_VRtrRsvpIfAuthKeyChain_Object = MibTableColumn
vRtrRsvpIfAuthKeyChain = _VRtrRsvpIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 3, 1, 47),
    _VRtrRsvpIfAuthKeyChain_Type()
)
vRtrRsvpIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfAuthKeyChain.setStatus("current")
_VRtrRsvpIfStatTable_Object = MibTable
vRtrRsvpIfStatTable = _VRtrRsvpIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTable.setStatus("current")
_VRtrRsvpIfStatEntry_Object = MibTableRow
vRtrRsvpIfStatEntry = _VRtrRsvpIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1)
)
vRtrRsvpIfStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrRsvpIfStatEntry.setStatus("current")
_VRtrRsvpIfStatTxPaths_Type = Counter64
_VRtrRsvpIfStatTxPaths_Object = MibTableColumn
vRtrRsvpIfStatTxPaths = _VRtrRsvpIfStatTxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 1),
    _VRtrRsvpIfStatTxPaths_Type()
)
vRtrRsvpIfStatTxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxPaths.setStatus("current")
_VRtrRsvpIfStatTxPathErrors_Type = Counter64
_VRtrRsvpIfStatTxPathErrors_Object = MibTableColumn
vRtrRsvpIfStatTxPathErrors = _VRtrRsvpIfStatTxPathErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 2),
    _VRtrRsvpIfStatTxPathErrors_Type()
)
vRtrRsvpIfStatTxPathErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxPathErrors.setStatus("current")
_VRtrRsvpIfStatTxPathTears_Type = Counter64
_VRtrRsvpIfStatTxPathTears_Object = MibTableColumn
vRtrRsvpIfStatTxPathTears = _VRtrRsvpIfStatTxPathTears_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 3),
    _VRtrRsvpIfStatTxPathTears_Type()
)
vRtrRsvpIfStatTxPathTears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxPathTears.setStatus("current")
_VRtrRsvpIfStatTxResvs_Type = Counter64
_VRtrRsvpIfStatTxResvs_Object = MibTableColumn
vRtrRsvpIfStatTxResvs = _VRtrRsvpIfStatTxResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 4),
    _VRtrRsvpIfStatTxResvs_Type()
)
vRtrRsvpIfStatTxResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxResvs.setStatus("current")
_VRtrRsvpIfStatTxResvErrors_Type = Counter64
_VRtrRsvpIfStatTxResvErrors_Object = MibTableColumn
vRtrRsvpIfStatTxResvErrors = _VRtrRsvpIfStatTxResvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 5),
    _VRtrRsvpIfStatTxResvErrors_Type()
)
vRtrRsvpIfStatTxResvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxResvErrors.setStatus("current")
_VRtrRsvpIfStatTxResvTears_Type = Counter64
_VRtrRsvpIfStatTxResvTears_Object = MibTableColumn
vRtrRsvpIfStatTxResvTears = _VRtrRsvpIfStatTxResvTears_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 6),
    _VRtrRsvpIfStatTxResvTears_Type()
)
vRtrRsvpIfStatTxResvTears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxResvTears.setStatus("current")
_VRtrRsvpIfStatTxResvConfirms_Type = Counter64
_VRtrRsvpIfStatTxResvConfirms_Object = MibTableColumn
vRtrRsvpIfStatTxResvConfirms = _VRtrRsvpIfStatTxResvConfirms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 7),
    _VRtrRsvpIfStatTxResvConfirms_Type()
)
vRtrRsvpIfStatTxResvConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxResvConfirms.setStatus("current")
_VRtrRsvpIfStatTxBundles_Type = Counter64
_VRtrRsvpIfStatTxBundles_Object = MibTableColumn
vRtrRsvpIfStatTxBundles = _VRtrRsvpIfStatTxBundles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 8),
    _VRtrRsvpIfStatTxBundles_Type()
)
vRtrRsvpIfStatTxBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxBundles.setStatus("current")
_VRtrRsvpIfStatTxAcks_Type = Counter64
_VRtrRsvpIfStatTxAcks_Object = MibTableColumn
vRtrRsvpIfStatTxAcks = _VRtrRsvpIfStatTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 9),
    _VRtrRsvpIfStatTxAcks_Type()
)
vRtrRsvpIfStatTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxAcks.setStatus("current")
_VRtrRsvpIfStatTxHelloReqs_Type = Counter64
_VRtrRsvpIfStatTxHelloReqs_Object = MibTableColumn
vRtrRsvpIfStatTxHelloReqs = _VRtrRsvpIfStatTxHelloReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 10),
    _VRtrRsvpIfStatTxHelloReqs_Type()
)
vRtrRsvpIfStatTxHelloReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxHelloReqs.setStatus("current")
_VRtrRsvpIfStatTxSRefreshes_Type = Counter64
_VRtrRsvpIfStatTxSRefreshes_Object = MibTableColumn
vRtrRsvpIfStatTxSRefreshes = _VRtrRsvpIfStatTxSRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 11),
    _VRtrRsvpIfStatTxSRefreshes_Type()
)
vRtrRsvpIfStatTxSRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxSRefreshes.setStatus("current")
_VRtrRsvpIfStatTxPkts_Type = Counter64
_VRtrRsvpIfStatTxPkts_Object = MibTableColumn
vRtrRsvpIfStatTxPkts = _VRtrRsvpIfStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 12),
    _VRtrRsvpIfStatTxPkts_Type()
)
vRtrRsvpIfStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxPkts.setStatus("current")
_VRtrRsvpIfStatTxErrorPkts_Type = Counter64
_VRtrRsvpIfStatTxErrorPkts_Object = MibTableColumn
vRtrRsvpIfStatTxErrorPkts = _VRtrRsvpIfStatTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 13),
    _VRtrRsvpIfStatTxErrorPkts_Type()
)
vRtrRsvpIfStatTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxErrorPkts.setStatus("current")
_VRtrRsvpIfStatTxTotalPkts_Type = Counter64
_VRtrRsvpIfStatTxTotalPkts_Object = MibTableColumn
vRtrRsvpIfStatTxTotalPkts = _VRtrRsvpIfStatTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 14),
    _VRtrRsvpIfStatTxTotalPkts_Type()
)
vRtrRsvpIfStatTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxTotalPkts.setStatus("current")
_VRtrRsvpIfStatRxPaths_Type = Counter64
_VRtrRsvpIfStatRxPaths_Object = MibTableColumn
vRtrRsvpIfStatRxPaths = _VRtrRsvpIfStatRxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 15),
    _VRtrRsvpIfStatRxPaths_Type()
)
vRtrRsvpIfStatRxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxPaths.setStatus("current")
_VRtrRsvpIfStatRxPathErrors_Type = Counter64
_VRtrRsvpIfStatRxPathErrors_Object = MibTableColumn
vRtrRsvpIfStatRxPathErrors = _VRtrRsvpIfStatRxPathErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 16),
    _VRtrRsvpIfStatRxPathErrors_Type()
)
vRtrRsvpIfStatRxPathErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxPathErrors.setStatus("current")
_VRtrRsvpIfStatRxPathTears_Type = Counter64
_VRtrRsvpIfStatRxPathTears_Object = MibTableColumn
vRtrRsvpIfStatRxPathTears = _VRtrRsvpIfStatRxPathTears_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 17),
    _VRtrRsvpIfStatRxPathTears_Type()
)
vRtrRsvpIfStatRxPathTears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxPathTears.setStatus("current")
_VRtrRsvpIfStatRxResvs_Type = Counter64
_VRtrRsvpIfStatRxResvs_Object = MibTableColumn
vRtrRsvpIfStatRxResvs = _VRtrRsvpIfStatRxResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 18),
    _VRtrRsvpIfStatRxResvs_Type()
)
vRtrRsvpIfStatRxResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxResvs.setStatus("current")
_VRtrRsvpIfStatRxResvErrors_Type = Counter64
_VRtrRsvpIfStatRxResvErrors_Object = MibTableColumn
vRtrRsvpIfStatRxResvErrors = _VRtrRsvpIfStatRxResvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 19),
    _VRtrRsvpIfStatRxResvErrors_Type()
)
vRtrRsvpIfStatRxResvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxResvErrors.setStatus("current")
_VRtrRsvpIfStatRxResvTears_Type = Counter64
_VRtrRsvpIfStatRxResvTears_Object = MibTableColumn
vRtrRsvpIfStatRxResvTears = _VRtrRsvpIfStatRxResvTears_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 20),
    _VRtrRsvpIfStatRxResvTears_Type()
)
vRtrRsvpIfStatRxResvTears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxResvTears.setStatus("current")
_VRtrRsvpIfStatRxResvConfirms_Type = Counter64
_VRtrRsvpIfStatRxResvConfirms_Object = MibTableColumn
vRtrRsvpIfStatRxResvConfirms = _VRtrRsvpIfStatRxResvConfirms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 21),
    _VRtrRsvpIfStatRxResvConfirms_Type()
)
vRtrRsvpIfStatRxResvConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxResvConfirms.setStatus("current")
_VRtrRsvpIfStatRxBundles_Type = Counter64
_VRtrRsvpIfStatRxBundles_Object = MibTableColumn
vRtrRsvpIfStatRxBundles = _VRtrRsvpIfStatRxBundles_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 22),
    _VRtrRsvpIfStatRxBundles_Type()
)
vRtrRsvpIfStatRxBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxBundles.setStatus("current")
_VRtrRsvpIfStatRxAcks_Type = Counter64
_VRtrRsvpIfStatRxAcks_Object = MibTableColumn
vRtrRsvpIfStatRxAcks = _VRtrRsvpIfStatRxAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 23),
    _VRtrRsvpIfStatRxAcks_Type()
)
vRtrRsvpIfStatRxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxAcks.setStatus("current")
_VRtrRsvpIfStatRxHelloReqs_Type = Counter64
_VRtrRsvpIfStatRxHelloReqs_Object = MibTableColumn
vRtrRsvpIfStatRxHelloReqs = _VRtrRsvpIfStatRxHelloReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 24),
    _VRtrRsvpIfStatRxHelloReqs_Type()
)
vRtrRsvpIfStatRxHelloReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxHelloReqs.setStatus("current")
_VRtrRsvpIfStatRxSRefreshes_Type = Counter64
_VRtrRsvpIfStatRxSRefreshes_Object = MibTableColumn
vRtrRsvpIfStatRxSRefreshes = _VRtrRsvpIfStatRxSRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 25),
    _VRtrRsvpIfStatRxSRefreshes_Type()
)
vRtrRsvpIfStatRxSRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxSRefreshes.setStatus("current")
_VRtrRsvpIfStatRxPkts_Type = Counter64
_VRtrRsvpIfStatRxPkts_Object = MibTableColumn
vRtrRsvpIfStatRxPkts = _VRtrRsvpIfStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 26),
    _VRtrRsvpIfStatRxPkts_Type()
)
vRtrRsvpIfStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxPkts.setStatus("current")
_VRtrRsvpIfStatRxErrorPkts_Type = Counter64
_VRtrRsvpIfStatRxErrorPkts_Object = MibTableColumn
vRtrRsvpIfStatRxErrorPkts = _VRtrRsvpIfStatRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 27),
    _VRtrRsvpIfStatRxErrorPkts_Type()
)
vRtrRsvpIfStatRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxErrorPkts.setStatus("current")
_VRtrRsvpIfStatRxTotalPkts_Type = Counter64
_VRtrRsvpIfStatRxTotalPkts_Object = MibTableColumn
vRtrRsvpIfStatRxTotalPkts = _VRtrRsvpIfStatRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 28),
    _VRtrRsvpIfStatRxTotalPkts_Type()
)
vRtrRsvpIfStatRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxTotalPkts.setStatus("current")
_VRtrRsvpIfStatHelloTimeout_Type = Counter32
_VRtrRsvpIfStatHelloTimeout_Object = MibTableColumn
vRtrRsvpIfStatHelloTimeout = _VRtrRsvpIfStatHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 29),
    _VRtrRsvpIfStatHelloTimeout_Type()
)
vRtrRsvpIfStatHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatHelloTimeout.setStatus("current")
_VRtrRsvpIfStatTxAuthErrors_Type = Counter64
_VRtrRsvpIfStatTxAuthErrors_Object = MibTableColumn
vRtrRsvpIfStatTxAuthErrors = _VRtrRsvpIfStatTxAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 30),
    _VRtrRsvpIfStatTxAuthErrors_Type()
)
vRtrRsvpIfStatTxAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatTxAuthErrors.setStatus("current")
_VRtrRsvpIfStatRxAuthErrors_Type = Counter64
_VRtrRsvpIfStatRxAuthErrors_Object = MibTableColumn
vRtrRsvpIfStatRxAuthErrors = _VRtrRsvpIfStatRxAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 4, 1, 31),
    _VRtrRsvpIfStatRxAuthErrors_Type()
)
vRtrRsvpIfStatRxAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfStatRxAuthErrors.setStatus("current")
_VRtrRsvpSessionTable_Object = MibTable
vRtrRsvpSessionTable = _VRtrRsvpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5)
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionTable.setStatus("current")
_VRtrRsvpSessionEntry_Object = MibTableRow
vRtrRsvpSessionEntry = _VRtrRsvpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1)
)
vRtrRsvpSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpSessionIndex"),
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionEntry.setStatus("current")
_VRtrRsvpSessionIndex_Type = Unsigned32
_VRtrRsvpSessionIndex_Object = MibTableColumn
vRtrRsvpSessionIndex = _VRtrRsvpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 1),
    _VRtrRsvpSessionIndex_Type()
)
vRtrRsvpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpSessionIndex.setStatus("current")
_VRtrRsvpSessionState_Type = TmnxOperState
_VRtrRsvpSessionState_Object = MibTableColumn
vRtrRsvpSessionState = _VRtrRsvpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 2),
    _VRtrRsvpSessionState_Type()
)
vRtrRsvpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionState.setStatus("current")


class _VRtrRsvpSessionName_Type(DisplayString):
    """Custom type vRtrRsvpSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrRsvpSessionName_Type.__name__ = "DisplayString"
_VRtrRsvpSessionName_Object = MibTableColumn
vRtrRsvpSessionName = _VRtrRsvpSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 3),
    _VRtrRsvpSessionName_Type()
)
vRtrRsvpSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionName.setStatus("current")


class _VRtrRsvpSessionSetupPriority_Type(Unsigned32):
    """Custom type vRtrRsvpSessionSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrRsvpSessionSetupPriority_Type.__name__ = "Unsigned32"
_VRtrRsvpSessionSetupPriority_Object = MibTableColumn
vRtrRsvpSessionSetupPriority = _VRtrRsvpSessionSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 4),
    _VRtrRsvpSessionSetupPriority_Type()
)
vRtrRsvpSessionSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionSetupPriority.setStatus("current")


class _VRtrRsvpSessionHoldPriority_Type(Unsigned32):
    """Custom type vRtrRsvpSessionHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrRsvpSessionHoldPriority_Type.__name__ = "Unsigned32"
_VRtrRsvpSessionHoldPriority_Object = MibTableColumn
vRtrRsvpSessionHoldPriority = _VRtrRsvpSessionHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 5),
    _VRtrRsvpSessionHoldPriority_Type()
)
vRtrRsvpSessionHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionHoldPriority.setStatus("current")
_VRtrRsvpSessionFlags_Type = Unsigned32
_VRtrRsvpSessionFlags_Object = MibTableColumn
vRtrRsvpSessionFlags = _VRtrRsvpSessionFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 6),
    _VRtrRsvpSessionFlags_Type()
)
vRtrRsvpSessionFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionFlags.setStatus("current")
_VRtrRsvpSessionEndpointAddress_Type = IpAddress
_VRtrRsvpSessionEndpointAddress_Object = MibTableColumn
vRtrRsvpSessionEndpointAddress = _VRtrRsvpSessionEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 7),
    _VRtrRsvpSessionEndpointAddress_Type()
)
vRtrRsvpSessionEndpointAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionEndpointAddress.setStatus("current")


class _VRtrRsvpSessionLspId_Type(Unsigned32):
    """Custom type vRtrRsvpSessionLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrRsvpSessionLspId_Type.__name__ = "Unsigned32"
_VRtrRsvpSessionLspId_Object = MibTableColumn
vRtrRsvpSessionLspId = _VRtrRsvpSessionLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 8),
    _VRtrRsvpSessionLspId_Type()
)
vRtrRsvpSessionLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionLspId.setStatus("current")
_VRtrRsvpSessionSenderAddress_Type = IpAddress
_VRtrRsvpSessionSenderAddress_Object = MibTableColumn
vRtrRsvpSessionSenderAddress = _VRtrRsvpSessionSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 9),
    _VRtrRsvpSessionSenderAddress_Type()
)
vRtrRsvpSessionSenderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionSenderAddress.setStatus("current")


class _VRtrRsvpSessionType_Type(Integer32):
    """Custom type vRtrRsvpSessionType based on Integer32"""
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
        *(("unknown", 1),
          ("originating", 2),
          ("transit", 3),
          ("terminating", 4),
          ("detour", 5),
          ("detourTransit", 6),
          ("detourTerminating", 7),
          ("bypassTunnel", 8),
          ("manualBypass", 9),
          ("p2mpS2lSubLspOrig", 10),
          ("p2mpS2lSubLspTransit", 11),
          ("p2mpS2lSubLspTerminate", 12),
          ("s2lBypassTunnel", 13))
    )


_VRtrRsvpSessionType_Type.__name__ = "Integer32"
_VRtrRsvpSessionType_Object = MibTableColumn
vRtrRsvpSessionType = _VRtrRsvpSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 10),
    _VRtrRsvpSessionType_Type()
)
vRtrRsvpSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionType.setStatus("current")
_VRtrRsvpSessionLocalProtectAvailable_Type = TruthValue
_VRtrRsvpSessionLocalProtectAvailable_Object = MibTableColumn
vRtrRsvpSessionLocalProtectAvailable = _VRtrRsvpSessionLocalProtectAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 11),
    _VRtrRsvpSessionLocalProtectAvailable_Type()
)
vRtrRsvpSessionLocalProtectAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionLocalProtectAvailable.setStatus("current")
_VRtrRsvpSessionLocalProtectInUse_Type = TruthValue
_VRtrRsvpSessionLocalProtectInUse_Object = MibTableColumn
vRtrRsvpSessionLocalProtectInUse = _VRtrRsvpSessionLocalProtectInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 12),
    _VRtrRsvpSessionLocalProtectInUse_Type()
)
vRtrRsvpSessionLocalProtectInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionLocalProtectInUse.setStatus("current")


class _VRtrRsvpSessionStyle_Type(Integer32):
    """Custom type vRtrRsvpSessionStyle based on Integer32"""
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
          ("styleSE", 2),
          ("styleFF", 3))
    )


_VRtrRsvpSessionStyle_Type.__name__ = "Integer32"
_VRtrRsvpSessionStyle_Object = MibTableColumn
vRtrRsvpSessionStyle = _VRtrRsvpSessionStyle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 13),
    _VRtrRsvpSessionStyle_Type()
)
vRtrRsvpSessionStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionStyle.setStatus("current")
_VRtrRsvpSessionTunnelId_Type = Unsigned32
_VRtrRsvpSessionTunnelId_Object = MibTableColumn
vRtrRsvpSessionTunnelId = _VRtrRsvpSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 14),
    _VRtrRsvpSessionTunnelId_Type()
)
vRtrRsvpSessionTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTunnelId.setStatus("current")
_VRtrRsvpSessionExtTunnelId_Type = IpAddress
_VRtrRsvpSessionExtTunnelId_Object = MibTableColumn
vRtrRsvpSessionExtTunnelId = _VRtrRsvpSessionExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 15),
    _VRtrRsvpSessionExtTunnelId_Type()
)
vRtrRsvpSessionExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionExtTunnelId.setStatus("current")
_VRtrRsvpSessionNextHopIpAddress_Type = IpAddress
_VRtrRsvpSessionNextHopIpAddress_Object = MibTableColumn
vRtrRsvpSessionNextHopIpAddress = _VRtrRsvpSessionNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 16),
    _VRtrRsvpSessionNextHopIpAddress_Type()
)
vRtrRsvpSessionNextHopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionNextHopIpAddress.setStatus("current")
_VRtrRsvpSessionDetourIndex_Type = Unsigned32
_VRtrRsvpSessionDetourIndex_Object = MibTableColumn
vRtrRsvpSessionDetourIndex = _VRtrRsvpSessionDetourIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 17),
    _VRtrRsvpSessionDetourIndex_Type()
)
vRtrRsvpSessionDetourIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionDetourIndex.setStatus("current")
_VRtrRsvpSessionDetourPLRId_Type = IpAddress
_VRtrRsvpSessionDetourPLRId_Object = MibTableColumn
vRtrRsvpSessionDetourPLRId = _VRtrRsvpSessionDetourPLRId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 18),
    _VRtrRsvpSessionDetourPLRId_Type()
)
vRtrRsvpSessionDetourPLRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionDetourPLRId.setStatus("current")
_VRtrRsvpSessionDetourAvoidNodeId_Type = IpAddress
_VRtrRsvpSessionDetourAvoidNodeId_Object = MibTableColumn
vRtrRsvpSessionDetourAvoidNodeId = _VRtrRsvpSessionDetourAvoidNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 19),
    _VRtrRsvpSessionDetourAvoidNodeId_Type()
)
vRtrRsvpSessionDetourAvoidNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionDetourAvoidNodeId.setStatus("current")
_VRtrRsvpSessionPreviousHop_Type = IpAddress
_VRtrRsvpSessionPreviousHop_Object = MibTableColumn
vRtrRsvpSessionPreviousHop = _VRtrRsvpSessionPreviousHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 20),
    _VRtrRsvpSessionPreviousHop_Type()
)
vRtrRsvpSessionPreviousHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionPreviousHop.setStatus("current")
_VRtrRsvpSessionFailCode_Type = TmnxRsvpSessionFailCode
_VRtrRsvpSessionFailCode_Object = MibTableColumn
vRtrRsvpSessionFailCode = _VRtrRsvpSessionFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 21),
    _VRtrRsvpSessionFailCode_Type()
)
vRtrRsvpSessionFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionFailCode.setStatus("current")
_VRtrRsvpSessionFailNodeAddr_Type = IpAddress
_VRtrRsvpSessionFailNodeAddr_Object = MibTableColumn
vRtrRsvpSessionFailNodeAddr = _VRtrRsvpSessionFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 22),
    _VRtrRsvpSessionFailNodeAddr_Type()
)
vRtrRsvpSessionFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionFailNodeAddr.setStatus("current")


class _VRtrRsvpSessionXCIndex_Type(Integer32):
    """Custom type vRtrRsvpSessionXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrRsvpSessionXCIndex_Type.__name__ = "Integer32"
_VRtrRsvpSessionXCIndex_Object = MibTableColumn
vRtrRsvpSessionXCIndex = _VRtrRsvpSessionXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 23),
    _VRtrRsvpSessionXCIndex_Type()
)
vRtrRsvpSessionXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionXCIndex.setStatus("current")
_VRtrRsvpSessionBypassIndex_Type = Unsigned32
_VRtrRsvpSessionBypassIndex_Object = MibTableColumn
vRtrRsvpSessionBypassIndex = _VRtrRsvpSessionBypassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 24),
    _VRtrRsvpSessionBypassIndex_Type()
)
vRtrRsvpSessionBypassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassIndex.setStatus("current")
_VRtrRsvpSessionBypassAvoid_Type = IpAddress
_VRtrRsvpSessionBypassAvoid_Object = MibTableColumn
vRtrRsvpSessionBypassAvoid = _VRtrRsvpSessionBypassAvoid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 25),
    _VRtrRsvpSessionBypassAvoid_Type()
)
vRtrRsvpSessionBypassAvoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassAvoid.setStatus("current")
_VRtrRsvpSessionBypassActive_Type = TruthValue
_VRtrRsvpSessionBypassActive_Object = MibTableColumn
vRtrRsvpSessionBypassActive = _VRtrRsvpSessionBypassActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 26),
    _VRtrRsvpSessionBypassActive_Type()
)
vRtrRsvpSessionBypassActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassActive.setStatus("current")
_VRtrRsvpSessionBypassDnstrmLabel_Type = MplsLabel
_VRtrRsvpSessionBypassDnstrmLabel_Object = MibTableColumn
vRtrRsvpSessionBypassDnstrmLabel = _VRtrRsvpSessionBypassDnstrmLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 27),
    _VRtrRsvpSessionBypassDnstrmLabel_Type()
)
vRtrRsvpSessionBypassDnstrmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassDnstrmLabel.setStatus("current")
_VRtrRsvpSessionSubGrpId_Type = Unsigned32
_VRtrRsvpSessionSubGrpId_Object = MibTableColumn
vRtrRsvpSessionSubGrpId = _VRtrRsvpSessionSubGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 28),
    _VRtrRsvpSessionSubGrpId_Type()
)
vRtrRsvpSessionSubGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionSubGrpId.setStatus("current")
_VRtrRsvpSessionSubGrpOrgIdType_Type = InetAddressType
_VRtrRsvpSessionSubGrpOrgIdType_Object = MibTableColumn
vRtrRsvpSessionSubGrpOrgIdType = _VRtrRsvpSessionSubGrpOrgIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 29),
    _VRtrRsvpSessionSubGrpOrgIdType_Type()
)
vRtrRsvpSessionSubGrpOrgIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionSubGrpOrgIdType.setStatus("current")


class _VRtrRsvpSessionSubGrpOrgIdAddr_Type(InetAddress):
    """Custom type vRtrRsvpSessionSubGrpOrgIdAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrRsvpSessionSubGrpOrgIdAddr_Type.__name__ = "InetAddress"
_VRtrRsvpSessionSubGrpOrgIdAddr_Object = MibTableColumn
vRtrRsvpSessionSubGrpOrgIdAddr = _VRtrRsvpSessionSubGrpOrgIdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 30),
    _VRtrRsvpSessionSubGrpOrgIdAddr_Type()
)
vRtrRsvpSessionSubGrpOrgIdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionSubGrpOrgIdAddr.setStatus("current")
_VRtrRsvpSessionLeafAddrType_Type = InetAddressType
_VRtrRsvpSessionLeafAddrType_Object = MibTableColumn
vRtrRsvpSessionLeafAddrType = _VRtrRsvpSessionLeafAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 31),
    _VRtrRsvpSessionLeafAddrType_Type()
)
vRtrRsvpSessionLeafAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionLeafAddrType.setStatus("current")


class _VRtrRsvpSessionLeafAddr_Type(InetAddress):
    """Custom type vRtrRsvpSessionLeafAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrRsvpSessionLeafAddr_Type.__name__ = "InetAddress"
_VRtrRsvpSessionLeafAddr_Object = MibTableColumn
vRtrRsvpSessionLeafAddr = _VRtrRsvpSessionLeafAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 32),
    _VRtrRsvpSessionLeafAddr_Type()
)
vRtrRsvpSessionLeafAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionLeafAddr.setStatus("current")
_VRtrRsvpSessionP2mpId_Type = Unsigned32
_VRtrRsvpSessionP2mpId_Object = MibTableColumn
vRtrRsvpSessionP2mpId = _VRtrRsvpSessionP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 33),
    _VRtrRsvpSessionP2mpId_Type()
)
vRtrRsvpSessionP2mpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionP2mpId.setStatus("current")
_VRtrRsvpSessionClassType_Type = TmnxRsvpDSTEClassType
_VRtrRsvpSessionClassType_Object = MibTableColumn
vRtrRsvpSessionClassType = _VRtrRsvpSessionClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 34),
    _VRtrRsvpSessionClassType_Type()
)
vRtrRsvpSessionClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionClassType.setStatus("current")


class _VRtrRsvpSessionFrrProperties_Type(Bits):
    """Custom type vRtrRsvpSessionFrrProperties based on Bits"""
    namedValues = NamedValues(
        *(("srlgNotStrict", 0),
          ("srlgDisjoint", 1))
    )

_VRtrRsvpSessionFrrProperties_Type.__name__ = "Bits"
_VRtrRsvpSessionFrrProperties_Object = MibTableColumn
vRtrRsvpSessionFrrProperties = _VRtrRsvpSessionFrrProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 35),
    _VRtrRsvpSessionFrrProperties_Type()
)
vRtrRsvpSessionFrrProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionFrrProperties.setStatus("current")
_VRtrRsvpSessionExNodeAddrType_Type = InetAddressType
_VRtrRsvpSessionExNodeAddrType_Object = MibTableColumn
vRtrRsvpSessionExNodeAddrType = _VRtrRsvpSessionExNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 36),
    _VRtrRsvpSessionExNodeAddrType_Type()
)
vRtrRsvpSessionExNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionExNodeAddrType.setStatus("current")


class _VRtrRsvpSessionExNodeAddr_Type(InetAddress):
    """Custom type vRtrRsvpSessionExNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrRsvpSessionExNodeAddr_Type.__name__ = "InetAddress"
_VRtrRsvpSessionExNodeAddr_Object = MibTableColumn
vRtrRsvpSessionExNodeAddr = _VRtrRsvpSessionExNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 37),
    _VRtrRsvpSessionExNodeAddr_Type()
)
vRtrRsvpSessionExNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionExNodeAddr.setStatus("current")
_VRtrRsvpSessionBypassInterArea_Type = TruthValue
_VRtrRsvpSessionBypassInterArea_Object = MibTableColumn
vRtrRsvpSessionBypassInterArea = _VRtrRsvpSessionBypassInterArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 38),
    _VRtrRsvpSessionBypassInterArea_Type()
)
vRtrRsvpSessionBypassInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassInterArea.setStatus("current")
_VRtrRsvpSessionBypassPathCost_Type = Unsigned32
_VRtrRsvpSessionBypassPathCost_Object = MibTableColumn
vRtrRsvpSessionBypassPathCost = _VRtrRsvpSessionBypassPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 39),
    _VRtrRsvpSessionBypassPathCost_Type()
)
vRtrRsvpSessionBypassPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassPathCost.setStatus("current")
_VRtrRsvpSessBypLastResigAttempt_Type = TimeStamp
_VRtrRsvpSessBypLastResigAttempt_Object = MibTableColumn
vRtrRsvpSessBypLastResigAttempt = _VRtrRsvpSessBypLastResigAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 40),
    _VRtrRsvpSessBypLastResigAttempt_Type()
)
vRtrRsvpSessBypLastResigAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessBypLastResigAttempt.setStatus("current")


class _VRtrRsvpSessBypLastResigReason_Type(Integer32):
    """Custom type vRtrRsvpSessBypLastResigReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("timerExpiry", 1),
          ("manualResignal", 2))
    )


_VRtrRsvpSessBypLastResigReason_Type.__name__ = "Integer32"
_VRtrRsvpSessBypLastResigReason_Object = MibTableColumn
vRtrRsvpSessBypLastResigReason = _VRtrRsvpSessBypLastResigReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 41),
    _VRtrRsvpSessBypLastResigReason_Type()
)
vRtrRsvpSessBypLastResigReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessBypLastResigReason.setStatus("current")


class _VRtrRsvpSessBypLastResigStatus_Type(Integer32):
    """Custom type vRtrRsvpSessBypLastResigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("notAttempted", 1),
          ("failed", 2),
          ("successful", 3))
    )


_VRtrRsvpSessBypLastResigStatus_Type.__name__ = "Integer32"
_VRtrRsvpSessBypLastResigStatus_Object = MibTableColumn
vRtrRsvpSessBypLastResigStatus = _VRtrRsvpSessBypLastResigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 42),
    _VRtrRsvpSessBypLastResigStatus_Type()
)
vRtrRsvpSessBypLastResigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessBypLastResigStatus.setStatus("current")


class _VRtrRsvpSBLastResigStatusReason_Type(Integer32):
    """Custom type vRtrRsvpSBLastResigStatusReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pathOptimal", 1),
          ("noConnectedPlrs", 2),
          ("nodeProtRetryInProg", 3),
          ("resignalInProg", 4),
          ("nodeProtRetryBypass", 5),
          ("resignalBypass", 6),
          ("cspfFailed", 7),
          ("setupFailed", 8))
    )


_VRtrRsvpSBLastResigStatusReason_Type.__name__ = "Integer32"
_VRtrRsvpSBLastResigStatusReason_Object = MibTableColumn
vRtrRsvpSBLastResigStatusReason = _VRtrRsvpSBLastResigStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 5, 1, 43),
    _VRtrRsvpSBLastResigStatusReason_Type()
)
vRtrRsvpSBLastResigStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSBLastResigStatusReason.setStatus("current")
_VRtrRsvpSessionStatTable_Object = MibTable
vRtrRsvpSessionStatTable = _VRtrRsvpSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6)
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionStatTable.setStatus("current")
_VRtrRsvpSessionStatEntry_Object = MibTableRow
vRtrRsvpSessionStatEntry = _VRtrRsvpSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionStatEntry.setStatus("current")
_VRtrRsvpSessionTxPaths_Type = Counter64
_VRtrRsvpSessionTxPaths_Object = MibTableColumn
vRtrRsvpSessionTxPaths = _VRtrRsvpSessionTxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 1),
    _VRtrRsvpSessionTxPaths_Type()
)
vRtrRsvpSessionTxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTxPaths.setStatus("current")
_VRtrRsvpSessionRxPaths_Type = Counter64
_VRtrRsvpSessionRxPaths_Object = MibTableColumn
vRtrRsvpSessionRxPaths = _VRtrRsvpSessionRxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 2),
    _VRtrRsvpSessionRxPaths_Type()
)
vRtrRsvpSessionRxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionRxPaths.setStatus("current")
_VRtrRsvpSessionTxResvs_Type = Counter64
_VRtrRsvpSessionTxResvs_Object = MibTableColumn
vRtrRsvpSessionTxResvs = _VRtrRsvpSessionTxResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 3),
    _VRtrRsvpSessionTxResvs_Type()
)
vRtrRsvpSessionTxResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTxResvs.setStatus("current")
_VRtrRsvpSessionRxResvs_Type = Counter64
_VRtrRsvpSessionRxResvs_Object = MibTableColumn
vRtrRsvpSessionRxResvs = _VRtrRsvpSessionRxResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 4),
    _VRtrRsvpSessionRxResvs_Type()
)
vRtrRsvpSessionRxResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionRxResvs.setStatus("current")
_VRtrRsvpSessionDetourTimeUp_Type = TimeInterval
_VRtrRsvpSessionDetourTimeUp_Object = MibTableColumn
vRtrRsvpSessionDetourTimeUp = _VRtrRsvpSessionDetourTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 5),
    _VRtrRsvpSessionDetourTimeUp_Type()
)
vRtrRsvpSessionDetourTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionDetourTimeUp.setStatus("current")
_VRtrRsvpSessionDetourAge_Type = TimeInterval
_VRtrRsvpSessionDetourAge_Object = MibTableColumn
vRtrRsvpSessionDetourAge = _VRtrRsvpSessionDetourAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 6),
    _VRtrRsvpSessionDetourAge_Type()
)
vRtrRsvpSessionDetourAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionDetourAge.setStatus("current")
_VRtrRsvpSessionBypassTimeUp_Type = TimeInterval
_VRtrRsvpSessionBypassTimeUp_Object = MibTableColumn
vRtrRsvpSessionBypassTimeUp = _VRtrRsvpSessionBypassTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 7),
    _VRtrRsvpSessionBypassTimeUp_Type()
)
vRtrRsvpSessionBypassTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassTimeUp.setStatus("current")
_VRtrRsvpSessionBypassAge_Type = TimeInterval
_VRtrRsvpSessionBypassAge_Object = MibTableColumn
vRtrRsvpSessionBypassAge = _VRtrRsvpSessionBypassAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 8),
    _VRtrRsvpSessionBypassAge_Type()
)
vRtrRsvpSessionBypassAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassAge.setStatus("current")
_VRtrRsvpSessionBypassLspCount_Type = Gauge32
_VRtrRsvpSessionBypassLspCount_Object = MibTableColumn
vRtrRsvpSessionBypassLspCount = _VRtrRsvpSessionBypassLspCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 9),
    _VRtrRsvpSessionBypassLspCount_Type()
)
vRtrRsvpSessionBypassLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionBypassLspCount.setStatus("current")
_VRtrRsvpSessionTxSrefreshPaths_Type = Counter64
_VRtrRsvpSessionTxSrefreshPaths_Object = MibTableColumn
vRtrRsvpSessionTxSrefreshPaths = _VRtrRsvpSessionTxSrefreshPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 10),
    _VRtrRsvpSessionTxSrefreshPaths_Type()
)
vRtrRsvpSessionTxSrefreshPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTxSrefreshPaths.setStatus("current")
_VRtrRsvpSessionRxSrefreshPaths_Type = Counter64
_VRtrRsvpSessionRxSrefreshPaths_Object = MibTableColumn
vRtrRsvpSessionRxSrefreshPaths = _VRtrRsvpSessionRxSrefreshPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 11),
    _VRtrRsvpSessionRxSrefreshPaths_Type()
)
vRtrRsvpSessionRxSrefreshPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionRxSrefreshPaths.setStatus("current")
_VRtrRsvpSessionTxSrefreshResvs_Type = Counter64
_VRtrRsvpSessionTxSrefreshResvs_Object = MibTableColumn
vRtrRsvpSessionTxSrefreshResvs = _VRtrRsvpSessionTxSrefreshResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 12),
    _VRtrRsvpSessionTxSrefreshResvs_Type()
)
vRtrRsvpSessionTxSrefreshResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTxSrefreshResvs.setStatus("current")
_VRtrRsvpSessionRxSrefreshResvs_Type = Counter64
_VRtrRsvpSessionRxSrefreshResvs_Object = MibTableColumn
vRtrRsvpSessionRxSrefreshResvs = _VRtrRsvpSessionRxSrefreshResvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 6, 1, 13),
    _VRtrRsvpSessionRxSrefreshResvs_Type()
)
vRtrRsvpSessionRxSrefreshResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionRxSrefreshResvs.setStatus("current")
_TmnxRsvpNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxRsvpNotificationObjects = _TmnxRsvpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 7)
)


class _VRtrRsvpIfNbrDownReasonCode_Type(Integer32):
    """Custom type vRtrRsvpIfNbrDownReasonCode based on Integer32"""
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
        *(("linkDown", 1),
          ("helloTimedOut", 2),
          ("instanceMismatch", 3),
          ("bfdDown", 4))
    )


_VRtrRsvpIfNbrDownReasonCode_Type.__name__ = "Integer32"
_VRtrRsvpIfNbrDownReasonCode_Object = MibScalar
vRtrRsvpIfNbrDownReasonCode = _VRtrRsvpIfNbrDownReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 7, 1),
    _VRtrRsvpIfNbrDownReasonCode_Type()
)
vRtrRsvpIfNbrDownReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrRsvpIfNbrDownReasonCode.setStatus("current")


class _VRtrRsvpPEFailOverReasonCode_Type(Integer32):
    """Custom type vRtrRsvpPEFailOverReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnelDown", 1),
          ("ufdSessionDown", 2))
    )


_VRtrRsvpPEFailOverReasonCode_Type.__name__ = "Integer32"
_VRtrRsvpPEFailOverReasonCode_Object = MibScalar
vRtrRsvpPEFailOverReasonCode = _VRtrRsvpPEFailOverReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 7, 2),
    _VRtrRsvpPEFailOverReasonCode_Type()
)
vRtrRsvpPEFailOverReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrRsvpPEFailOverReasonCode.setStatus("current")
_VRtrRsvpSessionTypeTable_Object = MibTable
vRtrRsvpSessionTypeTable = _VRtrRsvpSessionTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 8)
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionTypeTable.setStatus("current")
_VRtrRsvpSessionTypeEntry_Object = MibTableRow
vRtrRsvpSessionTypeEntry = _VRtrRsvpSessionTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 8, 1)
)
vRtrRsvpSessionTypeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpSessionType"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpSessionIndex"),
)
if mibBuilder.loadTexts:
    vRtrRsvpSessionTypeEntry.setStatus("current")


class _VRtrRsvpSessionTypeName_Type(DisplayString):
    """Custom type vRtrRsvpSessionTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrRsvpSessionTypeName_Type.__name__ = "DisplayString"
_VRtrRsvpSessionTypeName_Object = MibTableColumn
vRtrRsvpSessionTypeName = _VRtrRsvpSessionTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 8, 1, 1),
    _VRtrRsvpSessionTypeName_Type()
)
vRtrRsvpSessionTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpSessionTypeName.setStatus("current")
_VRtrRsvpProtectedSessionTable_Object = MibTable
vRtrRsvpProtectedSessionTable = _VRtrRsvpProtectedSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 9)
)
if mibBuilder.loadTexts:
    vRtrRsvpProtectedSessionTable.setStatus("current")
_VRtrRsvpProtectedSessionEntry_Object = MibTableRow
vRtrRsvpProtectedSessionEntry = _VRtrRsvpProtectedSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 9, 1)
)
vRtrRsvpProtectedSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpSessionIndex"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpProtectedSessionPLRIndex"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpProtectedSessionSessIndex"),
)
if mibBuilder.loadTexts:
    vRtrRsvpProtectedSessionEntry.setStatus("current")
_VRtrRsvpProtectedSessionPLRIndex_Type = Unsigned32
_VRtrRsvpProtectedSessionPLRIndex_Object = MibTableColumn
vRtrRsvpProtectedSessionPLRIndex = _VRtrRsvpProtectedSessionPLRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 9, 1, 1),
    _VRtrRsvpProtectedSessionPLRIndex_Type()
)
vRtrRsvpProtectedSessionPLRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpProtectedSessionPLRIndex.setStatus("current")
_VRtrRsvpProtectedSessionSessIndex_Type = Unsigned32
_VRtrRsvpProtectedSessionSessIndex_Object = MibTableColumn
vRtrRsvpProtectedSessionSessIndex = _VRtrRsvpProtectedSessionSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 9, 1, 2),
    _VRtrRsvpProtectedSessionSessIndex_Type()
)
vRtrRsvpProtectedSessionSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpProtectedSessionSessIndex.setStatus("current")


class _VRtrRsvpProtectedSessionName_Type(DisplayString):
    """Custom type vRtrRsvpProtectedSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrRsvpProtectedSessionName_Type.__name__ = "DisplayString"
_VRtrRsvpProtectedSessionName_Object = MibTableColumn
vRtrRsvpProtectedSessionName = _VRtrRsvpProtectedSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 9, 1, 3),
    _VRtrRsvpProtectedSessionName_Type()
)
vRtrRsvpProtectedSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpProtectedSessionName.setStatus("current")
_VRtrRsvpNbrTable_Object = MibTable
vRtrRsvpNbrTable = _VRtrRsvpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10)
)
if mibBuilder.loadTexts:
    vRtrRsvpNbrTable.setStatus("current")
_VRtrRsvpNbrEntry_Object = MibTableRow
vRtrRsvpNbrEntry = _VRtrRsvpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1)
)
vRtrRsvpNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpIfVRtrIfIndex"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpNbrAddressType"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpNbrAddress"),
)
if mibBuilder.loadTexts:
    vRtrRsvpNbrEntry.setStatus("current")
_VRtrRsvpNbrAddressType_Type = InetAddressType
_VRtrRsvpNbrAddressType_Object = MibTableColumn
vRtrRsvpNbrAddressType = _VRtrRsvpNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 1),
    _VRtrRsvpNbrAddressType_Type()
)
vRtrRsvpNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpNbrAddressType.setStatus("current")


class _VRtrRsvpNbrAddress_Type(InetAddress):
    """Custom type vRtrRsvpNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrRsvpNbrAddress_Type.__name__ = "InetAddress"
_VRtrRsvpNbrAddress_Object = MibTableColumn
vRtrRsvpNbrAddress = _VRtrRsvpNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 2),
    _VRtrRsvpNbrAddress_Type()
)
vRtrRsvpNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpNbrAddress.setStatus("current")
_VRtrRsvpNbrOperState_Type = TmnxOperState
_VRtrRsvpNbrOperState_Object = MibTableColumn
vRtrRsvpNbrOperState = _VRtrRsvpNbrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 3),
    _VRtrRsvpNbrOperState_Type()
)
vRtrRsvpNbrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrOperState.setStatus("current")
_VRtrRsvpNbrLastOperChange_Type = TimeInterval
_VRtrRsvpNbrLastOperChange_Object = MibTableColumn
vRtrRsvpNbrLastOperChange = _VRtrRsvpNbrLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 4),
    _VRtrRsvpNbrLastOperChange_Type()
)
vRtrRsvpNbrLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrLastOperChange.setStatus("current")


class _VRtrRsvpNbrFlags_Type(Bits):
    """Custom type vRtrRsvpNbrFlags based on Bits"""
    namedValues = NamedValues(
        *(("localRefreshReduction", 0),
          ("localReliableDelivery", 1),
          ("remoteRefreshReduction", 2),
          ("remoteMessageId", 3))
    )

_VRtrRsvpNbrFlags_Type.__name__ = "Bits"
_VRtrRsvpNbrFlags_Object = MibTableColumn
vRtrRsvpNbrFlags = _VRtrRsvpNbrFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 5),
    _VRtrRsvpNbrFlags_Type()
)
vRtrRsvpNbrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrFlags.setStatus("current")
_VRtrRsvpNbrSrcInstance_Type = Unsigned32
_VRtrRsvpNbrSrcInstance_Object = MibTableColumn
vRtrRsvpNbrSrcInstance = _VRtrRsvpNbrSrcInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 6),
    _VRtrRsvpNbrSrcInstance_Type()
)
vRtrRsvpNbrSrcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrSrcInstance.setStatus("current")
_VRtrRsvpNbrDstInstance_Type = Unsigned32
_VRtrRsvpNbrDstInstance_Object = MibTableColumn
vRtrRsvpNbrDstInstance = _VRtrRsvpNbrDstInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 7),
    _VRtrRsvpNbrDstInstance_Type()
)
vRtrRsvpNbrDstInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrDstInstance.setStatus("current")
_VRtrRsvpNbrHelloRefreshTimeRem_Type = Unsigned32
_VRtrRsvpNbrHelloRefreshTimeRem_Object = MibTableColumn
vRtrRsvpNbrHelloRefreshTimeRem = _VRtrRsvpNbrHelloRefreshTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 8),
    _VRtrRsvpNbrHelloRefreshTimeRem_Type()
)
vRtrRsvpNbrHelloRefreshTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrHelloRefreshTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrHelloRefreshTimeRem.setUnits("seconds")
_VRtrRsvpNbrHelloTimeoutTimeRem_Type = Unsigned32
_VRtrRsvpNbrHelloTimeoutTimeRem_Object = MibTableColumn
vRtrRsvpNbrHelloTimeoutTimeRem = _VRtrRsvpNbrHelloTimeoutTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 9),
    _VRtrRsvpNbrHelloTimeoutTimeRem_Type()
)
vRtrRsvpNbrHelloTimeoutTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrHelloTimeoutTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrHelloTimeoutTimeRem.setUnits("seconds")
_VRtrRsvpNbrHelloTimeoutCnt_Type = Counter32
_VRtrRsvpNbrHelloTimeoutCnt_Object = MibTableColumn
vRtrRsvpNbrHelloTimeoutCnt = _VRtrRsvpNbrHelloTimeoutCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 10),
    _VRtrRsvpNbrHelloTimeoutCnt_Type()
)
vRtrRsvpNbrHelloTimeoutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrHelloTimeoutCnt.setStatus("current")
_VRtrRsvpNbrInstanceMismatchCnt_Type = Counter32
_VRtrRsvpNbrInstanceMismatchCnt_Object = MibTableColumn
vRtrRsvpNbrInstanceMismatchCnt = _VRtrRsvpNbrInstanceMismatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 11),
    _VRtrRsvpNbrInstanceMismatchCnt_Type()
)
vRtrRsvpNbrInstanceMismatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrInstanceMismatchCnt.setStatus("current")
_VRtrRsvpNbrSrefreshTimeRem_Type = Unsigned32
_VRtrRsvpNbrSrefreshTimeRem_Object = MibTableColumn
vRtrRsvpNbrSrefreshTimeRem = _VRtrRsvpNbrSrefreshTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 12),
    _VRtrRsvpNbrSrefreshTimeRem_Type()
)
vRtrRsvpNbrSrefreshTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrSrefreshTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrSrefreshTimeRem.setUnits("seconds")
_VRtrRsvpNbrEpochNum_Type = Unsigned32
_VRtrRsvpNbrEpochNum_Object = MibTableColumn
vRtrRsvpNbrEpochNum = _VRtrRsvpNbrEpochNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 13),
    _VRtrRsvpNbrEpochNum_Type()
)
vRtrRsvpNbrEpochNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrEpochNum.setStatus("current")
_VRtrRsvpNbrMaxMsgId_Type = Unsigned32
_VRtrRsvpNbrMaxMsgId_Object = MibTableColumn
vRtrRsvpNbrMaxMsgId = _VRtrRsvpNbrMaxMsgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 14),
    _VRtrRsvpNbrMaxMsgId_Type()
)
vRtrRsvpNbrMaxMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrMaxMsgId.setStatus("current")
_VRtrRsvpNbrOutofOrderMsgs_Type = Counter32
_VRtrRsvpNbrOutofOrderMsgs_Object = MibTableColumn
vRtrRsvpNbrOutofOrderMsgs = _VRtrRsvpNbrOutofOrderMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 15),
    _VRtrRsvpNbrOutofOrderMsgs_Type()
)
vRtrRsvpNbrOutofOrderMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrOutofOrderMsgs.setStatus("current")
_VRtrRsvpNbrRetransmittedMsgs_Type = Counter32
_VRtrRsvpNbrRetransmittedMsgs_Object = MibTableColumn
vRtrRsvpNbrRetransmittedMsgs = _VRtrRsvpNbrRetransmittedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 16),
    _VRtrRsvpNbrRetransmittedMsgs_Type()
)
vRtrRsvpNbrRetransmittedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrRetransmittedMsgs.setStatus("current")


class _VRtrRsvpNbrGrState_Type(Integer32):
    """Custom type vRtrRsvpNbrGrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("restartInProg", 1),
          ("recoveryInProg", 2),
          ("cleanup", 3))
    )


_VRtrRsvpNbrGrState_Type.__name__ = "Integer32"
_VRtrRsvpNbrGrState_Object = MibTableColumn
vRtrRsvpNbrGrState = _VRtrRsvpNbrGrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 17),
    _VRtrRsvpNbrGrState_Type()
)
vRtrRsvpNbrGrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrState.setStatus("current")
_VRtrRsvpNbrGrHelperInvkCnt_Type = Counter32
_VRtrRsvpNbrGrHelperInvkCnt_Object = MibTableColumn
vRtrRsvpNbrGrHelperInvkCnt = _VRtrRsvpNbrGrHelperInvkCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 18),
    _VRtrRsvpNbrGrHelperInvkCnt_Type()
)
vRtrRsvpNbrGrHelperInvkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrHelperInvkCnt.setStatus("current")
_VRtrRsvpNbrGrHelperTimeRem_Type = Unsigned32
_VRtrRsvpNbrGrHelperTimeRem_Object = MibTableColumn
vRtrRsvpNbrGrHelperTimeRem = _VRtrRsvpNbrGrHelperTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 19),
    _VRtrRsvpNbrGrHelperTimeRem_Type()
)
vRtrRsvpNbrGrHelperTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrHelperTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrHelperTimeRem.setUnits("seconds")
_VRtrRsvpNbrGrRestartCap_Type = TruthValue
_VRtrRsvpNbrGrRestartCap_Object = MibTableColumn
vRtrRsvpNbrGrRestartCap = _VRtrRsvpNbrGrRestartCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 20),
    _VRtrRsvpNbrGrRestartCap_Type()
)
vRtrRsvpNbrGrRestartCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrRestartCap.setStatus("current")
_VRtrRsvpNbrGrRestartTime_Type = Unsigned32
_VRtrRsvpNbrGrRestartTime_Object = MibTableColumn
vRtrRsvpNbrGrRestartTime = _VRtrRsvpNbrGrRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 21),
    _VRtrRsvpNbrGrRestartTime_Type()
)
vRtrRsvpNbrGrRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrRestartTime.setUnits("milliseconds")
_VRtrRsvpNbrGrRecoveryTime_Type = Unsigned32
_VRtrRsvpNbrGrRecoveryTime_Object = MibTableColumn
vRtrRsvpNbrGrRecoveryTime = _VRtrRsvpNbrGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 10, 1, 22),
    _VRtrRsvpNbrGrRecoveryTime_Type()
)
vRtrRsvpNbrGrRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpNbrGrRecoveryTime.setUnits("milliseconds")
_VRtrRsvpIfDSTETable_Object = MibTable
vRtrRsvpIfDSTETable = _VRtrRsvpIfDSTETable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 11)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTETable.setStatus("current")
_VRtrRsvpIfDSTEEntry_Object = MibTableRow
vRtrRsvpIfDSTEEntry = _VRtrRsvpIfDSTEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 11, 1)
)
vRtrRsvpIfDSTEEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTETEClass"),
)
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEEntry.setStatus("current")
_VRtrRsvpIfDSTETEClass_Type = TmnxRsvpDSTETeClass
_VRtrRsvpIfDSTETEClass_Object = MibTableColumn
vRtrRsvpIfDSTETEClass = _VRtrRsvpIfDSTETEClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 11, 1, 1),
    _VRtrRsvpIfDSTETEClass_Type()
)
vRtrRsvpIfDSTETEClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTETEClass.setStatus("current")
_VRtrRsvpIfDSTEReservedBw_Type = Counter64
_VRtrRsvpIfDSTEReservedBw_Object = MibTableColumn
vRtrRsvpIfDSTEReservedBw = _VRtrRsvpIfDSTEReservedBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 11, 1, 2),
    _VRtrRsvpIfDSTEReservedBw_Type()
)
vRtrRsvpIfDSTEReservedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEReservedBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEReservedBw.setUnits("Kbps")
_VRtrRsvpIfDSTEUnreservedBw_Type = Counter64
_VRtrRsvpIfDSTEUnreservedBw_Object = MibTableColumn
vRtrRsvpIfDSTEUnreservedBw = _VRtrRsvpIfDSTEUnreservedBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 11, 1, 3),
    _VRtrRsvpIfDSTEUnreservedBw_Type()
)
vRtrRsvpIfDSTEUnreservedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEUnreservedBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRsvpIfDSTEUnreservedBw.setUnits("Kbps")
_VRtrRsvpDSTETeClassTable_Object = MibTable
vRtrRsvpDSTETeClassTable = _VRtrRsvpDSTETeClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 12)
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTETeClassTable.setStatus("current")
_VRtrRsvpDSTETeClassEntry_Object = MibTableRow
vRtrRsvpDSTETeClassEntry = _VRtrRsvpDSTETeClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 12, 1)
)
vRtrRsvpDSTETeClassEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpDSTETeClass"),
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTETeClassEntry.setStatus("current")
_VRtrRsvpDSTETeClass_Type = TmnxRsvpDSTETeClass
_VRtrRsvpDSTETeClass_Object = MibTableColumn
vRtrRsvpDSTETeClass = _VRtrRsvpDSTETeClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 12, 1, 1),
    _VRtrRsvpDSTETeClass_Type()
)
vRtrRsvpDSTETeClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpDSTETeClass.setStatus("current")


class _VRtrRsvpDSTETeClassClassType_Type(Integer32):
    """Custom type vRtrRsvpDSTETeClassClassType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrRsvpDSTETeClassClassType_Type.__name__ = "Integer32"
_VRtrRsvpDSTETeClassClassType_Object = MibTableColumn
vRtrRsvpDSTETeClassClassType = _VRtrRsvpDSTETeClassClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 12, 1, 2),
    _VRtrRsvpDSTETeClassClassType_Type()
)
vRtrRsvpDSTETeClassClassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrRsvpDSTETeClassClassType.setStatus("current")


class _VRtrRsvpDSTETeClassPriority_Type(Integer32):
    """Custom type vRtrRsvpDSTETeClassPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_VRtrRsvpDSTETeClassPriority_Type.__name__ = "Integer32"
_VRtrRsvpDSTETeClassPriority_Object = MibTableColumn
vRtrRsvpDSTETeClassPriority = _VRtrRsvpDSTETeClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 12, 1, 3),
    _VRtrRsvpDSTETeClassPriority_Type()
)
vRtrRsvpDSTETeClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrRsvpDSTETeClassPriority.setStatus("current")
_VRtrRsvpDSTETable_Object = MibTable
vRtrRsvpDSTETable = _VRtrRsvpDSTETable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13)
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTETable.setStatus("current")
_VRtrRsvpDSTEEntry_Object = MibTableRow
vRtrRsvpDSTEEntry = _VRtrRsvpDSTEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTEEntry.setStatus("current")


class _VRtrRsvpDSTEAdmCtlModel_Type(Integer32):
    """Custom type vRtrRsvpDSTEAdmCtlModel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("mam", 1),
          ("rdm", 2))
    )


_VRtrRsvpDSTEAdmCtlModel_Type.__name__ = "Integer32"
_VRtrRsvpDSTEAdmCtlModel_Object = MibTableColumn
vRtrRsvpDSTEAdmCtlModel = _VRtrRsvpDSTEAdmCtlModel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 1),
    _VRtrRsvpDSTEAdmCtlModel_Type()
)
vRtrRsvpDSTEAdmCtlModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTEAdmCtlModel.setStatus("current")


class _VRtrRsvpDSTECt0BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt0BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 100


_VRtrRsvpDSTECt0BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt0BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt0BwPercent = _VRtrRsvpDSTECt0BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 2),
    _VRtrRsvpDSTECt0BwPercent_Type()
)
vRtrRsvpDSTECt0BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt0BwPercent.setStatus("current")


class _VRtrRsvpDSTECt1BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt1BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt1BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt1BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt1BwPercent = _VRtrRsvpDSTECt1BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 3),
    _VRtrRsvpDSTECt1BwPercent_Type()
)
vRtrRsvpDSTECt1BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt1BwPercent.setStatus("current")


class _VRtrRsvpDSTECt2BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt2BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt2BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt2BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt2BwPercent = _VRtrRsvpDSTECt2BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 4),
    _VRtrRsvpDSTECt2BwPercent_Type()
)
vRtrRsvpDSTECt2BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt2BwPercent.setStatus("current")


class _VRtrRsvpDSTECt3BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt3BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt3BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt3BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt3BwPercent = _VRtrRsvpDSTECt3BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 5),
    _VRtrRsvpDSTECt3BwPercent_Type()
)
vRtrRsvpDSTECt3BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt3BwPercent.setStatus("current")


class _VRtrRsvpDSTECt4BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt4BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt4BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt4BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt4BwPercent = _VRtrRsvpDSTECt4BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 6),
    _VRtrRsvpDSTECt4BwPercent_Type()
)
vRtrRsvpDSTECt4BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt4BwPercent.setStatus("current")


class _VRtrRsvpDSTECt5BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt5BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt5BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt5BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt5BwPercent = _VRtrRsvpDSTECt5BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 7),
    _VRtrRsvpDSTECt5BwPercent_Type()
)
vRtrRsvpDSTECt5BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt5BwPercent.setStatus("current")


class _VRtrRsvpDSTECt6BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt6BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt6BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt6BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt6BwPercent = _VRtrRsvpDSTECt6BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 8),
    _VRtrRsvpDSTECt6BwPercent_Type()
)
vRtrRsvpDSTECt6BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt6BwPercent.setStatus("current")


class _VRtrRsvpDSTECt7BwPercent_Type(TmnxRsvpDSTEBwPercent):
    """Custom type vRtrRsvpDSTECt7BwPercent based on TmnxRsvpDSTEBwPercent"""
    defaultValue = 0


_VRtrRsvpDSTECt7BwPercent_Type.__name__ = "TmnxRsvpDSTEBwPercent"
_VRtrRsvpDSTECt7BwPercent_Object = MibTableColumn
vRtrRsvpDSTECt7BwPercent = _VRtrRsvpDSTECt7BwPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 13, 1, 9),
    _VRtrRsvpDSTECt7BwPercent_Type()
)
vRtrRsvpDSTECt7BwPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTECt7BwPercent.setStatus("current")
_VRtrRsvpDSTEFCMappingTable_Object = MibTable
vRtrRsvpDSTEFCMappingTable = _VRtrRsvpDSTEFCMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 14)
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTEFCMappingTable.setStatus("current")
_VRtrRsvpDSTEFCMappingEntry_Object = MibTableRow
vRtrRsvpDSTEFCMappingEntry = _VRtrRsvpDSTEFCMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 14, 1)
)
vRtrRsvpDSTEFCMappingEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RSVP-MIB", "vRtrRsvpDSTEFCMappingName"),
)
if mibBuilder.loadTexts:
    vRtrRsvpDSTEFCMappingEntry.setStatus("current")
_VRtrRsvpDSTEFCMappingName_Type = TNamedItem
_VRtrRsvpDSTEFCMappingName_Object = MibTableColumn
vRtrRsvpDSTEFCMappingName = _VRtrRsvpDSTEFCMappingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 14, 1, 1),
    _VRtrRsvpDSTEFCMappingName_Type()
)
vRtrRsvpDSTEFCMappingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRsvpDSTEFCMappingName.setStatus("current")
_VRtrRsvpDSTEFCMappingRowStatus_Type = RowStatus
_VRtrRsvpDSTEFCMappingRowStatus_Object = MibTableColumn
vRtrRsvpDSTEFCMappingRowStatus = _VRtrRsvpDSTEFCMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 14, 1, 2),
    _VRtrRsvpDSTEFCMappingRowStatus_Type()
)
vRtrRsvpDSTEFCMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTEFCMappingRowStatus.setStatus("current")
_VRtrRsvpDSTEFCMappingClassType_Type = TmnxRsvpDSTEClassType
_VRtrRsvpDSTEFCMappingClassType_Object = MibTableColumn
vRtrRsvpDSTEFCMappingClassType = _VRtrRsvpDSTEFCMappingClassType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 14, 1, 3),
    _VRtrRsvpDSTEFCMappingClassType_Type()
)
vRtrRsvpDSTEFCMappingClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpDSTEFCMappingClassType.setStatus("current")
_VRtrRsvpGenTEThresholdTable_Object = MibTable
vRtrRsvpGenTEThresholdTable = _VRtrRsvpGenTEThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15)
)
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdTable.setStatus("current")
_VRtrRsvpGenTEThresholdEntry_Object = MibTableRow
vRtrRsvpGenTEThresholdEntry = _VRtrRsvpGenTEThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdEntry.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp1_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp1 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 0


_VRtrRsvpGenTEThresholdLevelUp1_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp1_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp1 = _VRtrRsvpGenTEThresholdLevelUp1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 1),
    _VRtrRsvpGenTEThresholdLevelUp1_Type()
)
vRtrRsvpGenTEThresholdLevelUp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp1.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp2_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp2 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 15


_VRtrRsvpGenTEThresholdLevelUp2_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp2_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp2 = _VRtrRsvpGenTEThresholdLevelUp2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 2),
    _VRtrRsvpGenTEThresholdLevelUp2_Type()
)
vRtrRsvpGenTEThresholdLevelUp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp2.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp3_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp3 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 30


_VRtrRsvpGenTEThresholdLevelUp3_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp3_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp3 = _VRtrRsvpGenTEThresholdLevelUp3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 3),
    _VRtrRsvpGenTEThresholdLevelUp3_Type()
)
vRtrRsvpGenTEThresholdLevelUp3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp3.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp4_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp4 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 45


_VRtrRsvpGenTEThresholdLevelUp4_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp4_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp4 = _VRtrRsvpGenTEThresholdLevelUp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 4),
    _VRtrRsvpGenTEThresholdLevelUp4_Type()
)
vRtrRsvpGenTEThresholdLevelUp4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp4.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp5_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp5 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 60


_VRtrRsvpGenTEThresholdLevelUp5_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp5_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp5 = _VRtrRsvpGenTEThresholdLevelUp5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 5),
    _VRtrRsvpGenTEThresholdLevelUp5_Type()
)
vRtrRsvpGenTEThresholdLevelUp5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp5.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp6_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp6 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 75


_VRtrRsvpGenTEThresholdLevelUp6_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp6_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp6 = _VRtrRsvpGenTEThresholdLevelUp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 6),
    _VRtrRsvpGenTEThresholdLevelUp6_Type()
)
vRtrRsvpGenTEThresholdLevelUp6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp6.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp7_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp7 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 80


_VRtrRsvpGenTEThresholdLevelUp7_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp7_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp7 = _VRtrRsvpGenTEThresholdLevelUp7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 7),
    _VRtrRsvpGenTEThresholdLevelUp7_Type()
)
vRtrRsvpGenTEThresholdLevelUp7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp7.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp8_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp8 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 85


_VRtrRsvpGenTEThresholdLevelUp8_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp8_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp8 = _VRtrRsvpGenTEThresholdLevelUp8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 8),
    _VRtrRsvpGenTEThresholdLevelUp8_Type()
)
vRtrRsvpGenTEThresholdLevelUp8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp8.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp9_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp9 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 90


_VRtrRsvpGenTEThresholdLevelUp9_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp9_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp9 = _VRtrRsvpGenTEThresholdLevelUp9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 9),
    _VRtrRsvpGenTEThresholdLevelUp9_Type()
)
vRtrRsvpGenTEThresholdLevelUp9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp9.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp10_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp10 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 95


_VRtrRsvpGenTEThresholdLevelUp10_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp10_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp10 = _VRtrRsvpGenTEThresholdLevelUp10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 10),
    _VRtrRsvpGenTEThresholdLevelUp10_Type()
)
vRtrRsvpGenTEThresholdLevelUp10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp10.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp11_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp11 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 96


_VRtrRsvpGenTEThresholdLevelUp11_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp11_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp11 = _VRtrRsvpGenTEThresholdLevelUp11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 11),
    _VRtrRsvpGenTEThresholdLevelUp11_Type()
)
vRtrRsvpGenTEThresholdLevelUp11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp11.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp12_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp12 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 97


_VRtrRsvpGenTEThresholdLevelUp12_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp12_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp12 = _VRtrRsvpGenTEThresholdLevelUp12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 12),
    _VRtrRsvpGenTEThresholdLevelUp12_Type()
)
vRtrRsvpGenTEThresholdLevelUp12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp12.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp13_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp13 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 98


_VRtrRsvpGenTEThresholdLevelUp13_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp13_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp13 = _VRtrRsvpGenTEThresholdLevelUp13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 13),
    _VRtrRsvpGenTEThresholdLevelUp13_Type()
)
vRtrRsvpGenTEThresholdLevelUp13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp13.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp14_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp14 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 99


_VRtrRsvpGenTEThresholdLevelUp14_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp14_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp14 = _VRtrRsvpGenTEThresholdLevelUp14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 14),
    _VRtrRsvpGenTEThresholdLevelUp14_Type()
)
vRtrRsvpGenTEThresholdLevelUp14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp14.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp15_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp15 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 100


_VRtrRsvpGenTEThresholdLevelUp15_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp15_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp15 = _VRtrRsvpGenTEThresholdLevelUp15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 15),
    _VRtrRsvpGenTEThresholdLevelUp15_Type()
)
vRtrRsvpGenTEThresholdLevelUp15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp15.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelUp16_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelUp16 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = -1


_VRtrRsvpGenTEThresholdLevelUp16_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelUp16_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelUp16 = _VRtrRsvpGenTEThresholdLevelUp16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 16),
    _VRtrRsvpGenTEThresholdLevelUp16_Type()
)
vRtrRsvpGenTEThresholdLevelUp16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelUp16.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn1_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn1 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 100


_VRtrRsvpGenTEThresholdLevelDn1_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn1_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn1 = _VRtrRsvpGenTEThresholdLevelDn1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 33),
    _VRtrRsvpGenTEThresholdLevelDn1_Type()
)
vRtrRsvpGenTEThresholdLevelDn1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn1.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn2_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn2 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 99


_VRtrRsvpGenTEThresholdLevelDn2_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn2_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn2 = _VRtrRsvpGenTEThresholdLevelDn2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 34),
    _VRtrRsvpGenTEThresholdLevelDn2_Type()
)
vRtrRsvpGenTEThresholdLevelDn2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn2.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn3_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn3 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 98


_VRtrRsvpGenTEThresholdLevelDn3_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn3_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn3 = _VRtrRsvpGenTEThresholdLevelDn3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 35),
    _VRtrRsvpGenTEThresholdLevelDn3_Type()
)
vRtrRsvpGenTEThresholdLevelDn3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn3.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn4_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn4 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 97


_VRtrRsvpGenTEThresholdLevelDn4_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn4_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn4 = _VRtrRsvpGenTEThresholdLevelDn4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 36),
    _VRtrRsvpGenTEThresholdLevelDn4_Type()
)
vRtrRsvpGenTEThresholdLevelDn4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn4.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn5_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn5 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 96


_VRtrRsvpGenTEThresholdLevelDn5_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn5_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn5 = _VRtrRsvpGenTEThresholdLevelDn5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 37),
    _VRtrRsvpGenTEThresholdLevelDn5_Type()
)
vRtrRsvpGenTEThresholdLevelDn5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn5.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn6_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn6 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 95


_VRtrRsvpGenTEThresholdLevelDn6_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn6_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn6 = _VRtrRsvpGenTEThresholdLevelDn6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 38),
    _VRtrRsvpGenTEThresholdLevelDn6_Type()
)
vRtrRsvpGenTEThresholdLevelDn6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn6.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn7_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn7 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 90


_VRtrRsvpGenTEThresholdLevelDn7_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn7_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn7 = _VRtrRsvpGenTEThresholdLevelDn7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 39),
    _VRtrRsvpGenTEThresholdLevelDn7_Type()
)
vRtrRsvpGenTEThresholdLevelDn7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn7.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn8_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn8 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 85


_VRtrRsvpGenTEThresholdLevelDn8_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn8_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn8 = _VRtrRsvpGenTEThresholdLevelDn8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 40),
    _VRtrRsvpGenTEThresholdLevelDn8_Type()
)
vRtrRsvpGenTEThresholdLevelDn8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn8.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn9_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn9 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 80


_VRtrRsvpGenTEThresholdLevelDn9_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn9_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn9 = _VRtrRsvpGenTEThresholdLevelDn9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 41),
    _VRtrRsvpGenTEThresholdLevelDn9_Type()
)
vRtrRsvpGenTEThresholdLevelDn9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn9.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn10_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn10 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 75


_VRtrRsvpGenTEThresholdLevelDn10_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn10_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn10 = _VRtrRsvpGenTEThresholdLevelDn10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 42),
    _VRtrRsvpGenTEThresholdLevelDn10_Type()
)
vRtrRsvpGenTEThresholdLevelDn10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn10.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn11_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn11 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 60


_VRtrRsvpGenTEThresholdLevelDn11_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn11_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn11 = _VRtrRsvpGenTEThresholdLevelDn11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 43),
    _VRtrRsvpGenTEThresholdLevelDn11_Type()
)
vRtrRsvpGenTEThresholdLevelDn11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn11.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn12_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn12 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 45


_VRtrRsvpGenTEThresholdLevelDn12_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn12_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn12 = _VRtrRsvpGenTEThresholdLevelDn12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 44),
    _VRtrRsvpGenTEThresholdLevelDn12_Type()
)
vRtrRsvpGenTEThresholdLevelDn12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn12.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn13_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn13 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 30


_VRtrRsvpGenTEThresholdLevelDn13_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn13_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn13 = _VRtrRsvpGenTEThresholdLevelDn13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 45),
    _VRtrRsvpGenTEThresholdLevelDn13_Type()
)
vRtrRsvpGenTEThresholdLevelDn13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn13.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn14_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn14 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 15


_VRtrRsvpGenTEThresholdLevelDn14_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn14_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn14 = _VRtrRsvpGenTEThresholdLevelDn14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 46),
    _VRtrRsvpGenTEThresholdLevelDn14_Type()
)
vRtrRsvpGenTEThresholdLevelDn14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn14.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn15_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn15 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 0


_VRtrRsvpGenTEThresholdLevelDn15_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn15_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn15 = _VRtrRsvpGenTEThresholdLevelDn15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 47),
    _VRtrRsvpGenTEThresholdLevelDn15_Type()
)
vRtrRsvpGenTEThresholdLevelDn15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn15.setStatus("current")


class _VRtrRsvpGenTEThresholdLevelDn16_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpGenTEThresholdLevelDn16 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = -1


_VRtrRsvpGenTEThresholdLevelDn16_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpGenTEThresholdLevelDn16_Object = MibTableColumn
vRtrRsvpGenTEThresholdLevelDn16 = _VRtrRsvpGenTEThresholdLevelDn16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 15, 1, 48),
    _VRtrRsvpGenTEThresholdLevelDn16_Type()
)
vRtrRsvpGenTEThresholdLevelDn16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpGenTEThresholdLevelDn16.setStatus("current")
_VRtrRsvpIfTEThresholdTable_Object = MibTable
vRtrRsvpIfTEThresholdTable = _VRtrRsvpIfTEThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdTable.setStatus("current")
_VRtrRsvpIfTEThresholdEntry_Object = MibTableRow
vRtrRsvpIfTEThresholdEntry = _VRtrRsvpIfTEThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1)
)
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdEntry.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp1_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp1 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 0


_VRtrRsvpIfTEThresholdLevelUp1_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp1_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp1 = _VRtrRsvpIfTEThresholdLevelUp1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 1),
    _VRtrRsvpIfTEThresholdLevelUp1_Type()
)
vRtrRsvpIfTEThresholdLevelUp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp1.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp2_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp2 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 15


_VRtrRsvpIfTEThresholdLevelUp2_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp2_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp2 = _VRtrRsvpIfTEThresholdLevelUp2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 2),
    _VRtrRsvpIfTEThresholdLevelUp2_Type()
)
vRtrRsvpIfTEThresholdLevelUp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp2.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp3_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp3 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 30


_VRtrRsvpIfTEThresholdLevelUp3_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp3_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp3 = _VRtrRsvpIfTEThresholdLevelUp3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 3),
    _VRtrRsvpIfTEThresholdLevelUp3_Type()
)
vRtrRsvpIfTEThresholdLevelUp3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp3.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp4_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp4 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 45


_VRtrRsvpIfTEThresholdLevelUp4_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp4_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp4 = _VRtrRsvpIfTEThresholdLevelUp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 4),
    _VRtrRsvpIfTEThresholdLevelUp4_Type()
)
vRtrRsvpIfTEThresholdLevelUp4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp4.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp5_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp5 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 60


_VRtrRsvpIfTEThresholdLevelUp5_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp5_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp5 = _VRtrRsvpIfTEThresholdLevelUp5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 5),
    _VRtrRsvpIfTEThresholdLevelUp5_Type()
)
vRtrRsvpIfTEThresholdLevelUp5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp5.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp6_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp6 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 75


_VRtrRsvpIfTEThresholdLevelUp6_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp6_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp6 = _VRtrRsvpIfTEThresholdLevelUp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 6),
    _VRtrRsvpIfTEThresholdLevelUp6_Type()
)
vRtrRsvpIfTEThresholdLevelUp6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp6.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp7_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp7 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 80


_VRtrRsvpIfTEThresholdLevelUp7_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp7_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp7 = _VRtrRsvpIfTEThresholdLevelUp7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 7),
    _VRtrRsvpIfTEThresholdLevelUp7_Type()
)
vRtrRsvpIfTEThresholdLevelUp7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp7.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp8_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp8 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 85


_VRtrRsvpIfTEThresholdLevelUp8_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp8_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp8 = _VRtrRsvpIfTEThresholdLevelUp8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 8),
    _VRtrRsvpIfTEThresholdLevelUp8_Type()
)
vRtrRsvpIfTEThresholdLevelUp8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp8.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp9_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp9 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 90


_VRtrRsvpIfTEThresholdLevelUp9_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp9_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp9 = _VRtrRsvpIfTEThresholdLevelUp9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 9),
    _VRtrRsvpIfTEThresholdLevelUp9_Type()
)
vRtrRsvpIfTEThresholdLevelUp9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp9.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp10_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp10 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 95


_VRtrRsvpIfTEThresholdLevelUp10_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp10_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp10 = _VRtrRsvpIfTEThresholdLevelUp10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 10),
    _VRtrRsvpIfTEThresholdLevelUp10_Type()
)
vRtrRsvpIfTEThresholdLevelUp10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp10.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp11_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp11 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 96


_VRtrRsvpIfTEThresholdLevelUp11_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp11_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp11 = _VRtrRsvpIfTEThresholdLevelUp11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 11),
    _VRtrRsvpIfTEThresholdLevelUp11_Type()
)
vRtrRsvpIfTEThresholdLevelUp11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp11.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp12_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp12 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 97


_VRtrRsvpIfTEThresholdLevelUp12_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp12_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp12 = _VRtrRsvpIfTEThresholdLevelUp12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 12),
    _VRtrRsvpIfTEThresholdLevelUp12_Type()
)
vRtrRsvpIfTEThresholdLevelUp12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp12.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp13_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp13 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 98


_VRtrRsvpIfTEThresholdLevelUp13_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp13_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp13 = _VRtrRsvpIfTEThresholdLevelUp13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 13),
    _VRtrRsvpIfTEThresholdLevelUp13_Type()
)
vRtrRsvpIfTEThresholdLevelUp13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp13.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp14_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp14 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 99


_VRtrRsvpIfTEThresholdLevelUp14_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp14_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp14 = _VRtrRsvpIfTEThresholdLevelUp14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 14),
    _VRtrRsvpIfTEThresholdLevelUp14_Type()
)
vRtrRsvpIfTEThresholdLevelUp14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp14.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp15_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp15 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 100


_VRtrRsvpIfTEThresholdLevelUp15_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp15_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp15 = _VRtrRsvpIfTEThresholdLevelUp15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 15),
    _VRtrRsvpIfTEThresholdLevelUp15_Type()
)
vRtrRsvpIfTEThresholdLevelUp15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp15.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelUp16_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelUp16 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = -1


_VRtrRsvpIfTEThresholdLevelUp16_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelUp16_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelUp16 = _VRtrRsvpIfTEThresholdLevelUp16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 16),
    _VRtrRsvpIfTEThresholdLevelUp16_Type()
)
vRtrRsvpIfTEThresholdLevelUp16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelUp16.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn1_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn1 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 100


_VRtrRsvpIfTEThresholdLevelDn1_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn1_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn1 = _VRtrRsvpIfTEThresholdLevelDn1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 33),
    _VRtrRsvpIfTEThresholdLevelDn1_Type()
)
vRtrRsvpIfTEThresholdLevelDn1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn1.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn2_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn2 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 99


_VRtrRsvpIfTEThresholdLevelDn2_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn2_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn2 = _VRtrRsvpIfTEThresholdLevelDn2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 34),
    _VRtrRsvpIfTEThresholdLevelDn2_Type()
)
vRtrRsvpIfTEThresholdLevelDn2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn2.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn3_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn3 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 98


_VRtrRsvpIfTEThresholdLevelDn3_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn3_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn3 = _VRtrRsvpIfTEThresholdLevelDn3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 35),
    _VRtrRsvpIfTEThresholdLevelDn3_Type()
)
vRtrRsvpIfTEThresholdLevelDn3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn3.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn4_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn4 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 97


_VRtrRsvpIfTEThresholdLevelDn4_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn4_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn4 = _VRtrRsvpIfTEThresholdLevelDn4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 36),
    _VRtrRsvpIfTEThresholdLevelDn4_Type()
)
vRtrRsvpIfTEThresholdLevelDn4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn4.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn5_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn5 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 96


_VRtrRsvpIfTEThresholdLevelDn5_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn5_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn5 = _VRtrRsvpIfTEThresholdLevelDn5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 37),
    _VRtrRsvpIfTEThresholdLevelDn5_Type()
)
vRtrRsvpIfTEThresholdLevelDn5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn5.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn6_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn6 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 95


_VRtrRsvpIfTEThresholdLevelDn6_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn6_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn6 = _VRtrRsvpIfTEThresholdLevelDn6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 38),
    _VRtrRsvpIfTEThresholdLevelDn6_Type()
)
vRtrRsvpIfTEThresholdLevelDn6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn6.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn7_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn7 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 90


_VRtrRsvpIfTEThresholdLevelDn7_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn7_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn7 = _VRtrRsvpIfTEThresholdLevelDn7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 39),
    _VRtrRsvpIfTEThresholdLevelDn7_Type()
)
vRtrRsvpIfTEThresholdLevelDn7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn7.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn8_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn8 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 85


_VRtrRsvpIfTEThresholdLevelDn8_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn8_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn8 = _VRtrRsvpIfTEThresholdLevelDn8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 40),
    _VRtrRsvpIfTEThresholdLevelDn8_Type()
)
vRtrRsvpIfTEThresholdLevelDn8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn8.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn9_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn9 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 80


_VRtrRsvpIfTEThresholdLevelDn9_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn9_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn9 = _VRtrRsvpIfTEThresholdLevelDn9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 41),
    _VRtrRsvpIfTEThresholdLevelDn9_Type()
)
vRtrRsvpIfTEThresholdLevelDn9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn9.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn10_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn10 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 75


_VRtrRsvpIfTEThresholdLevelDn10_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn10_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn10 = _VRtrRsvpIfTEThresholdLevelDn10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 42),
    _VRtrRsvpIfTEThresholdLevelDn10_Type()
)
vRtrRsvpIfTEThresholdLevelDn10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn10.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn11_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn11 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 60


_VRtrRsvpIfTEThresholdLevelDn11_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn11_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn11 = _VRtrRsvpIfTEThresholdLevelDn11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 43),
    _VRtrRsvpIfTEThresholdLevelDn11_Type()
)
vRtrRsvpIfTEThresholdLevelDn11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn11.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn12_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn12 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 45


_VRtrRsvpIfTEThresholdLevelDn12_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn12_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn12 = _VRtrRsvpIfTEThresholdLevelDn12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 44),
    _VRtrRsvpIfTEThresholdLevelDn12_Type()
)
vRtrRsvpIfTEThresholdLevelDn12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn12.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn13_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn13 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 30


_VRtrRsvpIfTEThresholdLevelDn13_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn13_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn13 = _VRtrRsvpIfTEThresholdLevelDn13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 45),
    _VRtrRsvpIfTEThresholdLevelDn13_Type()
)
vRtrRsvpIfTEThresholdLevelDn13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn13.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn14_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn14 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 15


_VRtrRsvpIfTEThresholdLevelDn14_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn14_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn14 = _VRtrRsvpIfTEThresholdLevelDn14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 46),
    _VRtrRsvpIfTEThresholdLevelDn14_Type()
)
vRtrRsvpIfTEThresholdLevelDn14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn14.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn15_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn15 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = 0


_VRtrRsvpIfTEThresholdLevelDn15_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn15_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn15 = _VRtrRsvpIfTEThresholdLevelDn15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 47),
    _VRtrRsvpIfTEThresholdLevelDn15_Type()
)
vRtrRsvpIfTEThresholdLevelDn15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn15.setStatus("current")


class _VRtrRsvpIfTEThresholdLevelDn16_Type(TmnxRsvpTEThresholdLevel):
    """Custom type vRtrRsvpIfTEThresholdLevelDn16 based on TmnxRsvpTEThresholdLevel"""
    defaultValue = -1


_VRtrRsvpIfTEThresholdLevelDn16_Type.__name__ = "TmnxRsvpTEThresholdLevel"
_VRtrRsvpIfTEThresholdLevelDn16_Object = MibTableColumn
vRtrRsvpIfTEThresholdLevelDn16 = _VRtrRsvpIfTEThresholdLevelDn16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 7, 16, 1, 48),
    _VRtrRsvpIfTEThresholdLevelDn16_Type()
)
vRtrRsvpIfTEThresholdLevelDn16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpIfTEThresholdLevelDn16.setStatus("current")
_TmnxRsvpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxRsvpNotifyPrefix = _TmnxRsvpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7)
)
_TmnxRsvpNotifications_ObjectIdentity = ObjectIdentity
tmnxRsvpNotifications = _TmnxRsvpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0)
)
vRtrRsvpGeneralEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpGeneralStatEntry")
)
vRtrRsvpGeneralStatEntry.setIndexNames(*vRtrRsvpGeneralEntry.getIndexNames())
rsvpIfEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpIfEntry")
)
vRtrRsvpIfEntry.setIndexNames(*rsvpIfEntry.getIndexNames())
vRtrRsvpSessionEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpSessionStatEntry")
)
vRtrRsvpSessionStatEntry.setIndexNames(*vRtrRsvpSessionEntry.getIndexNames())
vRtrRsvpGeneralEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpDSTEEntry")
)
vRtrRsvpDSTEEntry.setIndexNames(*vRtrRsvpGeneralEntry.getIndexNames())
vRtrRsvpGeneralEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpGenTEThresholdEntry")
)
vRtrRsvpGenTEThresholdEntry.setIndexNames(*vRtrRsvpGeneralEntry.getIndexNames())
rsvpIfEntry.registerAugmentions(
    ("TIMETRA-RSVP-MIB",
     "vRtrRsvpIfTEThresholdEntry")
)
vRtrRsvpIfTEThresholdEntry.setIndexNames(*rsvpIfEntry.getIndexNames())

# Managed Objects groups

tmnxRsvpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 1)
)
tmnxRsvpGeneralGroup.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralLastChange"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralAdminState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralOperState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralKeepMultiplier"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralRefreshTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralMsgPacing"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralMsgPacingMaxBurst"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralMsgPacingPeriod"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralPsbTimeouts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralRsbTimeouts"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralGroup.setStatus("current")

tmnxRsvpSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 3)
)
tmnxRsvpSessionGroup.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpSessionState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionName"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionSetupPriority"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionHoldPriority"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionFlags"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionEndpointAddress"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionLspId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionSenderAddress"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionType"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionLocalProtectAvailable"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionLocalProtectInUse"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionStyle"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTunnelId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionExtTunnelId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionNextHopIpAddress"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionDetourIndex"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionDetourPLRId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionDetourAvoidNodeId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionPreviousHop"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionFailCode"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionFailNodeAddr"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionXCIndex"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassIndex"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassAvoid"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassActive"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassDnstrmLabel"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionRxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionRxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionDetourTimeUp"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionDetourAge"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassTimeUp"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassAge"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassLspCount"))
)
if mibBuilder.loadTexts:
    tmnxRsvpSessionGroup.setStatus("current")

tmnxRsvpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 4)
)
tmnxRsvpNotifyObjsGroup.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfNbrDownReasonCode"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpPEFailOverReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxRsvpNotifyObjsGroup.setStatus("current")

tmnxRsvpIfV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 6)
)
tmnxRsvpIfV3v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfLastEnabledTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfVRtrIfIndex"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAggregate"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthenticationKey"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfHelloInterval"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfSubscription"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfOperState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfActiveSessionCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfActiveReservationCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTotalSessionCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfBandwidth"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfReservedBandwidth"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPathErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPathTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvConfirms"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxBundles"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxAcks"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxHelloReqs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxSRefreshes"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxErrorPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxTotalPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPathErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPathTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvConfirms"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxBundles"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxAcks"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxHelloReqs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxSRefreshes"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxErrorPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxTotalPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatHelloTimeout"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfV3v0Group.setStatus("obsolete")

tmnxRsvpObsoleteV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 7)
)
tmnxRsvpObsoleteV3v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfKeepMultiplier"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfRefreshTime"))
)
if mibBuilder.loadTexts:
    tmnxRsvpObsoleteV3v0Group.setStatus("current")

tmnxRsvpIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 8)
)
tmnxRsvpIfV5v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfLastEnabledTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfVRtrIfIndex"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAggregate"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthenticationKey"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfHelloInterval"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfSubscription"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfOperState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfActiveSessionCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfActiveReservationCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTotalSessionCount"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfBandwidth"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfReservedBandwidth"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthChallenge"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthentication"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthKeyId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthRxSeqNum"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthTxSeqNum"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthWindowSize"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPathErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPathTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxResvConfirms"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxBundles"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxAcks"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxHelloReqs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxSRefreshes"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxErrorPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxTotalPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPathErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPathTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvTears"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxResvConfirms"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxBundles"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxAcks"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxHelloReqs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxSRefreshes"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxErrorPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxTotalPkts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatHelloTimeout"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatTxAuthErrors"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStatRxAuthErrors"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfV5v0Group.setStatus("current")

tmnxRsvpSessionV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 9)
)
tmnxRsvpSessionV5v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTypeName"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpProtectedSessionName"))
)
if mibBuilder.loadTexts:
    tmnxRsvpSessionV5v0Group.setStatus("current")

tmnxRsvpGeneralV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 10)
)
tmnxRsvpGeneralV6v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralRefreshBypass"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenRapidRetransmitTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenRapidRetryLimit"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV6v0Group.setStatus("current")

tmnxRsvpIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 11)
)
tmnxRsvpIfV6v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfRefreshReduction"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfReliableDelivery"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfBfdEnabled"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfV6v0Group.setStatus("current")

tmnxRsvpNbrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 12)
)
tmnxRsvpNbrV6v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpNbrOperState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrLastOperChange"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrFlags"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrSrcInstance"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrDstInstance"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrHelloRefreshTimeRem"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrHelloTimeoutTimeRem"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrHelloTimeoutCnt"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrInstanceMismatchCnt"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrSrefreshTimeRem"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrEpochNum"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrMaxMsgId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrOutofOrderMsgs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrRetransmittedMsgs"))
)
if mibBuilder.loadTexts:
    tmnxRsvpNbrV6v0Group.setStatus("current")

tmnxRsvpSessionV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 13)
)
tmnxRsvpSessionV6v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTxSrefreshPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionRxSrefreshPaths"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionTxSrefreshResvs"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionRxSrefreshResvs"))
)
if mibBuilder.loadTexts:
    tmnxRsvpSessionV6v0Group.setStatus("current")

tmnxRsvpGeneralV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 14)
)
tmnxRsvpGeneralV6v1Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGenGracefulShutdown"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfGracefulShutdown"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV6v1Group.setStatus("current")

tmnxRsvpIfV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 15)
)
tmnxRsvpIfV7v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt0BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt1BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt2BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt3BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt4BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt5BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt6BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTECt7BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfInheritance"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC0Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC1Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC2Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC3Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC4Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC5Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC6Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEBC7Bw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEReservedBw"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfDSTEUnreservedBw"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfV7v0Group.setStatus("current")

tmnxRsvpDSTEV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 16)
)
tmnxRsvpDSTEV7v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpDSTETeClassClassType"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTETeClassPriority"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTEAdmCtlModel"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt0BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt1BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt2BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt3BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt4BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt5BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt6BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTECt7BwPercent"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTEFCMappingRowStatus"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpDSTEFCMappingClassType"))
)
if mibBuilder.loadTexts:
    tmnxRsvpDSTEV7v0Group.setStatus("current")

tmnxRsvpGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 17)
)
tmnxRsvpGeneralV7v0Group.setObjects(
    ("TIMETRA-RSVP-MIB", "vRtrRsvpGenPreemptionTimer")
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV7v0Group.setStatus("current")

tmnxRsvpSessionV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 18)
)
tmnxRsvpSessionV7v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpSessionSubGrpId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionSubGrpOrgIdType"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionSubGrpOrgIdAddr"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionLeafAddrType"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionLeafAddr"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionP2mpId"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionClassType"))
)
if mibBuilder.loadTexts:
    tmnxRsvpSessionV7v0Group.setStatus("current")

tmnxRsvpGenTEThresholdV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 19)
)
tmnxRsvpGenTEThresholdV8v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp1"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp2"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp3"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp4"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp5"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp6"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp7"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp8"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp9"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp10"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp11"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp12"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp13"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp14"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp15"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelUp16"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn1"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn2"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn3"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn4"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn5"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn6"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn7"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn8"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn9"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn10"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn11"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn12"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn13"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn14"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn15"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdLevelDn16"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGenTEThresholdV8v0Group.setStatus("current")

tmnxRsvpIfTEThresholdV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 20)
)
tmnxRsvpIfTEThresholdV8v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp1"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp2"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp3"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp4"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp5"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp6"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp7"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp8"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp9"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp10"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp11"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp12"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp13"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp14"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp15"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelUp16"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn1"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn2"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn3"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn4"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn5"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn6"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn7"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn8"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn9"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn10"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn11"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn12"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn13"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn14"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn15"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfTEThresholdLevelDn16"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfTEThresholdV8v0Group.setStatus("current")

tmnxRsvpGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 21)
)
tmnxRsvpGeneralV8v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEThresholdUpdate"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEUpdateOnCacFail"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenTEUpdateTimer"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenImplicitNull"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV8v0Group.setStatus("current")

tmnxRsvpIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 22)
)
tmnxRsvpIfV8v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfImplicitNull"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfIgpUpdatePending"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfIgpNextUpdate"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfMaxResvBandwidth"))
)
if mibBuilder.loadTexts:
    tmnxRsvpIfV8v0Group.setStatus("current")

tmnxRsvpGeneralV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 23)
)
tmnxRsvpGeneralV9v0Group.setObjects(
    ("TIMETRA-RSVP-MIB", "vRtrRsvpGenNodeIdInRro")
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV9v0Group.setStatus("current")

tmnxRsvpGeneralV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 25)
)
tmnxRsvpGeneralV10v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpGenP2PMrgPntAbrtTimer"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGenP2MPMrgPntAbrtTimer"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfGraceHelper"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralGrHlprMaxRcvryTm"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralGrHlprMaxRstrtTm"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrHelperInvkCnt"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrHelperTimeRem"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrRestartCap"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrRestartTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpNbrGrRecoveryTime"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionFrrProperties"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralGrhPsbTimeouts"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralGrhRsbTimeouts"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV10v0Group.setStatus("current")

tmnxRsvpGeneralV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 26)
)
tmnxRsvpGeneralV11v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpSessionExNodeAddrType"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionExNodeAddr"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassInterArea"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV11v0Group.setStatus("current")

tmnxRsvpGeneralV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 27)
)
tmnxRsvpGeneralV12v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpIfAuthKeyChain"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessionBypassPathCost"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessBypLastResigAttempt"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessBypLastResigReason"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSessBypLastResigStatus"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpSBLastResigStatusReason"))
)
if mibBuilder.loadTexts:
    tmnxRsvpGeneralV12v0Group.setStatus("current")


# Notification objects

vRtrRsvpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 1)
)
vRtrRsvpStateChange.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralAdminState"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpGeneralOperState"))
)
if mibBuilder.loadTexts:
    vRtrRsvpStateChange.setStatus(
        "current"
    )

vRtrRsvpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 2)
)
vRtrRsvpIfStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RSVP-MIB", "rsvpIfEnabled"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfOperState"))
)
if mibBuilder.loadTexts:
    vRtrRsvpIfStateChange.setStatus(
        "current"
    )

vRtrRsvpIfNbrStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 3)
)
vRtrRsvpIfNbrStateUp.setObjects(
    ("RSVP-MIB", "rsvpNbrProtocol")
)
if mibBuilder.loadTexts:
    vRtrRsvpIfNbrStateUp.setStatus(
        "current"
    )

vRtrRsvpIfNbrStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 4)
)
vRtrRsvpIfNbrStateDown.setObjects(
      *(("RSVP-MIB", "rsvpNbrProtocol"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfNbrDownReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrRsvpIfNbrStateDown.setStatus(
        "current"
    )

vRtrRsvpPEFailOverPriToStdBy = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 5)
)
vRtrRsvpPEFailOverPriToStdBy.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAddr"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpPEFailOverReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrRsvpPEFailOverPriToStdBy.setStatus(
        "current"
    )

vRtrRsvpPEFailOverStdByToPri = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 7, 0, 6)
)
vRtrRsvpPEFailOverStdByToPri.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAddr"))
)
if mibBuilder.loadTexts:
    vRtrRsvpPEFailOverStdByToPri.setStatus(
        "current"
    )


# Notifications groups

tmnxRsvpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 5)
)
tmnxRsvpNotificationGroup.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpStateChange"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfStateChange"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfNbrStateUp"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpIfNbrStateDown"))
)
if mibBuilder.loadTexts:
    tmnxRsvpNotificationGroup.setStatus(
        "current"
    )

tmnxRsvpNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 2, 24)
)
tmnxRsvpNotificationV9v0Group.setObjects(
      *(("TIMETRA-RSVP-MIB", "vRtrRsvpPEFailOverStdByToPri"),
        ("TIMETRA-RSVP-MIB", "vRtrRsvpPEFailOverPriToStdBy"))
)
if mibBuilder.loadTexts:
    tmnxRsvpNotificationV9v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxRsvpV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 2)
)
tmnxRsvpV3v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV3v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 3)
)
tmnxRsvpV5v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 4)
)
tmnxRsvpV6v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 5)
)
tmnxRsvpV6v1Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 6)
)
tmnxRsvpV7v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpDSTEV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 7)
)
tmnxRsvpV8v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpDSTEV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGenTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 8)
)
tmnxRsvpV9v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpDSTEV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGenTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV9v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 9)
)
tmnxRsvpV10v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpDSTEV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGenTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV9v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationV9v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV10v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxRsvpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 7, 1, 10)
)
tmnxRsvpV12v0Compliance.setObjects(
      *(("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationGroup"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV5v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNbrV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV6v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV6v1Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpDSTEV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpSessionV7v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGenTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfTEThresholdV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpIfV8v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV9v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpNotificationV9v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV10v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV11v0Group"),
        ("TIMETRA-RSVP-MIB", "tmnxRsvpGeneralV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRsvpV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-RSVP-MIB",
    **{"TmnxRsvpSessionFailCode": TmnxRsvpSessionFailCode,
       "TmnxRsvpDSTETeClass": TmnxRsvpDSTETeClass,
       "TmnxRsvpDSTEBwPercent": TmnxRsvpDSTEBwPercent,
       "TmnxRsvpTEThresholdLevel": TmnxRsvpTEThresholdLevel,
       "TmnxRsvpAuthenticationType": TmnxRsvpAuthenticationType,
       "timetraRsvpMIBModule": timetraRsvpMIBModule,
       "tmnxRsvpConformance": tmnxRsvpConformance,
       "tmnxRsvpCompliances": tmnxRsvpCompliances,
       "tmnxRsvpV3v0Compliance": tmnxRsvpV3v0Compliance,
       "tmnxRsvpV5v0Compliance": tmnxRsvpV5v0Compliance,
       "tmnxRsvpV6v0Compliance": tmnxRsvpV6v0Compliance,
       "tmnxRsvpV6v1Compliance": tmnxRsvpV6v1Compliance,
       "tmnxRsvpV7v0Compliance": tmnxRsvpV7v0Compliance,
       "tmnxRsvpV8v0Compliance": tmnxRsvpV8v0Compliance,
       "tmnxRsvpV9v0Compliance": tmnxRsvpV9v0Compliance,
       "tmnxRsvpV10v0Compliance": tmnxRsvpV10v0Compliance,
       "tmnxRsvpV12v0Compliance": tmnxRsvpV12v0Compliance,
       "tmnxRsvpGroups": tmnxRsvpGroups,
       "tmnxRsvpGeneralGroup": tmnxRsvpGeneralGroup,
       "tmnxRsvpSessionGroup": tmnxRsvpSessionGroup,
       "tmnxRsvpNotifyObjsGroup": tmnxRsvpNotifyObjsGroup,
       "tmnxRsvpNotificationGroup": tmnxRsvpNotificationGroup,
       "tmnxRsvpIfV3v0Group": tmnxRsvpIfV3v0Group,
       "tmnxRsvpObsoleteV3v0Group": tmnxRsvpObsoleteV3v0Group,
       "tmnxRsvpIfV5v0Group": tmnxRsvpIfV5v0Group,
       "tmnxRsvpSessionV5v0Group": tmnxRsvpSessionV5v0Group,
       "tmnxRsvpGeneralV6v0Group": tmnxRsvpGeneralV6v0Group,
       "tmnxRsvpIfV6v0Group": tmnxRsvpIfV6v0Group,
       "tmnxRsvpNbrV6v0Group": tmnxRsvpNbrV6v0Group,
       "tmnxRsvpSessionV6v0Group": tmnxRsvpSessionV6v0Group,
       "tmnxRsvpGeneralV6v1Group": tmnxRsvpGeneralV6v1Group,
       "tmnxRsvpIfV7v0Group": tmnxRsvpIfV7v0Group,
       "tmnxRsvpDSTEV7v0Group": tmnxRsvpDSTEV7v0Group,
       "tmnxRsvpGeneralV7v0Group": tmnxRsvpGeneralV7v0Group,
       "tmnxRsvpSessionV7v0Group": tmnxRsvpSessionV7v0Group,
       "tmnxRsvpGenTEThresholdV8v0Group": tmnxRsvpGenTEThresholdV8v0Group,
       "tmnxRsvpIfTEThresholdV8v0Group": tmnxRsvpIfTEThresholdV8v0Group,
       "tmnxRsvpGeneralV8v0Group": tmnxRsvpGeneralV8v0Group,
       "tmnxRsvpIfV8v0Group": tmnxRsvpIfV8v0Group,
       "tmnxRsvpGeneralV9v0Group": tmnxRsvpGeneralV9v0Group,
       "tmnxRsvpNotificationV9v0Group": tmnxRsvpNotificationV9v0Group,
       "tmnxRsvpGeneralV10v0Group": tmnxRsvpGeneralV10v0Group,
       "tmnxRsvpGeneralV11v0Group": tmnxRsvpGeneralV11v0Group,
       "tmnxRsvpGeneralV12v0Group": tmnxRsvpGeneralV12v0Group,
       "tmnxRsvpObjs": tmnxRsvpObjs,
       "vRtrRsvpGeneralTable": vRtrRsvpGeneralTable,
       "vRtrRsvpGeneralEntry": vRtrRsvpGeneralEntry,
       "vRtrRsvpGeneralLastChange": vRtrRsvpGeneralLastChange,
       "vRtrRsvpGeneralAdminState": vRtrRsvpGeneralAdminState,
       "vRtrRsvpGeneralOperState": vRtrRsvpGeneralOperState,
       "vRtrRsvpGeneralKeepMultiplier": vRtrRsvpGeneralKeepMultiplier,
       "vRtrRsvpGeneralRefreshTime": vRtrRsvpGeneralRefreshTime,
       "vRtrRsvpGeneralMsgPacing": vRtrRsvpGeneralMsgPacing,
       "vRtrRsvpGeneralMsgPacingMaxBurst": vRtrRsvpGeneralMsgPacingMaxBurst,
       "vRtrRsvpGeneralMsgPacingPeriod": vRtrRsvpGeneralMsgPacingPeriod,
       "vRtrRsvpGeneralRefreshBypass": vRtrRsvpGeneralRefreshBypass,
       "vRtrRsvpGenRapidRetransmitTime": vRtrRsvpGenRapidRetransmitTime,
       "vRtrRsvpGenRapidRetryLimit": vRtrRsvpGenRapidRetryLimit,
       "vRtrRsvpGenGracefulShutdown": vRtrRsvpGenGracefulShutdown,
       "vRtrRsvpGenPreemptionTimer": vRtrRsvpGenPreemptionTimer,
       "vRtrRsvpGenTEThresholdUpdate": vRtrRsvpGenTEThresholdUpdate,
       "vRtrRsvpGenTEUpdateOnCacFail": vRtrRsvpGenTEUpdateOnCacFail,
       "vRtrRsvpGenTEUpdateTimer": vRtrRsvpGenTEUpdateTimer,
       "vRtrRsvpGenImplicitNull": vRtrRsvpGenImplicitNull,
       "vRtrRsvpGenNodeIdInRro": vRtrRsvpGenNodeIdInRro,
       "vRtrRsvpGenP2PMrgPntAbrtTimer": vRtrRsvpGenP2PMrgPntAbrtTimer,
       "vRtrRsvpGenP2MPMrgPntAbrtTimer": vRtrRsvpGenP2MPMrgPntAbrtTimer,
       "vRtrRsvpGeneralGrHlprMaxRcvryTm": vRtrRsvpGeneralGrHlprMaxRcvryTm,
       "vRtrRsvpGeneralGrHlprMaxRstrtTm": vRtrRsvpGeneralGrHlprMaxRstrtTm,
       "vRtrRsvpGeneralStatTable": vRtrRsvpGeneralStatTable,
       "vRtrRsvpGeneralStatEntry": vRtrRsvpGeneralStatEntry,
       "vRtrRsvpGeneralPsbTimeouts": vRtrRsvpGeneralPsbTimeouts,
       "vRtrRsvpGeneralRsbTimeouts": vRtrRsvpGeneralRsbTimeouts,
       "vRtrRsvpGeneralGrhPsbTimeouts": vRtrRsvpGeneralGrhPsbTimeouts,
       "vRtrRsvpGeneralGrhRsbTimeouts": vRtrRsvpGeneralGrhRsbTimeouts,
       "vRtrRsvpIfTable": vRtrRsvpIfTable,
       "vRtrRsvpIfEntry": vRtrRsvpIfEntry,
       "vRtrRsvpIfLastEnabledTime": vRtrRsvpIfLastEnabledTime,
       "vRtrRsvpIfVRtrIfIndex": vRtrRsvpIfVRtrIfIndex,
       "vRtrRsvpIfAggregate": vRtrRsvpIfAggregate,
       "vRtrRsvpIfAuthenticationKey": vRtrRsvpIfAuthenticationKey,
       "vRtrRsvpIfHelloInterval": vRtrRsvpIfHelloInterval,
       "vRtrRsvpIfSubscription": vRtrRsvpIfSubscription,
       "vRtrRsvpIfKeepMultiplier": vRtrRsvpIfKeepMultiplier,
       "vRtrRsvpIfRefreshTime": vRtrRsvpIfRefreshTime,
       "vRtrRsvpIfOperState": vRtrRsvpIfOperState,
       "vRtrRsvpIfActiveSessionCount": vRtrRsvpIfActiveSessionCount,
       "vRtrRsvpIfActiveReservationCount": vRtrRsvpIfActiveReservationCount,
       "vRtrRsvpIfTotalSessionCount": vRtrRsvpIfTotalSessionCount,
       "vRtrRsvpIfBandwidth": vRtrRsvpIfBandwidth,
       "vRtrRsvpIfReservedBandwidth": vRtrRsvpIfReservedBandwidth,
       "vRtrRsvpIfAuthentication": vRtrRsvpIfAuthentication,
       "vRtrRsvpIfAuthChallenge": vRtrRsvpIfAuthChallenge,
       "vRtrRsvpIfAuthKeyId": vRtrRsvpIfAuthKeyId,
       "vRtrRsvpIfAuthRxSeqNum": vRtrRsvpIfAuthRxSeqNum,
       "vRtrRsvpIfAuthTxSeqNum": vRtrRsvpIfAuthTxSeqNum,
       "vRtrRsvpIfAuthWindowSize": vRtrRsvpIfAuthWindowSize,
       "vRtrRsvpIfRefreshReduction": vRtrRsvpIfRefreshReduction,
       "vRtrRsvpIfReliableDelivery": vRtrRsvpIfReliableDelivery,
       "vRtrRsvpIfBfdEnabled": vRtrRsvpIfBfdEnabled,
       "vRtrRsvpIfGracefulShutdown": vRtrRsvpIfGracefulShutdown,
       "vRtrRsvpIfDSTECt0BwPercent": vRtrRsvpIfDSTECt0BwPercent,
       "vRtrRsvpIfDSTECt1BwPercent": vRtrRsvpIfDSTECt1BwPercent,
       "vRtrRsvpIfDSTECt2BwPercent": vRtrRsvpIfDSTECt2BwPercent,
       "vRtrRsvpIfDSTECt3BwPercent": vRtrRsvpIfDSTECt3BwPercent,
       "vRtrRsvpIfDSTECt4BwPercent": vRtrRsvpIfDSTECt4BwPercent,
       "vRtrRsvpIfDSTECt5BwPercent": vRtrRsvpIfDSTECt5BwPercent,
       "vRtrRsvpIfDSTECt6BwPercent": vRtrRsvpIfDSTECt6BwPercent,
       "vRtrRsvpIfDSTECt7BwPercent": vRtrRsvpIfDSTECt7BwPercent,
       "vRtrRsvpIfInheritance": vRtrRsvpIfInheritance,
       "vRtrRsvpIfDSTEBC0Bw": vRtrRsvpIfDSTEBC0Bw,
       "vRtrRsvpIfDSTEBC1Bw": vRtrRsvpIfDSTEBC1Bw,
       "vRtrRsvpIfDSTEBC2Bw": vRtrRsvpIfDSTEBC2Bw,
       "vRtrRsvpIfDSTEBC3Bw": vRtrRsvpIfDSTEBC3Bw,
       "vRtrRsvpIfDSTEBC4Bw": vRtrRsvpIfDSTEBC4Bw,
       "vRtrRsvpIfDSTEBC5Bw": vRtrRsvpIfDSTEBC5Bw,
       "vRtrRsvpIfDSTEBC6Bw": vRtrRsvpIfDSTEBC6Bw,
       "vRtrRsvpIfDSTEBC7Bw": vRtrRsvpIfDSTEBC7Bw,
       "vRtrRsvpIfImplicitNull": vRtrRsvpIfImplicitNull,
       "vRtrRsvpIfIgpUpdatePending": vRtrRsvpIfIgpUpdatePending,
       "vRtrRsvpIfIgpNextUpdate": vRtrRsvpIfIgpNextUpdate,
       "vRtrRsvpIfGraceHelper": vRtrRsvpIfGraceHelper,
       "vRtrRsvpIfMaxResvBandwidth": vRtrRsvpIfMaxResvBandwidth,
       "vRtrRsvpIfAuthKeyChain": vRtrRsvpIfAuthKeyChain,
       "vRtrRsvpIfStatTable": vRtrRsvpIfStatTable,
       "vRtrRsvpIfStatEntry": vRtrRsvpIfStatEntry,
       "vRtrRsvpIfStatTxPaths": vRtrRsvpIfStatTxPaths,
       "vRtrRsvpIfStatTxPathErrors": vRtrRsvpIfStatTxPathErrors,
       "vRtrRsvpIfStatTxPathTears": vRtrRsvpIfStatTxPathTears,
       "vRtrRsvpIfStatTxResvs": vRtrRsvpIfStatTxResvs,
       "vRtrRsvpIfStatTxResvErrors": vRtrRsvpIfStatTxResvErrors,
       "vRtrRsvpIfStatTxResvTears": vRtrRsvpIfStatTxResvTears,
       "vRtrRsvpIfStatTxResvConfirms": vRtrRsvpIfStatTxResvConfirms,
       "vRtrRsvpIfStatTxBundles": vRtrRsvpIfStatTxBundles,
       "vRtrRsvpIfStatTxAcks": vRtrRsvpIfStatTxAcks,
       "vRtrRsvpIfStatTxHelloReqs": vRtrRsvpIfStatTxHelloReqs,
       "vRtrRsvpIfStatTxSRefreshes": vRtrRsvpIfStatTxSRefreshes,
       "vRtrRsvpIfStatTxPkts": vRtrRsvpIfStatTxPkts,
       "vRtrRsvpIfStatTxErrorPkts": vRtrRsvpIfStatTxErrorPkts,
       "vRtrRsvpIfStatTxTotalPkts": vRtrRsvpIfStatTxTotalPkts,
       "vRtrRsvpIfStatRxPaths": vRtrRsvpIfStatRxPaths,
       "vRtrRsvpIfStatRxPathErrors": vRtrRsvpIfStatRxPathErrors,
       "vRtrRsvpIfStatRxPathTears": vRtrRsvpIfStatRxPathTears,
       "vRtrRsvpIfStatRxResvs": vRtrRsvpIfStatRxResvs,
       "vRtrRsvpIfStatRxResvErrors": vRtrRsvpIfStatRxResvErrors,
       "vRtrRsvpIfStatRxResvTears": vRtrRsvpIfStatRxResvTears,
       "vRtrRsvpIfStatRxResvConfirms": vRtrRsvpIfStatRxResvConfirms,
       "vRtrRsvpIfStatRxBundles": vRtrRsvpIfStatRxBundles,
       "vRtrRsvpIfStatRxAcks": vRtrRsvpIfStatRxAcks,
       "vRtrRsvpIfStatRxHelloReqs": vRtrRsvpIfStatRxHelloReqs,
       "vRtrRsvpIfStatRxSRefreshes": vRtrRsvpIfStatRxSRefreshes,
       "vRtrRsvpIfStatRxPkts": vRtrRsvpIfStatRxPkts,
       "vRtrRsvpIfStatRxErrorPkts": vRtrRsvpIfStatRxErrorPkts,
       "vRtrRsvpIfStatRxTotalPkts": vRtrRsvpIfStatRxTotalPkts,
       "vRtrRsvpIfStatHelloTimeout": vRtrRsvpIfStatHelloTimeout,
       "vRtrRsvpIfStatTxAuthErrors": vRtrRsvpIfStatTxAuthErrors,
       "vRtrRsvpIfStatRxAuthErrors": vRtrRsvpIfStatRxAuthErrors,
       "vRtrRsvpSessionTable": vRtrRsvpSessionTable,
       "vRtrRsvpSessionEntry": vRtrRsvpSessionEntry,
       "vRtrRsvpSessionIndex": vRtrRsvpSessionIndex,
       "vRtrRsvpSessionState": vRtrRsvpSessionState,
       "vRtrRsvpSessionName": vRtrRsvpSessionName,
       "vRtrRsvpSessionSetupPriority": vRtrRsvpSessionSetupPriority,
       "vRtrRsvpSessionHoldPriority": vRtrRsvpSessionHoldPriority,
       "vRtrRsvpSessionFlags": vRtrRsvpSessionFlags,
       "vRtrRsvpSessionEndpointAddress": vRtrRsvpSessionEndpointAddress,
       "vRtrRsvpSessionLspId": vRtrRsvpSessionLspId,
       "vRtrRsvpSessionSenderAddress": vRtrRsvpSessionSenderAddress,
       "vRtrRsvpSessionType": vRtrRsvpSessionType,
       "vRtrRsvpSessionLocalProtectAvailable": vRtrRsvpSessionLocalProtectAvailable,
       "vRtrRsvpSessionLocalProtectInUse": vRtrRsvpSessionLocalProtectInUse,
       "vRtrRsvpSessionStyle": vRtrRsvpSessionStyle,
       "vRtrRsvpSessionTunnelId": vRtrRsvpSessionTunnelId,
       "vRtrRsvpSessionExtTunnelId": vRtrRsvpSessionExtTunnelId,
       "vRtrRsvpSessionNextHopIpAddress": vRtrRsvpSessionNextHopIpAddress,
       "vRtrRsvpSessionDetourIndex": vRtrRsvpSessionDetourIndex,
       "vRtrRsvpSessionDetourPLRId": vRtrRsvpSessionDetourPLRId,
       "vRtrRsvpSessionDetourAvoidNodeId": vRtrRsvpSessionDetourAvoidNodeId,
       "vRtrRsvpSessionPreviousHop": vRtrRsvpSessionPreviousHop,
       "vRtrRsvpSessionFailCode": vRtrRsvpSessionFailCode,
       "vRtrRsvpSessionFailNodeAddr": vRtrRsvpSessionFailNodeAddr,
       "vRtrRsvpSessionXCIndex": vRtrRsvpSessionXCIndex,
       "vRtrRsvpSessionBypassIndex": vRtrRsvpSessionBypassIndex,
       "vRtrRsvpSessionBypassAvoid": vRtrRsvpSessionBypassAvoid,
       "vRtrRsvpSessionBypassActive": vRtrRsvpSessionBypassActive,
       "vRtrRsvpSessionBypassDnstrmLabel": vRtrRsvpSessionBypassDnstrmLabel,
       "vRtrRsvpSessionSubGrpId": vRtrRsvpSessionSubGrpId,
       "vRtrRsvpSessionSubGrpOrgIdType": vRtrRsvpSessionSubGrpOrgIdType,
       "vRtrRsvpSessionSubGrpOrgIdAddr": vRtrRsvpSessionSubGrpOrgIdAddr,
       "vRtrRsvpSessionLeafAddrType": vRtrRsvpSessionLeafAddrType,
       "vRtrRsvpSessionLeafAddr": vRtrRsvpSessionLeafAddr,
       "vRtrRsvpSessionP2mpId": vRtrRsvpSessionP2mpId,
       "vRtrRsvpSessionClassType": vRtrRsvpSessionClassType,
       "vRtrRsvpSessionFrrProperties": vRtrRsvpSessionFrrProperties,
       "vRtrRsvpSessionExNodeAddrType": vRtrRsvpSessionExNodeAddrType,
       "vRtrRsvpSessionExNodeAddr": vRtrRsvpSessionExNodeAddr,
       "vRtrRsvpSessionBypassInterArea": vRtrRsvpSessionBypassInterArea,
       "vRtrRsvpSessionBypassPathCost": vRtrRsvpSessionBypassPathCost,
       "vRtrRsvpSessBypLastResigAttempt": vRtrRsvpSessBypLastResigAttempt,
       "vRtrRsvpSessBypLastResigReason": vRtrRsvpSessBypLastResigReason,
       "vRtrRsvpSessBypLastResigStatus": vRtrRsvpSessBypLastResigStatus,
       "vRtrRsvpSBLastResigStatusReason": vRtrRsvpSBLastResigStatusReason,
       "vRtrRsvpSessionStatTable": vRtrRsvpSessionStatTable,
       "vRtrRsvpSessionStatEntry": vRtrRsvpSessionStatEntry,
       "vRtrRsvpSessionTxPaths": vRtrRsvpSessionTxPaths,
       "vRtrRsvpSessionRxPaths": vRtrRsvpSessionRxPaths,
       "vRtrRsvpSessionTxResvs": vRtrRsvpSessionTxResvs,
       "vRtrRsvpSessionRxResvs": vRtrRsvpSessionRxResvs,
       "vRtrRsvpSessionDetourTimeUp": vRtrRsvpSessionDetourTimeUp,
       "vRtrRsvpSessionDetourAge": vRtrRsvpSessionDetourAge,
       "vRtrRsvpSessionBypassTimeUp": vRtrRsvpSessionBypassTimeUp,
       "vRtrRsvpSessionBypassAge": vRtrRsvpSessionBypassAge,
       "vRtrRsvpSessionBypassLspCount": vRtrRsvpSessionBypassLspCount,
       "vRtrRsvpSessionTxSrefreshPaths": vRtrRsvpSessionTxSrefreshPaths,
       "vRtrRsvpSessionRxSrefreshPaths": vRtrRsvpSessionRxSrefreshPaths,
       "vRtrRsvpSessionTxSrefreshResvs": vRtrRsvpSessionTxSrefreshResvs,
       "vRtrRsvpSessionRxSrefreshResvs": vRtrRsvpSessionRxSrefreshResvs,
       "tmnxRsvpNotificationObjects": tmnxRsvpNotificationObjects,
       "vRtrRsvpIfNbrDownReasonCode": vRtrRsvpIfNbrDownReasonCode,
       "vRtrRsvpPEFailOverReasonCode": vRtrRsvpPEFailOverReasonCode,
       "vRtrRsvpSessionTypeTable": vRtrRsvpSessionTypeTable,
       "vRtrRsvpSessionTypeEntry": vRtrRsvpSessionTypeEntry,
       "vRtrRsvpSessionTypeName": vRtrRsvpSessionTypeName,
       "vRtrRsvpProtectedSessionTable": vRtrRsvpProtectedSessionTable,
       "vRtrRsvpProtectedSessionEntry": vRtrRsvpProtectedSessionEntry,
       "vRtrRsvpProtectedSessionPLRIndex": vRtrRsvpProtectedSessionPLRIndex,
       "vRtrRsvpProtectedSessionSessIndex": vRtrRsvpProtectedSessionSessIndex,
       "vRtrRsvpProtectedSessionName": vRtrRsvpProtectedSessionName,
       "vRtrRsvpNbrTable": vRtrRsvpNbrTable,
       "vRtrRsvpNbrEntry": vRtrRsvpNbrEntry,
       "vRtrRsvpNbrAddressType": vRtrRsvpNbrAddressType,
       "vRtrRsvpNbrAddress": vRtrRsvpNbrAddress,
       "vRtrRsvpNbrOperState": vRtrRsvpNbrOperState,
       "vRtrRsvpNbrLastOperChange": vRtrRsvpNbrLastOperChange,
       "vRtrRsvpNbrFlags": vRtrRsvpNbrFlags,
       "vRtrRsvpNbrSrcInstance": vRtrRsvpNbrSrcInstance,
       "vRtrRsvpNbrDstInstance": vRtrRsvpNbrDstInstance,
       "vRtrRsvpNbrHelloRefreshTimeRem": vRtrRsvpNbrHelloRefreshTimeRem,
       "vRtrRsvpNbrHelloTimeoutTimeRem": vRtrRsvpNbrHelloTimeoutTimeRem,
       "vRtrRsvpNbrHelloTimeoutCnt": vRtrRsvpNbrHelloTimeoutCnt,
       "vRtrRsvpNbrInstanceMismatchCnt": vRtrRsvpNbrInstanceMismatchCnt,
       "vRtrRsvpNbrSrefreshTimeRem": vRtrRsvpNbrSrefreshTimeRem,
       "vRtrRsvpNbrEpochNum": vRtrRsvpNbrEpochNum,
       "vRtrRsvpNbrMaxMsgId": vRtrRsvpNbrMaxMsgId,
       "vRtrRsvpNbrOutofOrderMsgs": vRtrRsvpNbrOutofOrderMsgs,
       "vRtrRsvpNbrRetransmittedMsgs": vRtrRsvpNbrRetransmittedMsgs,
       "vRtrRsvpNbrGrState": vRtrRsvpNbrGrState,
       "vRtrRsvpNbrGrHelperInvkCnt": vRtrRsvpNbrGrHelperInvkCnt,
       "vRtrRsvpNbrGrHelperTimeRem": vRtrRsvpNbrGrHelperTimeRem,
       "vRtrRsvpNbrGrRestartCap": vRtrRsvpNbrGrRestartCap,
       "vRtrRsvpNbrGrRestartTime": vRtrRsvpNbrGrRestartTime,
       "vRtrRsvpNbrGrRecoveryTime": vRtrRsvpNbrGrRecoveryTime,
       "vRtrRsvpIfDSTETable": vRtrRsvpIfDSTETable,
       "vRtrRsvpIfDSTEEntry": vRtrRsvpIfDSTEEntry,
       "vRtrRsvpIfDSTETEClass": vRtrRsvpIfDSTETEClass,
       "vRtrRsvpIfDSTEReservedBw": vRtrRsvpIfDSTEReservedBw,
       "vRtrRsvpIfDSTEUnreservedBw": vRtrRsvpIfDSTEUnreservedBw,
       "vRtrRsvpDSTETeClassTable": vRtrRsvpDSTETeClassTable,
       "vRtrRsvpDSTETeClassEntry": vRtrRsvpDSTETeClassEntry,
       "vRtrRsvpDSTETeClass": vRtrRsvpDSTETeClass,
       "vRtrRsvpDSTETeClassClassType": vRtrRsvpDSTETeClassClassType,
       "vRtrRsvpDSTETeClassPriority": vRtrRsvpDSTETeClassPriority,
       "vRtrRsvpDSTETable": vRtrRsvpDSTETable,
       "vRtrRsvpDSTEEntry": vRtrRsvpDSTEEntry,
       "vRtrRsvpDSTEAdmCtlModel": vRtrRsvpDSTEAdmCtlModel,
       "vRtrRsvpDSTECt0BwPercent": vRtrRsvpDSTECt0BwPercent,
       "vRtrRsvpDSTECt1BwPercent": vRtrRsvpDSTECt1BwPercent,
       "vRtrRsvpDSTECt2BwPercent": vRtrRsvpDSTECt2BwPercent,
       "vRtrRsvpDSTECt3BwPercent": vRtrRsvpDSTECt3BwPercent,
       "vRtrRsvpDSTECt4BwPercent": vRtrRsvpDSTECt4BwPercent,
       "vRtrRsvpDSTECt5BwPercent": vRtrRsvpDSTECt5BwPercent,
       "vRtrRsvpDSTECt6BwPercent": vRtrRsvpDSTECt6BwPercent,
       "vRtrRsvpDSTECt7BwPercent": vRtrRsvpDSTECt7BwPercent,
       "vRtrRsvpDSTEFCMappingTable": vRtrRsvpDSTEFCMappingTable,
       "vRtrRsvpDSTEFCMappingEntry": vRtrRsvpDSTEFCMappingEntry,
       "vRtrRsvpDSTEFCMappingName": vRtrRsvpDSTEFCMappingName,
       "vRtrRsvpDSTEFCMappingRowStatus": vRtrRsvpDSTEFCMappingRowStatus,
       "vRtrRsvpDSTEFCMappingClassType": vRtrRsvpDSTEFCMappingClassType,
       "vRtrRsvpGenTEThresholdTable": vRtrRsvpGenTEThresholdTable,
       "vRtrRsvpGenTEThresholdEntry": vRtrRsvpGenTEThresholdEntry,
       "vRtrRsvpGenTEThresholdLevelUp1": vRtrRsvpGenTEThresholdLevelUp1,
       "vRtrRsvpGenTEThresholdLevelUp2": vRtrRsvpGenTEThresholdLevelUp2,
       "vRtrRsvpGenTEThresholdLevelUp3": vRtrRsvpGenTEThresholdLevelUp3,
       "vRtrRsvpGenTEThresholdLevelUp4": vRtrRsvpGenTEThresholdLevelUp4,
       "vRtrRsvpGenTEThresholdLevelUp5": vRtrRsvpGenTEThresholdLevelUp5,
       "vRtrRsvpGenTEThresholdLevelUp6": vRtrRsvpGenTEThresholdLevelUp6,
       "vRtrRsvpGenTEThresholdLevelUp7": vRtrRsvpGenTEThresholdLevelUp7,
       "vRtrRsvpGenTEThresholdLevelUp8": vRtrRsvpGenTEThresholdLevelUp8,
       "vRtrRsvpGenTEThresholdLevelUp9": vRtrRsvpGenTEThresholdLevelUp9,
       "vRtrRsvpGenTEThresholdLevelUp10": vRtrRsvpGenTEThresholdLevelUp10,
       "vRtrRsvpGenTEThresholdLevelUp11": vRtrRsvpGenTEThresholdLevelUp11,
       "vRtrRsvpGenTEThresholdLevelUp12": vRtrRsvpGenTEThresholdLevelUp12,
       "vRtrRsvpGenTEThresholdLevelUp13": vRtrRsvpGenTEThresholdLevelUp13,
       "vRtrRsvpGenTEThresholdLevelUp14": vRtrRsvpGenTEThresholdLevelUp14,
       "vRtrRsvpGenTEThresholdLevelUp15": vRtrRsvpGenTEThresholdLevelUp15,
       "vRtrRsvpGenTEThresholdLevelUp16": vRtrRsvpGenTEThresholdLevelUp16,
       "vRtrRsvpGenTEThresholdLevelDn1": vRtrRsvpGenTEThresholdLevelDn1,
       "vRtrRsvpGenTEThresholdLevelDn2": vRtrRsvpGenTEThresholdLevelDn2,
       "vRtrRsvpGenTEThresholdLevelDn3": vRtrRsvpGenTEThresholdLevelDn3,
       "vRtrRsvpGenTEThresholdLevelDn4": vRtrRsvpGenTEThresholdLevelDn4,
       "vRtrRsvpGenTEThresholdLevelDn5": vRtrRsvpGenTEThresholdLevelDn5,
       "vRtrRsvpGenTEThresholdLevelDn6": vRtrRsvpGenTEThresholdLevelDn6,
       "vRtrRsvpGenTEThresholdLevelDn7": vRtrRsvpGenTEThresholdLevelDn7,
       "vRtrRsvpGenTEThresholdLevelDn8": vRtrRsvpGenTEThresholdLevelDn8,
       "vRtrRsvpGenTEThresholdLevelDn9": vRtrRsvpGenTEThresholdLevelDn9,
       "vRtrRsvpGenTEThresholdLevelDn10": vRtrRsvpGenTEThresholdLevelDn10,
       "vRtrRsvpGenTEThresholdLevelDn11": vRtrRsvpGenTEThresholdLevelDn11,
       "vRtrRsvpGenTEThresholdLevelDn12": vRtrRsvpGenTEThresholdLevelDn12,
       "vRtrRsvpGenTEThresholdLevelDn13": vRtrRsvpGenTEThresholdLevelDn13,
       "vRtrRsvpGenTEThresholdLevelDn14": vRtrRsvpGenTEThresholdLevelDn14,
       "vRtrRsvpGenTEThresholdLevelDn15": vRtrRsvpGenTEThresholdLevelDn15,
       "vRtrRsvpGenTEThresholdLevelDn16": vRtrRsvpGenTEThresholdLevelDn16,
       "vRtrRsvpIfTEThresholdTable": vRtrRsvpIfTEThresholdTable,
       "vRtrRsvpIfTEThresholdEntry": vRtrRsvpIfTEThresholdEntry,
       "vRtrRsvpIfTEThresholdLevelUp1": vRtrRsvpIfTEThresholdLevelUp1,
       "vRtrRsvpIfTEThresholdLevelUp2": vRtrRsvpIfTEThresholdLevelUp2,
       "vRtrRsvpIfTEThresholdLevelUp3": vRtrRsvpIfTEThresholdLevelUp3,
       "vRtrRsvpIfTEThresholdLevelUp4": vRtrRsvpIfTEThresholdLevelUp4,
       "vRtrRsvpIfTEThresholdLevelUp5": vRtrRsvpIfTEThresholdLevelUp5,
       "vRtrRsvpIfTEThresholdLevelUp6": vRtrRsvpIfTEThresholdLevelUp6,
       "vRtrRsvpIfTEThresholdLevelUp7": vRtrRsvpIfTEThresholdLevelUp7,
       "vRtrRsvpIfTEThresholdLevelUp8": vRtrRsvpIfTEThresholdLevelUp8,
       "vRtrRsvpIfTEThresholdLevelUp9": vRtrRsvpIfTEThresholdLevelUp9,
       "vRtrRsvpIfTEThresholdLevelUp10": vRtrRsvpIfTEThresholdLevelUp10,
       "vRtrRsvpIfTEThresholdLevelUp11": vRtrRsvpIfTEThresholdLevelUp11,
       "vRtrRsvpIfTEThresholdLevelUp12": vRtrRsvpIfTEThresholdLevelUp12,
       "vRtrRsvpIfTEThresholdLevelUp13": vRtrRsvpIfTEThresholdLevelUp13,
       "vRtrRsvpIfTEThresholdLevelUp14": vRtrRsvpIfTEThresholdLevelUp14,
       "vRtrRsvpIfTEThresholdLevelUp15": vRtrRsvpIfTEThresholdLevelUp15,
       "vRtrRsvpIfTEThresholdLevelUp16": vRtrRsvpIfTEThresholdLevelUp16,
       "vRtrRsvpIfTEThresholdLevelDn1": vRtrRsvpIfTEThresholdLevelDn1,
       "vRtrRsvpIfTEThresholdLevelDn2": vRtrRsvpIfTEThresholdLevelDn2,
       "vRtrRsvpIfTEThresholdLevelDn3": vRtrRsvpIfTEThresholdLevelDn3,
       "vRtrRsvpIfTEThresholdLevelDn4": vRtrRsvpIfTEThresholdLevelDn4,
       "vRtrRsvpIfTEThresholdLevelDn5": vRtrRsvpIfTEThresholdLevelDn5,
       "vRtrRsvpIfTEThresholdLevelDn6": vRtrRsvpIfTEThresholdLevelDn6,
       "vRtrRsvpIfTEThresholdLevelDn7": vRtrRsvpIfTEThresholdLevelDn7,
       "vRtrRsvpIfTEThresholdLevelDn8": vRtrRsvpIfTEThresholdLevelDn8,
       "vRtrRsvpIfTEThresholdLevelDn9": vRtrRsvpIfTEThresholdLevelDn9,
       "vRtrRsvpIfTEThresholdLevelDn10": vRtrRsvpIfTEThresholdLevelDn10,
       "vRtrRsvpIfTEThresholdLevelDn11": vRtrRsvpIfTEThresholdLevelDn11,
       "vRtrRsvpIfTEThresholdLevelDn12": vRtrRsvpIfTEThresholdLevelDn12,
       "vRtrRsvpIfTEThresholdLevelDn13": vRtrRsvpIfTEThresholdLevelDn13,
       "vRtrRsvpIfTEThresholdLevelDn14": vRtrRsvpIfTEThresholdLevelDn14,
       "vRtrRsvpIfTEThresholdLevelDn15": vRtrRsvpIfTEThresholdLevelDn15,
       "vRtrRsvpIfTEThresholdLevelDn16": vRtrRsvpIfTEThresholdLevelDn16,
       "tmnxRsvpNotifyPrefix": tmnxRsvpNotifyPrefix,
       "tmnxRsvpNotifications": tmnxRsvpNotifications,
       "vRtrRsvpStateChange": vRtrRsvpStateChange,
       "vRtrRsvpIfStateChange": vRtrRsvpIfStateChange,
       "vRtrRsvpIfNbrStateUp": vRtrRsvpIfNbrStateUp,
       "vRtrRsvpIfNbrStateDown": vRtrRsvpIfNbrStateDown,
       "vRtrRsvpPEFailOverPriToStdBy": vRtrRsvpPEFailOverPriToStdBy,
       "vRtrRsvpPEFailOverStdByToPri": vRtrRsvpPEFailOverStdByToPri}
)
