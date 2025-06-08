# SNMP MIB module (GGSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_10923/GGSN-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:07:41 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ggsnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PerceivedSeverity(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("cleared", 6),
          ("informational", 7))
    )



class AlarmEventCause(TextualConvention, Integer32):
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
        *(("new", 1),
          ("changed", 2),
          ("cleared", 3),
          ("notification", 4),
          ("mibcleared", 5),
          ("usercleared", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EjnmobileipABmib_ObjectIdentity = ObjectIdentity
ejnmobileipABmib = _EjnmobileipABmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923)
)
_EjnxMibs_ObjectIdentity = ObjectIdentity
ejnxMibs = _EjnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1)
)
_GgsnMibs_ObjectIdentity = ObjectIdentity
ggsnMibs = _GgsnMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1)
)
_GgsnMIBObjects_ObjectIdentity = ObjectIdentity
ggsnMIBObjects = _GgsnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1)
)
_GgsnGeneralInfo_ObjectIdentity = ObjectIdentity
ggsnGeneralInfo = _GgsnGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1)
)


class _GgsnVersion_Type(DisplayString):
    """Custom type ggsnVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GgsnVersion_Type.__name__ = "DisplayString"
_GgsnVersion_Object = MibScalar
ggsnVersion = _GgsnVersion_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 1),
    _GgsnVersion_Type()
)
ggsnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnVersion.setStatus("current")
_GgsnInstalled_Type = TimeStamp
_GgsnInstalled_Object = MibScalar
ggsnInstalled = _GgsnInstalled_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 2),
    _GgsnInstalled_Type()
)
ggsnInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnInstalled.setStatus("current")
_GgsnGlobalStats_ObjectIdentity = ObjectIdentity
ggsnGlobalStats = _GgsnGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3)
)
_GgsnStatReportTime_Type = TimeStamp
_GgsnStatReportTime_Object = MibScalar
ggsnStatReportTime = _GgsnStatReportTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 1),
    _GgsnStatReportTime_Type()
)
ggsnStatReportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnStatReportTime.setStatus("current")
_GgsnNbrOfActivePdpContexts_Type = Gauge32
_GgsnNbrOfActivePdpContexts_Object = MibScalar
ggsnNbrOfActivePdpContexts = _GgsnNbrOfActivePdpContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 2),
    _GgsnNbrOfActivePdpContexts_Type()
)
ggsnNbrOfActivePdpContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfActivePdpContexts.setStatus("current")
_GgsnPdpContextsStatsAttempted_ObjectIdentity = ObjectIdentity
ggsnPdpContextsStatsAttempted = _GgsnPdpContextsStatsAttempted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3)
)
_GgsnAttemptedActivation_Type = Counter64
_GgsnAttemptedActivation_Object = MibScalar
ggsnAttemptedActivation = _GgsnAttemptedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 1),
    _GgsnAttemptedActivation_Type()
)
ggsnAttemptedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivation.setStatus("current")
_GgsnAttemptedDeactivation_Type = Counter64
_GgsnAttemptedDeactivation_Object = MibScalar
ggsnAttemptedDeactivation = _GgsnAttemptedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 2),
    _GgsnAttemptedDeactivation_Type()
)
ggsnAttemptedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedDeactivation.setStatus("current")
_GgsnAttemptedSelfDeactivation_Type = Counter64
_GgsnAttemptedSelfDeactivation_Object = MibScalar
ggsnAttemptedSelfDeactivation = _GgsnAttemptedSelfDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 3),
    _GgsnAttemptedSelfDeactivation_Type()
)
ggsnAttemptedSelfDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedSelfDeactivation.setStatus("current")
_GgsnAttemptedUpdate_Type = Counter64
_GgsnAttemptedUpdate_Object = MibScalar
ggsnAttemptedUpdate = _GgsnAttemptedUpdate_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 4),
    _GgsnAttemptedUpdate_Type()
)
ggsnAttemptedUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedUpdate.setStatus("current")
_GgsnAttemptedTimeDeactivation_Type = Counter64
_GgsnAttemptedTimeDeactivation_Object = MibScalar
ggsnAttemptedTimeDeactivation = _GgsnAttemptedTimeDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 5),
    _GgsnAttemptedTimeDeactivation_Type()
)
ggsnAttemptedTimeDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedTimeDeactivation.setStatus("deprecated")
_GgsnAttemptedManualDeactivation_Type = Counter64
_GgsnAttemptedManualDeactivation_Object = MibScalar
ggsnAttemptedManualDeactivation = _GgsnAttemptedManualDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 6),
    _GgsnAttemptedManualDeactivation_Type()
)
ggsnAttemptedManualDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedManualDeactivation.setStatus("current")
_GgsnAttemptedSecondaryActivation_Type = Counter64
_GgsnAttemptedSecondaryActivation_Object = MibScalar
ggsnAttemptedSecondaryActivation = _GgsnAttemptedSecondaryActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 7),
    _GgsnAttemptedSecondaryActivation_Type()
)
ggsnAttemptedSecondaryActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedSecondaryActivation.setStatus("current")
_GgsnAttemptedActivationIpv6_Type = Counter64
_GgsnAttemptedActivationIpv6_Object = MibScalar
ggsnAttemptedActivationIpv6 = _GgsnAttemptedActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 8),
    _GgsnAttemptedActivationIpv6_Type()
)
ggsnAttemptedActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationIpv6.setStatus("current")
_GgsnAttemptedSecondaryActivationIpv6_Type = Counter64
_GgsnAttemptedSecondaryActivationIpv6_Object = MibScalar
ggsnAttemptedSecondaryActivationIpv6 = _GgsnAttemptedSecondaryActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 9),
    _GgsnAttemptedSecondaryActivationIpv6_Type()
)
ggsnAttemptedSecondaryActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedSecondaryActivationIpv6.setStatus("current")
_GgsnAttemptedActivationWlan_Type = Counter64
_GgsnAttemptedActivationWlan_Object = MibScalar
ggsnAttemptedActivationWlan = _GgsnAttemptedActivationWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 10),
    _GgsnAttemptedActivationWlan_Type()
)
ggsnAttemptedActivationWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationWlan.setStatus("current")
_GgsnAttemptedActivationConversational_Type = Counter64
_GgsnAttemptedActivationConversational_Object = MibScalar
ggsnAttemptedActivationConversational = _GgsnAttemptedActivationConversational_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 11),
    _GgsnAttemptedActivationConversational_Type()
)
ggsnAttemptedActivationConversational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationConversational.setStatus("current")
_GgsnAttemptedActivationStreaming_Type = Counter64
_GgsnAttemptedActivationStreaming_Object = MibScalar
ggsnAttemptedActivationStreaming = _GgsnAttemptedActivationStreaming_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 12),
    _GgsnAttemptedActivationStreaming_Type()
)
ggsnAttemptedActivationStreaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationStreaming.setStatus("current")
_GgsnAttemptedActivationInteractive_Type = Counter64
_GgsnAttemptedActivationInteractive_Object = MibScalar
ggsnAttemptedActivationInteractive = _GgsnAttemptedActivationInteractive_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 13),
    _GgsnAttemptedActivationInteractive_Type()
)
ggsnAttemptedActivationInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationInteractive.setStatus("current")
_GgsnAttemptedActivationBackground_Type = Counter64
_GgsnAttemptedActivationBackground_Object = MibScalar
ggsnAttemptedActivationBackground = _GgsnAttemptedActivationBackground_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 14),
    _GgsnAttemptedActivationBackground_Type()
)
ggsnAttemptedActivationBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationBackground.setStatus("current")
_GgsnAttemptedActivationDiscarded_Type = Counter64
_GgsnAttemptedActivationDiscarded_Object = MibScalar
ggsnAttemptedActivationDiscarded = _GgsnAttemptedActivationDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 15),
    _GgsnAttemptedActivationDiscarded_Type()
)
ggsnAttemptedActivationDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationDiscarded.setStatus("current")
_GgsnAttemptedActivationIpv4v6_Type = Counter64
_GgsnAttemptedActivationIpv4v6_Object = MibScalar
ggsnAttemptedActivationIpv4v6 = _GgsnAttemptedActivationIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 3, 16),
    _GgsnAttemptedActivationIpv4v6_Type()
)
ggsnAttemptedActivationIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAttemptedActivationIpv4v6.setStatus("current")
_GgsnPdpContextsStatsCompleted_ObjectIdentity = ObjectIdentity
ggsnPdpContextsStatsCompleted = _GgsnPdpContextsStatsCompleted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4)
)
_GgsnCompletedActivation_Type = Counter64
_GgsnCompletedActivation_Object = MibScalar
ggsnCompletedActivation = _GgsnCompletedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 1),
    _GgsnCompletedActivation_Type()
)
ggsnCompletedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivation.setStatus("current")
_GgsnCompletedDeactivation_Type = Counter64
_GgsnCompletedDeactivation_Object = MibScalar
ggsnCompletedDeactivation = _GgsnCompletedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 2),
    _GgsnCompletedDeactivation_Type()
)
ggsnCompletedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedDeactivation.setStatus("current")
_GgsnCompletedSelfDeactivation_Type = Counter64
_GgsnCompletedSelfDeactivation_Object = MibScalar
ggsnCompletedSelfDeactivation = _GgsnCompletedSelfDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 3),
    _GgsnCompletedSelfDeactivation_Type()
)
ggsnCompletedSelfDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedSelfDeactivation.setStatus("current")
_GgsnCompletedUpdate_Type = Counter64
_GgsnCompletedUpdate_Object = MibScalar
ggsnCompletedUpdate = _GgsnCompletedUpdate_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 4),
    _GgsnCompletedUpdate_Type()
)
ggsnCompletedUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedUpdate.setStatus("current")
_GgsnIdleTimeoutDeactivation_Type = Counter64
_GgsnIdleTimeoutDeactivation_Object = MibScalar
ggsnIdleTimeoutDeactivation = _GgsnIdleTimeoutDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 5),
    _GgsnIdleTimeoutDeactivation_Type()
)
ggsnIdleTimeoutDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnIdleTimeoutDeactivation.setStatus("current")
_GgsnCompletedManualDeactivation_Type = Counter64
_GgsnCompletedManualDeactivation_Object = MibScalar
ggsnCompletedManualDeactivation = _GgsnCompletedManualDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 6),
    _GgsnCompletedManualDeactivation_Type()
)
ggsnCompletedManualDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedManualDeactivation.setStatus("current")
_GgsnCompletedSecondaryActivation_Type = Counter64
_GgsnCompletedSecondaryActivation_Object = MibScalar
ggsnCompletedSecondaryActivation = _GgsnCompletedSecondaryActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 7),
    _GgsnCompletedSecondaryActivation_Type()
)
ggsnCompletedSecondaryActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedSecondaryActivation.setStatus("current")
_GgsnSessionTimeoutDeactivation_Type = Counter64
_GgsnSessionTimeoutDeactivation_Object = MibScalar
ggsnSessionTimeoutDeactivation = _GgsnSessionTimeoutDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 8),
    _GgsnSessionTimeoutDeactivation_Type()
)
ggsnSessionTimeoutDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSessionTimeoutDeactivation.setStatus("current")
_GgsnCompletedActivationIpv6_Type = Counter64
_GgsnCompletedActivationIpv6_Object = MibScalar
ggsnCompletedActivationIpv6 = _GgsnCompletedActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 9),
    _GgsnCompletedActivationIpv6_Type()
)
ggsnCompletedActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationIpv6.setStatus("current")
_GgsnCompletedSecondaryActivationIpv6_Type = Counter64
_GgsnCompletedSecondaryActivationIpv6_Object = MibScalar
ggsnCompletedSecondaryActivationIpv6 = _GgsnCompletedSecondaryActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 10),
    _GgsnCompletedSecondaryActivationIpv6_Type()
)
ggsnCompletedSecondaryActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedSecondaryActivationIpv6.setStatus("current")
_GgsnCompletedActivationWlan_Type = Counter64
_GgsnCompletedActivationWlan_Object = MibScalar
ggsnCompletedActivationWlan = _GgsnCompletedActivationWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 11),
    _GgsnCompletedActivationWlan_Type()
)
ggsnCompletedActivationWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationWlan.setStatus("current")
_GgsnCompletedActivationConversational_Type = Counter64
_GgsnCompletedActivationConversational_Object = MibScalar
ggsnCompletedActivationConversational = _GgsnCompletedActivationConversational_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 12),
    _GgsnCompletedActivationConversational_Type()
)
ggsnCompletedActivationConversational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationConversational.setStatus("current")
_GgsnCompletedActivationStreaming_Type = Counter64
_GgsnCompletedActivationStreaming_Object = MibScalar
ggsnCompletedActivationStreaming = _GgsnCompletedActivationStreaming_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 13),
    _GgsnCompletedActivationStreaming_Type()
)
ggsnCompletedActivationStreaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationStreaming.setStatus("current")
_GgsnCompletedActivationInteractive_Type = Counter64
_GgsnCompletedActivationInteractive_Object = MibScalar
ggsnCompletedActivationInteractive = _GgsnCompletedActivationInteractive_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 14),
    _GgsnCompletedActivationInteractive_Type()
)
ggsnCompletedActivationInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationInteractive.setStatus("current")
_GgsnCompletedActivationBackground_Type = Counter64
_GgsnCompletedActivationBackground_Object = MibScalar
ggsnCompletedActivationBackground = _GgsnCompletedActivationBackground_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 15),
    _GgsnCompletedActivationBackground_Type()
)
ggsnCompletedActivationBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationBackground.setStatus("current")
_GgsnCompletedActivationIpv4v6_Type = Counter64
_GgsnCompletedActivationIpv4v6_Object = MibScalar
ggsnCompletedActivationIpv4v6 = _GgsnCompletedActivationIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 4, 16),
    _GgsnCompletedActivationIpv4v6_Type()
)
ggsnCompletedActivationIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnCompletedActivationIpv4v6.setStatus("current")
_GgsnPdpContextsStatsFailed_ObjectIdentity = ObjectIdentity
ggsnPdpContextsStatsFailed = _GgsnPdpContextsStatsFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 5)
)
_GgsnFailedActivation_Type = Counter64
_GgsnFailedActivation_Object = MibScalar
ggsnFailedActivation = _GgsnFailedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 5, 1),
    _GgsnFailedActivation_Type()
)
ggsnFailedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFailedActivation.setStatus("current")
_GgsnGtpStats_ObjectIdentity = ObjectIdentity
ggsnGtpStats = _GgsnGtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6)
)
_GgsnGtpUplinkPackets_Type = Counter64
_GgsnGtpUplinkPackets_Object = MibScalar
ggsnGtpUplinkPackets = _GgsnGtpUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 1),
    _GgsnGtpUplinkPackets_Type()
)
ggsnGtpUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpUplinkPackets.setStatus("current")
_GgsnGtpUplinkBytes_Type = Counter64
_GgsnGtpUplinkBytes_Object = MibScalar
ggsnGtpUplinkBytes = _GgsnGtpUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 2),
    _GgsnGtpUplinkBytes_Type()
)
ggsnGtpUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpUplinkBytes.setStatus("current")
_GgsnGtpDownlinkPackets_Type = Counter64
_GgsnGtpDownlinkPackets_Object = MibScalar
ggsnGtpDownlinkPackets = _GgsnGtpDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 3),
    _GgsnGtpDownlinkPackets_Type()
)
ggsnGtpDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpDownlinkPackets.setStatus("current")
_GgsnGtpDownlinkBytes_Type = Counter64
_GgsnGtpDownlinkBytes_Object = MibScalar
ggsnGtpDownlinkBytes = _GgsnGtpDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 4),
    _GgsnGtpDownlinkBytes_Type()
)
ggsnGtpDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpDownlinkBytes.setStatus("current")
_GgsnGtpControlPacketDrops_Type = Counter64
_GgsnGtpControlPacketDrops_Object = MibScalar
ggsnGtpControlPacketDrops = _GgsnGtpControlPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 5),
    _GgsnGtpControlPacketDrops_Type()
)
ggsnGtpControlPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpControlPacketDrops.setStatus("current")
_GgsnGtpVerUnsupPacketsReceived_Type = Counter64
_GgsnGtpVerUnsupPacketsReceived_Object = MibScalar
ggsnGtpVerUnsupPacketsReceived = _GgsnGtpVerUnsupPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 6),
    _GgsnGtpVerUnsupPacketsReceived_Type()
)
ggsnGtpVerUnsupPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpVerUnsupPacketsReceived.setStatus("current")
_GgsnGtpVerUnsupPacketsSent_Type = Counter64
_GgsnGtpVerUnsupPacketsSent_Object = MibScalar
ggsnGtpVerUnsupPacketsSent = _GgsnGtpVerUnsupPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 7),
    _GgsnGtpVerUnsupPacketsSent_Type()
)
ggsnGtpVerUnsupPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpVerUnsupPacketsSent.setStatus("current")
_GgsnGtpEchoReqReceived_Type = Counter64
_GgsnGtpEchoReqReceived_Object = MibScalar
ggsnGtpEchoReqReceived = _GgsnGtpEchoReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 8),
    _GgsnGtpEchoReqReceived_Type()
)
ggsnGtpEchoReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpEchoReqReceived.setStatus("current")
_GgsnGtpEchoReqSent_Type = Counter64
_GgsnGtpEchoReqSent_Object = MibScalar
ggsnGtpEchoReqSent = _GgsnGtpEchoReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 9),
    _GgsnGtpEchoReqSent_Type()
)
ggsnGtpEchoReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpEchoReqSent.setStatus("current")
_GgsnGtpEchoRespReceived_Type = Counter64
_GgsnGtpEchoRespReceived_Object = MibScalar
ggsnGtpEchoRespReceived = _GgsnGtpEchoRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 10),
    _GgsnGtpEchoRespReceived_Type()
)
ggsnGtpEchoRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpEchoRespReceived.setStatus("current")
_GgsnGtpEchoRespSent_Type = Counter64
_GgsnGtpEchoRespSent_Object = MibScalar
ggsnGtpEchoRespSent = _GgsnGtpEchoRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 11),
    _GgsnGtpEchoRespSent_Type()
)
ggsnGtpEchoRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpEchoRespSent.setStatus("current")
_GgsnGtpPdpCreateReqReceived_Type = Counter64
_GgsnGtpPdpCreateReqReceived_Object = MibScalar
ggsnGtpPdpCreateReqReceived = _GgsnGtpPdpCreateReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 12),
    _GgsnGtpPdpCreateReqReceived_Type()
)
ggsnGtpPdpCreateReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpCreateReqReceived.setStatus("current")
_GgsnGtpPdpCreateRespSent_Type = Counter64
_GgsnGtpPdpCreateRespSent_Object = MibScalar
ggsnGtpPdpCreateRespSent = _GgsnGtpPdpCreateRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 13),
    _GgsnGtpPdpCreateRespSent_Type()
)
ggsnGtpPdpCreateRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpCreateRespSent.setStatus("current")
_GgsnGtpPdpUpdateReqReceived_Type = Counter64
_GgsnGtpPdpUpdateReqReceived_Object = MibScalar
ggsnGtpPdpUpdateReqReceived = _GgsnGtpPdpUpdateReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 14),
    _GgsnGtpPdpUpdateReqReceived_Type()
)
ggsnGtpPdpUpdateReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpUpdateReqReceived.setStatus("current")
_GgsnGtpPdpUpdateReqSent_Type = Counter64
_GgsnGtpPdpUpdateReqSent_Object = MibScalar
ggsnGtpPdpUpdateReqSent = _GgsnGtpPdpUpdateReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 15),
    _GgsnGtpPdpUpdateReqSent_Type()
)
ggsnGtpPdpUpdateReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpUpdateReqSent.setStatus("current")
_GgsnGtpPdpUpdateRespReceived_Type = Counter64
_GgsnGtpPdpUpdateRespReceived_Object = MibScalar
ggsnGtpPdpUpdateRespReceived = _GgsnGtpPdpUpdateRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 16),
    _GgsnGtpPdpUpdateRespReceived_Type()
)
ggsnGtpPdpUpdateRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpUpdateRespReceived.setStatus("current")
_GgsnGtpPdpUpdateRespSent_Type = Counter64
_GgsnGtpPdpUpdateRespSent_Object = MibScalar
ggsnGtpPdpUpdateRespSent = _GgsnGtpPdpUpdateRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 17),
    _GgsnGtpPdpUpdateRespSent_Type()
)
ggsnGtpPdpUpdateRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpUpdateRespSent.setStatus("current")
_GgsnGtpPdpDeleteReqReceived_Type = Counter64
_GgsnGtpPdpDeleteReqReceived_Object = MibScalar
ggsnGtpPdpDeleteReqReceived = _GgsnGtpPdpDeleteReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 18),
    _GgsnGtpPdpDeleteReqReceived_Type()
)
ggsnGtpPdpDeleteReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpDeleteReqReceived.setStatus("current")
_GgsnGtpPdpDeleteReqSent_Type = Counter64
_GgsnGtpPdpDeleteReqSent_Object = MibScalar
ggsnGtpPdpDeleteReqSent = _GgsnGtpPdpDeleteReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 19),
    _GgsnGtpPdpDeleteReqSent_Type()
)
ggsnGtpPdpDeleteReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpDeleteReqSent.setStatus("current")
_GgsnGtpPdpDeleteRespReceived_Type = Counter64
_GgsnGtpPdpDeleteRespReceived_Object = MibScalar
ggsnGtpPdpDeleteRespReceived = _GgsnGtpPdpDeleteRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 20),
    _GgsnGtpPdpDeleteRespReceived_Type()
)
ggsnGtpPdpDeleteRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpDeleteRespReceived.setStatus("current")
_GgsnGtpPdpDeleteRespSent_Type = Counter64
_GgsnGtpPdpDeleteRespSent_Object = MibScalar
ggsnGtpPdpDeleteRespSent = _GgsnGtpPdpDeleteRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 21),
    _GgsnGtpPdpDeleteRespSent_Type()
)
ggsnGtpPdpDeleteRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpDeleteRespSent.setStatus("current")
_GgsnGtpRequestsAccepted_Type = Counter64
_GgsnGtpRequestsAccepted_Object = MibScalar
ggsnGtpRequestsAccepted = _GgsnGtpRequestsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 22),
    _GgsnGtpRequestsAccepted_Type()
)
ggsnGtpRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpRequestsAccepted.setStatus("current")
_GgsnGtpNbrOfTunnels_Type = Gauge32
_GgsnGtpNbrOfTunnels_Object = MibScalar
ggsnGtpNbrOfTunnels = _GgsnGtpNbrOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 23),
    _GgsnGtpNbrOfTunnels_Type()
)
ggsnGtpNbrOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpNbrOfTunnels.setStatus("current")
_GgsnGtpNbrOfCreatedTunnels_Type = Counter64
_GgsnGtpNbrOfCreatedTunnels_Object = MibScalar
ggsnGtpNbrOfCreatedTunnels = _GgsnGtpNbrOfCreatedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 24),
    _GgsnGtpNbrOfCreatedTunnels_Type()
)
ggsnGtpNbrOfCreatedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpNbrOfCreatedTunnels.setStatus("current")
_GgsnGtpPdpInitiateContextActivationRespReceived_Type = Counter64
_GgsnGtpPdpInitiateContextActivationRespReceived_Object = MibScalar
ggsnGtpPdpInitiateContextActivationRespReceived = _GgsnGtpPdpInitiateContextActivationRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 25),
    _GgsnGtpPdpInitiateContextActivationRespReceived_Type()
)
ggsnGtpPdpInitiateContextActivationRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpInitiateContextActivationRespReceived.setStatus("current")
_GgsnGtpPdpInitiateContextActivationReqSent_Type = Counter64
_GgsnGtpPdpInitiateContextActivationReqSent_Object = MibScalar
ggsnGtpPdpInitiateContextActivationReqSent = _GgsnGtpPdpInitiateContextActivationReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 26),
    _GgsnGtpPdpInitiateContextActivationReqSent_Type()
)
ggsnGtpPdpInitiateContextActivationReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPdpInitiateContextActivationReqSent.setStatus("current")
_GgsnGtpv0PdpCreateReqReceived_Type = Counter64
_GgsnGtpv0PdpCreateReqReceived_Object = MibScalar
ggsnGtpv0PdpCreateReqReceived = _GgsnGtpv0PdpCreateReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 6, 27),
    _GgsnGtpv0PdpCreateReqReceived_Type()
)
ggsnGtpv0PdpCreateReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpv0PdpCreateReqReceived.setStatus("current")
_GgsnGtpErrorStats_ObjectIdentity = ObjectIdentity
ggsnGtpErrorStats = _GgsnGtpErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7)
)
_GgsnGtpErrorIndicationReceived_Type = Counter64
_GgsnGtpErrorIndicationReceived_Object = MibScalar
ggsnGtpErrorIndicationReceived = _GgsnGtpErrorIndicationReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 1),
    _GgsnGtpErrorIndicationReceived_Type()
)
ggsnGtpErrorIndicationReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorIndicationReceived.setStatus("current")
_GgsnGtpErrorIndicationSent_Type = Counter64
_GgsnGtpErrorIndicationSent_Object = MibScalar
ggsnGtpErrorIndicationSent = _GgsnGtpErrorIndicationSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 2),
    _GgsnGtpErrorIndicationSent_Type()
)
ggsnGtpErrorIndicationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorIndicationSent.setStatus("current")
_GgsnGtpErrorInvalidRequestFormat_Type = Counter64
_GgsnGtpErrorInvalidRequestFormat_Object = MibScalar
ggsnGtpErrorInvalidRequestFormat = _GgsnGtpErrorInvalidRequestFormat_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 3),
    _GgsnGtpErrorInvalidRequestFormat_Type()
)
ggsnGtpErrorInvalidRequestFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorInvalidRequestFormat.setStatus("current")
_GgsnGtpErrorResourcesUnavailable_Type = Counter64
_GgsnGtpErrorResourcesUnavailable_Object = MibScalar
ggsnGtpErrorResourcesUnavailable = _GgsnGtpErrorResourcesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 4),
    _GgsnGtpErrorResourcesUnavailable_Type()
)
ggsnGtpErrorResourcesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorResourcesUnavailable.setStatus("current")
_GgsnGtpErrorDynAddrUnavailable_Type = Counter64
_GgsnGtpErrorDynAddrUnavailable_Object = MibScalar
ggsnGtpErrorDynAddrUnavailable = _GgsnGtpErrorDynAddrUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 5),
    _GgsnGtpErrorDynAddrUnavailable_Type()
)
ggsnGtpErrorDynAddrUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorDynAddrUnavailable.setStatus("current")
_GgsnGtpErrorMemoryUnavailable_Type = Counter64
_GgsnGtpErrorMemoryUnavailable_Object = MibScalar
ggsnGtpErrorMemoryUnavailable = _GgsnGtpErrorMemoryUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 6),
    _GgsnGtpErrorMemoryUnavailable_Type()
)
ggsnGtpErrorMemoryUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMemoryUnavailable.setStatus("current")
_GgsnGtpErrorApnUnknown_Type = Counter64
_GgsnGtpErrorApnUnknown_Object = MibScalar
ggsnGtpErrorApnUnknown = _GgsnGtpErrorApnUnknown_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 7),
    _GgsnGtpErrorApnUnknown_Type()
)
ggsnGtpErrorApnUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorApnUnknown.setStatus("current")
_GgsnGtpErrorPdpAddrUnknown_Type = Counter64
_GgsnGtpErrorPdpAddrUnknown_Object = MibScalar
ggsnGtpErrorPdpAddrUnknown = _GgsnGtpErrorPdpAddrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 8),
    _GgsnGtpErrorPdpAddrUnknown_Type()
)
ggsnGtpErrorPdpAddrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPdpAddrUnknown.setStatus("current")
_GgsnGtpErrorAuthenticationFailed_Type = Counter64
_GgsnGtpErrorAuthenticationFailed_Object = MibScalar
ggsnGtpErrorAuthenticationFailed = _GgsnGtpErrorAuthenticationFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 9),
    _GgsnGtpErrorAuthenticationFailed_Type()
)
ggsnGtpErrorAuthenticationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorAuthenticationFailed.setStatus("current")
_GgsnGtpErrorSystemFailure_Type = Counter64
_GgsnGtpErrorSystemFailure_Object = MibScalar
ggsnGtpErrorSystemFailure = _GgsnGtpErrorSystemFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 10),
    _GgsnGtpErrorSystemFailure_Type()
)
ggsnGtpErrorSystemFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorSystemFailure.setStatus("current")
_GgsnGtpErrorTftSemanticError_Type = Counter64
_GgsnGtpErrorTftSemanticError_Object = MibScalar
ggsnGtpErrorTftSemanticError = _GgsnGtpErrorTftSemanticError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 11),
    _GgsnGtpErrorTftSemanticError_Type()
)
ggsnGtpErrorTftSemanticError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorTftSemanticError.setStatus("current")
_GgsnGtpErrorTftSyntaxError_Type = Counter64
_GgsnGtpErrorTftSyntaxError_Object = MibScalar
ggsnGtpErrorTftSyntaxError = _GgsnGtpErrorTftSyntaxError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 12),
    _GgsnGtpErrorTftSyntaxError_Type()
)
ggsnGtpErrorTftSyntaxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorTftSyntaxError.setStatus("current")
_GgsnGtpErrorPackFiltSemantError_Type = Counter64
_GgsnGtpErrorPackFiltSemantError_Object = MibScalar
ggsnGtpErrorPackFiltSemantError = _GgsnGtpErrorPackFiltSemantError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 13),
    _GgsnGtpErrorPackFiltSemantError_Type()
)
ggsnGtpErrorPackFiltSemantError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPackFiltSemantError.setStatus("current")
_GgsnGtpErrorPackFiltSyntaxError_Type = Counter64
_GgsnGtpErrorPackFiltSyntaxError_Object = MibScalar
ggsnGtpErrorPackFiltSyntaxError = _GgsnGtpErrorPackFiltSyntaxError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 14),
    _GgsnGtpErrorPackFiltSyntaxError_Type()
)
ggsnGtpErrorPackFiltSyntaxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPackFiltSyntaxError.setStatus("current")
_GgsnGtpErrorMandatoryIEMissing_Type = Counter64
_GgsnGtpErrorMandatoryIEMissing_Object = MibScalar
ggsnGtpErrorMandatoryIEMissing = _GgsnGtpErrorMandatoryIEMissing_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 15),
    _GgsnGtpErrorMandatoryIEMissing_Type()
)
ggsnGtpErrorMandatoryIEMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEMissing.setStatus("current")
_GgsnGtpErrorMandatoryIEInvalid_Type = Counter64
_GgsnGtpErrorMandatoryIEInvalid_Object = MibScalar
ggsnGtpErrorMandatoryIEInvalid = _GgsnGtpErrorMandatoryIEInvalid_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 16),
    _GgsnGtpErrorMandatoryIEInvalid_Type()
)
ggsnGtpErrorMandatoryIEInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEInvalid.setStatus("current")
_GgsnGtpErrorOptionalIEInvalid_Type = Counter64
_GgsnGtpErrorOptionalIEInvalid_Object = MibScalar
ggsnGtpErrorOptionalIEInvalid = _GgsnGtpErrorOptionalIEInvalid_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 17),
    _GgsnGtpErrorOptionalIEInvalid_Type()
)
ggsnGtpErrorOptionalIEInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorOptionalIEInvalid.setStatus("current")
_GgsnGtpErrorReferenceInexistent_Type = Counter64
_GgsnGtpErrorReferenceInexistent_Object = MibScalar
ggsnGtpErrorReferenceInexistent = _GgsnGtpErrorReferenceInexistent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 18),
    _GgsnGtpErrorReferenceInexistent_Type()
)
ggsnGtpErrorReferenceInexistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorReferenceInexistent.setStatus("current")
_GgsnGtpErrorServiceUnsupported_Type = Counter64
_GgsnGtpErrorServiceUnsupported_Object = MibScalar
ggsnGtpErrorServiceUnsupported = _GgsnGtpErrorServiceUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 19),
    _GgsnGtpErrorServiceUnsupported_Type()
)
ggsnGtpErrorServiceUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorServiceUnsupported.setStatus("current")
_GgsnGtpErrorInvalidRequestFormatUpd_Type = Counter64
_GgsnGtpErrorInvalidRequestFormatUpd_Object = MibScalar
ggsnGtpErrorInvalidRequestFormatUpd = _GgsnGtpErrorInvalidRequestFormatUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 20),
    _GgsnGtpErrorInvalidRequestFormatUpd_Type()
)
ggsnGtpErrorInvalidRequestFormatUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorInvalidRequestFormatUpd.setStatus("current")
_GgsnGtpErrorInvalidRequestFormatDel_Type = Counter64
_GgsnGtpErrorInvalidRequestFormatDel_Object = MibScalar
ggsnGtpErrorInvalidRequestFormatDel = _GgsnGtpErrorInvalidRequestFormatDel_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 21),
    _GgsnGtpErrorInvalidRequestFormatDel_Type()
)
ggsnGtpErrorInvalidRequestFormatDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorInvalidRequestFormatDel.setStatus("current")
_GgsnGtpErrorSystemFailureUpd_Type = Counter64
_GgsnGtpErrorSystemFailureUpd_Object = MibScalar
ggsnGtpErrorSystemFailureUpd = _GgsnGtpErrorSystemFailureUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 22),
    _GgsnGtpErrorSystemFailureUpd_Type()
)
ggsnGtpErrorSystemFailureUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorSystemFailureUpd.setStatus("current")
_GgsnGtpErrorTftSemanticErrorUpd_Type = Counter64
_GgsnGtpErrorTftSemanticErrorUpd_Object = MibScalar
ggsnGtpErrorTftSemanticErrorUpd = _GgsnGtpErrorTftSemanticErrorUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 23),
    _GgsnGtpErrorTftSemanticErrorUpd_Type()
)
ggsnGtpErrorTftSemanticErrorUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorTftSemanticErrorUpd.setStatus("current")
_GgsnGtpErrorTftSyntaxErrorUpd_Type = Counter64
_GgsnGtpErrorTftSyntaxErrorUpd_Object = MibScalar
ggsnGtpErrorTftSyntaxErrorUpd = _GgsnGtpErrorTftSyntaxErrorUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 24),
    _GgsnGtpErrorTftSyntaxErrorUpd_Type()
)
ggsnGtpErrorTftSyntaxErrorUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorTftSyntaxErrorUpd.setStatus("current")
_GgsnGtpErrorPackFiltSemantErrorUpd_Type = Counter64
_GgsnGtpErrorPackFiltSemantErrorUpd_Object = MibScalar
ggsnGtpErrorPackFiltSemantErrorUpd = _GgsnGtpErrorPackFiltSemantErrorUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 25),
    _GgsnGtpErrorPackFiltSemantErrorUpd_Type()
)
ggsnGtpErrorPackFiltSemantErrorUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPackFiltSemantErrorUpd.setStatus("current")
_GgsnGtpErrorPackFiltSyntaxErrorUpd_Type = Counter64
_GgsnGtpErrorPackFiltSyntaxErrorUpd_Object = MibScalar
ggsnGtpErrorPackFiltSyntaxErrorUpd = _GgsnGtpErrorPackFiltSyntaxErrorUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 26),
    _GgsnGtpErrorPackFiltSyntaxErrorUpd_Type()
)
ggsnGtpErrorPackFiltSyntaxErrorUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPackFiltSyntaxErrorUpd.setStatus("current")
_GgsnGtpErrorMandatoryIEMissingUpd_Type = Counter64
_GgsnGtpErrorMandatoryIEMissingUpd_Object = MibScalar
ggsnGtpErrorMandatoryIEMissingUpd = _GgsnGtpErrorMandatoryIEMissingUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 27),
    _GgsnGtpErrorMandatoryIEMissingUpd_Type()
)
ggsnGtpErrorMandatoryIEMissingUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEMissingUpd.setStatus("current")
_GgsnGtpErrorMandatoryIEMissingDel_Type = Counter64
_GgsnGtpErrorMandatoryIEMissingDel_Object = MibScalar
ggsnGtpErrorMandatoryIEMissingDel = _GgsnGtpErrorMandatoryIEMissingDel_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 28),
    _GgsnGtpErrorMandatoryIEMissingDel_Type()
)
ggsnGtpErrorMandatoryIEMissingDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEMissingDel.setStatus("current")
_GgsnGtpErrorMandatoryIEInvalidUpd_Type = Counter64
_GgsnGtpErrorMandatoryIEInvalidUpd_Object = MibScalar
ggsnGtpErrorMandatoryIEInvalidUpd = _GgsnGtpErrorMandatoryIEInvalidUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 29),
    _GgsnGtpErrorMandatoryIEInvalidUpd_Type()
)
ggsnGtpErrorMandatoryIEInvalidUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEInvalidUpd.setStatus("current")
_GgsnGtpErrorMandatoryIEInvalidDel_Type = Counter64
_GgsnGtpErrorMandatoryIEInvalidDel_Object = MibScalar
ggsnGtpErrorMandatoryIEInvalidDel = _GgsnGtpErrorMandatoryIEInvalidDel_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 30),
    _GgsnGtpErrorMandatoryIEInvalidDel_Type()
)
ggsnGtpErrorMandatoryIEInvalidDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorMandatoryIEInvalidDel.setStatus("current")
_GgsnGtpErrorOptionalIEInvalidUpd_Type = Counter64
_GgsnGtpErrorOptionalIEInvalidUpd_Object = MibScalar
ggsnGtpErrorOptionalIEInvalidUpd = _GgsnGtpErrorOptionalIEInvalidUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 31),
    _GgsnGtpErrorOptionalIEInvalidUpd_Type()
)
ggsnGtpErrorOptionalIEInvalidUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorOptionalIEInvalidUpd.setStatus("current")
_GgsnGtpErrorOptionalIEInvalidDel_Type = Counter64
_GgsnGtpErrorOptionalIEInvalidDel_Object = MibScalar
ggsnGtpErrorOptionalIEInvalidDel = _GgsnGtpErrorOptionalIEInvalidDel_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 32),
    _GgsnGtpErrorOptionalIEInvalidDel_Type()
)
ggsnGtpErrorOptionalIEInvalidDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorOptionalIEInvalidDel.setStatus("current")
_GgsnGtpErrorReferenceInexistentUpd_Type = Counter64
_GgsnGtpErrorReferenceInexistentUpd_Object = MibScalar
ggsnGtpErrorReferenceInexistentUpd = _GgsnGtpErrorReferenceInexistentUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 33),
    _GgsnGtpErrorReferenceInexistentUpd_Type()
)
ggsnGtpErrorReferenceInexistentUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorReferenceInexistentUpd.setStatus("current")
_GgsnGtpErrorReferenceInexistentDel_Type = Counter64
_GgsnGtpErrorReferenceInexistentDel_Object = MibScalar
ggsnGtpErrorReferenceInexistentDel = _GgsnGtpErrorReferenceInexistentDel_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 34),
    _GgsnGtpErrorReferenceInexistentDel_Type()
)
ggsnGtpErrorReferenceInexistentDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorReferenceInexistentDel.setStatus("current")
_GgsnGtpErrorPdpWithoutTft_Type = Counter64
_GgsnGtpErrorPdpWithoutTft_Object = MibScalar
ggsnGtpErrorPdpWithoutTft = _GgsnGtpErrorPdpWithoutTft_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 35),
    _GgsnGtpErrorPdpWithoutTft_Type()
)
ggsnGtpErrorPdpWithoutTft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorPdpWithoutTft.setStatus("current")
_GgsnGtpErrorApnAccessDenied_Type = Counter64
_GgsnGtpErrorApnAccessDenied_Object = MibScalar
ggsnGtpErrorApnAccessDenied = _GgsnGtpErrorApnAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 36),
    _GgsnGtpErrorApnAccessDenied_Type()
)
ggsnGtpErrorApnAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpErrorApnAccessDenied.setStatus("current")
_GgsnGtpNewPdpTypeNwPreference_Type = Counter64
_GgsnGtpNewPdpTypeNwPreference_Object = MibScalar
ggsnGtpNewPdpTypeNwPreference = _GgsnGtpNewPdpTypeNwPreference_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 37),
    _GgsnGtpNewPdpTypeNwPreference_Type()
)
ggsnGtpNewPdpTypeNwPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpNewPdpTypeNwPreference.setStatus("current")
_GgsnGtpNewPdpTypeSingleAddressBearerOnly_Type = Counter64
_GgsnGtpNewPdpTypeSingleAddressBearerOnly_Object = MibScalar
ggsnGtpNewPdpTypeSingleAddressBearerOnly = _GgsnGtpNewPdpTypeSingleAddressBearerOnly_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 7, 38),
    _GgsnGtpNewPdpTypeSingleAddressBearerOnly_Type()
)
ggsnGtpNewPdpTypeSingleAddressBearerOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpNewPdpTypeSingleAddressBearerOnly.setStatus("current")
_GgsnGtpPrStats_ObjectIdentity = ObjectIdentity
ggsnGtpPrStats = _GgsnGtpPrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8)
)
_GgsnGtpPrEchoReqReceived_Type = Counter64
_GgsnGtpPrEchoReqReceived_Object = MibScalar
ggsnGtpPrEchoReqReceived = _GgsnGtpPrEchoReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 1),
    _GgsnGtpPrEchoReqReceived_Type()
)
ggsnGtpPrEchoReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrEchoReqReceived.setStatus("current")
_GgsnGtpPrEchoRequestsSent_Type = Counter64
_GgsnGtpPrEchoRequestsSent_Object = MibScalar
ggsnGtpPrEchoRequestsSent = _GgsnGtpPrEchoRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 2),
    _GgsnGtpPrEchoRequestsSent_Type()
)
ggsnGtpPrEchoRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrEchoRequestsSent.setStatus("current")
_GgsnGtpPrEchoRespReceived_Type = Counter64
_GgsnGtpPrEchoRespReceived_Object = MibScalar
ggsnGtpPrEchoRespReceived = _GgsnGtpPrEchoRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 3),
    _GgsnGtpPrEchoRespReceived_Type()
)
ggsnGtpPrEchoRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrEchoRespReceived.setStatus("current")
_GgsnGtpPrEchoRespSent_Type = Counter64
_GgsnGtpPrEchoRespSent_Object = MibScalar
ggsnGtpPrEchoRespSent = _GgsnGtpPrEchoRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 4),
    _GgsnGtpPrEchoRespSent_Type()
)
ggsnGtpPrEchoRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrEchoRespSent.setStatus("current")
_GgsnGtpPrVerUnsupPacketsReceived_Type = Counter64
_GgsnGtpPrVerUnsupPacketsReceived_Object = MibScalar
ggsnGtpPrVerUnsupPacketsReceived = _GgsnGtpPrVerUnsupPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 5),
    _GgsnGtpPrVerUnsupPacketsReceived_Type()
)
ggsnGtpPrVerUnsupPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrVerUnsupPacketsReceived.setStatus("current")
_GgsnGtpPrVerUnsupPacketsSent_Type = Counter64
_GgsnGtpPrVerUnsupPacketsSent_Object = MibScalar
ggsnGtpPrVerUnsupPacketsSent = _GgsnGtpPrVerUnsupPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 6),
    _GgsnGtpPrVerUnsupPacketsSent_Type()
)
ggsnGtpPrVerUnsupPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrVerUnsupPacketsSent.setStatus("current")
_GgsnGtpPrNodeAliveReqReceived_Type = Counter64
_GgsnGtpPrNodeAliveReqReceived_Object = MibScalar
ggsnGtpPrNodeAliveReqReceived = _GgsnGtpPrNodeAliveReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 7),
    _GgsnGtpPrNodeAliveReqReceived_Type()
)
ggsnGtpPrNodeAliveReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrNodeAliveReqReceived.setStatus("current")
_GgsnGtpPrNodeAliveReqSent_Type = Counter64
_GgsnGtpPrNodeAliveReqSent_Object = MibScalar
ggsnGtpPrNodeAliveReqSent = _GgsnGtpPrNodeAliveReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 8),
    _GgsnGtpPrNodeAliveReqSent_Type()
)
ggsnGtpPrNodeAliveReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrNodeAliveReqSent.setStatus("current")
_GgsnGtpPrNodeAliveRespReceived_Type = Counter64
_GgsnGtpPrNodeAliveRespReceived_Object = MibScalar
ggsnGtpPrNodeAliveRespReceived = _GgsnGtpPrNodeAliveRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 9),
    _GgsnGtpPrNodeAliveRespReceived_Type()
)
ggsnGtpPrNodeAliveRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrNodeAliveRespReceived.setStatus("current")
_GgsnGtpPrNodeAliveRespSent_Type = Counter64
_GgsnGtpPrNodeAliveRespSent_Object = MibScalar
ggsnGtpPrNodeAliveRespSent = _GgsnGtpPrNodeAliveRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 10),
    _GgsnGtpPrNodeAliveRespSent_Type()
)
ggsnGtpPrNodeAliveRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrNodeAliveRespSent.setStatus("current")
_GgsnGtpPrRedirectReqReceived_Type = Counter64
_GgsnGtpPrRedirectReqReceived_Object = MibScalar
ggsnGtpPrRedirectReqReceived = _GgsnGtpPrRedirectReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 11),
    _GgsnGtpPrRedirectReqReceived_Type()
)
ggsnGtpPrRedirectReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRedirectReqReceived.setStatus("current")
_GgsnGtpPrRedirectReqSent_Type = Counter64
_GgsnGtpPrRedirectReqSent_Object = MibScalar
ggsnGtpPrRedirectReqSent = _GgsnGtpPrRedirectReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 12),
    _GgsnGtpPrRedirectReqSent_Type()
)
ggsnGtpPrRedirectReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRedirectReqSent.setStatus("current")
_GgsnGtpPrRedirectRespReceived_Type = Counter64
_GgsnGtpPrRedirectRespReceived_Object = MibScalar
ggsnGtpPrRedirectRespReceived = _GgsnGtpPrRedirectRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 13),
    _GgsnGtpPrRedirectRespReceived_Type()
)
ggsnGtpPrRedirectRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRedirectRespReceived.setStatus("current")
_GgsnGtpPrRedirectRespSent_Type = Counter64
_GgsnGtpPrRedirectRespSent_Object = MibScalar
ggsnGtpPrRedirectRespSent = _GgsnGtpPrRedirectRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 14),
    _GgsnGtpPrRedirectRespSent_Type()
)
ggsnGtpPrRedirectRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRedirectRespSent.setStatus("current")
_GgsnGtpPrDataRecTransferReceived_Type = Counter64
_GgsnGtpPrDataRecTransferReceived_Object = MibScalar
ggsnGtpPrDataRecTransferReceived = _GgsnGtpPrDataRecTransferReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 15),
    _GgsnGtpPrDataRecTransferReceived_Type()
)
ggsnGtpPrDataRecTransferReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrDataRecTransferReceived.setStatus("current")
_GgsnGtpPrDataRecTransferSent_Type = Counter64
_GgsnGtpPrDataRecTransferSent_Object = MibScalar
ggsnGtpPrDataRecTransferSent = _GgsnGtpPrDataRecTransferSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 16),
    _GgsnGtpPrDataRecTransferSent_Type()
)
ggsnGtpPrDataRecTransferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrDataRecTransferSent.setStatus("current")
_GgsnGtpPrSndDataRecordPackets_Type = Counter64
_GgsnGtpPrSndDataRecordPackets_Object = MibScalar
ggsnGtpPrSndDataRecordPackets = _GgsnGtpPrSndDataRecordPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 17),
    _GgsnGtpPrSndDataRecordPackets_Type()
)
ggsnGtpPrSndDataRecordPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrSndDataRecordPackets.setStatus("current")
_GgsnGtpPrRequestAccepted_Type = Counter64
_GgsnGtpPrRequestAccepted_Object = MibScalar
ggsnGtpPrRequestAccepted = _GgsnGtpPrRequestAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 21),
    _GgsnGtpPrRequestAccepted_Type()
)
ggsnGtpPrRequestAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRequestAccepted.setStatus("current")
_GgsnGtpPrNoResource_Type = Counter64
_GgsnGtpPrNoResource_Object = MibScalar
ggsnGtpPrNoResource = _GgsnGtpPrNoResource_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 22),
    _GgsnGtpPrNoResource_Type()
)
ggsnGtpPrNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrNoResource.setStatus("current")
_GgsnGtpPrServiceUnsupported_Type = Counter64
_GgsnGtpPrServiceUnsupported_Object = MibScalar
ggsnGtpPrServiceUnsupported = _GgsnGtpPrServiceUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 23),
    _GgsnGtpPrServiceUnsupported_Type()
)
ggsnGtpPrServiceUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrServiceUnsupported.setStatus("current")
_GgsnGtpPrSystemFailure_Type = Counter64
_GgsnGtpPrSystemFailure_Object = MibScalar
ggsnGtpPrSystemFailure = _GgsnGtpPrSystemFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 24),
    _GgsnGtpPrSystemFailure_Type()
)
ggsnGtpPrSystemFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrSystemFailure.setStatus("current")
_GgsnGtpPrInvalidMessageFormat_Type = Counter64
_GgsnGtpPrInvalidMessageFormat_Object = MibScalar
ggsnGtpPrInvalidMessageFormat = _GgsnGtpPrInvalidMessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 25),
    _GgsnGtpPrInvalidMessageFormat_Type()
)
ggsnGtpPrInvalidMessageFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrInvalidMessageFormat.setStatus("current")
_GgsnGtpPrVersionUnsupported_Type = Counter64
_GgsnGtpPrVersionUnsupported_Object = MibScalar
ggsnGtpPrVersionUnsupported = _GgsnGtpPrVersionUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 26),
    _GgsnGtpPrVersionUnsupported_Type()
)
ggsnGtpPrVersionUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrVersionUnsupported.setStatus("current")
_GgsnGtpPrRequestUnfulfilled_Type = Counter64
_GgsnGtpPrRequestUnfulfilled_Object = MibScalar
ggsnGtpPrRequestUnfulfilled = _GgsnGtpPrRequestUnfulfilled_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 27),
    _GgsnGtpPrRequestUnfulfilled_Type()
)
ggsnGtpPrRequestUnfulfilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrRequestUnfulfilled.setStatus("current")
_GgsnGtpPrDecodingError_Type = Counter64
_GgsnGtpPrDecodingError_Object = MibScalar
ggsnGtpPrDecodingError = _GgsnGtpPrDecodingError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 28),
    _GgsnGtpPrDecodingError_Type()
)
ggsnGtpPrDecodingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrDecodingError.setStatus("current")
_GgsnGtpPrAlreadyFulfilled_Type = Counter64
_GgsnGtpPrAlreadyFulfilled_Object = MibScalar
ggsnGtpPrAlreadyFulfilled = _GgsnGtpPrAlreadyFulfilled_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 29),
    _GgsnGtpPrAlreadyFulfilled_Type()
)
ggsnGtpPrAlreadyFulfilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrAlreadyFulfilled.setStatus("current")
_GgsnGtpPrDupPacketFulfilled_Type = Counter64
_GgsnGtpPrDupPacketFulfilled_Object = MibScalar
ggsnGtpPrDupPacketFulfilled = _GgsnGtpPrDupPacketFulfilled_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 8, 30),
    _GgsnGtpPrDupPacketFulfilled_Type()
)
ggsnGtpPrDupPacketFulfilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrDupPacketFulfilled.setStatus("current")
_GgsnGtpPrErrorStats_ObjectIdentity = ObjectIdentity
ggsnGtpPrErrorStats = _GgsnGtpPrErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 9)
)
_GgsnGtpPrErrorMandatoryIEMissing_Type = Counter64
_GgsnGtpPrErrorMandatoryIEMissing_Object = MibScalar
ggsnGtpPrErrorMandatoryIEMissing = _GgsnGtpPrErrorMandatoryIEMissing_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 9, 1),
    _GgsnGtpPrErrorMandatoryIEMissing_Type()
)
ggsnGtpPrErrorMandatoryIEMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrErrorMandatoryIEMissing.setStatus("current")
_GgsnGtpPrErrorMandatoryIEInvalid_Type = Counter64
_GgsnGtpPrErrorMandatoryIEInvalid_Object = MibScalar
ggsnGtpPrErrorMandatoryIEInvalid = _GgsnGtpPrErrorMandatoryIEInvalid_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 9, 2),
    _GgsnGtpPrErrorMandatoryIEInvalid_Type()
)
ggsnGtpPrErrorMandatoryIEInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrErrorMandatoryIEInvalid.setStatus("current")
_GgsnGtpPrErrorOptionalIEInvalid_Type = Counter64
_GgsnGtpPrErrorOptionalIEInvalid_Object = MibScalar
ggsnGtpPrErrorOptionalIEInvalid = _GgsnGtpPrErrorOptionalIEInvalid_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 9, 3),
    _GgsnGtpPrErrorOptionalIEInvalid_Type()
)
ggsnGtpPrErrorOptionalIEInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrErrorOptionalIEInvalid.setStatus("current")
_GgsnGtpPrErrorRefInexistent_Type = Counter64
_GgsnGtpPrErrorRefInexistent_Object = MibScalar
ggsnGtpPrErrorRefInexistent = _GgsnGtpPrErrorRefInexistent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 9, 4),
    _GgsnGtpPrErrorRefInexistent_Type()
)
ggsnGtpPrErrorRefInexistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpPrErrorRefInexistent.setStatus("current")
_GgsnUplinkTrafficInfo_ObjectIdentity = ObjectIdentity
ggsnUplinkTrafficInfo = _GgsnUplinkTrafficInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11)
)
_GgsnUplinkPackets_Type = Counter64
_GgsnUplinkPackets_Object = MibScalar
ggsnUplinkPackets = _GgsnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 1),
    _GgsnUplinkPackets_Type()
)
ggsnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkPackets.setStatus("current")
_GgsnUplinkBytes_Type = Counter64
_GgsnUplinkBytes_Object = MibScalar
ggsnUplinkBytes = _GgsnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 2),
    _GgsnUplinkBytes_Type()
)
ggsnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkBytes.setStatus("current")
_GgsnUplinkDrops_Type = Counter64
_GgsnUplinkDrops_Object = MibScalar
ggsnUplinkDrops = _GgsnUplinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 3),
    _GgsnUplinkDrops_Type()
)
ggsnUplinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkDrops.setStatus("current")
_GgsnUplinkDropsBytes_Type = Counter64
_GgsnUplinkDropsBytes_Object = MibScalar
ggsnUplinkDropsBytes = _GgsnUplinkDropsBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 4),
    _GgsnUplinkDropsBytes_Type()
)
ggsnUplinkDropsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkDropsBytes.setStatus("current")
_GgsnUplinkPacketsIpv6_Type = Counter64
_GgsnUplinkPacketsIpv6_Object = MibScalar
ggsnUplinkPacketsIpv6 = _GgsnUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 5),
    _GgsnUplinkPacketsIpv6_Type()
)
ggsnUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkPacketsIpv6.setStatus("current")
_GgsnUplinkBytesIpv6_Type = Counter64
_GgsnUplinkBytesIpv6_Object = MibScalar
ggsnUplinkBytesIpv6 = _GgsnUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 6),
    _GgsnUplinkBytesIpv6_Type()
)
ggsnUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkBytesIpv6.setStatus("current")
_GgsnUplinkDropsIpv6_Type = Counter64
_GgsnUplinkDropsIpv6_Object = MibScalar
ggsnUplinkDropsIpv6 = _GgsnUplinkDropsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 7),
    _GgsnUplinkDropsIpv6_Type()
)
ggsnUplinkDropsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkDropsIpv6.setStatus("current")
_GgsnUplinkBytesWlan_Type = Counter64
_GgsnUplinkBytesWlan_Object = MibScalar
ggsnUplinkBytesWlan = _GgsnUplinkBytesWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 8),
    _GgsnUplinkBytesWlan_Type()
)
ggsnUplinkBytesWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkBytesWlan.setStatus("obsolete")
_GgsnUplinkDropsWlan_Type = Counter64
_GgsnUplinkDropsWlan_Object = MibScalar
ggsnUplinkDropsWlan = _GgsnUplinkDropsWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 9),
    _GgsnUplinkDropsWlan_Type()
)
ggsnUplinkDropsWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkDropsWlan.setStatus("obsolete")
_GgsnUplinkPacketsWlan_Type = Counter64
_GgsnUplinkPacketsWlan_Object = MibScalar
ggsnUplinkPacketsWlan = _GgsnUplinkPacketsWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 11, 10),
    _GgsnUplinkPacketsWlan_Type()
)
ggsnUplinkPacketsWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnUplinkPacketsWlan.setStatus("obsolete")
_GgsnDownlinkTrafficInfo_ObjectIdentity = ObjectIdentity
ggsnDownlinkTrafficInfo = _GgsnDownlinkTrafficInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12)
)
_GgsnDownlinkPackets_Type = Counter64
_GgsnDownlinkPackets_Object = MibScalar
ggsnDownlinkPackets = _GgsnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 1),
    _GgsnDownlinkPackets_Type()
)
ggsnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkPackets.setStatus("current")
_GgsnDownlinkBytes_Type = Counter64
_GgsnDownlinkBytes_Object = MibScalar
ggsnDownlinkBytes = _GgsnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 2),
    _GgsnDownlinkBytes_Type()
)
ggsnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkBytes.setStatus("current")
_GgsnDownlinkDrops_Type = Counter64
_GgsnDownlinkDrops_Object = MibScalar
ggsnDownlinkDrops = _GgsnDownlinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 3),
    _GgsnDownlinkDrops_Type()
)
ggsnDownlinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkDrops.setStatus("current")
_GgsnDownlinkDropsBytes_Type = Counter64
_GgsnDownlinkDropsBytes_Object = MibScalar
ggsnDownlinkDropsBytes = _GgsnDownlinkDropsBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 4),
    _GgsnDownlinkDropsBytes_Type()
)
ggsnDownlinkDropsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkDropsBytes.setStatus("current")
_GgsnDownlinkPacketsIpv6_Type = Counter64
_GgsnDownlinkPacketsIpv6_Object = MibScalar
ggsnDownlinkPacketsIpv6 = _GgsnDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 5),
    _GgsnDownlinkPacketsIpv6_Type()
)
ggsnDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkPacketsIpv6.setStatus("current")
_GgsnDownlinkBytesIpv6_Type = Counter64
_GgsnDownlinkBytesIpv6_Object = MibScalar
ggsnDownlinkBytesIpv6 = _GgsnDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 6),
    _GgsnDownlinkBytesIpv6_Type()
)
ggsnDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkBytesIpv6.setStatus("current")
_GgsnDownlinkDropsIpv6_Type = Counter64
_GgsnDownlinkDropsIpv6_Object = MibScalar
ggsnDownlinkDropsIpv6 = _GgsnDownlinkDropsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 7),
    _GgsnDownlinkDropsIpv6_Type()
)
ggsnDownlinkDropsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkDropsIpv6.setStatus("current")
_GgsnDownlinkBytesWlan_Type = Counter64
_GgsnDownlinkBytesWlan_Object = MibScalar
ggsnDownlinkBytesWlan = _GgsnDownlinkBytesWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 8),
    _GgsnDownlinkBytesWlan_Type()
)
ggsnDownlinkBytesWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkBytesWlan.setStatus("obsolete")
_GgsnDownlinkDropsWlan_Type = Counter64
_GgsnDownlinkDropsWlan_Object = MibScalar
ggsnDownlinkDropsWlan = _GgsnDownlinkDropsWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 9),
    _GgsnDownlinkDropsWlan_Type()
)
ggsnDownlinkDropsWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkDropsWlan.setStatus("obsolete")
_GgsnDownlinkPacketsWlan_Type = Counter64
_GgsnDownlinkPacketsWlan_Object = MibScalar
ggsnDownlinkPacketsWlan = _GgsnDownlinkPacketsWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 12, 10),
    _GgsnDownlinkPacketsWlan_Type()
)
ggsnDownlinkPacketsWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDownlinkPacketsWlan.setStatus("obsolete")
_PdnConnectionsGgsn_ObjectIdentity = ObjectIdentity
pdnConnectionsGgsn = _PdnConnectionsGgsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 13)
)
_NbrOfGgsnPdnConnections_Type = Counter32
_NbrOfGgsnPdnConnections_Object = MibScalar
nbrOfGgsnPdnConnections = _NbrOfGgsnPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 13, 1),
    _NbrOfGgsnPdnConnections_Type()
)
nbrOfGgsnPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfGgsnPdnConnections.setStatus("current")
_GgsnNbrOfSubscribers_Type = Gauge32
_GgsnNbrOfSubscribers_Object = MibScalar
ggsnNbrOfSubscribers = _GgsnNbrOfSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 20),
    _GgsnNbrOfSubscribers_Type()
)
ggsnNbrOfSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfSubscribers.setStatus("current")
_GgsnNbrOfSubscribersMean_Type = Gauge32
_GgsnNbrOfSubscribersMean_Object = MibScalar
ggsnNbrOfSubscribersMean = _GgsnNbrOfSubscribersMean_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 21),
    _GgsnNbrOfSubscribersMean_Type()
)
ggsnNbrOfSubscribersMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfSubscribersMean.setStatus("current")
_GgsnNbrOfTftFilters_Type = Gauge32
_GgsnNbrOfTftFilters_Object = MibScalar
ggsnNbrOfTftFilters = _GgsnNbrOfTftFilters_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 22),
    _GgsnNbrOfTftFilters_Type()
)
ggsnNbrOfTftFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfTftFilters.setStatus("current")
_GgsnControlLoad_Type = Gauge32
_GgsnControlLoad_Object = MibScalar
ggsnControlLoad = _GgsnControlLoad_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 25),
    _GgsnControlLoad_Type()
)
ggsnControlLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnControlLoad.setStatus("current")
_GgsnPayloadLoad_Type = Gauge32
_GgsnPayloadLoad_Object = MibScalar
ggsnPayloadLoad = _GgsnPayloadLoad_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 26),
    _GgsnPayloadLoad_Type()
)
ggsnPayloadLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnPayloadLoad.setStatus("current")
_GgsnNbrOfActivePdpContextsIpv6_Type = Gauge32
_GgsnNbrOfActivePdpContextsIpv6_Object = MibScalar
ggsnNbrOfActivePdpContextsIpv6 = _GgsnNbrOfActivePdpContextsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 27),
    _GgsnNbrOfActivePdpContextsIpv6_Type()
)
ggsnNbrOfActivePdpContextsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfActivePdpContextsIpv6.setStatus("current")
_GgsnNeighborSolicitationRcv_Type = Counter64
_GgsnNeighborSolicitationRcv_Object = MibScalar
ggsnNeighborSolicitationRcv = _GgsnNeighborSolicitationRcv_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 28),
    _GgsnNeighborSolicitationRcv_Type()
)
ggsnNeighborSolicitationRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNeighborSolicitationRcv.setStatus("current")
_GgsnNeighborSolicitationRsp_Type = Counter64
_GgsnNeighborSolicitationRsp_Object = MibScalar
ggsnNeighborSolicitationRsp = _GgsnNeighborSolicitationRsp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 29),
    _GgsnNeighborSolicitationRsp_Type()
)
ggsnNeighborSolicitationRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNeighborSolicitationRsp.setStatus("current")
_GgsnRouterSolicitationRcv_Type = Counter64
_GgsnRouterSolicitationRcv_Object = MibScalar
ggsnRouterSolicitationRcv = _GgsnRouterSolicitationRcv_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 30),
    _GgsnRouterSolicitationRcv_Type()
)
ggsnRouterSolicitationRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnRouterSolicitationRcv.setStatus("current")
_GgsnRouterSolicitationRsp_Type = Counter64
_GgsnRouterSolicitationRsp_Object = MibScalar
ggsnRouterSolicitationRsp = _GgsnRouterSolicitationRsp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 31),
    _GgsnRouterSolicitationRsp_Type()
)
ggsnRouterSolicitationRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnRouterSolicitationRsp.setStatus("current")
_GgsnL2tpActiveTunnels_Type = Gauge32
_GgsnL2tpActiveTunnels_Object = MibScalar
ggsnL2tpActiveTunnels = _GgsnL2tpActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 32),
    _GgsnL2tpActiveTunnels_Type()
)
ggsnL2tpActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpActiveTunnels.setStatus("current")
_GgsnL2tpMaxActiveTunnels_Type = Gauge32
_GgsnL2tpMaxActiveTunnels_Object = MibScalar
ggsnL2tpMaxActiveTunnels = _GgsnL2tpMaxActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 33),
    _GgsnL2tpMaxActiveTunnels_Type()
)
ggsnL2tpMaxActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpMaxActiveTunnels.setStatus("current")
_GgsnL2tpActiveSessions_Type = Gauge32
_GgsnL2tpActiveSessions_Object = MibScalar
ggsnL2tpActiveSessions = _GgsnL2tpActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 34),
    _GgsnL2tpActiveSessions_Type()
)
ggsnL2tpActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpActiveSessions.setStatus("current")
_GgsnL2tpMaxActiveSessions_Type = Gauge32
_GgsnL2tpMaxActiveSessions_Object = MibScalar
ggsnL2tpMaxActiveSessions = _GgsnL2tpMaxActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 35),
    _GgsnL2tpMaxActiveSessions_Type()
)
ggsnL2tpMaxActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpMaxActiveSessions.setStatus("current")
_GgsnChgEncodedCdrs_Type = Counter64
_GgsnChgEncodedCdrs_Object = MibScalar
ggsnChgEncodedCdrs = _GgsnChgEncodedCdrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 36),
    _GgsnChgEncodedCdrs_Type()
)
ggsnChgEncodedCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgEncodedCdrs.setStatus("current")
_GgsnChgFailedEncodedCdrs_Type = Counter64
_GgsnChgFailedEncodedCdrs_Object = MibScalar
ggsnChgFailedEncodedCdrs = _GgsnChgFailedEncodedCdrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 37),
    _GgsnChgFailedEncodedCdrs_Type()
)
ggsnChgFailedEncodedCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgFailedEncodedCdrs.setStatus("current")
_GgsnChgGeneratedFtpCdrs_Type = Counter64
_GgsnChgGeneratedFtpCdrs_Object = MibScalar
ggsnChgGeneratedFtpCdrs = _GgsnChgGeneratedFtpCdrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 38),
    _GgsnChgGeneratedFtpCdrs_Type()
)
ggsnChgGeneratedFtpCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgGeneratedFtpCdrs.setStatus("current")
_GgsnChgGeneratedGtppCdrs_Type = Counter64
_GgsnChgGeneratedGtppCdrs_Object = MibScalar
ggsnChgGeneratedGtppCdrs = _GgsnChgGeneratedGtppCdrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 39),
    _GgsnChgGeneratedGtppCdrs_Type()
)
ggsnChgGeneratedGtppCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgGeneratedGtppCdrs.setStatus("current")
_GgsnChgGtppLogCdrs_Type = Counter64
_GgsnChgGtppLogCdrs_Object = MibScalar
ggsnChgGtppLogCdrs = _GgsnChgGtppLogCdrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 40),
    _GgsnChgGtppLogCdrs_Type()
)
ggsnChgGtppLogCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgGtppLogCdrs.setStatus("current")
_GgsnChgGtppAttemptedCdrsSend_Type = Counter64
_GgsnChgGtppAttemptedCdrsSend_Object = MibScalar
ggsnChgGtppAttemptedCdrsSend = _GgsnChgGtppAttemptedCdrsSend_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 41),
    _GgsnChgGtppAttemptedCdrsSend_Type()
)
ggsnChgGtppAttemptedCdrsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgGtppAttemptedCdrsSend.setStatus("current")
_GgsnChgGtppCdrsSendFailure_Type = Counter64
_GgsnChgGtppCdrsSendFailure_Object = MibScalar
ggsnChgGtppCdrsSendFailure = _GgsnChgGtppCdrsSendFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 42),
    _GgsnChgGtppCdrsSendFailure_Type()
)
ggsnChgGtppCdrsSendFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnChgGtppCdrsSendFailure.setStatus("current")
_GgsnNbActivePdpPerTrafficClassConversational_Type = Gauge32
_GgsnNbActivePdpPerTrafficClassConversational_Object = MibScalar
ggsnNbActivePdpPerTrafficClassConversational = _GgsnNbActivePdpPerTrafficClassConversational_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 43),
    _GgsnNbActivePdpPerTrafficClassConversational_Type()
)
ggsnNbActivePdpPerTrafficClassConversational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbActivePdpPerTrafficClassConversational.setStatus("current")
_GgsnNbActivePdpPerTrafficClassStreaming_Type = Gauge32
_GgsnNbActivePdpPerTrafficClassStreaming_Object = MibScalar
ggsnNbActivePdpPerTrafficClassStreaming = _GgsnNbActivePdpPerTrafficClassStreaming_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 44),
    _GgsnNbActivePdpPerTrafficClassStreaming_Type()
)
ggsnNbActivePdpPerTrafficClassStreaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbActivePdpPerTrafficClassStreaming.setStatus("current")
_GgsnNbActivePdpPerTrafficClassInteractive_Type = Gauge32
_GgsnNbActivePdpPerTrafficClassInteractive_Object = MibScalar
ggsnNbActivePdpPerTrafficClassInteractive = _GgsnNbActivePdpPerTrafficClassInteractive_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 45),
    _GgsnNbActivePdpPerTrafficClassInteractive_Type()
)
ggsnNbActivePdpPerTrafficClassInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbActivePdpPerTrafficClassInteractive.setStatus("current")
_GgsnNbActivePdpPerTrafficClassBackground_Type = Gauge32
_GgsnNbActivePdpPerTrafficClassBackground_Object = MibScalar
ggsnNbActivePdpPerTrafficClassBackground = _GgsnNbActivePdpPerTrafficClassBackground_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 46),
    _GgsnNbActivePdpPerTrafficClassBackground_Type()
)
ggsnNbActivePdpPerTrafficClassBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbActivePdpPerTrafficClassBackground.setStatus("current")
_GgsnRadiusAuthenticationFailure_Type = Counter64
_GgsnRadiusAuthenticationFailure_Object = MibScalar
ggsnRadiusAuthenticationFailure = _GgsnRadiusAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 47),
    _GgsnRadiusAuthenticationFailure_Type()
)
ggsnRadiusAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnRadiusAuthenticationFailure.setStatus("current")
_GgsnRadiusAccountingFailure_Type = Counter64
_GgsnRadiusAccountingFailure_Object = MibScalar
ggsnRadiusAccountingFailure = _GgsnRadiusAccountingFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 48),
    _GgsnRadiusAccountingFailure_Type()
)
ggsnRadiusAccountingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnRadiusAccountingFailure.setStatus("current")
_GgsnNbrOfActivePdpContextsWlan_Type = Gauge32
_GgsnNbrOfActivePdpContextsWlan_Object = MibScalar
ggsnNbrOfActivePdpContextsWlan = _GgsnNbrOfActivePdpContextsWlan_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 49),
    _GgsnNbrOfActivePdpContextsWlan_Type()
)
ggsnNbrOfActivePdpContextsWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfActivePdpContextsWlan.setStatus("current")
_Ggsn3gdtActiveContexts_Type = Gauge32
_Ggsn3gdtActiveContexts_Object = MibScalar
ggsn3gdtActiveContexts = _Ggsn3gdtActiveContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 50),
    _Ggsn3gdtActiveContexts_Type()
)
ggsn3gdtActiveContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsn3gdtActiveContexts.setStatus("current")
_Ggsn3gdtTotalCompletedEstablishment_Type = Gauge32
_Ggsn3gdtTotalCompletedEstablishment_Object = MibScalar
ggsn3gdtTotalCompletedEstablishment = _Ggsn3gdtTotalCompletedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 51),
    _Ggsn3gdtTotalCompletedEstablishment_Type()
)
ggsn3gdtTotalCompletedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsn3gdtTotalCompletedEstablishment.setStatus("deprecated")
_Ggsn3gdtTotalAttemptedEstablishment_Type = Gauge32
_Ggsn3gdtTotalAttemptedEstablishment_Object = MibScalar
ggsn3gdtTotalAttemptedEstablishment = _Ggsn3gdtTotalAttemptedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 52),
    _Ggsn3gdtTotalAttemptedEstablishment_Type()
)
ggsn3gdtTotalAttemptedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsn3gdtTotalAttemptedEstablishment.setStatus("deprecated")
_Ggsn3gdtErrorHandling_Type = Gauge32
_Ggsn3gdtErrorHandling_Object = MibScalar
ggsn3gdtErrorHandling = _Ggsn3gdtErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 53),
    _Ggsn3gdtErrorHandling_Type()
)
ggsn3gdtErrorHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsn3gdtErrorHandling.setStatus("deprecated")
_Gn3gdtTotalCompletedEstablishment_Type = Counter32
_Gn3gdtTotalCompletedEstablishment_Object = MibScalar
gn3gdtTotalCompletedEstablishment = _Gn3gdtTotalCompletedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 54),
    _Gn3gdtTotalCompletedEstablishment_Type()
)
gn3gdtTotalCompletedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gn3gdtTotalCompletedEstablishment.setStatus("current")
_Gn3gdtTotalAttemptedEstablishment_Type = Counter32
_Gn3gdtTotalAttemptedEstablishment_Object = MibScalar
gn3gdtTotalAttemptedEstablishment = _Gn3gdtTotalAttemptedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 55),
    _Gn3gdtTotalAttemptedEstablishment_Type()
)
gn3gdtTotalAttemptedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gn3gdtTotalAttemptedEstablishment.setStatus("current")
_Gn3gdtErrorHandling_Type = Counter32
_Gn3gdtErrorHandling_Object = MibScalar
gn3gdtErrorHandling = _Gn3gdtErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 56),
    _Gn3gdtErrorHandling_Type()
)
gn3gdtErrorHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gn3gdtErrorHandling.setStatus("current")
_GgsnNbrOfActivePdpContextsIpv4v6_Type = Gauge32
_GgsnNbrOfActivePdpContextsIpv4v6_Object = MibScalar
ggsnNbrOfActivePdpContextsIpv4v6 = _GgsnNbrOfActivePdpContextsIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 3, 57),
    _GgsnNbrOfActivePdpContextsIpv4v6_Type()
)
ggsnNbrOfActivePdpContextsIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbrOfActivePdpContextsIpv4v6.setStatus("current")
_GgsnPicStatsTable_Object = MibTable
ggsnPicStatsTable = _GgsnPicStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ggsnPicStatsTable.setStatus("deprecated")
_GgsnPicStatsEntry_Object = MibTableRow
ggsnPicStatsEntry = _GgsnPicStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 4, 1)
)
ggsnPicStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnPicIndex"),
)
if mibBuilder.loadTexts:
    ggsnPicStatsEntry.setStatus("deprecated")


class _GgsnPicIndex_Type(Integer32):
    """Custom type ggsnPicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnPicIndex_Type.__name__ = "Integer32"
_GgsnPicIndex_Object = MibTableColumn
ggsnPicIndex = _GgsnPicIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 4, 1, 1),
    _GgsnPicIndex_Type()
)
ggsnPicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnPicIndex.setStatus("deprecated")
_GgsnPicAddress_Type = IpAddress
_GgsnPicAddress_Object = MibTableColumn
ggsnPicAddress = _GgsnPicAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 4, 1, 2),
    _GgsnPicAddress_Type()
)
ggsnPicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnPicAddress.setStatus("deprecated")
_GgsnPicNbrOfActivePdpContexts_Type = Gauge32
_GgsnPicNbrOfActivePdpContexts_Object = MibTableColumn
ggsnPicNbrOfActivePdpContexts = _GgsnPicNbrOfActivePdpContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 4, 1, 3),
    _GgsnPicNbrOfActivePdpContexts_Type()
)
ggsnPicNbrOfActivePdpContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnPicNbrOfActivePdpContexts.setStatus("deprecated")
_GgsnApnStatsTable_Object = MibTable
ggsnApnStatsTable = _GgsnApnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ggsnApnStatsTable.setStatus("current")
_GgsnApnStatsEntry_Object = MibTableRow
ggsnApnStatsEntry = _GgsnApnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1)
)
ggsnApnStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnStatsEntry.setStatus("current")


class _GgsnApnIndex_Type(Integer32):
    """Custom type ggsnApnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnApnIndex_Type.__name__ = "Integer32"
_GgsnApnIndex_Object = MibTableColumn
ggsnApnIndex = _GgsnApnIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 1),
    _GgsnApnIndex_Type()
)
ggsnApnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnApnIndex.setStatus("current")
_GgsnApnName_Type = DisplayString
_GgsnApnName_Object = MibTableColumn
ggsnApnName = _GgsnApnName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 2),
    _GgsnApnName_Type()
)
ggsnApnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnName.setStatus("current")
_GgsnApnActivePdpContextCount_Type = Gauge32
_GgsnApnActivePdpContextCount_Object = MibTableColumn
ggsnApnActivePdpContextCount = _GgsnApnActivePdpContextCount_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 3),
    _GgsnApnActivePdpContextCount_Type()
)
ggsnApnActivePdpContextCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextCount.setStatus("current")
_GgsnApnAttemptedActivation_Type = Counter64
_GgsnApnAttemptedActivation_Object = MibTableColumn
ggsnApnAttemptedActivation = _GgsnApnAttemptedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 4),
    _GgsnApnAttemptedActivation_Type()
)
ggsnApnAttemptedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedActivation.setStatus("current")
_GgsnApnAttemptedDynActivation_Type = Counter64
_GgsnApnAttemptedDynActivation_Object = MibTableColumn
ggsnApnAttemptedDynActivation = _GgsnApnAttemptedDynActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 5),
    _GgsnApnAttemptedDynActivation_Type()
)
ggsnApnAttemptedDynActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedDynActivation.setStatus("current")
_GgsnApnAttemptedDeactivation_Type = Counter64
_GgsnApnAttemptedDeactivation_Object = MibTableColumn
ggsnApnAttemptedDeactivation = _GgsnApnAttemptedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 6),
    _GgsnApnAttemptedDeactivation_Type()
)
ggsnApnAttemptedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedDeactivation.setStatus("current")
_GgsnApnAttemptedSelfDeactivation_Type = Counter64
_GgsnApnAttemptedSelfDeactivation_Object = MibTableColumn
ggsnApnAttemptedSelfDeactivation = _GgsnApnAttemptedSelfDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 7),
    _GgsnApnAttemptedSelfDeactivation_Type()
)
ggsnApnAttemptedSelfDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedSelfDeactivation.setStatus("current")
_GgsnApnCompletedActivation_Type = Counter64
_GgsnApnCompletedActivation_Object = MibTableColumn
ggsnApnCompletedActivation = _GgsnApnCompletedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 8),
    _GgsnApnCompletedActivation_Type()
)
ggsnApnCompletedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedActivation.setStatus("current")
_GgsnApnCompletedDynActivation_Type = Counter64
_GgsnApnCompletedDynActivation_Object = MibTableColumn
ggsnApnCompletedDynActivation = _GgsnApnCompletedDynActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 9),
    _GgsnApnCompletedDynActivation_Type()
)
ggsnApnCompletedDynActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedDynActivation.setStatus("current")
_GgsnApnCompletedDeactivation_Type = Counter64
_GgsnApnCompletedDeactivation_Object = MibTableColumn
ggsnApnCompletedDeactivation = _GgsnApnCompletedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 10),
    _GgsnApnCompletedDeactivation_Type()
)
ggsnApnCompletedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedDeactivation.setStatus("current")
_GgsnApnCompletedSelfDeactivation_Type = Counter64
_GgsnApnCompletedSelfDeactivation_Object = MibTableColumn
ggsnApnCompletedSelfDeactivation = _GgsnApnCompletedSelfDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 11),
    _GgsnApnCompletedSelfDeactivation_Type()
)
ggsnApnCompletedSelfDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedSelfDeactivation.setStatus("current")
_GgsnApnUplinkPackets_Type = Counter64
_GgsnApnUplinkPackets_Object = MibTableColumn
ggsnApnUplinkPackets = _GgsnApnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 12),
    _GgsnApnUplinkPackets_Type()
)
ggsnApnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkPackets.setStatus("current")
_GgsnApnUplinkBytes_Type = Counter64
_GgsnApnUplinkBytes_Object = MibTableColumn
ggsnApnUplinkBytes = _GgsnApnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 13),
    _GgsnApnUplinkBytes_Type()
)
ggsnApnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkBytes.setStatus("current")
_GgsnApnUplinkDrops_Type = Counter64
_GgsnApnUplinkDrops_Object = MibTableColumn
ggsnApnUplinkDrops = _GgsnApnUplinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 14),
    _GgsnApnUplinkDrops_Type()
)
ggsnApnUplinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkDrops.setStatus("current")
_GgsnApnDownlinkPackets_Type = Counter64
_GgsnApnDownlinkPackets_Object = MibTableColumn
ggsnApnDownlinkPackets = _GgsnApnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 15),
    _GgsnApnDownlinkPackets_Type()
)
ggsnApnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkPackets.setStatus("current")
_GgsnApnDownlinkBytes_Type = Counter64
_GgsnApnDownlinkBytes_Object = MibTableColumn
ggsnApnDownlinkBytes = _GgsnApnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 16),
    _GgsnApnDownlinkBytes_Type()
)
ggsnApnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkBytes.setStatus("current")
_GgsnApnDownlinkDrops_Type = Counter64
_GgsnApnDownlinkDrops_Object = MibTableColumn
ggsnApnDownlinkDrops = _GgsnApnDownlinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 17),
    _GgsnApnDownlinkDrops_Type()
)
ggsnApnDownlinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkDrops.setStatus("current")
_GgsnApnAttemptedMSActivation_Type = Counter64
_GgsnApnAttemptedMSActivation_Object = MibTableColumn
ggsnApnAttemptedMSActivation = _GgsnApnAttemptedMSActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 18),
    _GgsnApnAttemptedMSActivation_Type()
)
ggsnApnAttemptedMSActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedMSActivation.setStatus("deprecated")
_GgsnApnCompletedMSActivation_Type = Counter64
_GgsnApnCompletedMSActivation_Object = MibTableColumn
ggsnApnCompletedMSActivation = _GgsnApnCompletedMSActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 19),
    _GgsnApnCompletedMSActivation_Type()
)
ggsnApnCompletedMSActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedMSActivation.setStatus("deprecated")
_GgsnApnAttemptedMSDeactivation_Type = Counter64
_GgsnApnAttemptedMSDeactivation_Object = MibTableColumn
ggsnApnAttemptedMSDeactivation = _GgsnApnAttemptedMSDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 20),
    _GgsnApnAttemptedMSDeactivation_Type()
)
ggsnApnAttemptedMSDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedMSDeactivation.setStatus("current")
_GgsnApnCompletedMSDeactivation_Type = Counter64
_GgsnApnCompletedMSDeactivation_Object = MibTableColumn
ggsnApnCompletedMSDeactivation = _GgsnApnCompletedMSDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 21),
    _GgsnApnCompletedMSDeactivation_Type()
)
ggsnApnCompletedMSDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedMSDeactivation.setStatus("current")
_GgsnApnActivePdpContextMax_Type = Gauge32
_GgsnApnActivePdpContextMax_Object = MibTableColumn
ggsnApnActivePdpContextMax = _GgsnApnActivePdpContextMax_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 22),
    _GgsnApnActivePdpContextMax_Type()
)
ggsnApnActivePdpContextMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextMax.setStatus("current")
_GgsnApnActivePdpContextMean_Type = Gauge32
_GgsnApnActivePdpContextMean_Object = MibTableColumn
ggsnApnActivePdpContextMean = _GgsnApnActivePdpContextMean_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 23),
    _GgsnApnActivePdpContextMean_Type()
)
ggsnApnActivePdpContextMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextMean.setStatus("current")
_GgsnApnAttemptedAuthActivation_Type = Counter64
_GgsnApnAttemptedAuthActivation_Object = MibTableColumn
ggsnApnAttemptedAuthActivation = _GgsnApnAttemptedAuthActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 24),
    _GgsnApnAttemptedAuthActivation_Type()
)
ggsnApnAttemptedAuthActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedAuthActivation.setStatus("current")
_GgsnApnFailedAuthActivation_Type = Counter64
_GgsnApnFailedAuthActivation_Object = MibTableColumn
ggsnApnFailedAuthActivation = _GgsnApnFailedAuthActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 25),
    _GgsnApnFailedAuthActivation_Type()
)
ggsnApnFailedAuthActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFailedAuthActivation.setStatus("current")
_GgsnApnAttemptedUpdateMsAndSgsn_Type = Counter64
_GgsnApnAttemptedUpdateMsAndSgsn_Object = MibTableColumn
ggsnApnAttemptedUpdateMsAndSgsn = _GgsnApnAttemptedUpdateMsAndSgsn_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 26),
    _GgsnApnAttemptedUpdateMsAndSgsn_Type()
)
ggsnApnAttemptedUpdateMsAndSgsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedUpdateMsAndSgsn.setStatus("current")
_GgsnApnCompletedUpdateMsAndSgsn_Type = Counter64
_GgsnApnCompletedUpdateMsAndSgsn_Object = MibTableColumn
ggsnApnCompletedUpdateMsAndSgsn = _GgsnApnCompletedUpdateMsAndSgsn_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 27),
    _GgsnApnCompletedUpdateMsAndSgsn_Type()
)
ggsnApnCompletedUpdateMsAndSgsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedUpdateMsAndSgsn.setStatus("current")
_GgsnApnNbrOfTftFilters_Type = Gauge32
_GgsnApnNbrOfTftFilters_Object = MibTableColumn
ggsnApnNbrOfTftFilters = _GgsnApnNbrOfTftFilters_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 28),
    _GgsnApnNbrOfTftFilters_Type()
)
ggsnApnNbrOfTftFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnNbrOfTftFilters.setStatus("current")
_GgsnApnSessTimeoutDeactivation_Type = Counter64
_GgsnApnSessTimeoutDeactivation_Object = MibTableColumn
ggsnApnSessTimeoutDeactivation = _GgsnApnSessTimeoutDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 29),
    _GgsnApnSessTimeoutDeactivation_Type()
)
ggsnApnSessTimeoutDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSessTimeoutDeactivation.setStatus("current")
_GgsnApnIdleTimeoutDeactivation_Type = Counter64
_GgsnApnIdleTimeoutDeactivation_Object = MibTableColumn
ggsnApnIdleTimeoutDeactivation = _GgsnApnIdleTimeoutDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 30),
    _GgsnApnIdleTimeoutDeactivation_Type()
)
ggsnApnIdleTimeoutDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnIdleTimeoutDeactivation.setStatus("current")
_GgsnApnGiSignalingInPackets_Type = Counter64
_GgsnApnGiSignalingInPackets_Object = MibTableColumn
ggsnApnGiSignalingInPackets = _GgsnApnGiSignalingInPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 31),
    _GgsnApnGiSignalingInPackets_Type()
)
ggsnApnGiSignalingInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnGiSignalingInPackets.setStatus("current")
_GgsnApnGiSignalingInBytes_Type = Counter64
_GgsnApnGiSignalingInBytes_Object = MibTableColumn
ggsnApnGiSignalingInBytes = _GgsnApnGiSignalingInBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 32),
    _GgsnApnGiSignalingInBytes_Type()
)
ggsnApnGiSignalingInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnGiSignalingInBytes.setStatus("current")
_GgsnApnGiSignalingOutPackets_Type = Counter64
_GgsnApnGiSignalingOutPackets_Object = MibTableColumn
ggsnApnGiSignalingOutPackets = _GgsnApnGiSignalingOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 33),
    _GgsnApnGiSignalingOutPackets_Type()
)
ggsnApnGiSignalingOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnGiSignalingOutPackets.setStatus("current")
_GgsnApnGiSignalingOutBytes_Type = Counter64
_GgsnApnGiSignalingOutBytes_Object = MibTableColumn
ggsnApnGiSignalingOutBytes = _GgsnApnGiSignalingOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 34),
    _GgsnApnGiSignalingOutBytes_Type()
)
ggsnApnGiSignalingOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnGiSignalingOutBytes.setStatus("current")
_GgsnApnActivePdpContextCountIpv6_Type = Gauge32
_GgsnApnActivePdpContextCountIpv6_Object = MibTableColumn
ggsnApnActivePdpContextCountIpv6 = _GgsnApnActivePdpContextCountIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 35),
    _GgsnApnActivePdpContextCountIpv6_Type()
)
ggsnApnActivePdpContextCountIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextCountIpv6.setStatus("current")
_GgsnApnAttemptedActivationIpv6_Type = Counter64
_GgsnApnAttemptedActivationIpv6_Object = MibTableColumn
ggsnApnAttemptedActivationIpv6 = _GgsnApnAttemptedActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 36),
    _GgsnApnAttemptedActivationIpv6_Type()
)
ggsnApnAttemptedActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedActivationIpv6.setStatus("current")
_GgsnApnCompletedActivationIpv6_Type = Counter64
_GgsnApnCompletedActivationIpv6_Object = MibTableColumn
ggsnApnCompletedActivationIpv6 = _GgsnApnCompletedActivationIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 37),
    _GgsnApnCompletedActivationIpv6_Type()
)
ggsnApnCompletedActivationIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedActivationIpv6.setStatus("current")
_GgsnApnUplinkPacketsIpv6_Type = Counter64
_GgsnApnUplinkPacketsIpv6_Object = MibTableColumn
ggsnApnUplinkPacketsIpv6 = _GgsnApnUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 38),
    _GgsnApnUplinkPacketsIpv6_Type()
)
ggsnApnUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkPacketsIpv6.setStatus("current")
_GgsnApnUplinkBytesIpv6_Type = Counter64
_GgsnApnUplinkBytesIpv6_Object = MibTableColumn
ggsnApnUplinkBytesIpv6 = _GgsnApnUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 39),
    _GgsnApnUplinkBytesIpv6_Type()
)
ggsnApnUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkBytesIpv6.setStatus("current")
_GgsnApnUplinkDropsIpv6_Type = Counter64
_GgsnApnUplinkDropsIpv6_Object = MibTableColumn
ggsnApnUplinkDropsIpv6 = _GgsnApnUplinkDropsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 40),
    _GgsnApnUplinkDropsIpv6_Type()
)
ggsnApnUplinkDropsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUplinkDropsIpv6.setStatus("current")
_GgsnApnDownlinkPacketsIpv6_Type = Counter64
_GgsnApnDownlinkPacketsIpv6_Object = MibTableColumn
ggsnApnDownlinkPacketsIpv6 = _GgsnApnDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 41),
    _GgsnApnDownlinkPacketsIpv6_Type()
)
ggsnApnDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkPacketsIpv6.setStatus("current")
_GgsnApnDownlinkBytesIpv6_Type = Counter64
_GgsnApnDownlinkBytesIpv6_Object = MibTableColumn
ggsnApnDownlinkBytesIpv6 = _GgsnApnDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 42),
    _GgsnApnDownlinkBytesIpv6_Type()
)
ggsnApnDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkBytesIpv6.setStatus("current")
_GgsnApnDownlinkDropsIpv6_Type = Counter64
_GgsnApnDownlinkDropsIpv6_Object = MibTableColumn
ggsnApnDownlinkDropsIpv6 = _GgsnApnDownlinkDropsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 43),
    _GgsnApnDownlinkDropsIpv6_Type()
)
ggsnApnDownlinkDropsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnDownlinkDropsIpv6.setStatus("current")
_GgsnApnNeighborSolicitationRcv_Type = Counter64
_GgsnApnNeighborSolicitationRcv_Object = MibTableColumn
ggsnApnNeighborSolicitationRcv = _GgsnApnNeighborSolicitationRcv_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 44),
    _GgsnApnNeighborSolicitationRcv_Type()
)
ggsnApnNeighborSolicitationRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnNeighborSolicitationRcv.setStatus("current")
_GgsnApnNeighborSolicitationRsp_Type = Counter64
_GgsnApnNeighborSolicitationRsp_Object = MibTableColumn
ggsnApnNeighborSolicitationRsp = _GgsnApnNeighborSolicitationRsp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 45),
    _GgsnApnNeighborSolicitationRsp_Type()
)
ggsnApnNeighborSolicitationRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnNeighborSolicitationRsp.setStatus("current")
_GgsnApnRouterSolicitationRcv_Type = Counter64
_GgsnApnRouterSolicitationRcv_Object = MibTableColumn
ggsnApnRouterSolicitationRcv = _GgsnApnRouterSolicitationRcv_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 46),
    _GgsnApnRouterSolicitationRcv_Type()
)
ggsnApnRouterSolicitationRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRouterSolicitationRcv.setStatus("current")
_GgsnApnRouterSolicitationRsp_Type = Counter64
_GgsnApnRouterSolicitationRsp_Object = MibTableColumn
ggsnApnRouterSolicitationRsp = _GgsnApnRouterSolicitationRsp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 47),
    _GgsnApnRouterSolicitationRsp_Type()
)
ggsnApnRouterSolicitationRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRouterSolicitationRsp.setStatus("current")
_GgsnNbApnActivePdpPerTrafficClassConversational_Type = Gauge32
_GgsnNbApnActivePdpPerTrafficClassConversational_Object = MibTableColumn
ggsnNbApnActivePdpPerTrafficClassConversational = _GgsnNbApnActivePdpPerTrafficClassConversational_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 48),
    _GgsnNbApnActivePdpPerTrafficClassConversational_Type()
)
ggsnNbApnActivePdpPerTrafficClassConversational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbApnActivePdpPerTrafficClassConversational.setStatus("current")
_GgsnNbApnActivePdpPerTrafficClassStreaming_Type = Gauge32
_GgsnNbApnActivePdpPerTrafficClassStreaming_Object = MibTableColumn
ggsnNbApnActivePdpPerTrafficClassStreaming = _GgsnNbApnActivePdpPerTrafficClassStreaming_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 49),
    _GgsnNbApnActivePdpPerTrafficClassStreaming_Type()
)
ggsnNbApnActivePdpPerTrafficClassStreaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbApnActivePdpPerTrafficClassStreaming.setStatus("current")
_GgsnNbApnActivePdpPerTrafficClassInteractive_Type = Gauge32
_GgsnNbApnActivePdpPerTrafficClassInteractive_Object = MibTableColumn
ggsnNbApnActivePdpPerTrafficClassInteractive = _GgsnNbApnActivePdpPerTrafficClassInteractive_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 50),
    _GgsnNbApnActivePdpPerTrafficClassInteractive_Type()
)
ggsnNbApnActivePdpPerTrafficClassInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbApnActivePdpPerTrafficClassInteractive.setStatus("current")
_GgsnNbApnActivePdpPerTrafficClassBackground_Type = Gauge32
_GgsnNbApnActivePdpPerTrafficClassBackground_Object = MibTableColumn
ggsnNbApnActivePdpPerTrafficClassBackground = _GgsnNbApnActivePdpPerTrafficClassBackground_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 51),
    _GgsnNbApnActivePdpPerTrafficClassBackground_Type()
)
ggsnNbApnActivePdpPerTrafficClassBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNbApnActivePdpPerTrafficClassBackground.setStatus("current")
_GgsnApnImsDedicatedCompletedActivation_Type = Counter64
_GgsnApnImsDedicatedCompletedActivation_Object = MibTableColumn
ggsnApnImsDedicatedCompletedActivation = _GgsnApnImsDedicatedCompletedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 52),
    _GgsnApnImsDedicatedCompletedActivation_Type()
)
ggsnApnImsDedicatedCompletedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnImsDedicatedCompletedActivation.setStatus("current")
_GgsnApnImsDedicatedNotConfiguredActivationFailed_Type = Counter64
_GgsnApnImsDedicatedNotConfiguredActivationFailed_Object = MibTableColumn
ggsnApnImsDedicatedNotConfiguredActivationFailed = _GgsnApnImsDedicatedNotConfiguredActivationFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 53),
    _GgsnApnImsDedicatedNotConfiguredActivationFailed_Type()
)
ggsnApnImsDedicatedNotConfiguredActivationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnImsDedicatedNotConfiguredActivationFailed.setStatus("current")
_GgsnApnImsGeneralPurposeCompletedActivation_Type = Counter64
_GgsnApnImsGeneralPurposeCompletedActivation_Object = MibTableColumn
ggsnApnImsGeneralPurposeCompletedActivation = _GgsnApnImsGeneralPurposeCompletedActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 54),
    _GgsnApnImsGeneralPurposeCompletedActivation_Type()
)
ggsnApnImsGeneralPurposeCompletedActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnImsGeneralPurposeCompletedActivation.setStatus("current")
_GgsnApnImsGeneralNotConfiguredActivationFailed_Type = Counter64
_GgsnApnImsGeneralNotConfiguredActivationFailed_Object = MibTableColumn
ggsnApnImsGeneralNotConfiguredActivationFailed = _GgsnApnImsGeneralNotConfiguredActivationFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 55),
    _GgsnApnImsGeneralNotConfiguredActivationFailed_Type()
)
ggsnApnImsGeneralNotConfiguredActivationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnImsGeneralNotConfiguredActivationFailed.setStatus("current")
_GgsnApnActivationFailedDuetoGeneralPurposeNotConfigured_Type = Counter64
_GgsnApnActivationFailedDuetoGeneralPurposeNotConfigured_Object = MibTableColumn
ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured = _GgsnApnActivationFailedDuetoGeneralPurposeNotConfigured_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 56),
    _GgsnApnActivationFailedDuetoGeneralPurposeNotConfigured_Type()
)
ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured.setStatus("current")
_GgsnApnUnauthorizedImsPackets_Type = Counter64
_GgsnApnUnauthorizedImsPackets_Object = MibTableColumn
ggsnApnUnauthorizedImsPackets = _GgsnApnUnauthorizedImsPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 57),
    _GgsnApnUnauthorizedImsPackets_Type()
)
ggsnApnUnauthorizedImsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnUnauthorizedImsPackets.setStatus("current")
_GgsnApnRadiusAccountingFailure_Type = Counter64
_GgsnApnRadiusAccountingFailure_Object = MibTableColumn
ggsnApnRadiusAccountingFailure = _GgsnApnRadiusAccountingFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 58),
    _GgsnApnRadiusAccountingFailure_Type()
)
ggsnApnRadiusAccountingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAccountingFailure.setStatus("current")
_GgsnApnRadiusAuthenticationFailure_Type = Counter64
_GgsnApnRadiusAuthenticationFailure_Object = MibTableColumn
ggsnApnRadiusAuthenticationFailure = _GgsnApnRadiusAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 59),
    _GgsnApnRadiusAuthenticationFailure_Type()
)
ggsnApnRadiusAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthenticationFailure.setStatus("current")
_GgsnApnSaccRsInstalledDynRules_Type = Gauge32
_GgsnApnSaccRsInstalledDynRules_Object = MibTableColumn
ggsnApnSaccRsInstalledDynRules = _GgsnApnSaccRsInstalledDynRules_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 60),
    _GgsnApnSaccRsInstalledDynRules_Type()
)
ggsnApnSaccRsInstalledDynRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsInstalledDynRules.setStatus("current")
_GgsnApnSaccRsActivePredefinedChargingRules_Type = Gauge32
_GgsnApnSaccRsActivePredefinedChargingRules_Object = MibTableColumn
ggsnApnSaccRsActivePredefinedChargingRules = _GgsnApnSaccRsActivePredefinedChargingRules_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 61),
    _GgsnApnSaccRsActivePredefinedChargingRules_Type()
)
ggsnApnSaccRsActivePredefinedChargingRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsActivePredefinedChargingRules.setStatus("current")
_GgsnApnSaccRsActivePredefinedChargingRuleBases_Type = Gauge32
_GgsnApnSaccRsActivePredefinedChargingRuleBases_Object = MibTableColumn
ggsnApnSaccRsActivePredefinedChargingRuleBases = _GgsnApnSaccRsActivePredefinedChargingRuleBases_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 62),
    _GgsnApnSaccRsActivePredefinedChargingRuleBases_Type()
)
ggsnApnSaccRsActivePredefinedChargingRuleBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsActivePredefinedChargingRuleBases.setStatus("current")
_GgsnApnAvailableIpAddressesInInternalPool_Type = Gauge32
_GgsnApnAvailableIpAddressesInInternalPool_Object = MibTableColumn
ggsnApnAvailableIpAddressesInInternalPool = _GgsnApnAvailableIpAddressesInInternalPool_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 63),
    _GgsnApnAvailableIpAddressesInInternalPool_Type()
)
ggsnApnAvailableIpAddressesInInternalPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAvailableIpAddressesInInternalPool.setStatus("deprecated")
_GgsnApnIpAddressesInQuarantineInInternalPool_Type = Gauge32
_GgsnApnIpAddressesInQuarantineInInternalPool_Object = MibTableColumn
ggsnApnIpAddressesInQuarantineInInternalPool = _GgsnApnIpAddressesInQuarantineInInternalPool_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 64),
    _GgsnApnIpAddressesInQuarantineInInternalPool_Type()
)
ggsnApnIpAddressesInQuarantineInInternalPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnIpAddressesInQuarantineInInternalPool.setStatus("deprecated")
_GgsnApn3gdtActiveContexts_Type = Gauge32
_GgsnApn3gdtActiveContexts_Object = MibTableColumn
ggsnApn3gdtActiveContexts = _GgsnApn3gdtActiveContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 65),
    _GgsnApn3gdtActiveContexts_Type()
)
ggsnApn3gdtActiveContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApn3gdtActiveContexts.setStatus("current")
_GgsnApn3gdtTotalCompletedEstablishment_Type = Gauge32
_GgsnApn3gdtTotalCompletedEstablishment_Object = MibTableColumn
ggsnApn3gdtTotalCompletedEstablishment = _GgsnApn3gdtTotalCompletedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 66),
    _GgsnApn3gdtTotalCompletedEstablishment_Type()
)
ggsnApn3gdtTotalCompletedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApn3gdtTotalCompletedEstablishment.setStatus("deprecated")
_GgsnApn3gdtTotalAttemptedEstablishment_Type = Gauge32
_GgsnApn3gdtTotalAttemptedEstablishment_Object = MibTableColumn
ggsnApn3gdtTotalAttemptedEstablishment = _GgsnApn3gdtTotalAttemptedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 67),
    _GgsnApn3gdtTotalAttemptedEstablishment_Type()
)
ggsnApn3gdtTotalAttemptedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApn3gdtTotalAttemptedEstablishment.setStatus("deprecated")
_GgsnApn3gdtErrorHandling_Type = Gauge32
_GgsnApn3gdtErrorHandling_Object = MibTableColumn
ggsnApn3gdtErrorHandling = _GgsnApn3gdtErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 68),
    _GgsnApn3gdtErrorHandling_Type()
)
ggsnApn3gdtErrorHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApn3gdtErrorHandling.setStatus("deprecated")
_GgsnApnAttemptedUpdateGgsn_Type = Counter64
_GgsnApnAttemptedUpdateGgsn_Object = MibTableColumn
ggsnApnAttemptedUpdateGgsn = _GgsnApnAttemptedUpdateGgsn_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 69),
    _GgsnApnAttemptedUpdateGgsn_Type()
)
ggsnApnAttemptedUpdateGgsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedUpdateGgsn.setStatus("current")
_GgsnApnCompletedUpdateGgsn_Type = Counter64
_GgsnApnCompletedUpdateGgsn_Object = MibTableColumn
ggsnApnCompletedUpdateGgsn = _GgsnApnCompletedUpdateGgsn_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 70),
    _GgsnApnCompletedUpdateGgsn_Type()
)
ggsnApnCompletedUpdateGgsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedUpdateGgsn.setStatus("current")
_GgsnApnAttemptedActivationNonDuplicated_Type = Counter64
_GgsnApnAttemptedActivationNonDuplicated_Object = MibTableColumn
ggsnApnAttemptedActivationNonDuplicated = _GgsnApnAttemptedActivationNonDuplicated_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 71),
    _GgsnApnAttemptedActivationNonDuplicated_Type()
)
ggsnApnAttemptedActivationNonDuplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedActivationNonDuplicated.setStatus("current")
_GgsnApnActivePdpContextMaxDuringLastPeriod_Type = Gauge32
_GgsnApnActivePdpContextMaxDuringLastPeriod_Object = MibTableColumn
ggsnApnActivePdpContextMaxDuringLastPeriod = _GgsnApnActivePdpContextMaxDuringLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 72),
    _GgsnApnActivePdpContextMaxDuringLastPeriod_Type()
)
ggsnApnActivePdpContextMaxDuringLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextMaxDuringLastPeriod.setStatus("current")
_PgwApnActiveEpsBearer_Type = Gauge32
_PgwApnActiveEpsBearer_Object = MibTableColumn
pgwApnActiveEpsBearer = _PgwApnActiveEpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 73),
    _PgwApnActiveEpsBearer_Type()
)
pgwApnActiveEpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnActiveEpsBearer.setStatus("current")
_PgwApnActiveIpv6EpsBearer_Type = Gauge32
_PgwApnActiveIpv6EpsBearer_Object = MibTableColumn
pgwApnActiveIpv6EpsBearer = _PgwApnActiveIpv6EpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 74),
    _PgwApnActiveIpv6EpsBearer_Type()
)
pgwApnActiveIpv6EpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnActiveIpv6EpsBearer.setStatus("current")
_PgwApnAttemptedEpsBearerActivation_Type = Counter64
_PgwApnAttemptedEpsBearerActivation_Object = MibTableColumn
pgwApnAttemptedEpsBearerActivation = _PgwApnAttemptedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 75),
    _PgwApnAttemptedEpsBearerActivation_Type()
)
pgwApnAttemptedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedEpsBearerActivation.setStatus("current")
_PgwApnCompletedEpsBearerActivation_Type = Counter64
_PgwApnCompletedEpsBearerActivation_Object = MibTableColumn
pgwApnCompletedEpsBearerActivation = _PgwApnCompletedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 76),
    _PgwApnCompletedEpsBearerActivation_Type()
)
pgwApnCompletedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedEpsBearerActivation.setStatus("current")
_PgwApnAttemptedIpv6EpsBearerActivation_Type = Counter64
_PgwApnAttemptedIpv6EpsBearerActivation_Object = MibTableColumn
pgwApnAttemptedIpv6EpsBearerActivation = _PgwApnAttemptedIpv6EpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 77),
    _PgwApnAttemptedIpv6EpsBearerActivation_Type()
)
pgwApnAttemptedIpv6EpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedIpv6EpsBearerActivation.setStatus("current")
_PgwApnCompletedIpv6EpsBearerActivation_Type = Counter64
_PgwApnCompletedIpv6EpsBearerActivation_Object = MibTableColumn
pgwApnCompletedIpv6EpsBearerActivation = _PgwApnCompletedIpv6EpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 78),
    _PgwApnCompletedIpv6EpsBearerActivation_Type()
)
pgwApnCompletedIpv6EpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedIpv6EpsBearerActivation.setStatus("current")
_PgwApnAttemptedEpsBearerDeactivation_Type = Counter64
_PgwApnAttemptedEpsBearerDeactivation_Object = MibTableColumn
pgwApnAttemptedEpsBearerDeactivation = _PgwApnAttemptedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 79),
    _PgwApnAttemptedEpsBearerDeactivation_Type()
)
pgwApnAttemptedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedEpsBearerDeactivation.setStatus("current")
_PgwApnCompletedEpsBearerDeactivation_Type = Counter64
_PgwApnCompletedEpsBearerDeactivation_Object = MibTableColumn
pgwApnCompletedEpsBearerDeactivation = _PgwApnCompletedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 80),
    _PgwApnCompletedEpsBearerDeactivation_Type()
)
pgwApnCompletedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedEpsBearerDeactivation.setStatus("current")
_PgwApnAttemptedS5NetworkDeactivation_Type = Counter64
_PgwApnAttemptedS5NetworkDeactivation_Object = MibTableColumn
pgwApnAttemptedS5NetworkDeactivation = _PgwApnAttemptedS5NetworkDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 81),
    _PgwApnAttemptedS5NetworkDeactivation_Type()
)
pgwApnAttemptedS5NetworkDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5NetworkDeactivation.setStatus("current")
_PgwApnCompletedS5NetworkDeactivation_Type = Counter64
_PgwApnCompletedS5NetworkDeactivation_Object = MibTableColumn
pgwApnCompletedS5NetworkDeactivation = _PgwApnCompletedS5NetworkDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 82),
    _PgwApnCompletedS5NetworkDeactivation_Type()
)
pgwApnCompletedS5NetworkDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5NetworkDeactivation.setStatus("current")
_PgwApnAttemptedS5UeSgwModification_Type = Counter64
_PgwApnAttemptedS5UeSgwModification_Object = MibTableColumn
pgwApnAttemptedS5UeSgwModification = _PgwApnAttemptedS5UeSgwModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 83),
    _PgwApnAttemptedS5UeSgwModification_Type()
)
pgwApnAttemptedS5UeSgwModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5UeSgwModification.setStatus("current")
_PgwApnCompletedS5UeSgwModification_Type = Counter64
_PgwApnCompletedS5UeSgwModification_Object = MibTableColumn
pgwApnCompletedS5UeSgwModification = _PgwApnCompletedS5UeSgwModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 84),
    _PgwApnCompletedS5UeSgwModification_Type()
)
pgwApnCompletedS5UeSgwModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5UeSgwModification.setStatus("current")
_PgwApnAttemptedS5SgwSgsnModification_Type = Counter64
_PgwApnAttemptedS5SgwSgsnModification_Object = MibTableColumn
pgwApnAttemptedS5SgwSgsnModification = _PgwApnAttemptedS5SgwSgsnModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 85),
    _PgwApnAttemptedS5SgwSgsnModification_Type()
)
pgwApnAttemptedS5SgwSgsnModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5SgwSgsnModification.setStatus("current")
_PgwApnCompletedS5SgwSgsnModification_Type = Counter64
_PgwApnCompletedS5SgwSgsnModification_Object = MibTableColumn
pgwApnCompletedS5SgwSgsnModification = _PgwApnCompletedS5SgwSgsnModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 86),
    _PgwApnCompletedS5SgwSgsnModification_Type()
)
pgwApnCompletedS5SgwSgsnModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5SgwSgsnModification.setStatus("current")
_PgwApnAttemptedS5SgsnSgwModification_Type = Counter64
_PgwApnAttemptedS5SgsnSgwModification_Object = MibTableColumn
pgwApnAttemptedS5SgsnSgwModification = _PgwApnAttemptedS5SgsnSgwModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 87),
    _PgwApnAttemptedS5SgsnSgwModification_Type()
)
pgwApnAttemptedS5SgsnSgwModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5SgsnSgwModification.setStatus("current")
_PgwApnCompletedS5SgsnSgwModification_Type = Counter64
_PgwApnCompletedS5SgsnSgwModification_Object = MibTableColumn
pgwApnCompletedS5SgsnSgwModification = _PgwApnCompletedS5SgsnSgwModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 88),
    _PgwApnCompletedS5SgsnSgwModification_Type()
)
pgwApnCompletedS5SgsnSgwModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5SgsnSgwModification.setStatus("current")
_PgwApnAttemptedS5NetworkModification_Type = Counter64
_PgwApnAttemptedS5NetworkModification_Object = MibTableColumn
pgwApnAttemptedS5NetworkModification = _PgwApnAttemptedS5NetworkModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 89),
    _PgwApnAttemptedS5NetworkModification_Type()
)
pgwApnAttemptedS5NetworkModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5NetworkModification.setStatus("current")
_PgwApnCompletedS5NetworkModification_Type = Counter64
_PgwApnCompletedS5NetworkModification_Object = MibTableColumn
pgwApnCompletedS5NetworkModification = _PgwApnCompletedS5NetworkModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 90),
    _PgwApnCompletedS5NetworkModification_Type()
)
pgwApnCompletedS5NetworkModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5NetworkModification.setStatus("current")
_PgwApnAttemptedS5UeSgwDeactivation_Type = Counter64
_PgwApnAttemptedS5UeSgwDeactivation_Object = MibTableColumn
pgwApnAttemptedS5UeSgwDeactivation = _PgwApnAttemptedS5UeSgwDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 91),
    _PgwApnAttemptedS5UeSgwDeactivation_Type()
)
pgwApnAttemptedS5UeSgwDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5UeSgwDeactivation.setStatus("current")
_PgwApnCompletedS5UeSgwDeactivation_Type = Counter64
_PgwApnCompletedS5UeSgwDeactivation_Object = MibTableColumn
pgwApnCompletedS5UeSgwDeactivation = _PgwApnCompletedS5UeSgwDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 92),
    _PgwApnCompletedS5UeSgwDeactivation_Type()
)
pgwApnCompletedS5UeSgwDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5UeSgwDeactivation.setStatus("current")
_GnApnUplinkPackets_Type = Counter64
_GnApnUplinkPackets_Object = MibTableColumn
gnApnUplinkPackets = _GnApnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 93),
    _GnApnUplinkPackets_Type()
)
gnApnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnUplinkPackets.setStatus("current")
_GnApnUplinkBytes_Type = Counter64
_GnApnUplinkBytes_Object = MibTableColumn
gnApnUplinkBytes = _GnApnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 94),
    _GnApnUplinkBytes_Type()
)
gnApnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnUplinkBytes.setStatus("current")
_GnApnUplinkPacketsIpv6_Type = Counter64
_GnApnUplinkPacketsIpv6_Object = MibTableColumn
gnApnUplinkPacketsIpv6 = _GnApnUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 95),
    _GnApnUplinkPacketsIpv6_Type()
)
gnApnUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnUplinkPacketsIpv6.setStatus("current")
_GnApnUplinkBytesIpv6_Type = Counter64
_GnApnUplinkBytesIpv6_Object = MibTableColumn
gnApnUplinkBytesIpv6 = _GnApnUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 96),
    _GnApnUplinkBytesIpv6_Type()
)
gnApnUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnUplinkBytesIpv6.setStatus("current")
_GnApnDownlinkPackets_Type = Counter64
_GnApnDownlinkPackets_Object = MibTableColumn
gnApnDownlinkPackets = _GnApnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 97),
    _GnApnDownlinkPackets_Type()
)
gnApnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnDownlinkPackets.setStatus("current")
_GnApnDownlinkBytes_Type = Counter64
_GnApnDownlinkBytes_Object = MibTableColumn
gnApnDownlinkBytes = _GnApnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 98),
    _GnApnDownlinkBytes_Type()
)
gnApnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnDownlinkBytes.setStatus("current")
_GnApnDownlinkPacketsIpv6_Type = Counter64
_GnApnDownlinkPacketsIpv6_Object = MibTableColumn
gnApnDownlinkPacketsIpv6 = _GnApnDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 99),
    _GnApnDownlinkPacketsIpv6_Type()
)
gnApnDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnDownlinkPacketsIpv6.setStatus("current")
_GnApnDownlinkBytesIpv6_Type = Counter64
_GnApnDownlinkBytesIpv6_Object = MibTableColumn
gnApnDownlinkBytesIpv6 = _GnApnDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 100),
    _GnApnDownlinkBytesIpv6_Type()
)
gnApnDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApnDownlinkBytesIpv6.setStatus("current")
_S5ApnUplinkPackets_Type = Counter64
_S5ApnUplinkPackets_Object = MibTableColumn
s5ApnUplinkPackets = _S5ApnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 101),
    _S5ApnUplinkPackets_Type()
)
s5ApnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnUplinkPackets.setStatus("current")
_S5ApnUplinkBytes_Type = Counter64
_S5ApnUplinkBytes_Object = MibTableColumn
s5ApnUplinkBytes = _S5ApnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 102),
    _S5ApnUplinkBytes_Type()
)
s5ApnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnUplinkBytes.setStatus("current")
_S5ApnUplinkPacketsIpv6_Type = Counter64
_S5ApnUplinkPacketsIpv6_Object = MibTableColumn
s5ApnUplinkPacketsIpv6 = _S5ApnUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 103),
    _S5ApnUplinkPacketsIpv6_Type()
)
s5ApnUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnUplinkPacketsIpv6.setStatus("current")
_S5ApnUplinkBytesIpv6_Type = Counter64
_S5ApnUplinkBytesIpv6_Object = MibTableColumn
s5ApnUplinkBytesIpv6 = _S5ApnUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 104),
    _S5ApnUplinkBytesIpv6_Type()
)
s5ApnUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnUplinkBytesIpv6.setStatus("current")
_S5ApnDownlinkPackets_Type = Counter64
_S5ApnDownlinkPackets_Object = MibTableColumn
s5ApnDownlinkPackets = _S5ApnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 105),
    _S5ApnDownlinkPackets_Type()
)
s5ApnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnDownlinkPackets.setStatus("current")
_S5ApnDownlinkBytes_Type = Counter64
_S5ApnDownlinkBytes_Object = MibTableColumn
s5ApnDownlinkBytes = _S5ApnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 106),
    _S5ApnDownlinkBytes_Type()
)
s5ApnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnDownlinkBytes.setStatus("current")
_S5ApnDownlinkPacketsIpv6_Type = Counter64
_S5ApnDownlinkPacketsIpv6_Object = MibTableColumn
s5ApnDownlinkPacketsIpv6 = _S5ApnDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 107),
    _S5ApnDownlinkPacketsIpv6_Type()
)
s5ApnDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnDownlinkPacketsIpv6.setStatus("current")
_S5ApnDownlinkBytesIpv6_Type = Counter64
_S5ApnDownlinkBytesIpv6_Object = MibTableColumn
s5ApnDownlinkBytesIpv6 = _S5ApnDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 108),
    _S5ApnDownlinkBytesIpv6_Type()
)
s5ApnDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ApnDownlinkBytesIpv6.setStatus("current")
_GnApn3gdtUplinkBytes_Type = Counter64
_GnApn3gdtUplinkBytes_Object = MibTableColumn
gnApn3gdtUplinkBytes = _GnApn3gdtUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 109),
    _GnApn3gdtUplinkBytes_Type()
)
gnApn3gdtUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtUplinkBytes.setStatus("current")
_GnApn3gdtUplinkBytesIpv6_Type = Counter64
_GnApn3gdtUplinkBytesIpv6_Object = MibTableColumn
gnApn3gdtUplinkBytesIpv6 = _GnApn3gdtUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 110),
    _GnApn3gdtUplinkBytesIpv6_Type()
)
gnApn3gdtUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtUplinkBytesIpv6.setStatus("current")
_GnApn3gdtUplinkPackets_Type = Counter64
_GnApn3gdtUplinkPackets_Object = MibTableColumn
gnApn3gdtUplinkPackets = _GnApn3gdtUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 111),
    _GnApn3gdtUplinkPackets_Type()
)
gnApn3gdtUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtUplinkPackets.setStatus("current")
_GnApn3gdtUplinkPacketsIpv6_Type = Counter64
_GnApn3gdtUplinkPacketsIpv6_Object = MibTableColumn
gnApn3gdtUplinkPacketsIpv6 = _GnApn3gdtUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 112),
    _GnApn3gdtUplinkPacketsIpv6_Type()
)
gnApn3gdtUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtUplinkPacketsIpv6.setStatus("current")
_GnApn3gdtDownlinkBytes_Type = Counter64
_GnApn3gdtDownlinkBytes_Object = MibTableColumn
gnApn3gdtDownlinkBytes = _GnApn3gdtDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 113),
    _GnApn3gdtDownlinkBytes_Type()
)
gnApn3gdtDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtDownlinkBytes.setStatus("current")
_GnApn3gdtDownlinkBytesIpv6_Type = Counter64
_GnApn3gdtDownlinkBytesIpv6_Object = MibTableColumn
gnApn3gdtDownlinkBytesIpv6 = _GnApn3gdtDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 114),
    _GnApn3gdtDownlinkBytesIpv6_Type()
)
gnApn3gdtDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtDownlinkBytesIpv6.setStatus("current")
_GnApn3gdtDownlinkPackets_Type = Counter64
_GnApn3gdtDownlinkPackets_Object = MibTableColumn
gnApn3gdtDownlinkPackets = _GnApn3gdtDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 115),
    _GnApn3gdtDownlinkPackets_Type()
)
gnApn3gdtDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtDownlinkPackets.setStatus("current")
_GnApn3gdtDownlinkPacketsIpv6_Type = Counter64
_GnApn3gdtDownlinkPacketsIpv6_Object = MibTableColumn
gnApn3gdtDownlinkPacketsIpv6 = _GnApn3gdtDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 116),
    _GnApn3gdtDownlinkPacketsIpv6_Type()
)
gnApn3gdtDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtDownlinkPacketsIpv6.setStatus("current")
_GnApn3gdtDownlinkDropsErrorHandling_Type = Counter64
_GnApn3gdtDownlinkDropsErrorHandling_Object = MibTableColumn
gnApn3gdtDownlinkDropsErrorHandling = _GnApn3gdtDownlinkDropsErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 117),
    _GnApn3gdtDownlinkDropsErrorHandling_Type()
)
gnApn3gdtDownlinkDropsErrorHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtDownlinkDropsErrorHandling.setStatus("current")
_GgsnApn3gdtGtpError_Type = Counter64
_GgsnApn3gdtGtpError_Object = MibTableColumn
ggsnApn3gdtGtpError = _GgsnApn3gdtGtpError_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 118),
    _GgsnApn3gdtGtpError_Type()
)
ggsnApn3gdtGtpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApn3gdtGtpError.setStatus("current")
_GnApn3gdtTotalCompletedEstablishment_Type = Counter32
_GnApn3gdtTotalCompletedEstablishment_Object = MibTableColumn
gnApn3gdtTotalCompletedEstablishment = _GnApn3gdtTotalCompletedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 119),
    _GnApn3gdtTotalCompletedEstablishment_Type()
)
gnApn3gdtTotalCompletedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtTotalCompletedEstablishment.setStatus("current")
_GnApn3gdtTotalAttemptedEstablishment_Type = Counter32
_GnApn3gdtTotalAttemptedEstablishment_Object = MibTableColumn
gnApn3gdtTotalAttemptedEstablishment = _GnApn3gdtTotalAttemptedEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 120),
    _GnApn3gdtTotalAttemptedEstablishment_Type()
)
gnApn3gdtTotalAttemptedEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtTotalAttemptedEstablishment.setStatus("current")
_GnApn3gdtErrorHandling_Type = Counter32
_GnApn3gdtErrorHandling_Object = MibTableColumn
gnApn3gdtErrorHandling = _GnApn3gdtErrorHandling_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 121),
    _GnApn3gdtErrorHandling_Type()
)
gnApn3gdtErrorHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApn3gdtErrorHandling.setStatus("current")
_PgwApnActiveDedicatedEpsBearer_Type = Gauge32
_PgwApnActiveDedicatedEpsBearer_Object = MibTableColumn
pgwApnActiveDedicatedEpsBearer = _PgwApnActiveDedicatedEpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 122),
    _PgwApnActiveDedicatedEpsBearer_Type()
)
pgwApnActiveDedicatedEpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnActiveDedicatedEpsBearer.setStatus("current")
_PgwApnAttemptedDedicatedEpsBearerActivation_Type = Counter64
_PgwApnAttemptedDedicatedEpsBearerActivation_Object = MibTableColumn
pgwApnAttemptedDedicatedEpsBearerActivation = _PgwApnAttemptedDedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 123),
    _PgwApnAttemptedDedicatedEpsBearerActivation_Type()
)
pgwApnAttemptedDedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedDedicatedEpsBearerActivation.setStatus("current")
_PgwApnCompletedDedicatedEpsBearerActivation_Type = Counter64
_PgwApnCompletedDedicatedEpsBearerActivation_Object = MibTableColumn
pgwApnCompletedDedicatedEpsBearerActivation = _PgwApnCompletedDedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 124),
    _PgwApnCompletedDedicatedEpsBearerActivation_Type()
)
pgwApnCompletedDedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedDedicatedEpsBearerActivation.setStatus("current")
_PgwApnAttemptedIpv6DedicatedEpsBearerActivation_Type = Counter64
_PgwApnAttemptedIpv6DedicatedEpsBearerActivation_Object = MibTableColumn
pgwApnAttemptedIpv6DedicatedEpsBearerActivation = _PgwApnAttemptedIpv6DedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 125),
    _PgwApnAttemptedIpv6DedicatedEpsBearerActivation_Type()
)
pgwApnAttemptedIpv6DedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedIpv6DedicatedEpsBearerActivation.setStatus("current")
_PgwApnCompletedIpv6DedicatedEpsBearerActivation_Type = Counter64
_PgwApnCompletedIpv6DedicatedEpsBearerActivation_Object = MibTableColumn
pgwApnCompletedIpv6DedicatedEpsBearerActivation = _PgwApnCompletedIpv6DedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 126),
    _PgwApnCompletedIpv6DedicatedEpsBearerActivation_Type()
)
pgwApnCompletedIpv6DedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedIpv6DedicatedEpsBearerActivation.setStatus("current")
_PgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation_Type = Counter64
_PgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation_Object = MibTableColumn
pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation = _PgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 127),
    _PgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation_Type()
)
pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation.setStatus("current")
_PgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation_Type = Counter64
_PgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation_Object = MibTableColumn
pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation = _PgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 128),
    _PgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation_Type()
)
pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation.setStatus("current")
_PgwApnAttemptedS5NetworkDedicatedEpsBearerModification_Type = Counter64
_PgwApnAttemptedS5NetworkDedicatedEpsBearerModification_Object = MibTableColumn
pgwApnAttemptedS5NetworkDedicatedEpsBearerModification = _PgwApnAttemptedS5NetworkDedicatedEpsBearerModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 129),
    _PgwApnAttemptedS5NetworkDedicatedEpsBearerModification_Type()
)
pgwApnAttemptedS5NetworkDedicatedEpsBearerModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5NetworkDedicatedEpsBearerModification.setStatus("current")
_PgwApnCompletedS5NetworkDedicatedEpsBearerModification_Type = Counter64
_PgwApnCompletedS5NetworkDedicatedEpsBearerModification_Object = MibTableColumn
pgwApnCompletedS5NetworkDedicatedEpsBearerModification = _PgwApnCompletedS5NetworkDedicatedEpsBearerModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 130),
    _PgwApnCompletedS5NetworkDedicatedEpsBearerModification_Type()
)
pgwApnCompletedS5NetworkDedicatedEpsBearerModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5NetworkDedicatedEpsBearerModification.setStatus("current")
_PgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation_Type = Counter64
_PgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation_Object = MibTableColumn
pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation = _PgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 131),
    _PgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation_Type()
)
pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation.setStatus("current")
_PgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation_Type = Counter64
_PgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation_Object = MibTableColumn
pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation = _PgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 132),
    _PgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation_Type()
)
pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation.setStatus("current")
_GgsnApnActivePdpContextCountIpv4v6_Type = Gauge32
_GgsnApnActivePdpContextCountIpv4v6_Object = MibTableColumn
ggsnApnActivePdpContextCountIpv4v6 = _GgsnApnActivePdpContextCountIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 133),
    _GgsnApnActivePdpContextCountIpv4v6_Type()
)
ggsnApnActivePdpContextCountIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnActivePdpContextCountIpv4v6.setStatus("current")
_PgwApnActiveIpv4v6EpsBearer_Type = Gauge32
_PgwApnActiveIpv4v6EpsBearer_Object = MibTableColumn
pgwApnActiveIpv4v6EpsBearer = _PgwApnActiveIpv4v6EpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 134),
    _PgwApnActiveIpv4v6EpsBearer_Type()
)
pgwApnActiveIpv4v6EpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnActiveIpv4v6EpsBearer.setStatus("current")
_GgsnApnAttemptedActivationIpv4v6_Type = Counter64
_GgsnApnAttemptedActivationIpv4v6_Object = MibTableColumn
ggsnApnAttemptedActivationIpv4v6 = _GgsnApnAttemptedActivationIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 135),
    _GgsnApnAttemptedActivationIpv4v6_Type()
)
ggsnApnAttemptedActivationIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnAttemptedActivationIpv4v6.setStatus("current")
_GgsnApnCompletedActivationIpv4v6_Type = Counter64
_GgsnApnCompletedActivationIpv4v6_Object = MibTableColumn
ggsnApnCompletedActivationIpv4v6 = _GgsnApnCompletedActivationIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 136),
    _GgsnApnCompletedActivationIpv4v6_Type()
)
ggsnApnCompletedActivationIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnCompletedActivationIpv4v6.setStatus("current")
_PgwApnAttemptedIpv4v6EpsBearerActivation_Type = Counter64
_PgwApnAttemptedIpv4v6EpsBearerActivation_Object = MibTableColumn
pgwApnAttemptedIpv4v6EpsBearerActivation = _PgwApnAttemptedIpv4v6EpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 137),
    _PgwApnAttemptedIpv4v6EpsBearerActivation_Type()
)
pgwApnAttemptedIpv4v6EpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnAttemptedIpv4v6EpsBearerActivation.setStatus("current")
_PgwApnCompletedIpv4v6EpsBearerActivation_Type = Counter64
_PgwApnCompletedIpv4v6EpsBearerActivation_Object = MibTableColumn
pgwApnCompletedIpv4v6EpsBearerActivation = _PgwApnCompletedIpv4v6EpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 138),
    _PgwApnCompletedIpv4v6EpsBearerActivation_Type()
)
pgwApnCompletedIpv4v6EpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnCompletedIpv4v6EpsBearerActivation.setStatus("current")
_PgwApnActiveWlanEpsBearer_Type = Gauge32
_PgwApnActiveWlanEpsBearer_Object = MibTableColumn
pgwApnActiveWlanEpsBearer = _PgwApnActiveWlanEpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 139),
    _PgwApnActiveWlanEpsBearer_Type()
)
pgwApnActiveWlanEpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnActiveWlanEpsBearer.setStatus("current")
_S2aApnUplinkPackets_Type = Counter64
_S2aApnUplinkPackets_Object = MibTableColumn
s2aApnUplinkPackets = _S2aApnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 140),
    _S2aApnUplinkPackets_Type()
)
s2aApnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnUplinkPackets.setStatus("current")
_S2aApnUplinkBytes_Type = Counter64
_S2aApnUplinkBytes_Object = MibTableColumn
s2aApnUplinkBytes = _S2aApnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 141),
    _S2aApnUplinkBytes_Type()
)
s2aApnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnUplinkBytes.setStatus("current")
_S2aApnDownlinkPackets_Type = Counter64
_S2aApnDownlinkPackets_Object = MibTableColumn
s2aApnDownlinkPackets = _S2aApnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 142),
    _S2aApnDownlinkPackets_Type()
)
s2aApnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnDownlinkPackets.setStatus("current")
_S2aApnDownlinkBytes_Type = Counter64
_S2aApnDownlinkBytes_Object = MibTableColumn
s2aApnDownlinkBytes = _S2aApnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 143),
    _S2aApnDownlinkBytes_Type()
)
s2aApnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnDownlinkBytes.setStatus("current")
_S2aApnUplinkPacketsIpv6_Type = Counter64
_S2aApnUplinkPacketsIpv6_Object = MibTableColumn
s2aApnUplinkPacketsIpv6 = _S2aApnUplinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 144),
    _S2aApnUplinkPacketsIpv6_Type()
)
s2aApnUplinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnUplinkPacketsIpv6.setStatus("deprecated")
_S2aApnUplinkBytesIpv6_Type = Counter64
_S2aApnUplinkBytesIpv6_Object = MibTableColumn
s2aApnUplinkBytesIpv6 = _S2aApnUplinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 145),
    _S2aApnUplinkBytesIpv6_Type()
)
s2aApnUplinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnUplinkBytesIpv6.setStatus("deprecated")
_S2aApnDownlinkPacketsIpv6_Type = Counter64
_S2aApnDownlinkPacketsIpv6_Object = MibTableColumn
s2aApnDownlinkPacketsIpv6 = _S2aApnDownlinkPacketsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 146),
    _S2aApnDownlinkPacketsIpv6_Type()
)
s2aApnDownlinkPacketsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnDownlinkPacketsIpv6.setStatus("deprecated")
_S2aApnDownlinkBytesIpv6_Type = Counter64
_S2aApnDownlinkBytesIpv6_Object = MibTableColumn
s2aApnDownlinkBytesIpv6 = _S2aApnDownlinkBytesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 5, 1, 147),
    _S2aApnDownlinkBytesIpv6_Type()
)
s2aApnDownlinkBytesIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2aApnDownlinkBytesIpv6.setStatus("deprecated")
_GgsnSgsnStatsTable_Object = MibTable
ggsnSgsnStatsTable = _GgsnSgsnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ggsnSgsnStatsTable.setStatus("obsolete")
_GgsnSgsnStatsEntry_Object = MibTableRow
ggsnSgsnStatsEntry = _GgsnSgsnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1)
)
ggsnSgsnStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnSgsnIndex"),
)
if mibBuilder.loadTexts:
    ggsnSgsnStatsEntry.setStatus("obsolete")


class _GgsnSgsnIndex_Type(Integer32):
    """Custom type ggsnSgsnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnSgsnIndex_Type.__name__ = "Integer32"
_GgsnSgsnIndex_Object = MibTableColumn
ggsnSgsnIndex = _GgsnSgsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 1),
    _GgsnSgsnIndex_Type()
)
ggsnSgsnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnSgsnIndex.setStatus("obsolete")
_GgsnSgsnAddress_Type = IpAddress
_GgsnSgsnAddress_Object = MibTableColumn
ggsnSgsnAddress = _GgsnSgsnAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 2),
    _GgsnSgsnAddress_Type()
)
ggsnSgsnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnAddress.setStatus("obsolete")
_GgsnSgsnUplinkPackets_Type = Counter64
_GgsnSgsnUplinkPackets_Object = MibTableColumn
ggsnSgsnUplinkPackets = _GgsnSgsnUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 3),
    _GgsnSgsnUplinkPackets_Type()
)
ggsnSgsnUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnUplinkPackets.setStatus("obsolete")
_GgsnSgsnUplinkBytes_Type = Counter64
_GgsnSgsnUplinkBytes_Object = MibTableColumn
ggsnSgsnUplinkBytes = _GgsnSgsnUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 4),
    _GgsnSgsnUplinkBytes_Type()
)
ggsnSgsnUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnUplinkBytes.setStatus("obsolete")
_GgsnSgsnUplinkDrops_Type = Counter64
_GgsnSgsnUplinkDrops_Object = MibTableColumn
ggsnSgsnUplinkDrops = _GgsnSgsnUplinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 5),
    _GgsnSgsnUplinkDrops_Type()
)
ggsnSgsnUplinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnUplinkDrops.setStatus("obsolete")
_GgsnSgsnDownlinkPackets_Type = Counter64
_GgsnSgsnDownlinkPackets_Object = MibTableColumn
ggsnSgsnDownlinkPackets = _GgsnSgsnDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 6),
    _GgsnSgsnDownlinkPackets_Type()
)
ggsnSgsnDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnDownlinkPackets.setStatus("obsolete")
_GgsnSgsnDownlinkBytes_Type = Counter64
_GgsnSgsnDownlinkBytes_Object = MibTableColumn
ggsnSgsnDownlinkBytes = _GgsnSgsnDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 7),
    _GgsnSgsnDownlinkBytes_Type()
)
ggsnSgsnDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnDownlinkBytes.setStatus("obsolete")
_GgsnSgsnDownlinkDrops_Type = Counter64
_GgsnSgsnDownlinkDrops_Object = MibTableColumn
ggsnSgsnDownlinkDrops = _GgsnSgsnDownlinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 6, 1, 8),
    _GgsnSgsnDownlinkDrops_Type()
)
ggsnSgsnDownlinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnSgsnDownlinkDrops.setStatus("obsolete")
_GgsnL2tpTunnelStatsTable_Object = MibTable
ggsnL2tpTunnelStatsTable = _GgsnL2tpTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ggsnL2tpTunnelStatsTable.setStatus("current")
_GgsnL2tpTunnelStatsEntry_Object = MibTableRow
ggsnL2tpTunnelStatsEntry = _GgsnL2tpTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1)
)
ggsnL2tpTunnelStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnL2tpTunnelIndex"),
)
if mibBuilder.loadTexts:
    ggsnL2tpTunnelStatsEntry.setStatus("current")
_GgsnL2tpTunnelIndex_Type = Integer32
_GgsnL2tpTunnelIndex_Object = MibTableColumn
ggsnL2tpTunnelIndex = _GgsnL2tpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 1),
    _GgsnL2tpTunnelIndex_Type()
)
ggsnL2tpTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelIndex.setStatus("current")
_GgsnL2tpTunnelLocalTID_Type = Integer32
_GgsnL2tpTunnelLocalTID_Object = MibTableColumn
ggsnL2tpTunnelLocalTID = _GgsnL2tpTunnelLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 2),
    _GgsnL2tpTunnelLocalTID_Type()
)
ggsnL2tpTunnelLocalTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelLocalTID.setStatus("current")
_GgsnL2tpTunnelRemoteTID_Type = Integer32
_GgsnL2tpTunnelRemoteTID_Object = MibTableColumn
ggsnL2tpTunnelRemoteTID = _GgsnL2tpTunnelRemoteTID_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 3),
    _GgsnL2tpTunnelRemoteTID_Type()
)
ggsnL2tpTunnelRemoteTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelRemoteTID.setStatus("current")
_GgsnL2tpTunnelLocalIp_Type = IpAddress
_GgsnL2tpTunnelLocalIp_Object = MibTableColumn
ggsnL2tpTunnelLocalIp = _GgsnL2tpTunnelLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 4),
    _GgsnL2tpTunnelLocalIp_Type()
)
ggsnL2tpTunnelLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelLocalIp.setStatus("current")
_GgsnL2tpTunnelRemoteIp_Type = IpAddress
_GgsnL2tpTunnelRemoteIp_Object = MibTableColumn
ggsnL2tpTunnelRemoteIp = _GgsnL2tpTunnelRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 5),
    _GgsnL2tpTunnelRemoteIp_Type()
)
ggsnL2tpTunnelRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelRemoteIp.setStatus("current")
_GgsnL2tpTunnelActiveSessions_Type = Gauge32
_GgsnL2tpTunnelActiveSessions_Object = MibTableColumn
ggsnL2tpTunnelActiveSessions = _GgsnL2tpTunnelActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 6),
    _GgsnL2tpTunnelActiveSessions_Type()
)
ggsnL2tpTunnelActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelActiveSessions.setStatus("current")
_GgsnL2tpTunnelControlTxPackets_Type = Counter64
_GgsnL2tpTunnelControlTxPackets_Object = MibTableColumn
ggsnL2tpTunnelControlTxPackets = _GgsnL2tpTunnelControlTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 7),
    _GgsnL2tpTunnelControlTxPackets_Type()
)
ggsnL2tpTunnelControlTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelControlTxPackets.setStatus("current")
_GgsnL2tpTunnelControlRxPackets_Type = Counter64
_GgsnL2tpTunnelControlRxPackets_Object = MibTableColumn
ggsnL2tpTunnelControlRxPackets = _GgsnL2tpTunnelControlRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 8),
    _GgsnL2tpTunnelControlRxPackets_Type()
)
ggsnL2tpTunnelControlRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelControlRxPackets.setStatus("current")
_GgsnL2tpTunnelDataTxPackets_Type = Counter64
_GgsnL2tpTunnelDataTxPackets_Object = MibTableColumn
ggsnL2tpTunnelDataTxPackets = _GgsnL2tpTunnelDataTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 9),
    _GgsnL2tpTunnelDataTxPackets_Type()
)
ggsnL2tpTunnelDataTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelDataTxPackets.setStatus("current")
_GgsnL2tpTunnelDataRxPackets_Type = Counter64
_GgsnL2tpTunnelDataRxPackets_Object = MibTableColumn
ggsnL2tpTunnelDataRxPackets = _GgsnL2tpTunnelDataRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 10),
    _GgsnL2tpTunnelDataRxPackets_Type()
)
ggsnL2tpTunnelDataRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelDataRxPackets.setStatus("current")
_GgsnL2tpTunnelDiscardedTxPackets_Type = Counter64
_GgsnL2tpTunnelDiscardedTxPackets_Object = MibTableColumn
ggsnL2tpTunnelDiscardedTxPackets = _GgsnL2tpTunnelDiscardedTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 11),
    _GgsnL2tpTunnelDiscardedTxPackets_Type()
)
ggsnL2tpTunnelDiscardedTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelDiscardedTxPackets.setStatus("current")
_GgsnL2tpTunnelDiscardedRxPackets_Type = Counter64
_GgsnL2tpTunnelDiscardedRxPackets_Object = MibTableColumn
ggsnL2tpTunnelDiscardedRxPackets = _GgsnL2tpTunnelDiscardedRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 7, 1, 12),
    _GgsnL2tpTunnelDiscardedRxPackets_Type()
)
ggsnL2tpTunnelDiscardedRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnL2tpTunnelDiscardedRxPackets.setStatus("current")
_PgwGlobalStats_ObjectIdentity = ObjectIdentity
pgwGlobalStats = _PgwGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8)
)
_PgwAttemptedEpsBearerStats_ObjectIdentity = ObjectIdentity
pgwAttemptedEpsBearerStats = _PgwAttemptedEpsBearerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1)
)
_PgwAttemptedEpsBearerActivation_Type = Counter64
_PgwAttemptedEpsBearerActivation_Object = MibScalar
pgwAttemptedEpsBearerActivation = _PgwAttemptedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 1),
    _PgwAttemptedEpsBearerActivation_Type()
)
pgwAttemptedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerActivation.setStatus("current")
_PgwAttemptedEpsBearerIpv6Activation_Type = Counter64
_PgwAttemptedEpsBearerIpv6Activation_Object = MibScalar
pgwAttemptedEpsBearerIpv6Activation = _PgwAttemptedEpsBearerIpv6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 2),
    _PgwAttemptedEpsBearerIpv6Activation_Type()
)
pgwAttemptedEpsBearerIpv6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerIpv6Activation.setStatus("current")
_PgwAttemptedEpsBearerModification_Type = Counter64
_PgwAttemptedEpsBearerModification_Object = MibScalar
pgwAttemptedEpsBearerModification = _PgwAttemptedEpsBearerModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 3),
    _PgwAttemptedEpsBearerModification_Type()
)
pgwAttemptedEpsBearerModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerModification.setStatus("current")
_PgwAttemptedEpsBearerDeactivation_Type = Counter64
_PgwAttemptedEpsBearerDeactivation_Object = MibScalar
pgwAttemptedEpsBearerDeactivation = _PgwAttemptedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 4),
    _PgwAttemptedEpsBearerDeactivation_Type()
)
pgwAttemptedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerDeactivation.setStatus("current")
_PgwAttemptedDedicatedEpsBearerActivation_Type = Counter64
_PgwAttemptedDedicatedEpsBearerActivation_Object = MibScalar
pgwAttemptedDedicatedEpsBearerActivation = _PgwAttemptedDedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 5),
    _PgwAttemptedDedicatedEpsBearerActivation_Type()
)
pgwAttemptedDedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedDedicatedEpsBearerActivation.setStatus("current")
_PgwAttemptedDedicatedEpsBearerIpv6Activation_Type = Counter64
_PgwAttemptedDedicatedEpsBearerIpv6Activation_Object = MibScalar
pgwAttemptedDedicatedEpsBearerIpv6Activation = _PgwAttemptedDedicatedEpsBearerIpv6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 6),
    _PgwAttemptedDedicatedEpsBearerIpv6Activation_Type()
)
pgwAttemptedDedicatedEpsBearerIpv6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedDedicatedEpsBearerIpv6Activation.setStatus("current")
_PgwAttemptedEpsBearerIpv4v6Activation_Type = Counter64
_PgwAttemptedEpsBearerIpv4v6Activation_Object = MibScalar
pgwAttemptedEpsBearerIpv4v6Activation = _PgwAttemptedEpsBearerIpv4v6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 7),
    _PgwAttemptedEpsBearerIpv4v6Activation_Type()
)
pgwAttemptedEpsBearerIpv4v6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerIpv4v6Activation.setStatus("current")
_PgwAttempteds2aEpsBearerActivation_Type = Counter64
_PgwAttempteds2aEpsBearerActivation_Object = MibScalar
pgwAttempteds2aEpsBearerActivation = _PgwAttempteds2aEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 1, 8),
    _PgwAttempteds2aEpsBearerActivation_Type()
)
pgwAttempteds2aEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAttempteds2aEpsBearerActivation.setStatus("current")
_PgwCompletedEpsBearerStats_ObjectIdentity = ObjectIdentity
pgwCompletedEpsBearerStats = _PgwCompletedEpsBearerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2)
)
_PgwCompletedEpsBearerActivation_Type = Counter64
_PgwCompletedEpsBearerActivation_Object = MibScalar
pgwCompletedEpsBearerActivation = _PgwCompletedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 1),
    _PgwCompletedEpsBearerActivation_Type()
)
pgwCompletedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerActivation.setStatus("current")
_PgwCompletedEpsBearerIpv6Activation_Type = Counter64
_PgwCompletedEpsBearerIpv6Activation_Object = MibScalar
pgwCompletedEpsBearerIpv6Activation = _PgwCompletedEpsBearerIpv6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 2),
    _PgwCompletedEpsBearerIpv6Activation_Type()
)
pgwCompletedEpsBearerIpv6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerIpv6Activation.setStatus("current")
_PgwCompletedEpsBearerModification_Type = Counter64
_PgwCompletedEpsBearerModification_Object = MibScalar
pgwCompletedEpsBearerModification = _PgwCompletedEpsBearerModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 3),
    _PgwCompletedEpsBearerModification_Type()
)
pgwCompletedEpsBearerModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerModification.setStatus("current")
_PgwCompletedEpsBearerDeactivation_Type = Counter64
_PgwCompletedEpsBearerDeactivation_Object = MibScalar
pgwCompletedEpsBearerDeactivation = _PgwCompletedEpsBearerDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 4),
    _PgwCompletedEpsBearerDeactivation_Type()
)
pgwCompletedEpsBearerDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerDeactivation.setStatus("current")
_PgwCompletedDedicatedEpsBearerActivation_Type = Counter64
_PgwCompletedDedicatedEpsBearerActivation_Object = MibScalar
pgwCompletedDedicatedEpsBearerActivation = _PgwCompletedDedicatedEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 5),
    _PgwCompletedDedicatedEpsBearerActivation_Type()
)
pgwCompletedDedicatedEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedDedicatedEpsBearerActivation.setStatus("current")
_PgwCompletedDedicatedEpsBearerIpv6Activation_Type = Counter64
_PgwCompletedDedicatedEpsBearerIpv6Activation_Object = MibScalar
pgwCompletedDedicatedEpsBearerIpv6Activation = _PgwCompletedDedicatedEpsBearerIpv6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 6),
    _PgwCompletedDedicatedEpsBearerIpv6Activation_Type()
)
pgwCompletedDedicatedEpsBearerIpv6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedDedicatedEpsBearerIpv6Activation.setStatus("current")
_PgwCompletedEpsBearerIpv4v6Activation_Type = Counter64
_PgwCompletedEpsBearerIpv4v6Activation_Object = MibScalar
pgwCompletedEpsBearerIpv4v6Activation = _PgwCompletedEpsBearerIpv4v6Activation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 7),
    _PgwCompletedEpsBearerIpv4v6Activation_Type()
)
pgwCompletedEpsBearerIpv4v6Activation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerIpv4v6Activation.setStatus("current")
_PgwCompleteds2aEpsBearerActivation_Type = Counter64
_PgwCompleteds2aEpsBearerActivation_Object = MibScalar
pgwCompleteds2aEpsBearerActivation = _PgwCompleteds2aEpsBearerActivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 2, 8),
    _PgwCompleteds2aEpsBearerActivation_Type()
)
pgwCompleteds2aEpsBearerActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwCompleteds2aEpsBearerActivation.setStatus("current")
_PgwNbrOfActiveEpsBearer_Type = Gauge32
_PgwNbrOfActiveEpsBearer_Object = MibScalar
pgwNbrOfActiveEpsBearer = _PgwNbrOfActiveEpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 3),
    _PgwNbrOfActiveEpsBearer_Type()
)
pgwNbrOfActiveEpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwNbrOfActiveEpsBearer.setStatus("current")
_PgwNbrOfActiveIpv6EpsBearer_Type = Gauge32
_PgwNbrOfActiveIpv6EpsBearer_Object = MibScalar
pgwNbrOfActiveIpv6EpsBearer = _PgwNbrOfActiveIpv6EpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 4),
    _PgwNbrOfActiveIpv6EpsBearer_Type()
)
pgwNbrOfActiveIpv6EpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwNbrOfActiveIpv6EpsBearer.setStatus("current")
_PgwNbrOfActiveIpv4v6EpsBearer_Type = Gauge32
_PgwNbrOfActiveIpv4v6EpsBearer_Object = MibScalar
pgwNbrOfActiveIpv4v6EpsBearer = _PgwNbrOfActiveIpv4v6EpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 5),
    _PgwNbrOfActiveIpv4v6EpsBearer_Type()
)
pgwNbrOfActiveIpv4v6EpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwNbrOfActiveIpv4v6EpsBearer.setStatus("current")
_PgwWlanNbrOfActiveEpsBearer_Type = Gauge32
_PgwWlanNbrOfActiveEpsBearer_Object = MibScalar
pgwWlanNbrOfActiveEpsBearer = _PgwWlanNbrOfActiveEpsBearer_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 6),
    _PgwWlanNbrOfActiveEpsBearer_Type()
)
pgwWlanNbrOfActiveEpsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwWlanNbrOfActiveEpsBearer.setStatus("current")
_S6bInterface_ObjectIdentity = ObjectIdentity
s6bInterface = _S6bInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7)
)
_S6bAarSent_Type = Counter64
_S6bAarSent_Object = MibScalar
s6bAarSent = _S6bAarSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 1),
    _S6bAarSent_Type()
)
s6bAarSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bAarSent.setStatus("current")
_S6bAaaSuccRcvd_Type = Counter64
_S6bAaaSuccRcvd_Object = MibScalar
s6bAaaSuccRcvd = _S6bAaaSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 2),
    _S6bAaaSuccRcvd_Type()
)
s6bAaaSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bAaaSuccRcvd.setStatus("current")
_S6bAaaFailRcvd_Type = Counter64
_S6bAaaFailRcvd_Object = MibScalar
s6bAaaFailRcvd = _S6bAaaFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 3),
    _S6bAaaFailRcvd_Type()
)
s6bAaaFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bAaaFailRcvd.setStatus("current")
_S6bAaaInvalidRcvd_Type = Counter64
_S6bAaaInvalidRcvd_Object = MibScalar
s6bAaaInvalidRcvd = _S6bAaaInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 4),
    _S6bAaaInvalidRcvd_Type()
)
s6bAaaInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bAaaInvalidRcvd.setStatus("current")
_S6bStrSent_Type = Counter64
_S6bStrSent_Object = MibScalar
s6bStrSent = _S6bStrSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 5),
    _S6bStrSent_Type()
)
s6bStrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bStrSent.setStatus("current")
_S6bStaSuccRcvd_Type = Counter64
_S6bStaSuccRcvd_Object = MibScalar
s6bStaSuccRcvd = _S6bStaSuccRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 6),
    _S6bStaSuccRcvd_Type()
)
s6bStaSuccRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bStaSuccRcvd.setStatus("current")
_S6bStaFailRcvd_Type = Counter64
_S6bStaFailRcvd_Object = MibScalar
s6bStaFailRcvd = _S6bStaFailRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 7, 7),
    _S6bStaFailRcvd_Type()
)
s6bStaFailRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6bStaFailRcvd.setStatus("current")
_PdnConnectionsPgw_ObjectIdentity = ObjectIdentity
pdnConnectionsPgw = _PdnConnectionsPgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50)
)
_NbrOfPgwPdnConnections_Type = Gauge32
_NbrOfPgwPdnConnections_Object = MibScalar
nbrOfPgwPdnConnections = _NbrOfPgwPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 1),
    _NbrOfPgwPdnConnections_Type()
)
nbrOfPgwPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfPgwPdnConnections.setStatus("current")
_NbrOfPiscPdnConnections_Type = Gauge32
_NbrOfPiscPdnConnections_Object = MibScalar
nbrOfPiscPdnConnections = _NbrOfPiscPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 2),
    _NbrOfPiscPdnConnections_Type()
)
nbrOfPiscPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfPiscPdnConnections.setStatus("current")
_NbrOfOnlineChargingPdnConnections_Type = Gauge32
_NbrOfOnlineChargingPdnConnections_Object = MibScalar
nbrOfOnlineChargingPdnConnections = _NbrOfOnlineChargingPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 3),
    _NbrOfOnlineChargingPdnConnections_Type()
)
nbrOfOnlineChargingPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfOnlineChargingPdnConnections.setStatus("current")
_NbrOfDynamicPolicyControlPdnConnections_Type = Gauge32
_NbrOfDynamicPolicyControlPdnConnections_Object = MibScalar
nbrOfDynamicPolicyControlPdnConnections = _NbrOfDynamicPolicyControlPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 4),
    _NbrOfDynamicPolicyControlPdnConnections_Type()
)
nbrOfDynamicPolicyControlPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfDynamicPolicyControlPdnConnections.setStatus("current")
_NbrOfWlanPdnConnections_Type = Gauge32
_NbrOfWlanPdnConnections_Object = MibScalar
nbrOfWlanPdnConnections = _NbrOfWlanPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 5),
    _NbrOfWlanPdnConnections_Type()
)
nbrOfWlanPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfWlanPdnConnections.setStatus("current")
_NbrOfGeranPdnConnections_Type = Gauge32
_NbrOfGeranPdnConnections_Object = MibScalar
nbrOfGeranPdnConnections = _NbrOfGeranPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 6),
    _NbrOfGeranPdnConnections_Type()
)
nbrOfGeranPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfGeranPdnConnections.setStatus("current")
_NbrOfUtranPdnConnections_Type = Gauge32
_NbrOfUtranPdnConnections_Object = MibScalar
nbrOfUtranPdnConnections = _NbrOfUtranPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 7),
    _NbrOfUtranPdnConnections_Type()
)
nbrOfUtranPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfUtranPdnConnections.setStatus("current")
_NbrOfHspaEvolutionPdnConnections_Type = Gauge32
_NbrOfHspaEvolutionPdnConnections_Object = MibScalar
nbrOfHspaEvolutionPdnConnections = _NbrOfHspaEvolutionPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 8),
    _NbrOfHspaEvolutionPdnConnections_Type()
)
nbrOfHspaEvolutionPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfHspaEvolutionPdnConnections.setStatus("current")
_NbrOfEutranPdnConnections_Type = Gauge32
_NbrOfEutranPdnConnections_Object = MibScalar
nbrOfEutranPdnConnections = _NbrOfEutranPdnConnections_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 8, 50, 9),
    _NbrOfEutranPdnConnections_Type()
)
nbrOfEutranPdnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrOfEutranPdnConnections.setStatus("current")
_GgsnNodeName_Type = DisplayString
_GgsnNodeName_Object = MibScalar
ggsnNodeName = _GgsnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 9),
    _GgsnNodeName_Type()
)
ggsnNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnNodeName.setStatus("current")
_PgwRRreroutedStatsTable_Object = MibTable
pgwRRreroutedStatsTable = _PgwRRreroutedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pgwRRreroutedStatsTable.setStatus("current")
_PgwRRreroutedStatsEntry_Object = MibTableRow
pgwRRreroutedStatsEntry = _PgwRRreroutedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1)
)
pgwRRreroutedStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "pgwRoutingInstanceId"),
)
if mibBuilder.loadTexts:
    pgwRRreroutedStatsEntry.setStatus("current")
_PgwRoutingInstanceId_Type = Integer32
_PgwRoutingInstanceId_Object = MibTableColumn
pgwRoutingInstanceId = _PgwRoutingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 1),
    _PgwRoutingInstanceId_Type()
)
pgwRoutingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgwRoutingInstanceId.setStatus("current")
_PgwRoutingInstanceName_Type = DisplayString
_PgwRoutingInstanceName_Object = MibTableColumn
pgwRoutingInstanceName = _PgwRoutingInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 2),
    _PgwRoutingInstanceName_Type()
)
pgwRoutingInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRoutingInstanceName.setStatus("current")
_PgwRRreroutedDataDownlinkPkts_Type = Counter64
_PgwRRreroutedDataDownlinkPkts_Object = MibTableColumn
pgwRRreroutedDataDownlinkPkts = _PgwRRreroutedDataDownlinkPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 3),
    _PgwRRreroutedDataDownlinkPkts_Type()
)
pgwRRreroutedDataDownlinkPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataDownlinkPkts.setStatus("current")
_PgwRRreroutedDataRxPkts_Type = Counter64
_PgwRRreroutedDataRxPkts_Object = MibTableColumn
pgwRRreroutedDataRxPkts = _PgwRRreroutedDataRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 4),
    _PgwRRreroutedDataRxPkts_Type()
)
pgwRRreroutedDataRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataRxPkts.setStatus("current")
_PgwRRreroutedDataTxPkts_Type = Counter64
_PgwRRreroutedDataTxPkts_Object = MibTableColumn
pgwRRreroutedDataTxPkts = _PgwRRreroutedDataTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 5),
    _PgwRRreroutedDataTxPkts_Type()
)
pgwRRreroutedDataTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataTxPkts.setStatus("current")
_PgwRRreroutedDataIpv6DownlinkPkts_Type = Counter64
_PgwRRreroutedDataIpv6DownlinkPkts_Object = MibTableColumn
pgwRRreroutedDataIpv6DownlinkPkts = _PgwRRreroutedDataIpv6DownlinkPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 6),
    _PgwRRreroutedDataIpv6DownlinkPkts_Type()
)
pgwRRreroutedDataIpv6DownlinkPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataIpv6DownlinkPkts.setStatus("current")
_PgwRRreroutedDataIpv6RxPkts_Type = Counter64
_PgwRRreroutedDataIpv6RxPkts_Object = MibTableColumn
pgwRRreroutedDataIpv6RxPkts = _PgwRRreroutedDataIpv6RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 7),
    _PgwRRreroutedDataIpv6RxPkts_Type()
)
pgwRRreroutedDataIpv6RxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataIpv6RxPkts.setStatus("current")
_PgwRRreroutedDataIpv6TxPkts_Type = Counter64
_PgwRRreroutedDataIpv6TxPkts_Object = MibTableColumn
pgwRRreroutedDataIpv6TxPkts = _PgwRRreroutedDataIpv6TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 1, 11, 1, 8),
    _PgwRRreroutedDataIpv6TxPkts_Type()
)
pgwRRreroutedDataIpv6TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwRRreroutedDataIpv6TxPkts.setStatus("current")
_GgsnGtpcInfo_ObjectIdentity = ObjectIdentity
ggsnGtpcInfo = _GgsnGtpcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2)
)
_GgsnGtpcTable_Object = MibTable
ggsnGtpcTable = _GgsnGtpcTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ggsnGtpcTable.setStatus("current")
_GgsnGtpcEntry_Object = MibTableRow
ggsnGtpcEntry = _GgsnGtpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1)
)
ggsnGtpcEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpcIndex"),
)
if mibBuilder.loadTexts:
    ggsnGtpcEntry.setStatus("current")


class _GgsnGtpcIndex_Type(Integer32):
    """Custom type ggsnGtpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnGtpcIndex_Type.__name__ = "Integer32"
_GgsnGtpcIndex_Object = MibTableColumn
ggsnGtpcIndex = _GgsnGtpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 1),
    _GgsnGtpcIndex_Type()
)
ggsnGtpcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnGtpcIndex.setStatus("current")
_GgsnGtpcVersion_Type = DisplayString
_GgsnGtpcVersion_Object = MibTableColumn
ggsnGtpcVersion = _GgsnGtpcVersion_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 2),
    _GgsnGtpcVersion_Type()
)
ggsnGtpcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcVersion.setStatus("current")
_GgsnGtpcAddress_Type = IpAddress
_GgsnGtpcAddress_Object = MibTableColumn
ggsnGtpcAddress = _GgsnGtpcAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 3),
    _GgsnGtpcAddress_Type()
)
ggsnGtpcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcAddress.setStatus("current")
_GgsnGtpcPdpCapacity_Type = Integer32
_GgsnGtpcPdpCapacity_Object = MibTableColumn
ggsnGtpcPdpCapacity = _GgsnGtpcPdpCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 4),
    _GgsnGtpcPdpCapacity_Type()
)
ggsnGtpcPdpCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcPdpCapacity.setStatus("current")


class _GgsnGtpcRole_Type(Integer32):
    """Custom type ggsnGtpcRole based on Integer32"""
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
          ("master", 2),
          ("slave", 3),
          ("standby", 4))
    )


_GgsnGtpcRole_Type.__name__ = "Integer32"
_GgsnGtpcRole_Object = MibTableColumn
ggsnGtpcRole = _GgsnGtpcRole_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 5),
    _GgsnGtpcRole_Type()
)
ggsnGtpcRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcRole.setStatus("current")
_GgsnGtpcStatus_Type = DisplayString
_GgsnGtpcStatus_Object = MibTableColumn
ggsnGtpcStatus = _GgsnGtpcStatus_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 6),
    _GgsnGtpcStatus_Type()
)
ggsnGtpcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcStatus.setStatus("current")
_GgsnGtpcControlPacketDrops_Type = Counter64
_GgsnGtpcControlPacketDrops_Object = MibTableColumn
ggsnGtpcControlPacketDrops = _GgsnGtpcControlPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 7),
    _GgsnGtpcControlPacketDrops_Type()
)
ggsnGtpcControlPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcControlPacketDrops.setStatus("current")
_GgsnGtpcNbrOfActivePdpContexts_Type = Gauge32
_GgsnGtpcNbrOfActivePdpContexts_Object = MibTableColumn
ggsnGtpcNbrOfActivePdpContexts = _GgsnGtpcNbrOfActivePdpContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 8),
    _GgsnGtpcNbrOfActivePdpContexts_Type()
)
ggsnGtpcNbrOfActivePdpContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcNbrOfActivePdpContexts.setStatus("current")
_GgsnGtpcMemory_Type = Integer32
_GgsnGtpcMemory_Object = MibTableColumn
ggsnGtpcMemory = _GgsnGtpcMemory_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 9),
    _GgsnGtpcMemory_Type()
)
ggsnGtpcMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcMemory.setStatus("current")
_GgsnGtpcMemoryUsed_Type = Integer32
_GgsnGtpcMemoryUsed_Object = MibTableColumn
ggsnGtpcMemoryUsed = _GgsnGtpcMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 10),
    _GgsnGtpcMemoryUsed_Type()
)
ggsnGtpcMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcMemoryUsed.setStatus("current")
_GgsnGtpcCpuUsage_Type = Gauge32
_GgsnGtpcCpuUsage_Object = MibTableColumn
ggsnGtpcCpuUsage = _GgsnGtpcCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 11),
    _GgsnGtpcCpuUsage_Type()
)
ggsnGtpcCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcCpuUsage.setStatus("current")
_GgsnGtpcTftFilterDepthMax_Type = Gauge32
_GgsnGtpcTftFilterDepthMax_Object = MibTableColumn
ggsnGtpcTftFilterDepthMax = _GgsnGtpcTftFilterDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 12),
    _GgsnGtpcTftFilterDepthMax_Type()
)
ggsnGtpcTftFilterDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcTftFilterDepthMax.setStatus("current")
_GgsnGtpcTftFilterDepthMean_Type = Gauge32
_GgsnGtpcTftFilterDepthMean_Object = MibTableColumn
ggsnGtpcTftFilterDepthMean = _GgsnGtpcTftFilterDepthMean_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 13),
    _GgsnGtpcTftFilterDepthMean_Type()
)
ggsnGtpcTftFilterDepthMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcTftFilterDepthMean.setStatus("current")
_GgsnGtpcControlLoad_Type = Gauge32
_GgsnGtpcControlLoad_Object = MibTableColumn
ggsnGtpcControlLoad = _GgsnGtpcControlLoad_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 14),
    _GgsnGtpcControlLoad_Type()
)
ggsnGtpcControlLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcControlLoad.setStatus("current")
_GgsnGtpcNbrOfActivePdpContextsIpv6_Type = Gauge32
_GgsnGtpcNbrOfActivePdpContextsIpv6_Object = MibTableColumn
ggsnGtpcNbrOfActivePdpContextsIpv6 = _GgsnGtpcNbrOfActivePdpContextsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 15),
    _GgsnGtpcNbrOfActivePdpContextsIpv6_Type()
)
ggsnGtpcNbrOfActivePdpContextsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcNbrOfActivePdpContextsIpv6.setStatus("current")
_GgsnGtpcPeakCpuUsage_Type = Gauge32
_GgsnGtpcPeakCpuUsage_Object = MibTableColumn
ggsnGtpcPeakCpuUsage = _GgsnGtpcPeakCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 16),
    _GgsnGtpcPeakCpuUsage_Type()
)
ggsnGtpcPeakCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcPeakCpuUsage.setStatus("current")
_GgsnGtpcNbrOfActivePdpContextsIpv4v6_Type = Gauge32
_GgsnGtpcNbrOfActivePdpContextsIpv4v6_Object = MibTableColumn
ggsnGtpcNbrOfActivePdpContextsIpv4v6 = _GgsnGtpcNbrOfActivePdpContextsIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 2, 1, 1, 17),
    _GgsnGtpcNbrOfActivePdpContextsIpv4v6_Type()
)
ggsnGtpcNbrOfActivePdpContextsIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpcNbrOfActivePdpContextsIpv4v6.setStatus("current")
_GgsnChargingInfo_ObjectIdentity = ObjectIdentity
ggsnChargingInfo = _GgsnChargingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3)
)
_GgsnAcctPartialRecordGenerated_Type = Counter64
_GgsnAcctPartialRecordGenerated_Object = MibScalar
ggsnAcctPartialRecordGenerated = _GgsnAcctPartialRecordGenerated_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 1),
    _GgsnAcctPartialRecordGenerated_Type()
)
ggsnAcctPartialRecordGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctPartialRecordGenerated.setStatus("current")
_GgsnAcctBillingGatewayTable_Object = MibTable
ggsnAcctBillingGatewayTable = _GgsnAcctBillingGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ggsnAcctBillingGatewayTable.setStatus("current")
_GgsnAcctBillingGatewayEntry_Object = MibTableRow
ggsnAcctBillingGatewayEntry = _GgsnAcctBillingGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1)
)
ggsnAcctBillingGatewayEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnAcctBillingGatewayIndex"),
)
if mibBuilder.loadTexts:
    ggsnAcctBillingGatewayEntry.setStatus("current")


class _GgsnAcctBillingGatewayIndex_Type(Integer32):
    """Custom type ggsnAcctBillingGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnAcctBillingGatewayIndex_Type.__name__ = "Integer32"
_GgsnAcctBillingGatewayIndex_Object = MibTableColumn
ggsnAcctBillingGatewayIndex = _GgsnAcctBillingGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 1),
    _GgsnAcctBillingGatewayIndex_Type()
)
ggsnAcctBillingGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnAcctBillingGatewayIndex.setStatus("current")
_GgsnAcctBillingGatewayAddress_Type = IpAddress
_GgsnAcctBillingGatewayAddress_Object = MibTableColumn
ggsnAcctBillingGatewayAddress = _GgsnAcctBillingGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 2),
    _GgsnAcctBillingGatewayAddress_Type()
)
ggsnAcctBillingGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctBillingGatewayAddress.setStatus("current")
_GgsnAcctDataRecTransReqSent_Type = Counter64
_GgsnAcctDataRecTransReqSent_Object = MibTableColumn
ggsnAcctDataRecTransReqSent = _GgsnAcctDataRecTransReqSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 3),
    _GgsnAcctDataRecTransReqSent_Type()
)
ggsnAcctDataRecTransReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctDataRecTransReqSent.setStatus("current")
_GgsnAcctDataRecTransReqSentDup_Type = Counter64
_GgsnAcctDataRecTransReqSentDup_Object = MibTableColumn
ggsnAcctDataRecTransReqSentDup = _GgsnAcctDataRecTransReqSentDup_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 4),
    _GgsnAcctDataRecTransReqSentDup_Type()
)
ggsnAcctDataRecTransReqSentDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctDataRecTransReqSentDup.setStatus("current")
_GgsnAcctDataRecTransReqCancelled_Type = Counter64
_GgsnAcctDataRecTransReqCancelled_Object = MibTableColumn
ggsnAcctDataRecTransReqCancelled = _GgsnAcctDataRecTransReqCancelled_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 5),
    _GgsnAcctDataRecTransReqCancelled_Type()
)
ggsnAcctDataRecTransReqCancelled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctDataRecTransReqCancelled.setStatus("deprecated")
_GgsnAcctDataRecTransRespReceived_Type = Counter64
_GgsnAcctDataRecTransRespReceived_Object = MibTableColumn
ggsnAcctDataRecTransRespReceived = _GgsnAcctDataRecTransRespReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 6),
    _GgsnAcctDataRecTransRespReceived_Type()
)
ggsnAcctDataRecTransRespReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctDataRecTransRespReceived.setStatus("current")
_GgsnAcctRedirectionReqReceived_Type = Counter64
_GgsnAcctRedirectionReqReceived_Object = MibTableColumn
ggsnAcctRedirectionReqReceived = _GgsnAcctRedirectionReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 7),
    _GgsnAcctRedirectionReqReceived_Type()
)
ggsnAcctRedirectionReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctRedirectionReqReceived.setStatus("current")
_GgsnAcctRedirectionRespSent_Type = Counter64
_GgsnAcctRedirectionRespSent_Object = MibTableColumn
ggsnAcctRedirectionRespSent = _GgsnAcctRedirectionRespSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 3, 2, 1, 8),
    _GgsnAcctRedirectionRespSent_Type()
)
ggsnAcctRedirectionRespSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAcctRedirectionRespSent.setStatus("current")
_GgsnDhcpInfo_ObjectIdentity = ObjectIdentity
ggsnDhcpInfo = _GgsnDhcpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4)
)
_GgsnDhcpClientAddress_Type = IpAddress
_GgsnDhcpClientAddress_Object = MibScalar
ggsnDhcpClientAddress = _GgsnDhcpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 1),
    _GgsnDhcpClientAddress_Type()
)
ggsnDhcpClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientAddress.setStatus("current")
_GgsnDhcpServerTable_Object = MibTable
ggsnDhcpServerTable = _GgsnDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ggsnDhcpServerTable.setStatus("current")
_GgsnDhcpServerEntry_Object = MibTableRow
ggsnDhcpServerEntry = _GgsnDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1)
)
ggsnDhcpServerEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnDhcpServerIndex"),
)
if mibBuilder.loadTexts:
    ggsnDhcpServerEntry.setStatus("current")


class _GgsnDhcpServerIndex_Type(Integer32):
    """Custom type ggsnDhcpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnDhcpServerIndex_Type.__name__ = "Integer32"
_GgsnDhcpServerIndex_Object = MibTableColumn
ggsnDhcpServerIndex = _GgsnDhcpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 1),
    _GgsnDhcpServerIndex_Type()
)
ggsnDhcpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnDhcpServerIndex.setStatus("current")
_GgsnDhcpServerAddress_Type = IpAddress
_GgsnDhcpServerAddress_Object = MibTableColumn
ggsnDhcpServerAddress = _GgsnDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 2),
    _GgsnDhcpServerAddress_Type()
)
ggsnDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpServerAddress.setStatus("current")
_GgsnDhcpServerName_Type = DisplayString
_GgsnDhcpServerName_Object = MibTableColumn
ggsnDhcpServerName = _GgsnDhcpServerName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 3),
    _GgsnDhcpServerName_Type()
)
ggsnDhcpServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpServerName.setStatus("current")
_GgsnDhcpClientYiaddr_Type = IpAddress
_GgsnDhcpClientYiaddr_Object = MibTableColumn
ggsnDhcpClientYiaddr = _GgsnDhcpClientYiaddr_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 4),
    _GgsnDhcpClientYiaddr_Type()
)
ggsnDhcpClientYiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientYiaddr.setStatus("current")
_GgsnDhcpClientState_Type = DisplayString
_GgsnDhcpClientState_Object = MibTableColumn
ggsnDhcpClientState = _GgsnDhcpClientState_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 5),
    _GgsnDhcpClientState_Type()
)
ggsnDhcpClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientState.setStatus("current")
_GgsnDhcpClientRequestsSent_Type = Counter64
_GgsnDhcpClientRequestsSent_Object = MibTableColumn
ggsnDhcpClientRequestsSent = _GgsnDhcpClientRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 6),
    _GgsnDhcpClientRequestsSent_Type()
)
ggsnDhcpClientRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientRequestsSent.setStatus("current")
_GgsnDhcpClientRepliesReceived_Type = Counter64
_GgsnDhcpClientRepliesReceived_Object = MibTableColumn
ggsnDhcpClientRepliesReceived = _GgsnDhcpClientRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 7),
    _GgsnDhcpClientRepliesReceived_Type()
)
ggsnDhcpClientRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientRepliesReceived.setStatus("current")
_GgsnDhcpClientRepliesDiscarded_Type = Counter64
_GgsnDhcpClientRepliesDiscarded_Object = MibTableColumn
ggsnDhcpClientRepliesDiscarded = _GgsnDhcpClientRepliesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 8),
    _GgsnDhcpClientRepliesDiscarded_Type()
)
ggsnDhcpClientRepliesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientRepliesDiscarded.setStatus("current")
_GgsnDhcpClientDiscoversSent_Type = Counter64
_GgsnDhcpClientDiscoversSent_Object = MibTableColumn
ggsnDhcpClientDiscoversSent = _GgsnDhcpClientDiscoversSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 9),
    _GgsnDhcpClientDiscoversSent_Type()
)
ggsnDhcpClientDiscoversSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientDiscoversSent.setStatus("current")
_GgsnDhcpClientDeclinesSent_Type = Counter64
_GgsnDhcpClientDeclinesSent_Object = MibTableColumn
ggsnDhcpClientDeclinesSent = _GgsnDhcpClientDeclinesSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 10),
    _GgsnDhcpClientDeclinesSent_Type()
)
ggsnDhcpClientDeclinesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientDeclinesSent.setStatus("current")
_GgsnDhcpClientReleasesSent_Type = Counter64
_GgsnDhcpClientReleasesSent_Object = MibTableColumn
ggsnDhcpClientReleasesSent = _GgsnDhcpClientReleasesSent_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 11),
    _GgsnDhcpClientReleasesSent_Type()
)
ggsnDhcpClientReleasesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientReleasesSent.setStatus("current")
_GgsnDhcpClientOffersReceived_Type = Counter64
_GgsnDhcpClientOffersReceived_Object = MibTableColumn
ggsnDhcpClientOffersReceived = _GgsnDhcpClientOffersReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 12),
    _GgsnDhcpClientOffersReceived_Type()
)
ggsnDhcpClientOffersReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientOffersReceived.setStatus("current")
_GgsnDhcpClientAcksReceived_Type = Counter64
_GgsnDhcpClientAcksReceived_Object = MibTableColumn
ggsnDhcpClientAcksReceived = _GgsnDhcpClientAcksReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 13),
    _GgsnDhcpClientAcksReceived_Type()
)
ggsnDhcpClientAcksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientAcksReceived.setStatus("current")
_GgsnDhcpClientNaksReceived_Type = Counter64
_GgsnDhcpClientNaksReceived_Object = MibTableColumn
ggsnDhcpClientNaksReceived = _GgsnDhcpClientNaksReceived_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 14),
    _GgsnDhcpClientNaksReceived_Type()
)
ggsnDhcpClientNaksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientNaksReceived.setStatus("current")
_GgsnDhcpClientSendErrors_Type = Counter64
_GgsnDhcpClientSendErrors_Object = MibTableColumn
ggsnDhcpClientSendErrors = _GgsnDhcpClientSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 15),
    _GgsnDhcpClientSendErrors_Type()
)
ggsnDhcpClientSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpClientSendErrors.setStatus("current")
_GgsnDhcpServerRoutingInstance_Type = DisplayString
_GgsnDhcpServerRoutingInstance_Object = MibTableColumn
ggsnDhcpServerRoutingInstance = _GgsnDhcpServerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 4, 2, 1, 16),
    _GgsnDhcpServerRoutingInstance_Type()
)
ggsnDhcpServerRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnDhcpServerRoutingInstance.setStatus("current")
_GgsnAlarmInfo_ObjectIdentity = ObjectIdentity
ggsnAlarmInfo = _GgsnAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5)
)
_GgsnAlarmNumber_Type = Gauge32
_GgsnAlarmNumber_Object = MibScalar
ggsnAlarmNumber = _GgsnAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 1),
    _GgsnAlarmNumber_Type()
)
ggsnAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmNumber.setStatus("current")
_GgsnAlarmCriticalNumber_Type = Gauge32
_GgsnAlarmCriticalNumber_Object = MibScalar
ggsnAlarmCriticalNumber = _GgsnAlarmCriticalNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 2),
    _GgsnAlarmCriticalNumber_Type()
)
ggsnAlarmCriticalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmCriticalNumber.setStatus("current")
_GgsnAlarmMajorNumber_Type = Gauge32
_GgsnAlarmMajorNumber_Object = MibScalar
ggsnAlarmMajorNumber = _GgsnAlarmMajorNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 3),
    _GgsnAlarmMajorNumber_Type()
)
ggsnAlarmMajorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmMajorNumber.setStatus("current")
_GgsnAlarmMinorNumber_Type = Gauge32
_GgsnAlarmMinorNumber_Object = MibScalar
ggsnAlarmMinorNumber = _GgsnAlarmMinorNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 4),
    _GgsnAlarmMinorNumber_Type()
)
ggsnAlarmMinorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmMinorNumber.setStatus("current")
_GgsnAlarmWarningNumber_Type = Gauge32
_GgsnAlarmWarningNumber_Object = MibScalar
ggsnAlarmWarningNumber = _GgsnAlarmWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 5),
    _GgsnAlarmWarningNumber_Type()
)
ggsnAlarmWarningNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmWarningNumber.setStatus("current")
_GgsnAlarmUnknownNumber_Type = Gauge32
_GgsnAlarmUnknownNumber_Object = MibScalar
ggsnAlarmUnknownNumber = _GgsnAlarmUnknownNumber_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 6),
    _GgsnAlarmUnknownNumber_Type()
)
ggsnAlarmUnknownNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmUnknownNumber.setStatus("current")
_GgsnAlarmTable_Object = MibTable
ggsnAlarmTable = _GgsnAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    ggsnAlarmTable.setStatus("current")
_GgsnAlarmEntry_Object = MibTableRow
ggsnAlarmEntry = _GgsnAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1)
)
ggsnAlarmEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnAlarmId"),
)
if mibBuilder.loadTexts:
    ggsnAlarmEntry.setStatus("current")


class _GgsnAlarmId_Type(Integer32):
    """Custom type ggsnAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnAlarmId_Type.__name__ = "Integer32"
_GgsnAlarmId_Object = MibTableColumn
ggsnAlarmId = _GgsnAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 1),
    _GgsnAlarmId_Type()
)
ggsnAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmId.setStatus("current")
_GgsnAlarmName_Type = DisplayString
_GgsnAlarmName_Object = MibTableColumn
ggsnAlarmName = _GgsnAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 2),
    _GgsnAlarmName_Type()
)
ggsnAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmName.setStatus("current")
_GgsnAlarmTime_Type = TimeStamp
_GgsnAlarmTime_Object = MibTableColumn
ggsnAlarmTime = _GgsnAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 3),
    _GgsnAlarmTime_Type()
)
ggsnAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmTime.setStatus("current")
_GgsnAlarmSourceId_Type = DisplayString
_GgsnAlarmSourceId_Object = MibTableColumn
ggsnAlarmSourceId = _GgsnAlarmSourceId_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 4),
    _GgsnAlarmSourceId_Type()
)
ggsnAlarmSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmSourceId.setStatus("current")
_GgsnAlarmObjectClass_Type = DisplayString
_GgsnAlarmObjectClass_Object = MibTableColumn
ggsnAlarmObjectClass = _GgsnAlarmObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 5),
    _GgsnAlarmObjectClass_Type()
)
ggsnAlarmObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmObjectClass.setStatus("current")
_GgsnAlarmObjectInstance_Type = DisplayString
_GgsnAlarmObjectInstance_Object = MibTableColumn
ggsnAlarmObjectInstance = _GgsnAlarmObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 6),
    _GgsnAlarmObjectInstance_Type()
)
ggsnAlarmObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmObjectInstance.setStatus("current")
_GgsnAlarmSeverity_Type = PerceivedSeverity
_GgsnAlarmSeverity_Object = MibTableColumn
ggsnAlarmSeverity = _GgsnAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 7),
    _GgsnAlarmSeverity_Type()
)
ggsnAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmSeverity.setStatus("current")
_GgsnAlarmDescription_Type = DisplayString
_GgsnAlarmDescription_Object = MibTableColumn
ggsnAlarmDescription = _GgsnAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 7, 1, 8),
    _GgsnAlarmDescription_Type()
)
ggsnAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmDescription.setStatus("current")
_GgsnAlarmHistTable_Object = MibTable
ggsnAlarmHistTable = _GgsnAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    ggsnAlarmHistTable.setStatus("current")
_GgsnAlarmHistEntry_Object = MibTableRow
ggsnAlarmHistEntry = _GgsnAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1)
)
ggsnAlarmHistEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnAlarmHistTime"),
)
if mibBuilder.loadTexts:
    ggsnAlarmHistEntry.setStatus("current")
_GgsnAlarmHistTime_Type = TimeStamp
_GgsnAlarmHistTime_Object = MibTableColumn
ggsnAlarmHistTime = _GgsnAlarmHistTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 1),
    _GgsnAlarmHistTime_Type()
)
ggsnAlarmHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistTime.setStatus("current")
_GgsnAlarmHistEventCause_Type = AlarmEventCause
_GgsnAlarmHistEventCause_Object = MibTableColumn
ggsnAlarmHistEventCause = _GgsnAlarmHistEventCause_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 2),
    _GgsnAlarmHistEventCause_Type()
)
ggsnAlarmHistEventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistEventCause.setStatus("current")


class _GgsnAlarmHistAlarmId_Type(Integer32):
    """Custom type ggsnAlarmHistAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnAlarmHistAlarmId_Type.__name__ = "Integer32"
_GgsnAlarmHistAlarmId_Object = MibTableColumn
ggsnAlarmHistAlarmId = _GgsnAlarmHistAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 3),
    _GgsnAlarmHistAlarmId_Type()
)
ggsnAlarmHistAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmId.setStatus("current")
_GgsnAlarmHistAlarmName_Type = DisplayString
_GgsnAlarmHistAlarmName_Object = MibTableColumn
ggsnAlarmHistAlarmName = _GgsnAlarmHistAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 4),
    _GgsnAlarmHistAlarmName_Type()
)
ggsnAlarmHistAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmName.setStatus("current")
_GgsnAlarmHistAlarmTime_Type = TimeStamp
_GgsnAlarmHistAlarmTime_Object = MibTableColumn
ggsnAlarmHistAlarmTime = _GgsnAlarmHistAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 5),
    _GgsnAlarmHistAlarmTime_Type()
)
ggsnAlarmHistAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmTime.setStatus("current")
_GgsnAlarmHistAlarmSourceId_Type = DisplayString
_GgsnAlarmHistAlarmSourceId_Object = MibTableColumn
ggsnAlarmHistAlarmSourceId = _GgsnAlarmHistAlarmSourceId_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 6),
    _GgsnAlarmHistAlarmSourceId_Type()
)
ggsnAlarmHistAlarmSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmSourceId.setStatus("current")
_GgsnAlarmHistAlarmObjInstance_Type = DisplayString
_GgsnAlarmHistAlarmObjInstance_Object = MibTableColumn
ggsnAlarmHistAlarmObjInstance = _GgsnAlarmHistAlarmObjInstance_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 7),
    _GgsnAlarmHistAlarmObjInstance_Type()
)
ggsnAlarmHistAlarmObjInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmObjInstance.setStatus("current")
_GgsnAlarmHistAlarmSeverity_Type = PerceivedSeverity
_GgsnAlarmHistAlarmSeverity_Object = MibTableColumn
ggsnAlarmHistAlarmSeverity = _GgsnAlarmHistAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 8),
    _GgsnAlarmHistAlarmSeverity_Type()
)
ggsnAlarmHistAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmSeverity.setStatus("current")
_GgsnAlarmHistAlarmDescription_Type = DisplayString
_GgsnAlarmHistAlarmDescription_Object = MibTableColumn
ggsnAlarmHistAlarmDescription = _GgsnAlarmHistAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 5, 8, 1, 9),
    _GgsnAlarmHistAlarmDescription_Type()
)
ggsnAlarmHistAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnAlarmHistAlarmDescription.setStatus("current")
_GgsnGtpuInfo_ObjectIdentity = ObjectIdentity
ggsnGtpuInfo = _GgsnGtpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6)
)
_GgsnGtpuTable_Object = MibTable
ggsnGtpuTable = _GgsnGtpuTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ggsnGtpuTable.setStatus("current")
_GgsnGtpuEntry_Object = MibTableRow
ggsnGtpuEntry = _GgsnGtpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1)
)
ggsnGtpuEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
)
if mibBuilder.loadTexts:
    ggsnGtpuEntry.setStatus("current")


class _GgsnGtpuIndex_Type(Integer32):
    """Custom type ggsnGtpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GgsnGtpuIndex_Type.__name__ = "Integer32"
_GgsnGtpuIndex_Object = MibTableColumn
ggsnGtpuIndex = _GgsnGtpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 1),
    _GgsnGtpuIndex_Type()
)
ggsnGtpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnGtpuIndex.setStatus("current")
_GgsnGtpuVersion_Type = DisplayString
_GgsnGtpuVersion_Object = MibTableColumn
ggsnGtpuVersion = _GgsnGtpuVersion_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 2),
    _GgsnGtpuVersion_Type()
)
ggsnGtpuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuVersion.setStatus("current")
_GgsnGtpuAddress_Type = IpAddress
_GgsnGtpuAddress_Object = MibTableColumn
ggsnGtpuAddress = _GgsnGtpuAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 3),
    _GgsnGtpuAddress_Type()
)
ggsnGtpuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuAddress.setStatus("current")
_GgsnGtpuPdpCapacity_Type = Integer32
_GgsnGtpuPdpCapacity_Object = MibTableColumn
ggsnGtpuPdpCapacity = _GgsnGtpuPdpCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 4),
    _GgsnGtpuPdpCapacity_Type()
)
ggsnGtpuPdpCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuPdpCapacity.setStatus("current")


class _GgsnGtpuRole_Type(Integer32):
    """Custom type ggsnGtpuRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("standby", 4))
    )


_GgsnGtpuRole_Type.__name__ = "Integer32"
_GgsnGtpuRole_Object = MibTableColumn
ggsnGtpuRole = _GgsnGtpuRole_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 5),
    _GgsnGtpuRole_Type()
)
ggsnGtpuRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuRole.setStatus("current")
_GgsnGtpuStatus_Type = DisplayString
_GgsnGtpuStatus_Object = MibTableColumn
ggsnGtpuStatus = _GgsnGtpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 6),
    _GgsnGtpuStatus_Type()
)
ggsnGtpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuStatus.setStatus("current")
_GgsnGtpuUserUplinkDrops_Type = Counter64
_GgsnGtpuUserUplinkDrops_Object = MibTableColumn
ggsnGtpuUserUplinkDrops = _GgsnGtpuUserUplinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 7),
    _GgsnGtpuUserUplinkDrops_Type()
)
ggsnGtpuUserUplinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuUserUplinkDrops.setStatus("current")
_GgsnGtpuUserDownlinkDrops_Type = Counter64
_GgsnGtpuUserDownlinkDrops_Object = MibTableColumn
ggsnGtpuUserDownlinkDrops = _GgsnGtpuUserDownlinkDrops_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 8),
    _GgsnGtpuUserDownlinkDrops_Type()
)
ggsnGtpuUserDownlinkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuUserDownlinkDrops.setStatus("current")
_GgsnGtpuNbrOfActivePdpContexts_Type = Gauge32
_GgsnGtpuNbrOfActivePdpContexts_Object = MibTableColumn
ggsnGtpuNbrOfActivePdpContexts = _GgsnGtpuNbrOfActivePdpContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 9),
    _GgsnGtpuNbrOfActivePdpContexts_Type()
)
ggsnGtpuNbrOfActivePdpContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuNbrOfActivePdpContexts.setStatus("current")
_GgsnGtpuMemory_Type = Integer32
_GgsnGtpuMemory_Object = MibTableColumn
ggsnGtpuMemory = _GgsnGtpuMemory_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 10),
    _GgsnGtpuMemory_Type()
)
ggsnGtpuMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuMemory.setStatus("current")
_GgsnGtpuMemoryUsed_Type = Integer32
_GgsnGtpuMemoryUsed_Object = MibTableColumn
ggsnGtpuMemoryUsed = _GgsnGtpuMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 11),
    _GgsnGtpuMemoryUsed_Type()
)
ggsnGtpuMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuMemoryUsed.setStatus("current")
_GgsnGtpuCpuUsage_Type = Gauge32
_GgsnGtpuCpuUsage_Object = MibTableColumn
ggsnGtpuCpuUsage = _GgsnGtpuCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 12),
    _GgsnGtpuCpuUsage_Type()
)
ggsnGtpuCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuCpuUsage.setStatus("current")
_GgsnGtpuPayloadLoad_Type = Gauge32
_GgsnGtpuPayloadLoad_Object = MibTableColumn
ggsnGtpuPayloadLoad = _GgsnGtpuPayloadLoad_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 13),
    _GgsnGtpuPayloadLoad_Type()
)
ggsnGtpuPayloadLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuPayloadLoad.setStatus("current")
_GgsnGtpuNbrOfActivePdpContextsIpv6_Type = Gauge32
_GgsnGtpuNbrOfActivePdpContextsIpv6_Object = MibTableColumn
ggsnGtpuNbrOfActivePdpContextsIpv6 = _GgsnGtpuNbrOfActivePdpContextsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 14),
    _GgsnGtpuNbrOfActivePdpContextsIpv6_Type()
)
ggsnGtpuNbrOfActivePdpContextsIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuNbrOfActivePdpContextsIpv6.setStatus("current")
_GgsnGtpuPeakCpuUsage_Type = Gauge32
_GgsnGtpuPeakCpuUsage_Object = MibTableColumn
ggsnGtpuPeakCpuUsage = _GgsnGtpuPeakCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 15),
    _GgsnGtpuPeakCpuUsage_Type()
)
ggsnGtpuPeakCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuPeakCpuUsage.setStatus("current")
_GgsnGtpuUplinkPackets_Type = Counter64
_GgsnGtpuUplinkPackets_Object = MibTableColumn
ggsnGtpuUplinkPackets = _GgsnGtpuUplinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 16),
    _GgsnGtpuUplinkPackets_Type()
)
ggsnGtpuUplinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuUplinkPackets.setStatus("current")
_GgsnGtpuDownlinkPackets_Type = Counter64
_GgsnGtpuDownlinkPackets_Object = MibTableColumn
ggsnGtpuDownlinkPackets = _GgsnGtpuDownlinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 17),
    _GgsnGtpuDownlinkPackets_Type()
)
ggsnGtpuDownlinkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuDownlinkPackets.setStatus("current")
_GgsnGtpuNbrOfActivePdpContextsIpv4v6_Type = Gauge32
_GgsnGtpuNbrOfActivePdpContextsIpv4v6_Object = MibTableColumn
ggsnGtpuNbrOfActivePdpContextsIpv4v6 = _GgsnGtpuNbrOfActivePdpContextsIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 6, 1, 1, 18),
    _GgsnGtpuNbrOfActivePdpContextsIpv4v6_Type()
)
ggsnGtpuNbrOfActivePdpContextsIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtpuNbrOfActivePdpContextsIpv4v6.setStatus("current")
_GgsnFbcInfo_ObjectIdentity = ObjectIdentity
ggsnFbcInfo = _GgsnFbcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7)
)
_GgsnFbcStats_ObjectIdentity = ObjectIdentity
ggsnFbcStats = _GgsnFbcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1)
)
_GgsnFbcInitiatedDeactivation_Type = Counter64
_GgsnFbcInitiatedDeactivation_Object = MibScalar
ggsnFbcInitiatedDeactivation = _GgsnFbcInitiatedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 1),
    _GgsnFbcInitiatedDeactivation_Type()
)
ggsnFbcInitiatedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcInitiatedDeactivation.setStatus("current")
_GgsnFbcApplicationTransactionPps_Type = Counter64
_GgsnFbcApplicationTransactionPps_Object = MibScalar
ggsnFbcApplicationTransactionPps = _GgsnFbcApplicationTransactionPps_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 2),
    _GgsnFbcApplicationTransactionPps_Type()
)
ggsnFbcApplicationTransactionPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcApplicationTransactionPps.setStatus("deprecated")
_GgsnFbcApplicationTransactionPrs_Type = Counter64
_GgsnFbcApplicationTransactionPrs_Object = MibScalar
ggsnFbcApplicationTransactionPrs = _GgsnFbcApplicationTransactionPrs_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 3),
    _GgsnFbcApplicationTransactionPrs_Type()
)
ggsnFbcApplicationTransactionPrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcApplicationTransactionPrs.setStatus("deprecated")
_GgsnApnFbcStatsTable_Object = MibTable
ggsnApnFbcStatsTable = _GgsnApnFbcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ggsnApnFbcStatsTable.setStatus("current")
_GgsnApnFbcStatsEntry_Object = MibTableRow
ggsnApnFbcStatsEntry = _GgsnApnFbcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1)
)
ggsnApnFbcStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcStatsEntry.setStatus("current")
_GgsnApnFbcNbrOfPpsUsers_Type = Gauge32
_GgsnApnFbcNbrOfPpsUsers_Object = MibTableColumn
ggsnApnFbcNbrOfPpsUsers = _GgsnApnFbcNbrOfPpsUsers_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 2),
    _GgsnApnFbcNbrOfPpsUsers_Type()
)
ggsnApnFbcNbrOfPpsUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcNbrOfPpsUsers.setStatus("current")
_GgsnApnFbcNbrOfPpsPdpContexts_Type = Gauge32
_GgsnApnFbcNbrOfPpsPdpContexts_Object = MibTableColumn
ggsnApnFbcNbrOfPpsPdpContexts = _GgsnApnFbcNbrOfPpsPdpContexts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 3),
    _GgsnApnFbcNbrOfPpsPdpContexts_Type()
)
ggsnApnFbcNbrOfPpsPdpContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcNbrOfPpsPdpContexts.setStatus("deprecated")
_GgsnApnFbcPpsCreate_Type = Counter64
_GgsnApnFbcPpsCreate_Object = MibTableColumn
ggsnApnFbcPpsCreate = _GgsnApnFbcPpsCreate_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 4),
    _GgsnApnFbcPpsCreate_Type()
)
ggsnApnFbcPpsCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPpsCreate.setStatus("current")
_GgsnApnFbcPpsReject_Type = Counter64
_GgsnApnFbcPpsReject_Object = MibTableColumn
ggsnApnFbcPpsReject = _GgsnApnFbcPpsReject_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 5),
    _GgsnApnFbcPpsReject_Type()
)
ggsnApnFbcPpsReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPpsReject.setStatus("current")
_GgsnApnFbcInitiatedDeactivation_Type = Counter64
_GgsnApnFbcInitiatedDeactivation_Object = MibTableColumn
ggsnApnFbcInitiatedDeactivation = _GgsnApnFbcInitiatedDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 6),
    _GgsnApnFbcInitiatedDeactivation_Type()
)
ggsnApnFbcInitiatedDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcInitiatedDeactivation.setStatus("current")
_GgsnApnFbcInitialPrsReq_Type = Counter64
_GgsnApnFbcInitialPrsReq_Object = MibTableColumn
ggsnApnFbcInitialPrsReq = _GgsnApnFbcInitialPrsReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 7),
    _GgsnApnFbcInitialPrsReq_Type()
)
ggsnApnFbcInitialPrsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcInitialPrsReq.setStatus("deprecated")
_GgsnApnFbcInitialPrsReqFailed_Type = Counter64
_GgsnApnFbcInitialPrsReqFailed_Object = MibTableColumn
ggsnApnFbcInitialPrsReqFailed = _GgsnApnFbcInitialPrsReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 8),
    _GgsnApnFbcInitialPrsReqFailed_Type()
)
ggsnApnFbcInitialPrsReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcInitialPrsReqFailed.setStatus("deprecated")
_GgsnApnFbcUpdPrsReq_Type = Counter64
_GgsnApnFbcUpdPrsReq_Object = MibTableColumn
ggsnApnFbcUpdPrsReq = _GgsnApnFbcUpdPrsReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 9),
    _GgsnApnFbcUpdPrsReq_Type()
)
ggsnApnFbcUpdPrsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcUpdPrsReq.setStatus("deprecated")
_GgsnApnFbcUpdPrsReqFailed_Type = Counter64
_GgsnApnFbcUpdPrsReqFailed_Object = MibTableColumn
ggsnApnFbcUpdPrsReqFailed = _GgsnApnFbcUpdPrsReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 10),
    _GgsnApnFbcUpdPrsReqFailed_Type()
)
ggsnApnFbcUpdPrsReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcUpdPrsReqFailed.setStatus("deprecated")
_GgsnApnFbcStartCredReq_Type = Counter64
_GgsnApnFbcStartCredReq_Object = MibTableColumn
ggsnApnFbcStartCredReq = _GgsnApnFbcStartCredReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 11),
    _GgsnApnFbcStartCredReq_Type()
)
ggsnApnFbcStartCredReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcStartCredReq.setStatus("deprecated")
_GgsnApnFbcStartCredReqFailed_Type = Counter64
_GgsnApnFbcStartCredReqFailed_Object = MibTableColumn
ggsnApnFbcStartCredReqFailed = _GgsnApnFbcStartCredReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 12),
    _GgsnApnFbcStartCredReqFailed_Type()
)
ggsnApnFbcStartCredReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcStartCredReqFailed.setStatus("deprecated")
_GgsnApnFbcUpdCredReq_Type = Counter64
_GgsnApnFbcUpdCredReq_Object = MibTableColumn
ggsnApnFbcUpdCredReq = _GgsnApnFbcUpdCredReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 13),
    _GgsnApnFbcUpdCredReq_Type()
)
ggsnApnFbcUpdCredReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcUpdCredReq.setStatus("deprecated")
_GgsnApnFbcUpdCredReqFailed_Type = Counter64
_GgsnApnFbcUpdCredReqFailed_Object = MibTableColumn
ggsnApnFbcUpdCredReqFailed = _GgsnApnFbcUpdCredReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 14),
    _GgsnApnFbcUpdCredReqFailed_Type()
)
ggsnApnFbcUpdCredReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcUpdCredReqFailed.setStatus("deprecated")
_GgsnApnFbcStopCredReq_Type = Counter64
_GgsnApnFbcStopCredReq_Object = MibTableColumn
ggsnApnFbcStopCredReq = _GgsnApnFbcStopCredReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 15),
    _GgsnApnFbcStopCredReq_Type()
)
ggsnApnFbcStopCredReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcStopCredReq.setStatus("deprecated")
_GgsnApnFbcStopCredReqFailed_Type = Counter64
_GgsnApnFbcStopCredReqFailed_Object = MibTableColumn
ggsnApnFbcStopCredReqFailed = _GgsnApnFbcStopCredReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 16),
    _GgsnApnFbcStopCredReqFailed_Type()
)
ggsnApnFbcStopCredReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcStopCredReqFailed.setStatus("deprecated")
_GgsnApnFbcExtPrsUpd_Type = Counter64
_GgsnApnFbcExtPrsUpd_Object = MibTableColumn
ggsnApnFbcExtPrsUpd = _GgsnApnFbcExtPrsUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 17),
    _GgsnApnFbcExtPrsUpd_Type()
)
ggsnApnFbcExtPrsUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcExtPrsUpd.setStatus("current")
_GgsnApnFbcExtCreditUpd_Type = Counter64
_GgsnApnFbcExtCreditUpd_Object = MibTableColumn
ggsnApnFbcExtCreditUpd = _GgsnApnFbcExtCreditUpd_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 18),
    _GgsnApnFbcExtCreditUpd_Type()
)
ggsnApnFbcExtCreditUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcExtCreditUpd.setStatus("current")
_GgsnApnFbcDurationTime_Type = Counter64
_GgsnApnFbcDurationTime_Object = MibTableColumn
ggsnApnFbcDurationTime = _GgsnApnFbcDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 19),
    _GgsnApnFbcDurationTime_Type()
)
ggsnApnFbcDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcDurationTime.setStatus("deprecated")
_GgsnApnFbcActivationBearerCtrlAccept_Type = Counter64
_GgsnApnFbcActivationBearerCtrlAccept_Object = MibTableColumn
ggsnApnFbcActivationBearerCtrlAccept = _GgsnApnFbcActivationBearerCtrlAccept_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 20),
    _GgsnApnFbcActivationBearerCtrlAccept_Type()
)
ggsnApnFbcActivationBearerCtrlAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationBearerCtrlAccept.setStatus("current")
_GgsnApnFbcActivationBearerCtrlReject_Type = Counter64
_GgsnApnFbcActivationBearerCtrlReject_Object = MibTableColumn
ggsnApnFbcActivationBearerCtrlReject = _GgsnApnFbcActivationBearerCtrlReject_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 21),
    _GgsnApnFbcActivationBearerCtrlReject_Type()
)
ggsnApnFbcActivationBearerCtrlReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationBearerCtrlReject.setStatus("current")
_GgsnApnFbcActivationBearerCtrlUpgrade_Type = Counter64
_GgsnApnFbcActivationBearerCtrlUpgrade_Object = MibTableColumn
ggsnApnFbcActivationBearerCtrlUpgrade = _GgsnApnFbcActivationBearerCtrlUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 22),
    _GgsnApnFbcActivationBearerCtrlUpgrade_Type()
)
ggsnApnFbcActivationBearerCtrlUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationBearerCtrlUpgrade.setStatus("current")
_GgsnApnFbcActivationBearerCtrlDowngrade_Type = Counter64
_GgsnApnFbcActivationBearerCtrlDowngrade_Object = MibTableColumn
ggsnApnFbcActivationBearerCtrlDowngrade = _GgsnApnFbcActivationBearerCtrlDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 23),
    _GgsnApnFbcActivationBearerCtrlDowngrade_Type()
)
ggsnApnFbcActivationBearerCtrlDowngrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationBearerCtrlDowngrade.setStatus("current")
_GgsnApnFbcModificationBearerCtrlAccept_Type = Counter64
_GgsnApnFbcModificationBearerCtrlAccept_Object = MibTableColumn
ggsnApnFbcModificationBearerCtrlAccept = _GgsnApnFbcModificationBearerCtrlAccept_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 24),
    _GgsnApnFbcModificationBearerCtrlAccept_Type()
)
ggsnApnFbcModificationBearerCtrlAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationBearerCtrlAccept.setStatus("current")
_GgsnApnFbcModificationBearerCtrlDeactivate_Type = Counter64
_GgsnApnFbcModificationBearerCtrlDeactivate_Object = MibTableColumn
ggsnApnFbcModificationBearerCtrlDeactivate = _GgsnApnFbcModificationBearerCtrlDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 25),
    _GgsnApnFbcModificationBearerCtrlDeactivate_Type()
)
ggsnApnFbcModificationBearerCtrlDeactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationBearerCtrlDeactivate.setStatus("current")
_GgsnApnFbcModificationBearerCtrlUpgrade_Type = Counter64
_GgsnApnFbcModificationBearerCtrlUpgrade_Object = MibTableColumn
ggsnApnFbcModificationBearerCtrlUpgrade = _GgsnApnFbcModificationBearerCtrlUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 26),
    _GgsnApnFbcModificationBearerCtrlUpgrade_Type()
)
ggsnApnFbcModificationBearerCtrlUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationBearerCtrlUpgrade.setStatus("current")
_GgsnApnFbcModificationBearerCtrlDowngrade_Type = Counter64
_GgsnApnFbcModificationBearerCtrlDowngrade_Object = MibTableColumn
ggsnApnFbcModificationBearerCtrlDowngrade = _GgsnApnFbcModificationBearerCtrlDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 27),
    _GgsnApnFbcModificationBearerCtrlDowngrade_Type()
)
ggsnApnFbcModificationBearerCtrlDowngrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationBearerCtrlDowngrade.setStatus("current")
_GgsnApnFbcActivationNoBearerCtrlAccept_Type = Counter64
_GgsnApnFbcActivationNoBearerCtrlAccept_Object = MibTableColumn
ggsnApnFbcActivationNoBearerCtrlAccept = _GgsnApnFbcActivationNoBearerCtrlAccept_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 28),
    _GgsnApnFbcActivationNoBearerCtrlAccept_Type()
)
ggsnApnFbcActivationNoBearerCtrlAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationNoBearerCtrlAccept.setStatus("current")
_GgsnApnFbcActivationNoBearerCtrlReject_Type = Counter64
_GgsnApnFbcActivationNoBearerCtrlReject_Object = MibTableColumn
ggsnApnFbcActivationNoBearerCtrlReject = _GgsnApnFbcActivationNoBearerCtrlReject_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 29),
    _GgsnApnFbcActivationNoBearerCtrlReject_Type()
)
ggsnApnFbcActivationNoBearerCtrlReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationNoBearerCtrlReject.setStatus("current")
_GgsnApnFbcActivationNoBearerCtrlDowngrade_Type = Counter64
_GgsnApnFbcActivationNoBearerCtrlDowngrade_Object = MibTableColumn
ggsnApnFbcActivationNoBearerCtrlDowngrade = _GgsnApnFbcActivationNoBearerCtrlDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 30),
    _GgsnApnFbcActivationNoBearerCtrlDowngrade_Type()
)
ggsnApnFbcActivationNoBearerCtrlDowngrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcActivationNoBearerCtrlDowngrade.setStatus("current")
_GgsnApnFbcModificationNoBearerCtrlAccept_Type = Counter64
_GgsnApnFbcModificationNoBearerCtrlAccept_Object = MibTableColumn
ggsnApnFbcModificationNoBearerCtrlAccept = _GgsnApnFbcModificationNoBearerCtrlAccept_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 31),
    _GgsnApnFbcModificationNoBearerCtrlAccept_Type()
)
ggsnApnFbcModificationNoBearerCtrlAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationNoBearerCtrlAccept.setStatus("current")
_GgsnApnFbcModificationNoBearerCtrlDeactivate_Type = Counter64
_GgsnApnFbcModificationNoBearerCtrlDeactivate_Object = MibTableColumn
ggsnApnFbcModificationNoBearerCtrlDeactivate = _GgsnApnFbcModificationNoBearerCtrlDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 32),
    _GgsnApnFbcModificationNoBearerCtrlDeactivate_Type()
)
ggsnApnFbcModificationNoBearerCtrlDeactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationNoBearerCtrlDeactivate.setStatus("current")
_GgsnApnFbcModificationNoBearerCtrlDowngrade_Type = Counter64
_GgsnApnFbcModificationNoBearerCtrlDowngrade_Object = MibTableColumn
ggsnApnFbcModificationNoBearerCtrlDowngrade = _GgsnApnFbcModificationNoBearerCtrlDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 33),
    _GgsnApnFbcModificationNoBearerCtrlDowngrade_Type()
)
ggsnApnFbcModificationNoBearerCtrlDowngrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcModificationNoBearerCtrlDowngrade.setStatus("current")
_GgsnApnSaccAttemptedServiceInitiatedQoSModification_Type = Counter64
_GgsnApnSaccAttemptedServiceInitiatedQoSModification_Object = MibTableColumn
ggsnApnSaccAttemptedServiceInitiatedQoSModification = _GgsnApnSaccAttemptedServiceInitiatedQoSModification_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 4, 1, 34),
    _GgsnApnSaccAttemptedServiceInitiatedQoSModification_Type()
)
ggsnApnSaccAttemptedServiceInitiatedQoSModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccAttemptedServiceInitiatedQoSModification.setStatus("current")
_GgsnApnFbcServIdentStatsTable_Object = MibTable
ggsnApnFbcServIdentStatsTable = _GgsnApnFbcServIdentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5)
)
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentStatsTable.setStatus("current")
_GgsnApnFbcServIdentStatsEntry_Object = MibTableRow
ggsnApnFbcServIdentStatsEntry = _GgsnApnFbcServIdentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1)
)
ggsnApnFbcServIdentStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnServIdentIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentStatsEntry.setStatus("current")


class _GgsnServIdentIndex_Type(Integer32):
    """Custom type ggsnServIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_GgsnServIdentIndex_Type.__name__ = "Integer32"
_GgsnServIdentIndex_Object = MibTableColumn
ggsnServIdentIndex = _GgsnServIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 1),
    _GgsnServIdentIndex_Type()
)
ggsnServIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnServIdentIndex.setStatus("current")
_GgsnApnFbcServIdentUplinkBytes_Type = Counter64
_GgsnApnFbcServIdentUplinkBytes_Object = MibTableColumn
ggsnApnFbcServIdentUplinkBytes = _GgsnApnFbcServIdentUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 2),
    _GgsnApnFbcServIdentUplinkBytes_Type()
)
ggsnApnFbcServIdentUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentUplinkBytes.setStatus("current")
_GgsnApnFbcServIdentDownlinkBytes_Type = Counter64
_GgsnApnFbcServIdentDownlinkBytes_Object = MibTableColumn
ggsnApnFbcServIdentDownlinkBytes = _GgsnApnFbcServIdentDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 4),
    _GgsnApnFbcServIdentDownlinkBytes_Type()
)
ggsnApnFbcServIdentDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentDownlinkBytes.setStatus("current")
_GgsnApnFbcServIdentEventTrans_Type = Counter64
_GgsnApnFbcServIdentEventTrans_Object = MibTableColumn
ggsnApnFbcServIdentEventTrans = _GgsnApnFbcServIdentEventTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 5),
    _GgsnApnFbcServIdentEventTrans_Type()
)
ggsnApnFbcServIdentEventTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentEventTrans.setStatus("deprecated")
_GgsnApnFbcServIdentEventTransFail_Type = Counter64
_GgsnApnFbcServIdentEventTransFail_Object = MibTableColumn
ggsnApnFbcServIdentEventTransFail = _GgsnApnFbcServIdentEventTransFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 6),
    _GgsnApnFbcServIdentEventTransFail_Type()
)
ggsnApnFbcServIdentEventTransFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentEventTransFail.setStatus("deprecated")
_GgsnApnFbcServIdentEventStartTrans_Type = Counter64
_GgsnApnFbcServIdentEventStartTrans_Object = MibTableColumn
ggsnApnFbcServIdentEventStartTrans = _GgsnApnFbcServIdentEventStartTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 7),
    _GgsnApnFbcServIdentEventStartTrans_Type()
)
ggsnApnFbcServIdentEventStartTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentEventStartTrans.setStatus("deprecated")
_GgsnApnFbcServIdentEventSuccessTrans_Type = Counter64
_GgsnApnFbcServIdentEventSuccessTrans_Object = MibTableColumn
ggsnApnFbcServIdentEventSuccessTrans = _GgsnApnFbcServIdentEventSuccessTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 5, 1, 8),
    _GgsnApnFbcServIdentEventSuccessTrans_Type()
)
ggsnApnFbcServIdentEventSuccessTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentEventSuccessTrans.setStatus("deprecated")
_GgsnApnFbcServClassStatsTable_Object = MibTable
ggsnApnFbcServClassStatsTable = _GgsnApnFbcServClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6)
)
if mibBuilder.loadTexts:
    ggsnApnFbcServClassStatsTable.setStatus("deprecated")
_GgsnApnFbcServClassStatsEntry_Object = MibTableRow
ggsnApnFbcServClassStatsEntry = _GgsnApnFbcServClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6, 1)
)
ggsnApnFbcServClassStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnServClassIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcServClassStatsEntry.setStatus("deprecated")


class _GgsnServClassIndex_Type(Integer32):
    """Custom type ggsnServClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_GgsnServClassIndex_Type.__name__ = "Integer32"
_GgsnServClassIndex_Object = MibTableColumn
ggsnServClassIndex = _GgsnServClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6, 1, 1),
    _GgsnServClassIndex_Type()
)
ggsnServClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnServClassIndex.setStatus("deprecated")
_GgsnApnFbcServClassUplinkBytes_Type = Counter64
_GgsnApnFbcServClassUplinkBytes_Object = MibTableColumn
ggsnApnFbcServClassUplinkBytes = _GgsnApnFbcServClassUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6, 1, 2),
    _GgsnApnFbcServClassUplinkBytes_Type()
)
ggsnApnFbcServClassUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServClassUplinkBytes.setStatus("deprecated")
_GgsnApnFbcServClassDownlinkBytes_Type = Counter64
_GgsnApnFbcServClassDownlinkBytes_Object = MibTableColumn
ggsnApnFbcServClassDownlinkBytes = _GgsnApnFbcServClassDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6, 1, 4),
    _GgsnApnFbcServClassDownlinkBytes_Type()
)
ggsnApnFbcServClassDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServClassDownlinkBytes.setStatus("deprecated")
_GgsnApnFbcServClassActiveTime_Type = Counter64
_GgsnApnFbcServClassActiveTime_Object = MibTableColumn
ggsnApnFbcServClassActiveTime = _GgsnApnFbcServClassActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 6, 1, 6),
    _GgsnApnFbcServClassActiveTime_Type()
)
ggsnApnFbcServClassActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcServClassActiveTime.setStatus("deprecated")
_GgsnFbcExtPrsUpdReqNoMatch_Type = Counter64
_GgsnFbcExtPrsUpdReqNoMatch_Object = MibScalar
ggsnFbcExtPrsUpdReqNoMatch = _GgsnFbcExtPrsUpdReqNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 7),
    _GgsnFbcExtPrsUpdReqNoMatch_Type()
)
ggsnFbcExtPrsUpdReqNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcExtPrsUpdReqNoMatch.setStatus("deprecated")
_GgsnFbcExtCreditUpdReqNoMatch_Type = Counter64
_GgsnFbcExtCreditUpdReqNoMatch_Object = MibScalar
ggsnFbcExtCreditUpdReqNoMatch = _GgsnFbcExtCreditUpdReqNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 8),
    _GgsnFbcExtCreditUpdReqNoMatch_Type()
)
ggsnFbcExtCreditUpdReqNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcExtCreditUpdReqNoMatch.setStatus("deprecated")
_GgsnFbcExtUpdReqFailure_Type = Counter64
_GgsnFbcExtUpdReqFailure_Object = MibScalar
ggsnFbcExtUpdReqFailure = _GgsnFbcExtUpdReqFailure_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 9),
    _GgsnFbcExtUpdReqFailure_Type()
)
ggsnFbcExtUpdReqFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcExtUpdReqFailure.setStatus("deprecated")
_GgsnApnFbcPrasStatsTable_Object = MibTable
ggsnApnFbcPrasStatsTable = _GgsnApnFbcPrasStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10)
)
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStatsTable.setStatus("current")
_GgsnApnFbcPrasStatsEntry_Object = MibTableRow
ggsnApnFbcPrasStatsEntry = _GgsnApnFbcPrasStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1)
)
ggsnApnFbcPrasStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnPrasIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStatsEntry.setStatus("current")
_GgsnPrasIndex_Type = Integer32
_GgsnPrasIndex_Object = MibTableColumn
ggsnPrasIndex = _GgsnPrasIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 1),
    _GgsnPrasIndex_Type()
)
ggsnPrasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnPrasIndex.setStatus("current")
_GgsnApnFbcPrasName_Type = DisplayString
_GgsnApnFbcPrasName_Object = MibTableColumn
ggsnApnFbcPrasName = _GgsnApnFbcPrasName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 2),
    _GgsnApnFbcPrasName_Type()
)
ggsnApnFbcPrasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasName.setStatus("current")
_GgsnApnFbcPrasStartReq_Type = Counter64
_GgsnApnFbcPrasStartReq_Object = MibTableColumn
ggsnApnFbcPrasStartReq = _GgsnApnFbcPrasStartReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 3),
    _GgsnApnFbcPrasStartReq_Type()
)
ggsnApnFbcPrasStartReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStartReq.setStatus("current")
_GgsnApnFbcPrasStartReqFail_Type = Counter64
_GgsnApnFbcPrasStartReqFail_Object = MibTableColumn
ggsnApnFbcPrasStartReqFail = _GgsnApnFbcPrasStartReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 4),
    _GgsnApnFbcPrasStartReqFail_Type()
)
ggsnApnFbcPrasStartReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStartReqFail.setStatus("current")
_GgsnApnFbcPrasUpdateReq_Type = Counter64
_GgsnApnFbcPrasUpdateReq_Object = MibTableColumn
ggsnApnFbcPrasUpdateReq = _GgsnApnFbcPrasUpdateReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 5),
    _GgsnApnFbcPrasUpdateReq_Type()
)
ggsnApnFbcPrasUpdateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasUpdateReq.setStatus("current")
_GgsnApnFbcPrasUpdateReqFail_Type = Counter64
_GgsnApnFbcPrasUpdateReqFail_Object = MibTableColumn
ggsnApnFbcPrasUpdateReqFail = _GgsnApnFbcPrasUpdateReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 6),
    _GgsnApnFbcPrasUpdateReqFail_Type()
)
ggsnApnFbcPrasUpdateReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasUpdateReqFail.setStatus("current")
_GgsnApnFbcPrasStopReq_Type = Counter64
_GgsnApnFbcPrasStopReq_Object = MibTableColumn
ggsnApnFbcPrasStopReq = _GgsnApnFbcPrasStopReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 7),
    _GgsnApnFbcPrasStopReq_Type()
)
ggsnApnFbcPrasStopReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStopReq.setStatus("current")
_GgsnApnFbcPrasStopReqFail_Type = Counter64
_GgsnApnFbcPrasStopReqFail_Object = MibTableColumn
ggsnApnFbcPrasStopReqFail = _GgsnApnFbcPrasStopReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 8),
    _GgsnApnFbcPrasStopReqFail_Type()
)
ggsnApnFbcPrasStopReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStopReqFail.setStatus("current")
_GgsnApnFbcPrasUserServiceDenied_Type = Counter64
_GgsnApnFbcPrasUserServiceDenied_Object = MibTableColumn
ggsnApnFbcPrasUserServiceDenied = _GgsnApnFbcPrasUserServiceDenied_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 9),
    _GgsnApnFbcPrasUserServiceDenied_Type()
)
ggsnApnFbcPrasUserServiceDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasUserServiceDenied.setStatus("current")
_GgsnApnFbcPrasUserUnknown_Type = Counter64
_GgsnApnFbcPrasUserUnknown_Object = MibTableColumn
ggsnApnFbcPrasUserUnknown = _GgsnApnFbcPrasUserUnknown_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 10, 1, 10),
    _GgsnApnFbcPrasUserUnknown_Type()
)
ggsnApnFbcPrasUserUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcPrasUserUnknown.setStatus("current")
_GgsnApnFbcCcasStatsTable_Object = MibTable
ggsnApnFbcCcasStatsTable = _GgsnApnFbcCcasStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11)
)
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStatsTable.setStatus("current")
_GgsnApnFbcCcasStatsEntry_Object = MibTableRow
ggsnApnFbcCcasStatsEntry = _GgsnApnFbcCcasStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1)
)
ggsnApnFbcCcasStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnCcasIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStatsEntry.setStatus("current")
_GgsnCcasIndex_Type = Integer32
_GgsnCcasIndex_Object = MibTableColumn
ggsnCcasIndex = _GgsnCcasIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 1),
    _GgsnCcasIndex_Type()
)
ggsnCcasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnCcasIndex.setStatus("current")
_GgsnApnFbcCcasName_Type = DisplayString
_GgsnApnFbcCcasName_Object = MibTableColumn
ggsnApnFbcCcasName = _GgsnApnFbcCcasName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 2),
    _GgsnApnFbcCcasName_Type()
)
ggsnApnFbcCcasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasName.setStatus("current")
_GgsnApnFbcCcasStartReq_Type = Counter64
_GgsnApnFbcCcasStartReq_Object = MibTableColumn
ggsnApnFbcCcasStartReq = _GgsnApnFbcCcasStartReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 3),
    _GgsnApnFbcCcasStartReq_Type()
)
ggsnApnFbcCcasStartReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStartReq.setStatus("current")
_GgsnApnFbcCcasStartReqFail_Type = Counter64
_GgsnApnFbcCcasStartReqFail_Object = MibTableColumn
ggsnApnFbcCcasStartReqFail = _GgsnApnFbcCcasStartReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 4),
    _GgsnApnFbcCcasStartReqFail_Type()
)
ggsnApnFbcCcasStartReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStartReqFail.setStatus("current")
_GgsnApnFbcCcasUpdateReq_Type = Counter64
_GgsnApnFbcCcasUpdateReq_Object = MibTableColumn
ggsnApnFbcCcasUpdateReq = _GgsnApnFbcCcasUpdateReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 5),
    _GgsnApnFbcCcasUpdateReq_Type()
)
ggsnApnFbcCcasUpdateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasUpdateReq.setStatus("current")
_GgsnApnFbcCcasUpdateReqFail_Type = Counter64
_GgsnApnFbcCcasUpdateReqFail_Object = MibTableColumn
ggsnApnFbcCcasUpdateReqFail = _GgsnApnFbcCcasUpdateReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 6),
    _GgsnApnFbcCcasUpdateReqFail_Type()
)
ggsnApnFbcCcasUpdateReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasUpdateReqFail.setStatus("current")
_GgsnApnFbcCcasStopReq_Type = Counter64
_GgsnApnFbcCcasStopReq_Object = MibTableColumn
ggsnApnFbcCcasStopReq = _GgsnApnFbcCcasStopReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 7),
    _GgsnApnFbcCcasStopReq_Type()
)
ggsnApnFbcCcasStopReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStopReq.setStatus("current")
_GgsnApnFbcCcasStopReqFail_Type = Counter64
_GgsnApnFbcCcasStopReqFail_Object = MibTableColumn
ggsnApnFbcCcasStopReqFail = _GgsnApnFbcCcasStopReqFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 8),
    _GgsnApnFbcCcasStopReqFail_Type()
)
ggsnApnFbcCcasStopReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStopReqFail.setStatus("current")
_GgsnApnFbcCcasUserServiceDenied_Type = Counter64
_GgsnApnFbcCcasUserServiceDenied_Object = MibTableColumn
ggsnApnFbcCcasUserServiceDenied = _GgsnApnFbcCcasUserServiceDenied_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 9),
    _GgsnApnFbcCcasUserServiceDenied_Type()
)
ggsnApnFbcCcasUserServiceDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasUserServiceDenied.setStatus("current")
_GgsnApnFbcCcasUserUnknown_Type = Counter64
_GgsnApnFbcCcasUserUnknown_Object = MibTableColumn
ggsnApnFbcCcasUserUnknown = _GgsnApnFbcCcasUserUnknown_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 10),
    _GgsnApnFbcCcasUserUnknown_Type()
)
ggsnApnFbcCcasUserUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcCcasUserUnknown.setStatus("current")
_GgsnApnSaccCcasAuthReject_Type = Counter64
_GgsnApnSaccCcasAuthReject_Object = MibTableColumn
ggsnApnSaccCcasAuthReject = _GgsnApnSaccCcasAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 11),
    _GgsnApnSaccCcasAuthReject_Type()
)
ggsnApnSaccCcasAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccCcasAuthReject.setStatus("current")
_GgsnApnSaccCcasCcNotApplicable_Type = Counter64
_GgsnApnSaccCcasCcNotApplicable_Object = MibTableColumn
ggsnApnSaccCcasCcNotApplicable = _GgsnApnSaccCcasCcNotApplicable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 11, 1, 12),
    _GgsnApnSaccCcasCcNotApplicable_Type()
)
ggsnApnSaccCcasCcNotApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccCcasCcNotApplicable.setStatus("current")
_GgsnFbcDiamApplSysStatsTable_Object = MibTable
ggsnFbcDiamApplSysStatsTable = _GgsnFbcDiamApplSysStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 12)
)
if mibBuilder.loadTexts:
    ggsnFbcDiamApplSysStatsTable.setStatus("current")
_GgsnFbcDiamApplSysStatsEntry_Object = MibTableRow
ggsnFbcDiamApplSysStatsEntry = _GgsnFbcDiamApplSysStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 12, 1)
)
ggsnFbcDiamApplSysStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnDiamApplSysIndex"),
)
if mibBuilder.loadTexts:
    ggsnFbcDiamApplSysStatsEntry.setStatus("current")
_GgsnDiamApplSysIndex_Type = Integer32
_GgsnDiamApplSysIndex_Object = MibTableColumn
ggsnDiamApplSysIndex = _GgsnDiamApplSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 12, 1, 1),
    _GgsnDiamApplSysIndex_Type()
)
ggsnDiamApplSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnDiamApplSysIndex.setStatus("current")
_GgsnFbcDiamApplSysName_Type = DisplayString
_GgsnFbcDiamApplSysName_Object = MibTableColumn
ggsnFbcDiamApplSysName = _GgsnFbcDiamApplSysName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 12, 1, 2),
    _GgsnFbcDiamApplSysName_Type()
)
ggsnFbcDiamApplSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcDiamApplSysName.setStatus("current")
_GgsnFbcDiamApplSysReq_Type = Counter64
_GgsnFbcDiamApplSysReq_Object = MibTableColumn
ggsnFbcDiamApplSysReq = _GgsnFbcDiamApplSysReq_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 12, 1, 3),
    _GgsnFbcDiamApplSysReq_Type()
)
ggsnFbcDiamApplSysReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcDiamApplSysReq.setStatus("current")
_GgsnApnFbcRateGroupStatsTable_Object = MibTable
ggsnApnFbcRateGroupStatsTable = _GgsnApnFbcRateGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 13)
)
if mibBuilder.loadTexts:
    ggsnApnFbcRateGroupStatsTable.setStatus("obsolete")
_GgsnApnFbcRateGroupStatsEntry_Object = MibTableRow
ggsnApnFbcRateGroupStatsEntry = _GgsnApnFbcRateGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 13, 1)
)
ggsnApnFbcRateGroupStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnRateGroupIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnFbcRateGroupStatsEntry.setStatus("obsolete")


class _GgsnRateGroupIndex_Type(Integer32):
    """Custom type ggsnRateGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GgsnRateGroupIndex_Type.__name__ = "Integer32"
_GgsnRateGroupIndex_Object = MibTableColumn
ggsnRateGroupIndex = _GgsnRateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 13, 1, 1),
    _GgsnRateGroupIndex_Type()
)
ggsnRateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnRateGroupIndex.setStatus("obsolete")
_GgsnApnFbcRateGroupEventStartTrans_Type = Counter64
_GgsnApnFbcRateGroupEventStartTrans_Object = MibTableColumn
ggsnApnFbcRateGroupEventStartTrans = _GgsnApnFbcRateGroupEventStartTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 13, 1, 2),
    _GgsnApnFbcRateGroupEventStartTrans_Type()
)
ggsnApnFbcRateGroupEventStartTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcRateGroupEventStartTrans.setStatus("obsolete")
_GgsnApnFbcRateGroupEventSuccessTrans_Type = Counter64
_GgsnApnFbcRateGroupEventSuccessTrans_Object = MibTableColumn
ggsnApnFbcRateGroupEventSuccessTrans = _GgsnApnFbcRateGroupEventSuccessTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 13, 1, 3),
    _GgsnApnFbcRateGroupEventSuccessTrans_Type()
)
ggsnApnFbcRateGroupEventSuccessTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnFbcRateGroupEventSuccessTrans.setStatus("obsolete")
_GgsnApnSaccPcrfStatsTable_Object = MibTable
ggsnApnSaccPcrfStatsTable = _GgsnApnSaccPcrfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14)
)
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfStatsTable.setStatus("current")
_GgsnApnSaccPcrfStatsEntry_Object = MibTableRow
ggsnApnSaccPcrfStatsEntry = _GgsnApnSaccPcrfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1)
)
ggsnApnSaccPcrfStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnPcrfIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfStatsEntry.setStatus("current")
_GgsnPcrfIndex_Type = Integer32
_GgsnPcrfIndex_Object = MibTableColumn
ggsnPcrfIndex = _GgsnPcrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 1),
    _GgsnPcrfIndex_Type()
)
ggsnPcrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnPcrfIndex.setStatus("current")
_GgsnApnSaccPcrfName_Type = DisplayString
_GgsnApnSaccPcrfName_Object = MibTableColumn
ggsnApnSaccPcrfName = _GgsnApnSaccPcrfName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 2),
    _GgsnApnSaccPcrfName_Type()
)
ggsnApnSaccPcrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfName.setStatus("current")
_GgsnApnSaccPcrfAuthorFail_Type = Counter64
_GgsnApnSaccPcrfAuthorFail_Object = MibTableColumn
ggsnApnSaccPcrfAuthorFail = _GgsnApnSaccPcrfAuthorFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 3),
    _GgsnApnSaccPcrfAuthorFail_Type()
)
ggsnApnSaccPcrfAuthorFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfAuthorFail.setStatus("current")
_GgsnApnSaccPcrfAuthenFail_Type = Counter64
_GgsnApnSaccPcrfAuthenFail_Object = MibTableColumn
ggsnApnSaccPcrfAuthenFail = _GgsnApnSaccPcrfAuthenFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 4),
    _GgsnApnSaccPcrfAuthenFail_Type()
)
ggsnApnSaccPcrfAuthenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfAuthenFail.setStatus("current")
_GgsnApnSaccPcrfUpdCcReqSessIdNoMatch_Type = Counter64
_GgsnApnSaccPcrfUpdCcReqSessIdNoMatch_Object = MibTableColumn
ggsnApnSaccPcrfUpdCcReqSessIdNoMatch = _GgsnApnSaccPcrfUpdCcReqSessIdNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 5),
    _GgsnApnSaccPcrfUpdCcReqSessIdNoMatch_Type()
)
ggsnApnSaccPcrfUpdCcReqSessIdNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfUpdCcReqSessIdNoMatch.setStatus("current")
_GgsnApnSaccPcrfActivePdpContextUsageReporting_Type = Gauge32
_GgsnApnSaccPcrfActivePdpContextUsageReporting_Object = MibTableColumn
ggsnApnSaccPcrfActivePdpContextUsageReporting = _GgsnApnSaccPcrfActivePdpContextUsageReporting_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 6),
    _GgsnApnSaccPcrfActivePdpContextUsageReporting_Type()
)
ggsnApnSaccPcrfActivePdpContextUsageReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfActivePdpContextUsageReporting.setStatus("current")
_GgsnApnSaccPcrfActiveIPcanSessions_Type = Gauge32
_GgsnApnSaccPcrfActiveIPcanSessions_Object = MibTableColumn
ggsnApnSaccPcrfActiveIPcanSessions = _GgsnApnSaccPcrfActiveIPcanSessions_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 7),
    _GgsnApnSaccPcrfActiveIPcanSessions_Type()
)
ggsnApnSaccPcrfActiveIPcanSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfActiveIPcanSessions.setStatus("current")
_GgsnApnSaccPcrfActiveDedicatedIPcanBearers_Type = Gauge32
_GgsnApnSaccPcrfActiveDedicatedIPcanBearers_Object = MibTableColumn
ggsnApnSaccPcrfActiveDedicatedIPcanBearers = _GgsnApnSaccPcrfActiveDedicatedIPcanBearers_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 14, 1, 8),
    _GgsnApnSaccPcrfActiveDedicatedIPcanBearers_Type()
)
ggsnApnSaccPcrfActiveDedicatedIPcanBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfActiveDedicatedIPcanBearers.setStatus("current")
_GgsnApnSaccRsStatsTable_Object = MibTable
ggsnApnSaccRsStatsTable = _GgsnApnSaccRsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15)
)
if mibBuilder.loadTexts:
    ggsnApnSaccRsStatsTable.setStatus("current")
_GgsnApnSaccRsStatsEntry_Object = MibTableRow
ggsnApnSaccRsStatsEntry = _GgsnApnSaccRsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1)
)
ggsnApnSaccRsStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnRsIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSaccRsStatsEntry.setStatus("current")
_GgsnRsIndex_Type = Integer32
_GgsnRsIndex_Object = MibTableColumn
ggsnRsIndex = _GgsnRsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 1),
    _GgsnRsIndex_Type()
)
ggsnRsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnRsIndex.setStatus("current")
_GgsnApnSaccRsName_Type = DisplayString
_GgsnApnSaccRsName_Object = MibTableColumn
ggsnApnSaccRsName = _GgsnApnSaccRsName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 2),
    _GgsnApnSaccRsName_Type()
)
ggsnApnSaccRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsName.setStatus("current")
_GgsnApnSaccRsUplinkBytes_Type = Counter64
_GgsnApnSaccRsUplinkBytes_Object = MibTableColumn
ggsnApnSaccRsUplinkBytes = _GgsnApnSaccRsUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 3),
    _GgsnApnSaccRsUplinkBytes_Type()
)
ggsnApnSaccRsUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsUplinkBytes.setStatus("current")
_GgsnApnSaccRsDownlinkBytes_Type = Counter64
_GgsnApnSaccRsDownlinkBytes_Object = MibTableColumn
ggsnApnSaccRsDownlinkBytes = _GgsnApnSaccRsDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 4),
    _GgsnApnSaccRsDownlinkBytes_Type()
)
ggsnApnSaccRsDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsDownlinkBytes.setStatus("current")
_GgsnApnSaccRsServiceInstances_Type = Counter64
_GgsnApnSaccRsServiceInstances_Object = MibTableColumn
ggsnApnSaccRsServiceInstances = _GgsnApnSaccRsServiceInstances_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 5),
    _GgsnApnSaccRsServiceInstances_Type()
)
ggsnApnSaccRsServiceInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsServiceInstances.setStatus("deprecated")
_GgsnApnSaccRsAuthDownlinkPacketsDropped_Type = Counter64
_GgsnApnSaccRsAuthDownlinkPacketsDropped_Object = MibTableColumn
ggsnApnSaccRsAuthDownlinkPacketsDropped = _GgsnApnSaccRsAuthDownlinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 6),
    _GgsnApnSaccRsAuthDownlinkPacketsDropped_Type()
)
ggsnApnSaccRsAuthDownlinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsAuthDownlinkPacketsDropped.setStatus("current")
_GgsnApnSaccRsAuthUplinkPacketsDropped_Type = Counter64
_GgsnApnSaccRsAuthUplinkPacketsDropped_Object = MibTableColumn
ggsnApnSaccRsAuthUplinkPacketsDropped = _GgsnApnSaccRsAuthUplinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 7),
    _GgsnApnSaccRsAuthUplinkPacketsDropped_Type()
)
ggsnApnSaccRsAuthUplinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsAuthUplinkPacketsDropped.setStatus("current")
_GgsnApnSaccRsGateDownlinkPacketsDropped_Type = Counter64
_GgsnApnSaccRsGateDownlinkPacketsDropped_Object = MibTableColumn
ggsnApnSaccRsGateDownlinkPacketsDropped = _GgsnApnSaccRsGateDownlinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 8),
    _GgsnApnSaccRsGateDownlinkPacketsDropped_Type()
)
ggsnApnSaccRsGateDownlinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsGateDownlinkPacketsDropped.setStatus("current")
_GgsnApnSaccRsGateUplinkPacketsDropped_Type = Counter64
_GgsnApnSaccRsGateUplinkPacketsDropped_Object = MibTableColumn
ggsnApnSaccRsGateUplinkPacketsDropped = _GgsnApnSaccRsGateUplinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 15, 1, 9),
    _GgsnApnSaccRsGateUplinkPacketsDropped_Type()
)
ggsnApnSaccRsGateUplinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSaccRsGateUplinkPacketsDropped.setStatus("current")
_GgsnApnSacc2ServIdentStatsTable_Object = MibTable
ggsnApnSacc2ServIdentStatsTable = _GgsnApnSacc2ServIdentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16)
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentStatsTable.setStatus("deprecated")
_GgsnApnSacc2ServIdentStatsEntry_Object = MibTableRow
ggsnApnSacc2ServIdentStatsEntry = _GgsnApnSacc2ServIdentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1)
)
ggsnApnSacc2ServIdentStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnSacc2ServIdentIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentStatsEntry.setStatus("deprecated")
_GgsnSacc2ServIdentIndex_Type = Unsigned32
_GgsnSacc2ServIdentIndex_Object = MibTableColumn
ggsnSacc2ServIdentIndex = _GgsnSacc2ServIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 1),
    _GgsnSacc2ServIdentIndex_Type()
)
ggsnSacc2ServIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnSacc2ServIdentIndex.setStatus("deprecated")
_GgsnApnSacc2ServIdentUplinkBytes_Type = Counter64
_GgsnApnSacc2ServIdentUplinkBytes_Object = MibTableColumn
ggsnApnSacc2ServIdentUplinkBytes = _GgsnApnSacc2ServIdentUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 2),
    _GgsnApnSacc2ServIdentUplinkBytes_Type()
)
ggsnApnSacc2ServIdentUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentUplinkBytes.setStatus("deprecated")
_GgsnApnSacc2ServIdentDownlinkBytes_Type = Counter64
_GgsnApnSacc2ServIdentDownlinkBytes_Object = MibTableColumn
ggsnApnSacc2ServIdentDownlinkBytes = _GgsnApnSacc2ServIdentDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 4),
    _GgsnApnSacc2ServIdentDownlinkBytes_Type()
)
ggsnApnSacc2ServIdentDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentDownlinkBytes.setStatus("deprecated")
_GgsnApnSacc2ServIdentEventTrans_Type = Counter64
_GgsnApnSacc2ServIdentEventTrans_Object = MibTableColumn
ggsnApnSacc2ServIdentEventTrans = _GgsnApnSacc2ServIdentEventTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 5),
    _GgsnApnSacc2ServIdentEventTrans_Type()
)
ggsnApnSacc2ServIdentEventTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentEventTrans.setStatus("deprecated")
_GgsnApnSacc2ServIdentEventTransFail_Type = Counter64
_GgsnApnSacc2ServIdentEventTransFail_Object = MibTableColumn
ggsnApnSacc2ServIdentEventTransFail = _GgsnApnSacc2ServIdentEventTransFail_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 6),
    _GgsnApnSacc2ServIdentEventTransFail_Type()
)
ggsnApnSacc2ServIdentEventTransFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentEventTransFail.setStatus("deprecated")
_GgsnApnSacc2ServIdentEventStartTrans_Type = Counter64
_GgsnApnSacc2ServIdentEventStartTrans_Object = MibTableColumn
ggsnApnSacc2ServIdentEventStartTrans = _GgsnApnSacc2ServIdentEventStartTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 7),
    _GgsnApnSacc2ServIdentEventStartTrans_Type()
)
ggsnApnSacc2ServIdentEventStartTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentEventStartTrans.setStatus("deprecated")
_GgsnApnSacc2ServIdentEventSuccessTrans_Type = Counter64
_GgsnApnSacc2ServIdentEventSuccessTrans_Object = MibTableColumn
ggsnApnSacc2ServIdentEventSuccessTrans = _GgsnApnSacc2ServIdentEventSuccessTrans_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 16, 1, 8),
    _GgsnApnSacc2ServIdentEventSuccessTrans_Type()
)
ggsnApnSacc2ServIdentEventSuccessTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentEventSuccessTrans.setStatus("deprecated")
_GgsnApnSacc2ServClassStatsTable_Object = MibTable
ggsnApnSacc2ServClassStatsTable = _GgsnApnSacc2ServClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17)
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassStatsTable.setStatus("deprecated")
_GgsnApnSacc2ServClassStatsEntry_Object = MibTableRow
ggsnApnSacc2ServClassStatsEntry = _GgsnApnSacc2ServClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17, 1)
)
ggsnApnSacc2ServClassStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnSacc2ServClassIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassStatsEntry.setStatus("deprecated")
_GgsnSacc2ServClassIndex_Type = Unsigned32
_GgsnSacc2ServClassIndex_Object = MibTableColumn
ggsnSacc2ServClassIndex = _GgsnSacc2ServClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17, 1, 1),
    _GgsnSacc2ServClassIndex_Type()
)
ggsnSacc2ServClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnSacc2ServClassIndex.setStatus("deprecated")
_GgsnApnSacc2ServClassUplinkBytes_Type = Counter64
_GgsnApnSacc2ServClassUplinkBytes_Object = MibTableColumn
ggsnApnSacc2ServClassUplinkBytes = _GgsnApnSacc2ServClassUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17, 1, 2),
    _GgsnApnSacc2ServClassUplinkBytes_Type()
)
ggsnApnSacc2ServClassUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassUplinkBytes.setStatus("deprecated")
_GgsnApnSacc2ServClassDownlinkBytes_Type = Counter64
_GgsnApnSacc2ServClassDownlinkBytes_Object = MibTableColumn
ggsnApnSacc2ServClassDownlinkBytes = _GgsnApnSacc2ServClassDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17, 1, 4),
    _GgsnApnSacc2ServClassDownlinkBytes_Type()
)
ggsnApnSacc2ServClassDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassDownlinkBytes.setStatus("deprecated")
_GgsnApnSacc2ServClassActiveTime_Type = Counter64
_GgsnApnSacc2ServClassActiveTime_Object = MibTableColumn
ggsnApnSacc2ServClassActiveTime = _GgsnApnSacc2ServClassActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 17, 1, 6),
    _GgsnApnSacc2ServClassActiveTime_Type()
)
ggsnApnSacc2ServClassActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassActiveTime.setStatus("deprecated")
_GgsnApnSacc3ServIdentStatsTable_Object = MibTable
ggsnApnSacc3ServIdentStatsTable = _GgsnApnSacc3ServIdentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 18)
)
if mibBuilder.loadTexts:
    ggsnApnSacc3ServIdentStatsTable.setStatus("deprecated")
_GgsnApnSacc3ServIdentStatsEntry_Object = MibTableRow
ggsnApnSacc3ServIdentStatsEntry = _GgsnApnSacc3ServIdentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 18, 1)
)
ggsnApnSacc3ServIdentStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnSacc3ServIdentIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSacc3ServIdentStatsEntry.setStatus("deprecated")
_GgsnSacc3ServIdentIndex_Type = Unsigned32
_GgsnSacc3ServIdentIndex_Object = MibTableColumn
ggsnSacc3ServIdentIndex = _GgsnSacc3ServIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 18, 1, 1),
    _GgsnSacc3ServIdentIndex_Type()
)
ggsnSacc3ServIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnSacc3ServIdentIndex.setStatus("deprecated")
_GgsnApnSacc3ServIdentUplinkBytes_Type = Counter64
_GgsnApnSacc3ServIdentUplinkBytes_Object = MibTableColumn
ggsnApnSacc3ServIdentUplinkBytes = _GgsnApnSacc3ServIdentUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 18, 1, 2),
    _GgsnApnSacc3ServIdentUplinkBytes_Type()
)
ggsnApnSacc3ServIdentUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc3ServIdentUplinkBytes.setStatus("deprecated")
_GgsnApnSacc3ServIdentDownlinkBytes_Type = Counter64
_GgsnApnSacc3ServIdentDownlinkBytes_Object = MibTableColumn
ggsnApnSacc3ServIdentDownlinkBytes = _GgsnApnSacc3ServIdentDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 18, 1, 4),
    _GgsnApnSacc3ServIdentDownlinkBytes_Type()
)
ggsnApnSacc3ServIdentDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc3ServIdentDownlinkBytes.setStatus("deprecated")
_GgsnApnSacc3RatingGroupStatsTable_Object = MibTable
ggsnApnSacc3RatingGroupStatsTable = _GgsnApnSacc3RatingGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 19)
)
if mibBuilder.loadTexts:
    ggsnApnSacc3RatingGroupStatsTable.setStatus("deprecated")
_GgsnApnSacc3RatingGroupStatsEntry_Object = MibTableRow
ggsnApnSacc3RatingGroupStatsEntry = _GgsnApnSacc3RatingGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 19, 1)
)
ggsnApnSacc3RatingGroupStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnRatingGroupIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnSacc3RatingGroupStatsEntry.setStatus("deprecated")
_GgsnRatingGroupIndex_Type = Unsigned32
_GgsnRatingGroupIndex_Object = MibTableColumn
ggsnRatingGroupIndex = _GgsnRatingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 19, 1, 1),
    _GgsnRatingGroupIndex_Type()
)
ggsnRatingGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnRatingGroupIndex.setStatus("deprecated")
_GgsnApnSacc3RatingGroupUplinkBytes_Type = Counter64
_GgsnApnSacc3RatingGroupUplinkBytes_Object = MibTableColumn
ggsnApnSacc3RatingGroupUplinkBytes = _GgsnApnSacc3RatingGroupUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 19, 1, 2),
    _GgsnApnSacc3RatingGroupUplinkBytes_Type()
)
ggsnApnSacc3RatingGroupUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc3RatingGroupUplinkBytes.setStatus("deprecated")
_GgsnApnSacc3RatingGroupDownlinkBytes_Type = Counter64
_GgsnApnSacc3RatingGroupDownlinkBytes_Object = MibTableColumn
ggsnApnSacc3RatingGroupDownlinkBytes = _GgsnApnSacc3RatingGroupDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 19, 1, 3),
    _GgsnApnSacc3RatingGroupDownlinkBytes_Type()
)
ggsnApnSacc3RatingGroupDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnSacc3RatingGroupDownlinkBytes.setStatus("deprecated")
_PgwApnSaccRatingGroupStatsTable_Object = MibTable
pgwApnSaccRatingGroupStatsTable = _PgwApnSaccRatingGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 20)
)
if mibBuilder.loadTexts:
    pgwApnSaccRatingGroupStatsTable.setStatus("current")
_PgwApnSaccRatingGroupStatsEntry_Object = MibTableRow
pgwApnSaccRatingGroupStatsEntry = _PgwApnSaccRatingGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 20, 1)
)
pgwApnSaccRatingGroupStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtpuIndex"),
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "pgwRatingGroupIndex"),
)
if mibBuilder.loadTexts:
    pgwApnSaccRatingGroupStatsEntry.setStatus("current")
_PgwRatingGroupIndex_Type = Unsigned32
_PgwRatingGroupIndex_Object = MibTableColumn
pgwRatingGroupIndex = _PgwRatingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 20, 1, 1),
    _PgwRatingGroupIndex_Type()
)
pgwRatingGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgwRatingGroupIndex.setStatus("current")
_PgwApnSaccRatingGroupUplinkBytes_Type = Counter64
_PgwApnSaccRatingGroupUplinkBytes_Object = MibTableColumn
pgwApnSaccRatingGroupUplinkBytes = _PgwApnSaccRatingGroupUplinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 20, 1, 2),
    _PgwApnSaccRatingGroupUplinkBytes_Type()
)
pgwApnSaccRatingGroupUplinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnSaccRatingGroupUplinkBytes.setStatus("current")
_PgwApnSaccRatingGroupDownlinkBytes_Type = Counter64
_PgwApnSaccRatingGroupDownlinkBytes_Object = MibTableColumn
pgwApnSaccRatingGroupDownlinkBytes = _PgwApnSaccRatingGroupDownlinkBytes_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 1, 20, 1, 3),
    _PgwApnSaccRatingGroupDownlinkBytes_Type()
)
pgwApnSaccRatingGroupDownlinkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwApnSaccRatingGroupDownlinkBytes.setStatus("current")
_GgsnFbcAuthorizationStats_ObjectIdentity = ObjectIdentity
ggsnFbcAuthorizationStats = _GgsnFbcAuthorizationStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2)
)
_GgsnFbcAuthStats_ObjectIdentity = ObjectIdentity
ggsnFbcAuthStats = _GgsnFbcAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1)
)
_GgsnFbcUserAuthPacketsDropped_Type = Counter64
_GgsnFbcUserAuthPacketsDropped_Object = MibScalar
ggsnFbcUserAuthPacketsDropped = _GgsnFbcUserAuthPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1, 2),
    _GgsnFbcUserAuthPacketsDropped_Type()
)
ggsnFbcUserAuthPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcUserAuthPacketsDropped.setStatus("deprecated")
_GgsnFbcDefaultAuthPacketsDropped_Type = Counter64
_GgsnFbcDefaultAuthPacketsDropped_Object = MibScalar
ggsnFbcDefaultAuthPacketsDropped = _GgsnFbcDefaultAuthPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1, 3),
    _GgsnFbcDefaultAuthPacketsDropped_Type()
)
ggsnFbcDefaultAuthPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcDefaultAuthPacketsDropped.setStatus("deprecated")
_GgsnFbcEmptyBucketPacketsDropped_Type = Counter64
_GgsnFbcEmptyBucketPacketsDropped_Object = MibScalar
ggsnFbcEmptyBucketPacketsDropped = _GgsnFbcEmptyBucketPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1, 4),
    _GgsnFbcEmptyBucketPacketsDropped_Type()
)
ggsnFbcEmptyBucketPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcEmptyBucketPacketsDropped.setStatus("deprecated")
_GgsnFbcComFailAuthPacketsDropped_Type = Counter64
_GgsnFbcComFailAuthPacketsDropped_Object = MibScalar
ggsnFbcComFailAuthPacketsDropped = _GgsnFbcComFailAuthPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1, 5),
    _GgsnFbcComFailAuthPacketsDropped_Type()
)
ggsnFbcComFailAuthPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcComFailAuthPacketsDropped.setStatus("deprecated")
_GgsnFbcIdentErrorPacketsDropped_Type = Counter64
_GgsnFbcIdentErrorPacketsDropped_Object = MibScalar
ggsnFbcIdentErrorPacketsDropped = _GgsnFbcIdentErrorPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 7, 2, 1, 6),
    _GgsnFbcIdentErrorPacketsDropped_Type()
)
ggsnFbcIdentErrorPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnFbcIdentErrorPacketsDropped.setStatus("deprecated")
_GgsnMbmsInfo_ObjectIdentity = ObjectIdentity
ggsnMbmsInfo = _GgsnMbmsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8)
)
_GgsnMbmsGmbSessionStartAttempts_Type = Counter64
_GgsnMbmsGmbSessionStartAttempts_Object = MibScalar
ggsnMbmsGmbSessionStartAttempts = _GgsnMbmsGmbSessionStartAttempts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 1),
    _GgsnMbmsGmbSessionStartAttempts_Type()
)
ggsnMbmsGmbSessionStartAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsGmbSessionStartAttempts.setStatus("current")
_GgsnMbmsGmbSessionStartFailures_Type = Counter64
_GgsnMbmsGmbSessionStartFailures_Object = MibScalar
ggsnMbmsGmbSessionStartFailures = _GgsnMbmsGmbSessionStartFailures_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 2),
    _GgsnMbmsGmbSessionStartFailures_Type()
)
ggsnMbmsGmbSessionStartFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsGmbSessionStartFailures.setStatus("current")
_GgsnMbmsCurrentNbrOfSessions_Type = Gauge32
_GgsnMbmsCurrentNbrOfSessions_Object = MibScalar
ggsnMbmsCurrentNbrOfSessions = _GgsnMbmsCurrentNbrOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 3),
    _GgsnMbmsCurrentNbrOfSessions_Type()
)
ggsnMbmsCurrentNbrOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsCurrentNbrOfSessions.setStatus("current")
_GgsnMbmsCurrentAggregatedMbr_Type = Gauge32
_GgsnMbmsCurrentAggregatedMbr_Object = MibScalar
ggsnMbmsCurrentAggregatedMbr = _GgsnMbmsCurrentAggregatedMbr_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 4),
    _GgsnMbmsCurrentAggregatedMbr_Type()
)
ggsnMbmsCurrentAggregatedMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsCurrentAggregatedMbr.setStatus("current")
_GgsnMbmsGiIncomingPackets_Type = Counter64
_GgsnMbmsGiIncomingPackets_Object = MibScalar
ggsnMbmsGiIncomingPackets = _GgsnMbmsGiIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 5),
    _GgsnMbmsGiIncomingPackets_Type()
)
ggsnMbmsGiIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsGiIncomingPackets.setStatus("current")
_GgsnMbmsDiscardedPackets_Type = Counter64
_GgsnMbmsDiscardedPackets_Object = MibScalar
ggsnMbmsDiscardedPackets = _GgsnMbmsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 6),
    _GgsnMbmsDiscardedPackets_Type()
)
ggsnMbmsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsDiscardedPackets.setStatus("current")
_GgsnMbmsSgsnUserPlaneTable_Object = MibTable
ggsnMbmsSgsnUserPlaneTable = _GgsnMbmsSgsnUserPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 7)
)
if mibBuilder.loadTexts:
    ggsnMbmsSgsnUserPlaneTable.setStatus("deprecated")
_GgsnMbmsSgsnUserPlaneEntry_Object = MibTableRow
ggsnMbmsSgsnUserPlaneEntry = _GgsnMbmsSgsnUserPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 7, 1)
)
ggsnMbmsSgsnUserPlaneEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnMbmsSgsnUIndex"),
)
if mibBuilder.loadTexts:
    ggsnMbmsSgsnUserPlaneEntry.setStatus("deprecated")


class _GgsnMbmsSgsnUIndex_Type(Integer32):
    """Custom type ggsnMbmsSgsnUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnMbmsSgsnUIndex_Type.__name__ = "Integer32"
_GgsnMbmsSgsnUIndex_Object = MibTableColumn
ggsnMbmsSgsnUIndex = _GgsnMbmsSgsnUIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 7, 1, 1),
    _GgsnMbmsSgsnUIndex_Type()
)
ggsnMbmsSgsnUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnMbmsSgsnUIndex.setStatus("deprecated")
_GgsnMbmsSgsnUAddress_Type = IpAddress
_GgsnMbmsSgsnUAddress_Object = MibTableColumn
ggsnMbmsSgsnUAddress = _GgsnMbmsSgsnUAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 7, 1, 2),
    _GgsnMbmsSgsnUAddress_Type()
)
ggsnMbmsSgsnUAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsSgsnUAddress.setStatus("deprecated")
_GgsnMbmsSgsnForwardedPackets_Type = Counter64
_GgsnMbmsSgsnForwardedPackets_Object = MibTableColumn
ggsnMbmsSgsnForwardedPackets = _GgsnMbmsSgsnForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 7, 1, 3),
    _GgsnMbmsSgsnForwardedPackets_Type()
)
ggsnMbmsSgsnForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsSgsnForwardedPackets.setStatus("deprecated")
_GgsnMbmsSgsnControlPlaneTable_Object = MibTable
ggsnMbmsSgsnControlPlaneTable = _GgsnMbmsSgsnControlPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8)
)
if mibBuilder.loadTexts:
    ggsnMbmsSgsnControlPlaneTable.setStatus("current")
_GgsnMbmsSgsnControlPlaneEntry_Object = MibTableRow
ggsnMbmsSgsnControlPlaneEntry = _GgsnMbmsSgsnControlPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8, 1)
)
ggsnMbmsSgsnControlPlaneEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnMbmsSgsnCIndex"),
)
if mibBuilder.loadTexts:
    ggsnMbmsSgsnControlPlaneEntry.setStatus("current")


class _GgsnMbmsSgsnCIndex_Type(Integer32):
    """Custom type ggsnMbmsSgsnCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnMbmsSgsnCIndex_Type.__name__ = "Integer32"
_GgsnMbmsSgsnCIndex_Object = MibTableColumn
ggsnMbmsSgsnCIndex = _GgsnMbmsSgsnCIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8, 1, 1),
    _GgsnMbmsSgsnCIndex_Type()
)
ggsnMbmsSgsnCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnMbmsSgsnCIndex.setStatus("current")
_GgsnMbmsSgsnCAddress_Type = IpAddress
_GgsnMbmsSgsnCAddress_Object = MibTableColumn
ggsnMbmsSgsnCAddress = _GgsnMbmsSgsnCAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8, 1, 2),
    _GgsnMbmsSgsnCAddress_Type()
)
ggsnMbmsSgsnCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsSgsnCAddress.setStatus("current")
_GgsnMbmsGnSessionStartAttempts_Type = Counter64
_GgsnMbmsGnSessionStartAttempts_Object = MibTableColumn
ggsnMbmsGnSessionStartAttempts = _GgsnMbmsGnSessionStartAttempts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8, 1, 3),
    _GgsnMbmsGnSessionStartAttempts_Type()
)
ggsnMbmsGnSessionStartAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsGnSessionStartAttempts.setStatus("current")
_GgsnMbmsGnSessionStartFailures_Type = Counter64
_GgsnMbmsGnSessionStartFailures_Object = MibTableColumn
ggsnMbmsGnSessionStartFailures = _GgsnMbmsGnSessionStartFailures_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 8, 8, 1, 4),
    _GgsnMbmsGnSessionStartFailures_Type()
)
ggsnMbmsGnSessionStartFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnMbmsGnSessionStartFailures.setStatus("current")
_GgsnGtptInfo_ObjectIdentity = ObjectIdentity
ggsnGtptInfo = _GgsnGtptInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9)
)
_GgsnGtptTable_Object = MibTable
ggsnGtptTable = _GgsnGtptTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ggsnGtptTable.setStatus("deprecated")
_GgsnGtptEntry_Object = MibTableRow
ggsnGtptEntry = _GgsnGtptEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1)
)
ggsnGtptEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnGtptIndex"),
)
if mibBuilder.loadTexts:
    ggsnGtptEntry.setStatus("deprecated")


class _GgsnGtptIndex_Type(Integer32):
    """Custom type ggsnGtptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GgsnGtptIndex_Type.__name__ = "Integer32"
_GgsnGtptIndex_Object = MibTableColumn
ggsnGtptIndex = _GgsnGtptIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 1),
    _GgsnGtptIndex_Type()
)
ggsnGtptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnGtptIndex.setStatus("deprecated")
_GgsnGtptVersion_Type = DisplayString
_GgsnGtptVersion_Object = MibTableColumn
ggsnGtptVersion = _GgsnGtptVersion_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 2),
    _GgsnGtptVersion_Type()
)
ggsnGtptVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptVersion.setStatus("deprecated")
_GgsnGtptAddress_Type = IpAddress
_GgsnGtptAddress_Object = MibTableColumn
ggsnGtptAddress = _GgsnGtptAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 3),
    _GgsnGtptAddress_Type()
)
ggsnGtptAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptAddress.setStatus("deprecated")
_GgsnGtptCapacity_Type = Integer32
_GgsnGtptCapacity_Object = MibTableColumn
ggsnGtptCapacity = _GgsnGtptCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 4),
    _GgsnGtptCapacity_Type()
)
ggsnGtptCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptCapacity.setStatus("deprecated")


class _GgsnGtptRole_Type(Integer32):
    """Custom type ggsnGtptRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("standby", 4))
    )


_GgsnGtptRole_Type.__name__ = "Integer32"
_GgsnGtptRole_Object = MibTableColumn
ggsnGtptRole = _GgsnGtptRole_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 5),
    _GgsnGtptRole_Type()
)
ggsnGtptRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptRole.setStatus("deprecated")
_GgsnGtptStatus_Type = DisplayString
_GgsnGtptStatus_Object = MibTableColumn
ggsnGtptStatus = _GgsnGtptStatus_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 6),
    _GgsnGtptStatus_Type()
)
ggsnGtptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptStatus.setStatus("deprecated")
_GgsnGtptMemory_Type = Integer32
_GgsnGtptMemory_Object = MibTableColumn
ggsnGtptMemory = _GgsnGtptMemory_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 7),
    _GgsnGtptMemory_Type()
)
ggsnGtptMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptMemory.setStatus("deprecated")
_GgsnGtptMemoryUsed_Type = Integer32
_GgsnGtptMemoryUsed_Object = MibTableColumn
ggsnGtptMemoryUsed = _GgsnGtptMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 8),
    _GgsnGtptMemoryUsed_Type()
)
ggsnGtptMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptMemoryUsed.setStatus("deprecated")
_GgsnGtptCpuUsage_Type = Gauge32
_GgsnGtptCpuUsage_Object = MibTableColumn
ggsnGtptCpuUsage = _GgsnGtptCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 9),
    _GgsnGtptCpuUsage_Type()
)
ggsnGtptCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptCpuUsage.setStatus("deprecated")
_GgsnGtptPeakCpuUsage_Type = Gauge32
_GgsnGtptPeakCpuUsage_Object = MibTableColumn
ggsnGtptPeakCpuUsage = _GgsnGtptPeakCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 9, 1, 1, 10),
    _GgsnGtptPeakCpuUsage_Type()
)
ggsnGtptPeakCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnGtptPeakCpuUsage.setStatus("deprecated")
_GgsnRadiusInfo_ObjectIdentity = ObjectIdentity
ggsnRadiusInfo = _GgsnRadiusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10)
)
_GgsnApnRadiusAuthServersStatsTable_Object = MibTable
ggsnApnRadiusAuthServersStatsTable = _GgsnApnRadiusAuthServersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServersStatsTable.setStatus("current")
_GgsnApnRadiusAuthServersStatsEntry_Object = MibTableRow
ggsnApnRadiusAuthServersStatsEntry = _GgsnApnRadiusAuthServersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1)
)
ggsnApnRadiusAuthServersStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnApnRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServersStatsEntry.setStatus("current")


class _GgsnApnRadiusAuthServerIndex_Type(Integer32):
    """Custom type ggsnApnRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnApnRadiusAuthServerIndex_Type.__name__ = "Integer32"
_GgsnApnRadiusAuthServerIndex_Object = MibTableColumn
ggsnApnRadiusAuthServerIndex = _GgsnApnRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 1),
    _GgsnApnRadiusAuthServerIndex_Type()
)
ggsnApnRadiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerIndex.setStatus("current")
_GgsnApnRadiusAuthServerIpAddress_Type = IpAddress
_GgsnApnRadiusAuthServerIpAddress_Object = MibTableColumn
ggsnApnRadiusAuthServerIpAddress = _GgsnApnRadiusAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 2),
    _GgsnApnRadiusAuthServerIpAddress_Type()
)
ggsnApnRadiusAuthServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerIpAddress.setStatus("current")
_GgsnApnRadiusAuthServerAccessRequests_Type = Counter64
_GgsnApnRadiusAuthServerAccessRequests_Object = MibTableColumn
ggsnApnRadiusAuthServerAccessRequests = _GgsnApnRadiusAuthServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 3),
    _GgsnApnRadiusAuthServerAccessRequests_Type()
)
ggsnApnRadiusAuthServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerAccessRequests.setStatus("current")
_GgsnApnRadiusAuthServerAccessAccepts_Type = Counter64
_GgsnApnRadiusAuthServerAccessAccepts_Object = MibTableColumn
ggsnApnRadiusAuthServerAccessAccepts = _GgsnApnRadiusAuthServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 4),
    _GgsnApnRadiusAuthServerAccessAccepts_Type()
)
ggsnApnRadiusAuthServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerAccessAccepts.setStatus("current")
_GgsnApnRadiusAuthServerAccessRejects_Type = Counter64
_GgsnApnRadiusAuthServerAccessRejects_Object = MibTableColumn
ggsnApnRadiusAuthServerAccessRejects = _GgsnApnRadiusAuthServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 5),
    _GgsnApnRadiusAuthServerAccessRejects_Type()
)
ggsnApnRadiusAuthServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerAccessRejects.setStatus("current")
_GgsnApnRadiusAuthServerAccessRequestTimeouts_Type = Counter64
_GgsnApnRadiusAuthServerAccessRequestTimeouts_Object = MibTableColumn
ggsnApnRadiusAuthServerAccessRequestTimeouts = _GgsnApnRadiusAuthServerAccessRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 6),
    _GgsnApnRadiusAuthServerAccessRequestTimeouts_Type()
)
ggsnApnRadiusAuthServerAccessRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerAccessRequestTimeouts.setStatus("current")
_GgsnApnRadiusAuthServerAccessRequestRetransmits_Type = Counter64
_GgsnApnRadiusAuthServerAccessRequestRetransmits_Object = MibTableColumn
ggsnApnRadiusAuthServerAccessRequestRetransmits = _GgsnApnRadiusAuthServerAccessRequestRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 7),
    _GgsnApnRadiusAuthServerAccessRequestRetransmits_Type()
)
ggsnApnRadiusAuthServerAccessRequestRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerAccessRequestRetransmits.setStatus("current")
_GgsnApnRadiusAuthServerInvalidAuthenticators_Type = Counter64
_GgsnApnRadiusAuthServerInvalidAuthenticators_Object = MibTableColumn
ggsnApnRadiusAuthServerInvalidAuthenticators = _GgsnApnRadiusAuthServerInvalidAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 1, 1, 8),
    _GgsnApnRadiusAuthServerInvalidAuthenticators_Type()
)
ggsnApnRadiusAuthServerInvalidAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAuthServerInvalidAuthenticators.setStatus("current")
_GgsnApnRadiusAcctServersStatsTable_Object = MibTable
ggsnApnRadiusAcctServersStatsTable = _GgsnApnRadiusAcctServersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServersStatsTable.setStatus("current")
_GgsnApnRadiusAcctServersStatsEntry_Object = MibTableRow
ggsnApnRadiusAcctServersStatsEntry = _GgsnApnRadiusAcctServersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1)
)
ggsnApnRadiusAcctServersStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "ggsnApnIndex"),
    (0, "GGSN-MIB", "ggsnApnRadiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServersStatsEntry.setStatus("current")


class _GgsnApnRadiusAcctServerIndex_Type(Integer32):
    """Custom type ggsnApnRadiusAcctServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GgsnApnRadiusAcctServerIndex_Type.__name__ = "Integer32"
_GgsnApnRadiusAcctServerIndex_Object = MibTableColumn
ggsnApnRadiusAcctServerIndex = _GgsnApnRadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 1),
    _GgsnApnRadiusAcctServerIndex_Type()
)
ggsnApnRadiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerIndex.setStatus("current")
_GgsnApnRadiusAcctServerIpAddress_Type = IpAddress
_GgsnApnRadiusAcctServerIpAddress_Object = MibTableColumn
ggsnApnRadiusAcctServerIpAddress = _GgsnApnRadiusAcctServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 2),
    _GgsnApnRadiusAcctServerIpAddress_Type()
)
ggsnApnRadiusAcctServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerIpAddress.setStatus("current")
_GgsnApnRadiusAcctServerAccountingRequests_Type = Counter64
_GgsnApnRadiusAcctServerAccountingRequests_Object = MibTableColumn
ggsnApnRadiusAcctServerAccountingRequests = _GgsnApnRadiusAcctServerAccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 3),
    _GgsnApnRadiusAcctServerAccountingRequests_Type()
)
ggsnApnRadiusAcctServerAccountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerAccountingRequests.setStatus("current")
_GgsnApnRadiusAcctServerAccountingResponses_Type = Counter64
_GgsnApnRadiusAcctServerAccountingResponses_Object = MibTableColumn
ggsnApnRadiusAcctServerAccountingResponses = _GgsnApnRadiusAcctServerAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 4),
    _GgsnApnRadiusAcctServerAccountingResponses_Type()
)
ggsnApnRadiusAcctServerAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerAccountingResponses.setStatus("current")
_GgsnApnRadiusAcctServerAccountingRequestTimeouts_Type = Counter64
_GgsnApnRadiusAcctServerAccountingRequestTimeouts_Object = MibTableColumn
ggsnApnRadiusAcctServerAccountingRequestTimeouts = _GgsnApnRadiusAcctServerAccountingRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 5),
    _GgsnApnRadiusAcctServerAccountingRequestTimeouts_Type()
)
ggsnApnRadiusAcctServerAccountingRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerAccountingRequestTimeouts.setStatus("current")
_GgsnApnRadiusAcctServerAccountingRequestRetransmits_Type = Counter64
_GgsnApnRadiusAcctServerAccountingRequestRetransmits_Object = MibTableColumn
ggsnApnRadiusAcctServerAccountingRequestRetransmits = _GgsnApnRadiusAcctServerAccountingRequestRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 6),
    _GgsnApnRadiusAcctServerAccountingRequestRetransmits_Type()
)
ggsnApnRadiusAcctServerAccountingRequestRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerAccountingRequestRetransmits.setStatus("current")
_GgsnApnRadiusAcctServerInvalidAuthenticators_Type = Counter64
_GgsnApnRadiusAcctServerInvalidAuthenticators_Object = MibTableColumn
ggsnApnRadiusAcctServerInvalidAuthenticators = _GgsnApnRadiusAcctServerInvalidAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 10, 2, 1, 7),
    _GgsnApnRadiusAcctServerInvalidAuthenticators_Type()
)
ggsnApnRadiusAcctServerInvalidAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ggsnApnRadiusAcctServerInvalidAuthenticators.setStatus("current")
_PgwSharedIpPoolStatsTable_Object = MibTable
pgwSharedIpPoolStatsTable = _PgwSharedIpPoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pgwSharedIpPoolStatsTable.setStatus("current")
_PgwSharedIpPoolStatsEntry_Object = MibTableRow
pgwSharedIpPoolStatsEntry = _PgwSharedIpPoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11, 1)
)
pgwSharedIpPoolStatsEntry.setIndexNames(
    (0, "GGSN-MIB", "pgwSharedIpPoolIndex"),
)
if mibBuilder.loadTexts:
    pgwSharedIpPoolStatsEntry.setStatus("current")


class _PgwSharedIpPoolIndex_Type(Integer32):
    """Custom type pgwSharedIpPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PgwSharedIpPoolIndex_Type.__name__ = "Integer32"
_PgwSharedIpPoolIndex_Object = MibTableColumn
pgwSharedIpPoolIndex = _PgwSharedIpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11, 1, 1),
    _PgwSharedIpPoolIndex_Type()
)
pgwSharedIpPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgwSharedIpPoolIndex.setStatus("current")
_PgwSharedIpPoolName_Type = DisplayString
_PgwSharedIpPoolName_Object = MibTableColumn
pgwSharedIpPoolName = _PgwSharedIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11, 1, 2),
    _PgwSharedIpPoolName_Type()
)
pgwSharedIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwSharedIpPoolName.setStatus("current")
_PgwAvailableAddressesInSharedIpPool_Type = Gauge32
_PgwAvailableAddressesInSharedIpPool_Object = MibTableColumn
pgwAvailableAddressesInSharedIpPool = _PgwAvailableAddressesInSharedIpPool_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11, 1, 3),
    _PgwAvailableAddressesInSharedIpPool_Type()
)
pgwAvailableAddressesInSharedIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAvailableAddressesInSharedIpPool.setStatus("current")
_PgwAddressesInQuarantineInSharedIpPool_Type = Gauge32
_PgwAddressesInQuarantineInSharedIpPool_Object = MibTableColumn
pgwAddressesInQuarantineInSharedIpPool = _PgwAddressesInQuarantineInSharedIpPool_Object(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 1, 11, 1, 4),
    _PgwAddressesInQuarantineInSharedIpPool_Type()
)
pgwAddressesInQuarantineInSharedIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgwAddressesInQuarantineInSharedIpPool.setStatus("current")
_GgsnMIBConformance_ObjectIdentity = ObjectIdentity
ggsnMIBConformance = _GgsnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2)
)
_GgsnMIBCompliances_ObjectIdentity = ObjectIdentity
ggsnMIBCompliances = _GgsnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 1)
)
_GgsnMIBGroups_ObjectIdentity = ObjectIdentity
ggsnMIBGroups = _GgsnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2)
)
_GgsnTraps_ObjectIdentity = ObjectIdentity
ggsnTraps = _GgsnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 2)
)

# Managed Objects groups

ggsnSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 1)
)
ggsnSystemGroup.setObjects(
      *(("GGSN-MIB", "ggsnVersion"),
        ("GGSN-MIB", "ggsnInstalled"),
        ("GGSN-MIB", "ggsnGtpcVersion"),
        ("GGSN-MIB", "ggsnGtpcAddress"),
        ("GGSN-MIB", "ggsnGtpcPdpCapacity"),
        ("GGSN-MIB", "ggsnGtpcRole"),
        ("GGSN-MIB", "ggsnGtpcStatus"),
        ("GGSN-MIB", "ggsnGtpcControlPacketDrops"),
        ("GGSN-MIB", "ggsnGtpcNbrOfActivePdpContexts"),
        ("GGSN-MIB", "ggsnGtpcMemory"),
        ("GGSN-MIB", "ggsnGtpcMemoryUsed"),
        ("GGSN-MIB", "ggsnGtpcCpuUsage"),
        ("GGSN-MIB", "ggsnGtpcTftFilterDepthMax"),
        ("GGSN-MIB", "ggsnGtpcTftFilterDepthMean"),
        ("GGSN-MIB", "ggsnGtpcControlLoad"),
        ("GGSN-MIB", "ggsnGtpuVersion"),
        ("GGSN-MIB", "ggsnGtpuAddress"),
        ("GGSN-MIB", "ggsnGtpuPdpCapacity"),
        ("GGSN-MIB", "ggsnGtpuRole"),
        ("GGSN-MIB", "ggsnGtpuStatus"),
        ("GGSN-MIB", "ggsnGtpuUserUplinkDrops"),
        ("GGSN-MIB", "ggsnGtpuUserDownlinkDrops"),
        ("GGSN-MIB", "ggsnGtpuNbrOfActivePdpContexts"),
        ("GGSN-MIB", "ggsnGtpuMemory"),
        ("GGSN-MIB", "ggsnGtpuMemoryUsed"),
        ("GGSN-MIB", "ggsnGtpuCpuUsage"),
        ("GGSN-MIB", "ggsnGtpuPayloadLoad"),
        ("GGSN-MIB", "ggsnGtpuNbrOfActivePdpContextsIpv6"),
        ("GGSN-MIB", "ggsnGtpuNbrOfActivePdpContextsIpv4v6"),
        ("GGSN-MIB", "ggsnGtpcNbrOfActivePdpContextsIpv6"),
        ("GGSN-MIB", "ggsnGtpcNbrOfActivePdpContextsIpv4v6"),
        ("GGSN-MIB", "ggsnGtpuUplinkPackets"),
        ("GGSN-MIB", "ggsnGtpuDownlinkPackets"))
)
if mibBuilder.loadTexts:
    ggsnSystemGroup.setStatus("current")

ggsnGlobalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 2)
)
ggsnGlobalStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnStatReportTime"),
        ("GGSN-MIB", "ggsnNbrOfActivePdpContexts"),
        ("GGSN-MIB", "ggsnNbrOfSubscribers"),
        ("GGSN-MIB", "ggsnNbrOfSubscribersMean"),
        ("GGSN-MIB", "ggsnNbrOfTftFilters"),
        ("GGSN-MIB", "ggsnControlLoad"),
        ("GGSN-MIB", "ggsnPayloadLoad"),
        ("GGSN-MIB", "ggsnAttemptedActivation"),
        ("GGSN-MIB", "ggsnAttemptedDeactivation"),
        ("GGSN-MIB", "ggsnAttemptedSelfDeactivation"),
        ("GGSN-MIB", "ggsnAttemptedUpdate"),
        ("GGSN-MIB", "ggsnAttemptedManualDeactivation"),
        ("GGSN-MIB", "ggsnAttemptedSecondaryActivation"),
        ("GGSN-MIB", "ggsnCompletedActivation"),
        ("GGSN-MIB", "ggsnCompletedDeactivation"),
        ("GGSN-MIB", "ggsnCompletedSelfDeactivation"),
        ("GGSN-MIB", "ggsnCompletedUpdate"),
        ("GGSN-MIB", "ggsnIdleTimeoutDeactivation"),
        ("GGSN-MIB", "ggsnCompletedManualDeactivation"),
        ("GGSN-MIB", "ggsnCompletedSecondaryActivation"),
        ("GGSN-MIB", "ggsnSessionTimeoutDeactivation"),
        ("GGSN-MIB", "ggsnFailedActivation"),
        ("GGSN-MIB", "ggsnGtpUplinkPackets"),
        ("GGSN-MIB", "ggsnGtpUplinkBytes"),
        ("GGSN-MIB", "ggsnGtpDownlinkPackets"),
        ("GGSN-MIB", "ggsnGtpDownlinkBytes"),
        ("GGSN-MIB", "ggsnGtpControlPacketDrops"),
        ("GGSN-MIB", "ggsnGtpVerUnsupPacketsReceived"),
        ("GGSN-MIB", "ggsnGtpVerUnsupPacketsSent"),
        ("GGSN-MIB", "ggsnGtpEchoReqReceived"),
        ("GGSN-MIB", "ggsnGtpEchoReqSent"),
        ("GGSN-MIB", "ggsnGtpEchoRespReceived"),
        ("GGSN-MIB", "ggsnGtpEchoRespSent"),
        ("GGSN-MIB", "ggsnGtpPdpCreateReqReceived"),
        ("GGSN-MIB", "ggsnGtpv0PdpCreateReqReceived"),
        ("GGSN-MIB", "ggsnGtpPdpCreateRespSent"),
        ("GGSN-MIB", "ggsnGtpPdpUpdateReqReceived"),
        ("GGSN-MIB", "ggsnGtpPdpUpdateReqSent"),
        ("GGSN-MIB", "ggsnGtpPdpUpdateRespReceived"),
        ("GGSN-MIB", "ggsnGtpPdpUpdateRespSent"),
        ("GGSN-MIB", "ggsnGtpPdpDeleteReqReceived"),
        ("GGSN-MIB", "ggsnGtpPdpDeleteReqSent"),
        ("GGSN-MIB", "ggsnGtpPdpDeleteRespReceived"),
        ("GGSN-MIB", "ggsnGtpPdpDeleteRespSent"),
        ("GGSN-MIB", "ggsnGtpPdpInitiateContextActivationRespReceived"),
        ("GGSN-MIB", "ggsnGtpPdpInitiateContextActivationReqSent"),
        ("GGSN-MIB", "ggsnGtpRequestsAccepted"),
        ("GGSN-MIB", "ggsnGtpNbrOfTunnels"),
        ("GGSN-MIB", "ggsnGtpNbrOfCreatedTunnels"),
        ("GGSN-MIB", "ggsnGtpErrorIndicationReceived"),
        ("GGSN-MIB", "ggsnGtpErrorIndicationSent"),
        ("GGSN-MIB", "ggsnGtpErrorInvalidRequestFormat"),
        ("GGSN-MIB", "ggsnGtpErrorResourcesUnavailable"),
        ("GGSN-MIB", "ggsnGtpErrorDynAddrUnavailable"),
        ("GGSN-MIB", "ggsnGtpErrorMemoryUnavailable"),
        ("GGSN-MIB", "ggsnGtpErrorApnUnknown"),
        ("GGSN-MIB", "ggsnGtpErrorPdpAddrUnknown"),
        ("GGSN-MIB", "ggsnGtpErrorAuthenticationFailed"),
        ("GGSN-MIB", "ggsnGtpErrorSystemFailure"),
        ("GGSN-MIB", "ggsnGtpErrorTftSemanticError"),
        ("GGSN-MIB", "ggsnGtpErrorTftSyntaxError"),
        ("GGSN-MIB", "ggsnGtpErrorPackFiltSemantError"),
        ("GGSN-MIB", "ggsnGtpErrorPackFiltSyntaxError"),
        ("GGSN-MIB", "ggsnGtpErrorMandatoryIEMissing"),
        ("GGSN-MIB", "ggsnGtpErrorMandatoryIEInvalid"),
        ("GGSN-MIB", "ggsnGtpErrorOptionalIEInvalid"),
        ("GGSN-MIB", "ggsnGtpErrorReferenceInexistent"),
        ("GGSN-MIB", "ggsnGtpErrorServiceUnsupported"),
        ("GGSN-MIB", "ggsnGtpPrEchoReqReceived"),
        ("GGSN-MIB", "ggsnGtpPrEchoRequestsSent"),
        ("GGSN-MIB", "ggsnGtpPrEchoRespReceived"),
        ("GGSN-MIB", "ggsnGtpPrEchoRespSent"),
        ("GGSN-MIB", "ggsnGtpPrVerUnsupPacketsReceived"),
        ("GGSN-MIB", "ggsnGtpPrVerUnsupPacketsSent"),
        ("GGSN-MIB", "ggsnGtpPrNodeAliveReqReceived"),
        ("GGSN-MIB", "ggsnGtpPrNodeAliveReqSent"),
        ("GGSN-MIB", "ggsnGtpPrNodeAliveRespReceived"),
        ("GGSN-MIB", "ggsnGtpPrNodeAliveRespSent"),
        ("GGSN-MIB", "ggsnGtpPrRedirectReqReceived"),
        ("GGSN-MIB", "ggsnGtpPrRedirectReqSent"),
        ("GGSN-MIB", "ggsnGtpPrRedirectRespReceived"),
        ("GGSN-MIB", "ggsnGtpPrRedirectRespSent"),
        ("GGSN-MIB", "ggsnGtpPrDataRecTransferReceived"),
        ("GGSN-MIB", "ggsnGtpPrDataRecTransferSent"),
        ("GGSN-MIB", "ggsnGtpPrSndDataRecordPackets"),
        ("GGSN-MIB", "ggsnGtpPrRequestAccepted"),
        ("GGSN-MIB", "ggsnGtpPrNoResource"),
        ("GGSN-MIB", "ggsnGtpPrServiceUnsupported"),
        ("GGSN-MIB", "ggsnGtpPrSystemFailure"),
        ("GGSN-MIB", "ggsnGtpPrInvalidMessageFormat"),
        ("GGSN-MIB", "ggsnGtpPrVersionUnsupported"),
        ("GGSN-MIB", "ggsnGtpPrRequestUnfulfilled"),
        ("GGSN-MIB", "ggsnGtpPrDecodingError"),
        ("GGSN-MIB", "ggsnGtpPrAlreadyFulfilled"),
        ("GGSN-MIB", "ggsnGtpPrDupPacketFulfilled"),
        ("GGSN-MIB", "ggsnGtpPrErrorMandatoryIEMissing"),
        ("GGSN-MIB", "ggsnGtpPrErrorMandatoryIEInvalid"),
        ("GGSN-MIB", "ggsnGtpPrErrorOptionalIEInvalid"),
        ("GGSN-MIB", "ggsnGtpPrErrorRefInexistent"),
        ("GGSN-MIB", "ggsnUplinkPackets"),
        ("GGSN-MIB", "ggsnUplinkBytes"),
        ("GGSN-MIB", "ggsnUplinkDrops"),
        ("GGSN-MIB", "ggsnUplinkDropsBytes"),
        ("GGSN-MIB", "ggsnDownlinkPackets"),
        ("GGSN-MIB", "ggsnDownlinkBytes"),
        ("GGSN-MIB", "ggsnDownlinkDrops"),
        ("GGSN-MIB", "ggsnDownlinkDropsBytes"),
        ("GGSN-MIB", "ggsnNbrOfActivePdpContextsIpv6"),
        ("GGSN-MIB", "ggsnAttemptedActivationIpv6"),
        ("GGSN-MIB", "ggsnAttemptedSecondaryActivationIpv6"),
        ("GGSN-MIB", "ggsnCompletedActivationIpv6"),
        ("GGSN-MIB", "ggsnCompletedSecondaryActivationIpv6"),
        ("GGSN-MIB", "ggsnUplinkPacketsIpv6"),
        ("GGSN-MIB", "ggsnUplinkBytesIpv6"),
        ("GGSN-MIB", "ggsnUplinkDropsIpv6"),
        ("GGSN-MIB", "ggsnDownlinkPacketsIpv6"),
        ("GGSN-MIB", "ggsnDownlinkBytesIpv6"),
        ("GGSN-MIB", "ggsnDownlinkDropsIpv6"),
        ("GGSN-MIB", "ggsnNbrOfActivePdpContextsWlan"),
        ("GGSN-MIB", "ggsnAttemptedActivationWlan"),
        ("GGSN-MIB", "ggsnCompletedActivationWlan"),
        ("GGSN-MIB", "ggsnAttemptedActivationConversational"),
        ("GGSN-MIB", "ggsnAttemptedActivationStreaming"),
        ("GGSN-MIB", "ggsnAttemptedActivationInteractive"),
        ("GGSN-MIB", "ggsnAttemptedActivationBackground"),
        ("GGSN-MIB", "ggsnAttemptedActivationDiscarded"),
        ("GGSN-MIB", "ggsnCompletedActivationConversational"),
        ("GGSN-MIB", "ggsnCompletedActivationStreaming"),
        ("GGSN-MIB", "ggsnCompletedActivationInteractive"),
        ("GGSN-MIB", "ggsnCompletedActivationBackground"),
        ("GGSN-MIB", "ggsnAttemptedActivationIpv4v6"),
        ("GGSN-MIB", "ggsnCompletedActivationIpv4v6"),
        ("GGSN-MIB", "ggsnUplinkBytesWlan"),
        ("GGSN-MIB", "ggsnUplinkDropsWlan"),
        ("GGSN-MIB", "ggsnUplinkPacketsWlan"),
        ("GGSN-MIB", "ggsnDownlinkBytesWlan"),
        ("GGSN-MIB", "ggsnDownlinkDropsWlan"),
        ("GGSN-MIB", "ggsnDownlinkPacketsWlan"),
        ("GGSN-MIB", "ggsnNeighborSolicitationRcv"),
        ("GGSN-MIB", "ggsnNeighborSolicitationRsp"),
        ("GGSN-MIB", "ggsnRouterSolicitationRcv"),
        ("GGSN-MIB", "ggsnRouterSolicitationRsp"),
        ("GGSN-MIB", "ggsnL2tpActiveTunnels"),
        ("GGSN-MIB", "ggsnL2tpMaxActiveTunnels"),
        ("GGSN-MIB", "ggsnL2tpActiveSessions"),
        ("GGSN-MIB", "ggsnL2tpMaxActiveSessions"),
        ("GGSN-MIB", "ggsnChgEncodedCdrs"),
        ("GGSN-MIB", "ggsnChgFailedEncodedCdrs"),
        ("GGSN-MIB", "ggsnChgGeneratedFtpCdrs"),
        ("GGSN-MIB", "ggsnChgGeneratedGtppCdrs"),
        ("GGSN-MIB", "ggsnChgGtppLogCdrs"),
        ("GGSN-MIB", "ggsnChgGtppAttemptedCdrsSend"),
        ("GGSN-MIB", "ggsnChgGtppCdrsSendFailure"),
        ("GGSN-MIB", "ggsnNbActivePdpPerTrafficClassConversational"),
        ("GGSN-MIB", "ggsnNbActivePdpPerTrafficClassStreaming"),
        ("GGSN-MIB", "ggsnNbActivePdpPerTrafficClassInteractive"),
        ("GGSN-MIB", "ggsnNbActivePdpPerTrafficClassBackground"),
        ("GGSN-MIB", "ggsnRadiusAuthenticationFailure"),
        ("GGSN-MIB", "ggsnRadiusAccountingFailure"),
        ("GGSN-MIB", "ggsn3gdtActiveContexts"),
        ("GGSN-MIB", "ggsn3gdtTotalCompletedEstablishment"),
        ("GGSN-MIB", "ggsn3gdtTotalAttemptedEstablishment"),
        ("GGSN-MIB", "ggsn3gdtErrorHandling"),
        ("GGSN-MIB", "gn3gdtTotalCompletedEstablishment"),
        ("GGSN-MIB", "gn3gdtTotalAttemptedEstablishment"),
        ("GGSN-MIB", "gn3gdtErrorHandling"),
        ("GGSN-MIB", "ggsnNbrOfActivePdpContextsIpv4v6"))
)
if mibBuilder.loadTexts:
    ggsnGlobalStatisticsGroup.setStatus("current")

ggsnApnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 3)
)
ggsnApnStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnName"),
        ("GGSN-MIB", "ggsnApnActivePdpContextCount"),
        ("GGSN-MIB", "ggsnApnAttemptedActivation"),
        ("GGSN-MIB", "ggsnApnAttemptedDynActivation"),
        ("GGSN-MIB", "ggsnApnAttemptedDeactivation"),
        ("GGSN-MIB", "ggsnApnAttemptedSelfDeactivation"),
        ("GGSN-MIB", "ggsnApnCompletedActivation"),
        ("GGSN-MIB", "ggsnApnCompletedDynActivation"),
        ("GGSN-MIB", "ggsnApnCompletedDeactivation"),
        ("GGSN-MIB", "ggsnApnCompletedSelfDeactivation"),
        ("GGSN-MIB", "ggsnApnAvailableIpAddressesInInternalPool"),
        ("GGSN-MIB", "ggsnApnIpAddressesInQuarantineInInternalPool"),
        ("GGSN-MIB", "ggsnApnUplinkPackets"),
        ("GGSN-MIB", "ggsnApnUplinkBytes"),
        ("GGSN-MIB", "ggsnApnUplinkDrops"),
        ("GGSN-MIB", "ggsnApnDownlinkPackets"),
        ("GGSN-MIB", "ggsnApnDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnDownlinkDrops"),
        ("GGSN-MIB", "ggsnApnAttemptedMSActivation"),
        ("GGSN-MIB", "ggsnApnCompletedMSActivation"),
        ("GGSN-MIB", "ggsnApnAttemptedMSDeactivation"),
        ("GGSN-MIB", "ggsnApnCompletedMSDeactivation"),
        ("GGSN-MIB", "ggsnApnActivePdpContextMax"),
        ("GGSN-MIB", "ggsnApnActivePdpContextMean"),
        ("GGSN-MIB", "ggsnApnAttemptedAuthActivation"),
        ("GGSN-MIB", "ggsnApnFailedAuthActivation"),
        ("GGSN-MIB", "ggsnApnAttemptedUpdateMsAndSgsn"),
        ("GGSN-MIB", "ggsnApnCompletedUpdateMsAndSgsn"),
        ("GGSN-MIB", "ggsnApnNbrOfTftFilters"),
        ("GGSN-MIB", "ggsnApnSessTimeoutDeactivation"),
        ("GGSN-MIB", "ggsnApnIdleTimeoutDeactivation"),
        ("GGSN-MIB", "ggsnApnGiSignalingInPackets"),
        ("GGSN-MIB", "ggsnApnGiSignalingInBytes"),
        ("GGSN-MIB", "ggsnApnGiSignalingOutPackets"),
        ("GGSN-MIB", "ggsnApnGiSignalingOutBytes"),
        ("GGSN-MIB", "ggsnApnActivePdpContextCountIpv6"),
        ("GGSN-MIB", "ggsnApnAttemptedActivationIpv6"),
        ("GGSN-MIB", "ggsnApnCompletedActivationIpv6"),
        ("GGSN-MIB", "ggsnApnUplinkPacketsIpv6"),
        ("GGSN-MIB", "ggsnApnUplinkBytesIpv6"),
        ("GGSN-MIB", "ggsnApnUplinkDropsIpv6"),
        ("GGSN-MIB", "ggsnApnDownlinkPacketsIpv6"),
        ("GGSN-MIB", "ggsnApnDownlinkBytesIpv6"),
        ("GGSN-MIB", "ggsnApnDownlinkDropsIpv6"),
        ("GGSN-MIB", "ggsnApnNeighborSolicitationRcv"),
        ("GGSN-MIB", "ggsnApnNeighborSolicitationRsp"),
        ("GGSN-MIB", "ggsnApnRouterSolicitationRcv"),
        ("GGSN-MIB", "ggsnApnRouterSolicitationRsp"),
        ("GGSN-MIB", "ggsnNbApnActivePdpPerTrafficClassConversational"),
        ("GGSN-MIB", "ggsnNbApnActivePdpPerTrafficClassStreaming"),
        ("GGSN-MIB", "ggsnNbApnActivePdpPerTrafficClassInteractive"),
        ("GGSN-MIB", "ggsnNbApnActivePdpPerTrafficClassBackground"),
        ("GGSN-MIB", "ggsnApnImsDedicatedCompletedActivation"),
        ("GGSN-MIB", "ggsnApnImsDedicatedNotConfiguredActivationFailed"),
        ("GGSN-MIB", "ggsnApnImsGeneralPurposeCompletedActivation"),
        ("GGSN-MIB", "ggsnApnImsGeneralNotConfiguredActivationFailed"),
        ("GGSN-MIB", "ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured"),
        ("GGSN-MIB", "ggsnApnUnauthorizedImsPackets"),
        ("GGSN-MIB", "ggsnApnRadiusAccountingFailure"),
        ("GGSN-MIB", "ggsnApnRadiusAuthenticationFailure"),
        ("GGSN-MIB", "ggsnApnSaccRsInstalledDynRules"),
        ("GGSN-MIB", "ggsnApnSaccRsActivePredefinedChargingRules"),
        ("GGSN-MIB", "ggsnApnSaccRsActivePredefinedChargingRuleBases"),
        ("GGSN-MIB", "ggsnApn3gdtActiveContexts"),
        ("GGSN-MIB", "ggsnApn3gdtTotalCompletedEstablishment"),
        ("GGSN-MIB", "ggsnApn3gdtTotalAttemptedEstablishment"),
        ("GGSN-MIB", "ggsnApn3gdtErrorHandling"),
        ("GGSN-MIB", "ggsnApnAttemptedUpdateGgsn"),
        ("GGSN-MIB", "ggsnApnCompletedUpdateGgsn"),
        ("GGSN-MIB", "ggsnApnAttemptedActivationNonDuplicated"),
        ("GGSN-MIB", "ggsnApnActivePdpContextMaxDuringLastPeriod"),
        ("GGSN-MIB", "pgwApnActiveEpsBearer"),
        ("GGSN-MIB", "pgwApnActiveIpv6EpsBearer"),
        ("GGSN-MIB", "pgwApnAttemptedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnCompletedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnAttemptedIpv6EpsBearerActivation"),
        ("GGSN-MIB", "pgwApnCompletedIpv6EpsBearerActivation"),
        ("GGSN-MIB", "pgwApnAttemptedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwApnCompletedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwApnAttemptedS5NetworkDeactivation"),
        ("GGSN-MIB", "pgwApnCompletedS5NetworkDeactivation"),
        ("GGSN-MIB", "pgwApnAttemptedS5UeSgwModification"),
        ("GGSN-MIB", "pgwApnCompletedS5UeSgwModification"),
        ("GGSN-MIB", "pgwApnAttemptedS5SgwSgsnModification"),
        ("GGSN-MIB", "pgwApnCompletedS5SgwSgsnModification"),
        ("GGSN-MIB", "pgwApnAttemptedS5SgsnSgwModification"),
        ("GGSN-MIB", "pgwApnCompletedS5SgsnSgwModification"),
        ("GGSN-MIB", "pgwApnAttemptedS5NetworkModification"),
        ("GGSN-MIB", "pgwApnCompletedS5NetworkModification"),
        ("GGSN-MIB", "pgwApnAttemptedS5UeSgwDeactivation"),
        ("GGSN-MIB", "pgwApnCompletedS5UeSgwDeactivation"),
        ("GGSN-MIB", "gnApnUplinkPackets"),
        ("GGSN-MIB", "gnApnUplinkBytes"),
        ("GGSN-MIB", "gnApnUplinkPacketsIpv6"),
        ("GGSN-MIB", "gnApnUplinkBytesIpv6"),
        ("GGSN-MIB", "gnApnDownlinkPackets"),
        ("GGSN-MIB", "gnApnDownlinkBytes"),
        ("GGSN-MIB", "gnApnDownlinkPacketsIpv6"),
        ("GGSN-MIB", "gnApnDownlinkBytesIpv6"),
        ("GGSN-MIB", "s5ApnUplinkPackets"),
        ("GGSN-MIB", "s5ApnUplinkBytes"),
        ("GGSN-MIB", "s5ApnUplinkPacketsIpv6"),
        ("GGSN-MIB", "s5ApnUplinkBytesIpv6"),
        ("GGSN-MIB", "s5ApnDownlinkPackets"),
        ("GGSN-MIB", "s5ApnDownlinkBytes"),
        ("GGSN-MIB", "s5ApnDownlinkPacketsIpv6"),
        ("GGSN-MIB", "s5ApnDownlinkBytesIpv6"),
        ("GGSN-MIB", "gnApn3gdtUplinkBytes"),
        ("GGSN-MIB", "gnApn3gdtUplinkBytesIpv6"),
        ("GGSN-MIB", "gnApn3gdtUplinkPackets"),
        ("GGSN-MIB", "gnApn3gdtUplinkPacketsIpv6"),
        ("GGSN-MIB", "gnApn3gdtDownlinkBytes"),
        ("GGSN-MIB", "gnApn3gdtDownlinkBytesIpv6"),
        ("GGSN-MIB", "gnApn3gdtDownlinkPackets"),
        ("GGSN-MIB", "gnApn3gdtDownlinkPacketsIpv6"),
        ("GGSN-MIB", "gnApn3gdtDownlinkDropsErrorHandling"),
        ("GGSN-MIB", "ggsnApn3gdtGtpError"),
        ("GGSN-MIB", "pgwApnActiveDedicatedEpsBearer"),
        ("GGSN-MIB", "pgwApnAttemptedDedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnCompletedDedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnAttemptedIpv6DedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnCompletedIpv6DedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwApnAttemptedS5NetworkDedicatedEpsBearerModification"),
        ("GGSN-MIB", "pgwApnCompletedS5NetworkDedicatedEpsBearerModification"),
        ("GGSN-MIB", "pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation"),
        ("GGSN-MIB", "ggsnApnActivePdpContextCountIpv4v6"),
        ("GGSN-MIB", "pgwApnActiveIpv4v6EpsBearer"),
        ("GGSN-MIB", "ggsnApnAttemptedActivationIpv4v6"),
        ("GGSN-MIB", "ggsnApnCompletedActivationIpv4v6"),
        ("GGSN-MIB", "pgwApnAttemptedIpv4v6EpsBearerActivation"),
        ("GGSN-MIB", "pgwApnCompletedIpv4v6EpsBearerActivation"),
        ("GGSN-MIB", "pgwApnActiveWlanEpsBearer"),
        ("GGSN-MIB", "s2aApnUplinkPackets"),
        ("GGSN-MIB", "s2aApnUplinkBytes"),
        ("GGSN-MIB", "s2aApnDownlinkPackets"),
        ("GGSN-MIB", "s2aApnDownlinkBytes"),
        ("GGSN-MIB", "s2aApnUplinkPacketsIpv6"),
        ("GGSN-MIB", "s2aApnUplinkBytesIpv6"),
        ("GGSN-MIB", "s2aApnDownlinkPacketsIpv6"),
        ("GGSN-MIB", "s2aApnDownlinkBytesIpv6"))
)
if mibBuilder.loadTexts:
    ggsnApnStatisticsGroup.setStatus("current")

ggsnSgsnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 4)
)
ggsnSgsnStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnSgsnAddress"),
        ("GGSN-MIB", "ggsnSgsnUplinkPackets"),
        ("GGSN-MIB", "ggsnSgsnUplinkBytes"),
        ("GGSN-MIB", "ggsnSgsnUplinkDrops"),
        ("GGSN-MIB", "ggsnSgsnDownlinkPackets"),
        ("GGSN-MIB", "ggsnSgsnDownlinkBytes"),
        ("GGSN-MIB", "ggsnSgsnDownlinkDrops"))
)
if mibBuilder.loadTexts:
    ggsnSgsnStatisticsGroup.setStatus("current")

ggsnAcctClientStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 5)
)
ggsnAcctClientStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnAcctPartialRecordGenerated"),
        ("GGSN-MIB", "ggsnAcctBillingGatewayIndex"),
        ("GGSN-MIB", "ggsnAcctBillingGatewayAddress"),
        ("GGSN-MIB", "ggsnAcctDataRecTransReqSent"),
        ("GGSN-MIB", "ggsnAcctDataRecTransReqSentDup"),
        ("GGSN-MIB", "ggsnAcctDataRecTransReqCancelled"),
        ("GGSN-MIB", "ggsnAcctDataRecTransRespReceived"),
        ("GGSN-MIB", "ggsnAcctRedirectionReqReceived"),
        ("GGSN-MIB", "ggsnAcctRedirectionRespSent"))
)
if mibBuilder.loadTexts:
    ggsnAcctClientStatisticsGroup.setStatus("current")

ggsnDhcpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 6)
)
ggsnDhcpStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnDhcpClientAddress"),
        ("GGSN-MIB", "ggsnDhcpServerAddress"),
        ("GGSN-MIB", "ggsnDhcpServerName"),
        ("GGSN-MIB", "ggsnDhcpClientYiaddr"),
        ("GGSN-MIB", "ggsnDhcpClientState"),
        ("GGSN-MIB", "ggsnDhcpClientRequestsSent"),
        ("GGSN-MIB", "ggsnDhcpClientRepliesReceived"),
        ("GGSN-MIB", "ggsnDhcpClientRepliesDiscarded"),
        ("GGSN-MIB", "ggsnDhcpClientDiscoversSent"),
        ("GGSN-MIB", "ggsnDhcpClientDeclinesSent"),
        ("GGSN-MIB", "ggsnDhcpClientReleasesSent"),
        ("GGSN-MIB", "ggsnDhcpClientOffersReceived"),
        ("GGSN-MIB", "ggsnDhcpClientAcksReceived"),
        ("GGSN-MIB", "ggsnDhcpClientNaksReceived"),
        ("GGSN-MIB", "ggsnDhcpClientSendErrors"),
        ("GGSN-MIB", "ggsnDhcpServerRoutingInstance"))
)
if mibBuilder.loadTexts:
    ggsnDhcpStatisticsGroup.setStatus("current")

ggsnAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 7)
)
ggsnAlarmsGroup.setObjects(
      *(("GGSN-MIB", "ggsnAlarmNumber"),
        ("GGSN-MIB", "ggsnAlarmCriticalNumber"),
        ("GGSN-MIB", "ggsnAlarmMajorNumber"),
        ("GGSN-MIB", "ggsnAlarmMinorNumber"),
        ("GGSN-MIB", "ggsnAlarmWarningNumber"),
        ("GGSN-MIB", "ggsnAlarmUnknownNumber"))
)
if mibBuilder.loadTexts:
    ggsnAlarmsGroup.setStatus("current")

ggsnAlarmsEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 8)
)
ggsnAlarmsEntryGroup.setObjects(
      *(("GGSN-MIB", "ggsnAlarmId"),
        ("GGSN-MIB", "ggsnAlarmName"),
        ("GGSN-MIB", "ggsnAlarmTime"),
        ("GGSN-MIB", "ggsnAlarmSourceId"),
        ("GGSN-MIB", "ggsnAlarmObjectClass"),
        ("GGSN-MIB", "ggsnAlarmObjectInstance"),
        ("GGSN-MIB", "ggsnAlarmSeverity"),
        ("GGSN-MIB", "ggsnAlarmDescription"))
)
if mibBuilder.loadTexts:
    ggsnAlarmsEntryGroup.setStatus("current")

ggsnAlarmHistEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 10)
)
ggsnAlarmHistEntryGroup.setObjects(
      *(("GGSN-MIB", "ggsnAlarmHistTime"),
        ("GGSN-MIB", "ggsnAlarmHistEventCause"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmId"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmName"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmTime"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmSourceId"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmObjInstance"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmSeverity"),
        ("GGSN-MIB", "ggsnAlarmHistAlarmDescription"))
)
if mibBuilder.loadTexts:
    ggsnAlarmHistEntryGroup.setStatus("current")

ggsnOldObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 12)
)
ggsnOldObjectsGroup.setObjects(
      *(("GGSN-MIB", "ggsnPicAddress"),
        ("GGSN-MIB", "ggsnPicNbrOfActivePdpContexts"),
        ("GGSN-MIB", "ggsnAttemptedTimeDeactivation"),
        ("GGSN-MIB", "ggsnFbcApplicationTransactionPps"),
        ("GGSN-MIB", "ggsnFbcApplicationTransactionPrs"),
        ("GGSN-MIB", "ggsnApnFbcInitialPrsReq"),
        ("GGSN-MIB", "ggsnApnFbcInitialPrsReqFailed"),
        ("GGSN-MIB", "ggsnApnFbcUpdPrsReq"),
        ("GGSN-MIB", "ggsnApnFbcUpdPrsReqFailed"),
        ("GGSN-MIB", "ggsnApnFbcStartCredReq"),
        ("GGSN-MIB", "ggsnApnFbcStartCredReqFailed"),
        ("GGSN-MIB", "ggsnApnFbcUpdCredReq"),
        ("GGSN-MIB", "ggsnApnFbcUpdCredReqFailed"),
        ("GGSN-MIB", "ggsnApnFbcStopCredReq"),
        ("GGSN-MIB", "ggsnApnFbcStopCredReqFailed"))
)
if mibBuilder.loadTexts:
    ggsnOldObjectsGroup.setStatus("deprecated")

ggsnApnFbcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 13)
)
ggsnApnFbcStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcNbrOfPpsUsers"),
        ("GGSN-MIB", "ggsnApnFbcNbrOfPpsPdpContexts"),
        ("GGSN-MIB", "ggsnApnFbcPpsCreate"),
        ("GGSN-MIB", "ggsnApnFbcPpsReject"),
        ("GGSN-MIB", "ggsnApnFbcInitiatedDeactivation"),
        ("GGSN-MIB", "ggsnApnFbcExtPrsUpd"),
        ("GGSN-MIB", "ggsnApnFbcExtCreditUpd"),
        ("GGSN-MIB", "ggsnApnFbcDurationTime"),
        ("GGSN-MIB", "ggsnApnFbcActivationBearerCtrlAccept"),
        ("GGSN-MIB", "ggsnApnFbcActivationBearerCtrlReject"),
        ("GGSN-MIB", "ggsnApnFbcActivationBearerCtrlUpgrade"),
        ("GGSN-MIB", "ggsnApnFbcActivationBearerCtrlDowngrade"),
        ("GGSN-MIB", "ggsnApnFbcModificationBearerCtrlAccept"),
        ("GGSN-MIB", "ggsnApnFbcModificationBearerCtrlDeactivate"),
        ("GGSN-MIB", "ggsnApnFbcModificationBearerCtrlUpgrade"),
        ("GGSN-MIB", "ggsnApnFbcModificationBearerCtrlDowngrade"),
        ("GGSN-MIB", "ggsnApnFbcActivationNoBearerCtrlAccept"),
        ("GGSN-MIB", "ggsnApnFbcActivationNoBearerCtrlReject"),
        ("GGSN-MIB", "ggsnApnFbcActivationNoBearerCtrlDowngrade"),
        ("GGSN-MIB", "ggsnApnFbcModificationNoBearerCtrlAccept"),
        ("GGSN-MIB", "ggsnApnFbcModificationNoBearerCtrlDeactivate"),
        ("GGSN-MIB", "ggsnApnFbcModificationNoBearerCtrlDowngrade"),
        ("GGSN-MIB", "ggsnApnSaccAttemptedServiceInitiatedQoSModification"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcStatisticsGroup.setStatus("current")

ggsnFbcAuthStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 14)
)
ggsnFbcAuthStatisticsGroup.setObjects(
      *(("GGSN-MIB", "ggsnFbcUserAuthPacketsDropped"),
        ("GGSN-MIB", "ggsnFbcDefaultAuthPacketsDropped"),
        ("GGSN-MIB", "ggsnFbcEmptyBucketPacketsDropped"),
        ("GGSN-MIB", "ggsnFbcComFailAuthPacketsDropped"),
        ("GGSN-MIB", "ggsnFbcIdentErrorPacketsDropped"))
)
if mibBuilder.loadTexts:
    ggsnFbcAuthStatisticsGroup.setStatus("deprecated")

ggsnApnFbcServIdentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 15)
)
ggsnApnFbcServIdentStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcServIdentUplinkBytes"),
        ("GGSN-MIB", "ggsnApnFbcServIdentDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnFbcServIdentEventTrans"),
        ("GGSN-MIB", "ggsnApnFbcServIdentEventTransFail"),
        ("GGSN-MIB", "ggsnApnFbcServIdentEventStartTrans"),
        ("GGSN-MIB", "ggsnApnFbcServIdentEventSuccessTrans"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcServIdentStatsGroup.setStatus("current")

ggsnApnFbcServClassStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 16)
)
ggsnApnFbcServClassStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcServClassUplinkBytes"),
        ("GGSN-MIB", "ggsnApnFbcServClassDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnFbcServClassActiveTime"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcServClassStatsGroup.setStatus("deprecated")

ggsnFbcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 17)
)
ggsnFbcStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnFbcInitiatedDeactivation"),
        ("GGSN-MIB", "ggsnFbcExtPrsUpdReqNoMatch"),
        ("GGSN-MIB", "ggsnFbcExtCreditUpdReqNoMatch"),
        ("GGSN-MIB", "ggsnFbcExtUpdReqFailure"))
)
if mibBuilder.loadTexts:
    ggsnFbcStatsGroup.setStatus("current")

ggsnApnFbcPrasStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 18)
)
ggsnApnFbcPrasStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcPrasName"),
        ("GGSN-MIB", "ggsnApnFbcPrasStartReq"),
        ("GGSN-MIB", "ggsnApnFbcPrasStartReqFail"),
        ("GGSN-MIB", "ggsnApnFbcPrasUpdateReq"),
        ("GGSN-MIB", "ggsnApnFbcPrasUpdateReqFail"),
        ("GGSN-MIB", "ggsnApnFbcPrasStopReq"),
        ("GGSN-MIB", "ggsnApnFbcPrasStopReqFail"),
        ("GGSN-MIB", "ggsnApnFbcPrasUserServiceDenied"),
        ("GGSN-MIB", "ggsnApnFbcPrasUserUnknown"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcPrasStatsGroup.setStatus("current")

ggsnApnFbcCcasStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 19)
)
ggsnApnFbcCcasStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcCcasName"),
        ("GGSN-MIB", "ggsnApnFbcCcasStartReq"),
        ("GGSN-MIB", "ggsnApnFbcCcasStartReqFail"),
        ("GGSN-MIB", "ggsnApnFbcCcasUpdateReq"),
        ("GGSN-MIB", "ggsnApnFbcCcasUpdateReqFail"),
        ("GGSN-MIB", "ggsnApnFbcCcasStopReq"),
        ("GGSN-MIB", "ggsnApnFbcCcasStopReqFail"),
        ("GGSN-MIB", "ggsnApnFbcCcasUserServiceDenied"),
        ("GGSN-MIB", "ggsnApnFbcCcasUserUnknown"),
        ("GGSN-MIB", "ggsnApnSaccCcasAuthReject"),
        ("GGSN-MIB", "ggsnApnSaccCcasCcNotApplicable"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcCcasStatsGroup.setStatus("current")

ggsnFbcDiamApplSysStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 20)
)
ggsnFbcDiamApplSysStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnFbcDiamApplSysName"),
        ("GGSN-MIB", "ggsnFbcDiamApplSysReq"))
)
if mibBuilder.loadTexts:
    ggsnFbcDiamApplSysStatsGroup.setStatus("current")

ggsnApnFbcRateGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 21)
)
ggsnApnFbcRateGroupStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcRateGroupEventStartTrans"),
        ("GGSN-MIB", "ggsnApnFbcRateGroupEventSuccessTrans"))
)
if mibBuilder.loadTexts:
    ggsnApnFbcRateGroupStatsGroup.setStatus("obsolete")

ggsnL2tpTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 22)
)
ggsnL2tpTunnelStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnL2tpTunnelLocalTID"),
        ("GGSN-MIB", "ggsnL2tpTunnelRemoteTID"),
        ("GGSN-MIB", "ggsnL2tpTunnelLocalIp"),
        ("GGSN-MIB", "ggsnL2tpTunnelRemoteIp"),
        ("GGSN-MIB", "ggsnL2tpTunnelActiveSessions"),
        ("GGSN-MIB", "ggsnL2tpTunnelControlTxPackets"),
        ("GGSN-MIB", "ggsnL2tpTunnelControlRxPackets"),
        ("GGSN-MIB", "ggsnL2tpTunnelDataTxPackets"),
        ("GGSN-MIB", "ggsnL2tpTunnelDataRxPackets"),
        ("GGSN-MIB", "ggsnL2tpTunnelDiscardedTxPackets"),
        ("GGSN-MIB", "ggsnL2tpTunnelDiscardedRxPackets"))
)
if mibBuilder.loadTexts:
    ggsnL2tpTunnelStatsGroup.setStatus("current")

ggsnApnSaccPcrfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 23)
)
ggsnApnSaccPcrfStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnSaccPcrfName"),
        ("GGSN-MIB", "ggsnApnSaccPcrfAuthorFail"),
        ("GGSN-MIB", "ggsnApnSaccPcrfAuthenFail"),
        ("GGSN-MIB", "ggsnApnSaccPcrfUpdCcReqSessIdNoMatch"),
        ("GGSN-MIB", "ggsnApnSaccPcrfActivePdpContextUsageReporting"),
        ("GGSN-MIB", "ggsnApnSaccPcrfActiveIPcanSessions"),
        ("GGSN-MIB", "ggsnApnSaccPcrfActiveDedicatedIPcanBearers"))
)
if mibBuilder.loadTexts:
    ggsnApnSaccPcrfStatsGroup.setStatus("current")

ggsnApnSaccRsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 24)
)
ggsnApnSaccRsStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnSaccRsName"),
        ("GGSN-MIB", "ggsnApnSaccRsUplinkBytes"),
        ("GGSN-MIB", "ggsnApnSaccRsDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnSaccRsServiceInstances"),
        ("GGSN-MIB", "ggsnApnSaccRsAuthDownlinkPacketsDropped"),
        ("GGSN-MIB", "ggsnApnSaccRsAuthUplinkPacketsDropped"),
        ("GGSN-MIB", "ggsnApnSaccRsGateDownlinkPacketsDropped"),
        ("GGSN-MIB", "ggsnApnSaccRsGateUplinkPacketsDropped"))
)
if mibBuilder.loadTexts:
    ggsnApnSaccRsStatsGroup.setStatus("current")

ggsnApnSacc2ServIdentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 25)
)
ggsnApnSacc2ServIdentStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnSacc2ServIdentUplinkBytes"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentEventTrans"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentEventTransFail"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentEventStartTrans"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentEventSuccessTrans"))
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServIdentStatsGroup.setStatus("deprecated")

ggsnApnSacc2ServClassStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 26)
)
ggsnApnSacc2ServClassStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnSacc2ServClassUplinkBytes"),
        ("GGSN-MIB", "ggsnApnSacc2ServClassDownlinkBytes"),
        ("GGSN-MIB", "ggsnApnSacc2ServClassActiveTime"))
)
if mibBuilder.loadTexts:
    ggsnApnSacc2ServClassStatsGroup.setStatus("deprecated")

ggsnApnSacc3ServIdentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 27)
)
ggsnApnSacc3ServIdentStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnFbcServIdentUplinkBytes"),
        ("GGSN-MIB", "ggsnApnFbcServIdentDownlinkBytes"))
)
if mibBuilder.loadTexts:
    ggsnApnSacc3ServIdentStatsGroup.setStatus("deprecated")

ggsnApnSacc3RatingGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 28)
)
ggsnApnSacc3RatingGroupStatsGroup.setObjects(
      *(("GGSN-MIB", "ggsnApnSacc3RatingGroupUplinkBytes"),
        ("GGSN-MIB", "ggsnApnSacc3RatingGroupDownlinkBytes"))
)
if mibBuilder.loadTexts:
    ggsnApnSacc3RatingGroupStatsGroup.setStatus("deprecated")

pgwGlobalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 29)
)
pgwGlobalStatisticsGroup.setObjects(
      *(("GGSN-MIB", "pgwNbrOfActiveEpsBearer"),
        ("GGSN-MIB", "pgwNbrOfActiveIpv6EpsBearer"),
        ("GGSN-MIB", "pgwNbrOfActiveIpv4v6EpsBearer"),
        ("GGSN-MIB", "pgwWlanNbrOfActiveEpsBearer"))
)
if mibBuilder.loadTexts:
    pgwGlobalStatisticsGroup.setStatus("current")

pgwAttemptedEpsBearerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 30)
)
pgwAttemptedEpsBearerStatsGroup.setObjects(
      *(("GGSN-MIB", "pgwAttemptedEpsBearerActivation"),
        ("GGSN-MIB", "pgwAttemptedEpsBearerIpv6Activation"),
        ("GGSN-MIB", "pgwAttemptedEpsBearerModification"),
        ("GGSN-MIB", "pgwAttemptedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwAttemptedDedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwAttemptedDedicatedEpsBearerIpv6Activation"),
        ("GGSN-MIB", "pgwAttemptedEpsBearerIpv4v6Activation"),
        ("GGSN-MIB", "pgwAttempteds2aEpsBearerActivation"))
)
if mibBuilder.loadTexts:
    pgwAttemptedEpsBearerStatsGroup.setStatus("current")

pgwCompletedEpsBearerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 31)
)
pgwCompletedEpsBearerStatsGroup.setObjects(
      *(("GGSN-MIB", "pgwCompletedEpsBearerActivation"),
        ("GGSN-MIB", "pgwCompletedEpsBearerIpv6Activation"),
        ("GGSN-MIB", "pgwCompletedEpsBearerModification"),
        ("GGSN-MIB", "pgwCompletedEpsBearerDeactivation"),
        ("GGSN-MIB", "pgwCompletedDedicatedEpsBearerActivation"),
        ("GGSN-MIB", "pgwCompletedDedicatedEpsBearerIpv6Activation"),
        ("GGSN-MIB", "pgwCompletedEpsBearerIpv4v6Activation"),
        ("GGSN-MIB", "pgwCompleteds2aEpsBearerActivation"))
)
if mibBuilder.loadTexts:
    pgwCompletedEpsBearerStatsGroup.setStatus("current")

pgwApnSaccRatingGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 32)
)
pgwApnSaccRatingGroupStatsGroup.setObjects(
      *(("GGSN-MIB", "pgwApnSaccRatingGroupUplinkBytes"),
        ("GGSN-MIB", "pgwApnSaccRatingGroupDownlinkBytes"))
)
if mibBuilder.loadTexts:
    pgwApnSaccRatingGroupStatsGroup.setStatus("current")

s6bInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 33)
)
s6bInterfaceGroup.setObjects(
      *(("GGSN-MIB", "s6bAarSent"),
        ("GGSN-MIB", "s6bAaaSuccRcvd"),
        ("GGSN-MIB", "s6bAaaFailRcvd"),
        ("GGSN-MIB", "s6bAaaInvalidRcvd"),
        ("GGSN-MIB", "s6bStrSent"),
        ("GGSN-MIB", "s6bStaSuccRcvd"),
        ("GGSN-MIB", "s6bStaFailRcvd"))
)
if mibBuilder.loadTexts:
    s6bInterfaceGroup.setStatus("current")


# Notification objects

ggsnTrapNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 2, 1)
)
ggsnTrapNew.setObjects(
      *(("GGSN-MIB", "ggsnAlarmId"),
        ("GGSN-MIB", "ggsnAlarmName"),
        ("GGSN-MIB", "ggsnAlarmTime"),
        ("GGSN-MIB", "ggsnAlarmSourceId"),
        ("GGSN-MIB", "ggsnAlarmObjectClass"),
        ("GGSN-MIB", "ggsnAlarmObjectInstance"),
        ("GGSN-MIB", "ggsnAlarmSeverity"),
        ("GGSN-MIB", "ggsnAlarmDescription"))
)
if mibBuilder.loadTexts:
    ggsnTrapNew.setStatus(
        "current"
    )

ggsnTrapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 2, 2)
)
ggsnTrapChanged.setObjects(
      *(("GGSN-MIB", "ggsnAlarmId"),
        ("GGSN-MIB", "ggsnAlarmName"),
        ("GGSN-MIB", "ggsnAlarmTime"),
        ("GGSN-MIB", "ggsnAlarmSourceId"),
        ("GGSN-MIB", "ggsnAlarmObjectClass"),
        ("GGSN-MIB", "ggsnAlarmObjectInstance"),
        ("GGSN-MIB", "ggsnAlarmSeverity"),
        ("GGSN-MIB", "ggsnAlarmDescription"))
)
if mibBuilder.loadTexts:
    ggsnTrapChanged.setStatus(
        "current"
    )

ggsnTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 2, 3)
)
ggsnTrapCleared.setObjects(
      *(("GGSN-MIB", "ggsnAlarmId"),
        ("GGSN-MIB", "ggsnAlarmName"),
        ("GGSN-MIB", "ggsnAlarmTime"),
        ("GGSN-MIB", "ggsnAlarmSourceId"),
        ("GGSN-MIB", "ggsnAlarmObjectClass"),
        ("GGSN-MIB", "ggsnAlarmObjectInstance"),
        ("GGSN-MIB", "ggsnAlarmSeverity"),
        ("GGSN-MIB", "ggsnAlarmDescription"))
)
if mibBuilder.loadTexts:
    ggsnTrapCleared.setStatus(
        "current"
    )


# Notifications groups

ggsnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 2, 9)
)
ggsnNotificationsGroup.setObjects(
      *(("GGSN-MIB", "ggsnTrapNew"),
        ("GGSN-MIB", "ggsnTrapChanged"),
        ("GGSN-MIB", "ggsnTrapCleared"))
)
if mibBuilder.loadTexts:
    ggsnNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ggsnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10923, 1, 1, 1, 2, 1, 1)
)
ggsnMIBCompliance.setObjects(
      *(("GGSN-MIB", "ggsnSystemGroup"),
        ("GGSN-MIB", "ggsnGlobalStatisticsGroup"),
        ("GGSN-MIB", "ggsnApnStatisticsGroup"),
        ("GGSN-MIB", "ggsnSgsnStatisticsGroup"),
        ("GGSN-MIB", "ggsnAcctClientStatisticsGroup"),
        ("GGSN-MIB", "ggsnDhcpStatisticsGroup"),
        ("GGSN-MIB", "ggsnAlarmsGroup"),
        ("GGSN-MIB", "ggsnAlarmsEntryGroup"),
        ("GGSN-MIB", "ggsnNotificationsGroup"),
        ("GGSN-MIB", "ggsnAlarmHistEntryGroup"),
        ("GGSN-MIB", "ggsnApnFbcStatisticsGroup"),
        ("GGSN-MIB", "ggsnFbcAuthStatisticsGroup"),
        ("GGSN-MIB", "ggsnApnFbcServIdentStatsGroup"),
        ("GGSN-MIB", "ggsnApnFbcServClassStatsGroup"),
        ("GGSN-MIB", "ggsnApnSacc2ServIdentStatsGroup"),
        ("GGSN-MIB", "ggsnApnSacc2ServClassStatsGroup"),
        ("GGSN-MIB", "ggsnApnSacc3ServIdentStatsGroup"),
        ("GGSN-MIB", "ggsnApnSacc3RatingGroupStatsGroup"),
        ("GGSN-MIB", "ggsnFbcStatsGroup"),
        ("GGSN-MIB", "pgwApnSaccRatingGroupStatsGroup"))
)
if mibBuilder.loadTexts:
    ggsnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GGSN-MIB",
    **{"PerceivedSeverity": PerceivedSeverity,
       "AlarmEventCause": AlarmEventCause,
       "ejnmobileipABmib": ejnmobileipABmib,
       "ejnxMibs": ejnxMibs,
       "ggsnMIB": ggsnMIB,
       "ggsnMibs": ggsnMibs,
       "ggsnMIBObjects": ggsnMIBObjects,
       "ggsnGeneralInfo": ggsnGeneralInfo,
       "ggsnVersion": ggsnVersion,
       "ggsnInstalled": ggsnInstalled,
       "ggsnGlobalStats": ggsnGlobalStats,
       "ggsnStatReportTime": ggsnStatReportTime,
       "ggsnNbrOfActivePdpContexts": ggsnNbrOfActivePdpContexts,
       "ggsnPdpContextsStatsAttempted": ggsnPdpContextsStatsAttempted,
       "ggsnAttemptedActivation": ggsnAttemptedActivation,
       "ggsnAttemptedDeactivation": ggsnAttemptedDeactivation,
       "ggsnAttemptedSelfDeactivation": ggsnAttemptedSelfDeactivation,
       "ggsnAttemptedUpdate": ggsnAttemptedUpdate,
       "ggsnAttemptedTimeDeactivation": ggsnAttemptedTimeDeactivation,
       "ggsnAttemptedManualDeactivation": ggsnAttemptedManualDeactivation,
       "ggsnAttemptedSecondaryActivation": ggsnAttemptedSecondaryActivation,
       "ggsnAttemptedActivationIpv6": ggsnAttemptedActivationIpv6,
       "ggsnAttemptedSecondaryActivationIpv6": ggsnAttemptedSecondaryActivationIpv6,
       "ggsnAttemptedActivationWlan": ggsnAttemptedActivationWlan,
       "ggsnAttemptedActivationConversational": ggsnAttemptedActivationConversational,
       "ggsnAttemptedActivationStreaming": ggsnAttemptedActivationStreaming,
       "ggsnAttemptedActivationInteractive": ggsnAttemptedActivationInteractive,
       "ggsnAttemptedActivationBackground": ggsnAttemptedActivationBackground,
       "ggsnAttemptedActivationDiscarded": ggsnAttemptedActivationDiscarded,
       "ggsnAttemptedActivationIpv4v6": ggsnAttemptedActivationIpv4v6,
       "ggsnPdpContextsStatsCompleted": ggsnPdpContextsStatsCompleted,
       "ggsnCompletedActivation": ggsnCompletedActivation,
       "ggsnCompletedDeactivation": ggsnCompletedDeactivation,
       "ggsnCompletedSelfDeactivation": ggsnCompletedSelfDeactivation,
       "ggsnCompletedUpdate": ggsnCompletedUpdate,
       "ggsnIdleTimeoutDeactivation": ggsnIdleTimeoutDeactivation,
       "ggsnCompletedManualDeactivation": ggsnCompletedManualDeactivation,
       "ggsnCompletedSecondaryActivation": ggsnCompletedSecondaryActivation,
       "ggsnSessionTimeoutDeactivation": ggsnSessionTimeoutDeactivation,
       "ggsnCompletedActivationIpv6": ggsnCompletedActivationIpv6,
       "ggsnCompletedSecondaryActivationIpv6": ggsnCompletedSecondaryActivationIpv6,
       "ggsnCompletedActivationWlan": ggsnCompletedActivationWlan,
       "ggsnCompletedActivationConversational": ggsnCompletedActivationConversational,
       "ggsnCompletedActivationStreaming": ggsnCompletedActivationStreaming,
       "ggsnCompletedActivationInteractive": ggsnCompletedActivationInteractive,
       "ggsnCompletedActivationBackground": ggsnCompletedActivationBackground,
       "ggsnCompletedActivationIpv4v6": ggsnCompletedActivationIpv4v6,
       "ggsnPdpContextsStatsFailed": ggsnPdpContextsStatsFailed,
       "ggsnFailedActivation": ggsnFailedActivation,
       "ggsnGtpStats": ggsnGtpStats,
       "ggsnGtpUplinkPackets": ggsnGtpUplinkPackets,
       "ggsnGtpUplinkBytes": ggsnGtpUplinkBytes,
       "ggsnGtpDownlinkPackets": ggsnGtpDownlinkPackets,
       "ggsnGtpDownlinkBytes": ggsnGtpDownlinkBytes,
       "ggsnGtpControlPacketDrops": ggsnGtpControlPacketDrops,
       "ggsnGtpVerUnsupPacketsReceived": ggsnGtpVerUnsupPacketsReceived,
       "ggsnGtpVerUnsupPacketsSent": ggsnGtpVerUnsupPacketsSent,
       "ggsnGtpEchoReqReceived": ggsnGtpEchoReqReceived,
       "ggsnGtpEchoReqSent": ggsnGtpEchoReqSent,
       "ggsnGtpEchoRespReceived": ggsnGtpEchoRespReceived,
       "ggsnGtpEchoRespSent": ggsnGtpEchoRespSent,
       "ggsnGtpPdpCreateReqReceived": ggsnGtpPdpCreateReqReceived,
       "ggsnGtpPdpCreateRespSent": ggsnGtpPdpCreateRespSent,
       "ggsnGtpPdpUpdateReqReceived": ggsnGtpPdpUpdateReqReceived,
       "ggsnGtpPdpUpdateReqSent": ggsnGtpPdpUpdateReqSent,
       "ggsnGtpPdpUpdateRespReceived": ggsnGtpPdpUpdateRespReceived,
       "ggsnGtpPdpUpdateRespSent": ggsnGtpPdpUpdateRespSent,
       "ggsnGtpPdpDeleteReqReceived": ggsnGtpPdpDeleteReqReceived,
       "ggsnGtpPdpDeleteReqSent": ggsnGtpPdpDeleteReqSent,
       "ggsnGtpPdpDeleteRespReceived": ggsnGtpPdpDeleteRespReceived,
       "ggsnGtpPdpDeleteRespSent": ggsnGtpPdpDeleteRespSent,
       "ggsnGtpRequestsAccepted": ggsnGtpRequestsAccepted,
       "ggsnGtpNbrOfTunnels": ggsnGtpNbrOfTunnels,
       "ggsnGtpNbrOfCreatedTunnels": ggsnGtpNbrOfCreatedTunnels,
       "ggsnGtpPdpInitiateContextActivationRespReceived": ggsnGtpPdpInitiateContextActivationRespReceived,
       "ggsnGtpPdpInitiateContextActivationReqSent": ggsnGtpPdpInitiateContextActivationReqSent,
       "ggsnGtpv0PdpCreateReqReceived": ggsnGtpv0PdpCreateReqReceived,
       "ggsnGtpErrorStats": ggsnGtpErrorStats,
       "ggsnGtpErrorIndicationReceived": ggsnGtpErrorIndicationReceived,
       "ggsnGtpErrorIndicationSent": ggsnGtpErrorIndicationSent,
       "ggsnGtpErrorInvalidRequestFormat": ggsnGtpErrorInvalidRequestFormat,
       "ggsnGtpErrorResourcesUnavailable": ggsnGtpErrorResourcesUnavailable,
       "ggsnGtpErrorDynAddrUnavailable": ggsnGtpErrorDynAddrUnavailable,
       "ggsnGtpErrorMemoryUnavailable": ggsnGtpErrorMemoryUnavailable,
       "ggsnGtpErrorApnUnknown": ggsnGtpErrorApnUnknown,
       "ggsnGtpErrorPdpAddrUnknown": ggsnGtpErrorPdpAddrUnknown,
       "ggsnGtpErrorAuthenticationFailed": ggsnGtpErrorAuthenticationFailed,
       "ggsnGtpErrorSystemFailure": ggsnGtpErrorSystemFailure,
       "ggsnGtpErrorTftSemanticError": ggsnGtpErrorTftSemanticError,
       "ggsnGtpErrorTftSyntaxError": ggsnGtpErrorTftSyntaxError,
       "ggsnGtpErrorPackFiltSemantError": ggsnGtpErrorPackFiltSemantError,
       "ggsnGtpErrorPackFiltSyntaxError": ggsnGtpErrorPackFiltSyntaxError,
       "ggsnGtpErrorMandatoryIEMissing": ggsnGtpErrorMandatoryIEMissing,
       "ggsnGtpErrorMandatoryIEInvalid": ggsnGtpErrorMandatoryIEInvalid,
       "ggsnGtpErrorOptionalIEInvalid": ggsnGtpErrorOptionalIEInvalid,
       "ggsnGtpErrorReferenceInexistent": ggsnGtpErrorReferenceInexistent,
       "ggsnGtpErrorServiceUnsupported": ggsnGtpErrorServiceUnsupported,
       "ggsnGtpErrorInvalidRequestFormatUpd": ggsnGtpErrorInvalidRequestFormatUpd,
       "ggsnGtpErrorInvalidRequestFormatDel": ggsnGtpErrorInvalidRequestFormatDel,
       "ggsnGtpErrorSystemFailureUpd": ggsnGtpErrorSystemFailureUpd,
       "ggsnGtpErrorTftSemanticErrorUpd": ggsnGtpErrorTftSemanticErrorUpd,
       "ggsnGtpErrorTftSyntaxErrorUpd": ggsnGtpErrorTftSyntaxErrorUpd,
       "ggsnGtpErrorPackFiltSemantErrorUpd": ggsnGtpErrorPackFiltSemantErrorUpd,
       "ggsnGtpErrorPackFiltSyntaxErrorUpd": ggsnGtpErrorPackFiltSyntaxErrorUpd,
       "ggsnGtpErrorMandatoryIEMissingUpd": ggsnGtpErrorMandatoryIEMissingUpd,
       "ggsnGtpErrorMandatoryIEMissingDel": ggsnGtpErrorMandatoryIEMissingDel,
       "ggsnGtpErrorMandatoryIEInvalidUpd": ggsnGtpErrorMandatoryIEInvalidUpd,
       "ggsnGtpErrorMandatoryIEInvalidDel": ggsnGtpErrorMandatoryIEInvalidDel,
       "ggsnGtpErrorOptionalIEInvalidUpd": ggsnGtpErrorOptionalIEInvalidUpd,
       "ggsnGtpErrorOptionalIEInvalidDel": ggsnGtpErrorOptionalIEInvalidDel,
       "ggsnGtpErrorReferenceInexistentUpd": ggsnGtpErrorReferenceInexistentUpd,
       "ggsnGtpErrorReferenceInexistentDel": ggsnGtpErrorReferenceInexistentDel,
       "ggsnGtpErrorPdpWithoutTft": ggsnGtpErrorPdpWithoutTft,
       "ggsnGtpErrorApnAccessDenied": ggsnGtpErrorApnAccessDenied,
       "ggsnGtpNewPdpTypeNwPreference": ggsnGtpNewPdpTypeNwPreference,
       "ggsnGtpNewPdpTypeSingleAddressBearerOnly": ggsnGtpNewPdpTypeSingleAddressBearerOnly,
       "ggsnGtpPrStats": ggsnGtpPrStats,
       "ggsnGtpPrEchoReqReceived": ggsnGtpPrEchoReqReceived,
       "ggsnGtpPrEchoRequestsSent": ggsnGtpPrEchoRequestsSent,
       "ggsnGtpPrEchoRespReceived": ggsnGtpPrEchoRespReceived,
       "ggsnGtpPrEchoRespSent": ggsnGtpPrEchoRespSent,
       "ggsnGtpPrVerUnsupPacketsReceived": ggsnGtpPrVerUnsupPacketsReceived,
       "ggsnGtpPrVerUnsupPacketsSent": ggsnGtpPrVerUnsupPacketsSent,
       "ggsnGtpPrNodeAliveReqReceived": ggsnGtpPrNodeAliveReqReceived,
       "ggsnGtpPrNodeAliveReqSent": ggsnGtpPrNodeAliveReqSent,
       "ggsnGtpPrNodeAliveRespReceived": ggsnGtpPrNodeAliveRespReceived,
       "ggsnGtpPrNodeAliveRespSent": ggsnGtpPrNodeAliveRespSent,
       "ggsnGtpPrRedirectReqReceived": ggsnGtpPrRedirectReqReceived,
       "ggsnGtpPrRedirectReqSent": ggsnGtpPrRedirectReqSent,
       "ggsnGtpPrRedirectRespReceived": ggsnGtpPrRedirectRespReceived,
       "ggsnGtpPrRedirectRespSent": ggsnGtpPrRedirectRespSent,
       "ggsnGtpPrDataRecTransferReceived": ggsnGtpPrDataRecTransferReceived,
       "ggsnGtpPrDataRecTransferSent": ggsnGtpPrDataRecTransferSent,
       "ggsnGtpPrSndDataRecordPackets": ggsnGtpPrSndDataRecordPackets,
       "ggsnGtpPrRequestAccepted": ggsnGtpPrRequestAccepted,
       "ggsnGtpPrNoResource": ggsnGtpPrNoResource,
       "ggsnGtpPrServiceUnsupported": ggsnGtpPrServiceUnsupported,
       "ggsnGtpPrSystemFailure": ggsnGtpPrSystemFailure,
       "ggsnGtpPrInvalidMessageFormat": ggsnGtpPrInvalidMessageFormat,
       "ggsnGtpPrVersionUnsupported": ggsnGtpPrVersionUnsupported,
       "ggsnGtpPrRequestUnfulfilled": ggsnGtpPrRequestUnfulfilled,
       "ggsnGtpPrDecodingError": ggsnGtpPrDecodingError,
       "ggsnGtpPrAlreadyFulfilled": ggsnGtpPrAlreadyFulfilled,
       "ggsnGtpPrDupPacketFulfilled": ggsnGtpPrDupPacketFulfilled,
       "ggsnGtpPrErrorStats": ggsnGtpPrErrorStats,
       "ggsnGtpPrErrorMandatoryIEMissing": ggsnGtpPrErrorMandatoryIEMissing,
       "ggsnGtpPrErrorMandatoryIEInvalid": ggsnGtpPrErrorMandatoryIEInvalid,
       "ggsnGtpPrErrorOptionalIEInvalid": ggsnGtpPrErrorOptionalIEInvalid,
       "ggsnGtpPrErrorRefInexistent": ggsnGtpPrErrorRefInexistent,
       "ggsnUplinkTrafficInfo": ggsnUplinkTrafficInfo,
       "ggsnUplinkPackets": ggsnUplinkPackets,
       "ggsnUplinkBytes": ggsnUplinkBytes,
       "ggsnUplinkDrops": ggsnUplinkDrops,
       "ggsnUplinkDropsBytes": ggsnUplinkDropsBytes,
       "ggsnUplinkPacketsIpv6": ggsnUplinkPacketsIpv6,
       "ggsnUplinkBytesIpv6": ggsnUplinkBytesIpv6,
       "ggsnUplinkDropsIpv6": ggsnUplinkDropsIpv6,
       "ggsnUplinkBytesWlan": ggsnUplinkBytesWlan,
       "ggsnUplinkDropsWlan": ggsnUplinkDropsWlan,
       "ggsnUplinkPacketsWlan": ggsnUplinkPacketsWlan,
       "ggsnDownlinkTrafficInfo": ggsnDownlinkTrafficInfo,
       "ggsnDownlinkPackets": ggsnDownlinkPackets,
       "ggsnDownlinkBytes": ggsnDownlinkBytes,
       "ggsnDownlinkDrops": ggsnDownlinkDrops,
       "ggsnDownlinkDropsBytes": ggsnDownlinkDropsBytes,
       "ggsnDownlinkPacketsIpv6": ggsnDownlinkPacketsIpv6,
       "ggsnDownlinkBytesIpv6": ggsnDownlinkBytesIpv6,
       "ggsnDownlinkDropsIpv6": ggsnDownlinkDropsIpv6,
       "ggsnDownlinkBytesWlan": ggsnDownlinkBytesWlan,
       "ggsnDownlinkDropsWlan": ggsnDownlinkDropsWlan,
       "ggsnDownlinkPacketsWlan": ggsnDownlinkPacketsWlan,
       "pdnConnectionsGgsn": pdnConnectionsGgsn,
       "nbrOfGgsnPdnConnections": nbrOfGgsnPdnConnections,
       "ggsnNbrOfSubscribers": ggsnNbrOfSubscribers,
       "ggsnNbrOfSubscribersMean": ggsnNbrOfSubscribersMean,
       "ggsnNbrOfTftFilters": ggsnNbrOfTftFilters,
       "ggsnControlLoad": ggsnControlLoad,
       "ggsnPayloadLoad": ggsnPayloadLoad,
       "ggsnNbrOfActivePdpContextsIpv6": ggsnNbrOfActivePdpContextsIpv6,
       "ggsnNeighborSolicitationRcv": ggsnNeighborSolicitationRcv,
       "ggsnNeighborSolicitationRsp": ggsnNeighborSolicitationRsp,
       "ggsnRouterSolicitationRcv": ggsnRouterSolicitationRcv,
       "ggsnRouterSolicitationRsp": ggsnRouterSolicitationRsp,
       "ggsnL2tpActiveTunnels": ggsnL2tpActiveTunnels,
       "ggsnL2tpMaxActiveTunnels": ggsnL2tpMaxActiveTunnels,
       "ggsnL2tpActiveSessions": ggsnL2tpActiveSessions,
       "ggsnL2tpMaxActiveSessions": ggsnL2tpMaxActiveSessions,
       "ggsnChgEncodedCdrs": ggsnChgEncodedCdrs,
       "ggsnChgFailedEncodedCdrs": ggsnChgFailedEncodedCdrs,
       "ggsnChgGeneratedFtpCdrs": ggsnChgGeneratedFtpCdrs,
       "ggsnChgGeneratedGtppCdrs": ggsnChgGeneratedGtppCdrs,
       "ggsnChgGtppLogCdrs": ggsnChgGtppLogCdrs,
       "ggsnChgGtppAttemptedCdrsSend": ggsnChgGtppAttemptedCdrsSend,
       "ggsnChgGtppCdrsSendFailure": ggsnChgGtppCdrsSendFailure,
       "ggsnNbActivePdpPerTrafficClassConversational": ggsnNbActivePdpPerTrafficClassConversational,
       "ggsnNbActivePdpPerTrafficClassStreaming": ggsnNbActivePdpPerTrafficClassStreaming,
       "ggsnNbActivePdpPerTrafficClassInteractive": ggsnNbActivePdpPerTrafficClassInteractive,
       "ggsnNbActivePdpPerTrafficClassBackground": ggsnNbActivePdpPerTrafficClassBackground,
       "ggsnRadiusAuthenticationFailure": ggsnRadiusAuthenticationFailure,
       "ggsnRadiusAccountingFailure": ggsnRadiusAccountingFailure,
       "ggsnNbrOfActivePdpContextsWlan": ggsnNbrOfActivePdpContextsWlan,
       "ggsn3gdtActiveContexts": ggsn3gdtActiveContexts,
       "ggsn3gdtTotalCompletedEstablishment": ggsn3gdtTotalCompletedEstablishment,
       "ggsn3gdtTotalAttemptedEstablishment": ggsn3gdtTotalAttemptedEstablishment,
       "ggsn3gdtErrorHandling": ggsn3gdtErrorHandling,
       "gn3gdtTotalCompletedEstablishment": gn3gdtTotalCompletedEstablishment,
       "gn3gdtTotalAttemptedEstablishment": gn3gdtTotalAttemptedEstablishment,
       "gn3gdtErrorHandling": gn3gdtErrorHandling,
       "ggsnNbrOfActivePdpContextsIpv4v6": ggsnNbrOfActivePdpContextsIpv4v6,
       "ggsnPicStatsTable": ggsnPicStatsTable,
       "ggsnPicStatsEntry": ggsnPicStatsEntry,
       "ggsnPicIndex": ggsnPicIndex,
       "ggsnPicAddress": ggsnPicAddress,
       "ggsnPicNbrOfActivePdpContexts": ggsnPicNbrOfActivePdpContexts,
       "ggsnApnStatsTable": ggsnApnStatsTable,
       "ggsnApnStatsEntry": ggsnApnStatsEntry,
       "ggsnApnIndex": ggsnApnIndex,
       "ggsnApnName": ggsnApnName,
       "ggsnApnActivePdpContextCount": ggsnApnActivePdpContextCount,
       "ggsnApnAttemptedActivation": ggsnApnAttemptedActivation,
       "ggsnApnAttemptedDynActivation": ggsnApnAttemptedDynActivation,
       "ggsnApnAttemptedDeactivation": ggsnApnAttemptedDeactivation,
       "ggsnApnAttemptedSelfDeactivation": ggsnApnAttemptedSelfDeactivation,
       "ggsnApnCompletedActivation": ggsnApnCompletedActivation,
       "ggsnApnCompletedDynActivation": ggsnApnCompletedDynActivation,
       "ggsnApnCompletedDeactivation": ggsnApnCompletedDeactivation,
       "ggsnApnCompletedSelfDeactivation": ggsnApnCompletedSelfDeactivation,
       "ggsnApnUplinkPackets": ggsnApnUplinkPackets,
       "ggsnApnUplinkBytes": ggsnApnUplinkBytes,
       "ggsnApnUplinkDrops": ggsnApnUplinkDrops,
       "ggsnApnDownlinkPackets": ggsnApnDownlinkPackets,
       "ggsnApnDownlinkBytes": ggsnApnDownlinkBytes,
       "ggsnApnDownlinkDrops": ggsnApnDownlinkDrops,
       "ggsnApnAttemptedMSActivation": ggsnApnAttemptedMSActivation,
       "ggsnApnCompletedMSActivation": ggsnApnCompletedMSActivation,
       "ggsnApnAttemptedMSDeactivation": ggsnApnAttemptedMSDeactivation,
       "ggsnApnCompletedMSDeactivation": ggsnApnCompletedMSDeactivation,
       "ggsnApnActivePdpContextMax": ggsnApnActivePdpContextMax,
       "ggsnApnActivePdpContextMean": ggsnApnActivePdpContextMean,
       "ggsnApnAttemptedAuthActivation": ggsnApnAttemptedAuthActivation,
       "ggsnApnFailedAuthActivation": ggsnApnFailedAuthActivation,
       "ggsnApnAttemptedUpdateMsAndSgsn": ggsnApnAttemptedUpdateMsAndSgsn,
       "ggsnApnCompletedUpdateMsAndSgsn": ggsnApnCompletedUpdateMsAndSgsn,
       "ggsnApnNbrOfTftFilters": ggsnApnNbrOfTftFilters,
       "ggsnApnSessTimeoutDeactivation": ggsnApnSessTimeoutDeactivation,
       "ggsnApnIdleTimeoutDeactivation": ggsnApnIdleTimeoutDeactivation,
       "ggsnApnGiSignalingInPackets": ggsnApnGiSignalingInPackets,
       "ggsnApnGiSignalingInBytes": ggsnApnGiSignalingInBytes,
       "ggsnApnGiSignalingOutPackets": ggsnApnGiSignalingOutPackets,
       "ggsnApnGiSignalingOutBytes": ggsnApnGiSignalingOutBytes,
       "ggsnApnActivePdpContextCountIpv6": ggsnApnActivePdpContextCountIpv6,
       "ggsnApnAttemptedActivationIpv6": ggsnApnAttemptedActivationIpv6,
       "ggsnApnCompletedActivationIpv6": ggsnApnCompletedActivationIpv6,
       "ggsnApnUplinkPacketsIpv6": ggsnApnUplinkPacketsIpv6,
       "ggsnApnUplinkBytesIpv6": ggsnApnUplinkBytesIpv6,
       "ggsnApnUplinkDropsIpv6": ggsnApnUplinkDropsIpv6,
       "ggsnApnDownlinkPacketsIpv6": ggsnApnDownlinkPacketsIpv6,
       "ggsnApnDownlinkBytesIpv6": ggsnApnDownlinkBytesIpv6,
       "ggsnApnDownlinkDropsIpv6": ggsnApnDownlinkDropsIpv6,
       "ggsnApnNeighborSolicitationRcv": ggsnApnNeighborSolicitationRcv,
       "ggsnApnNeighborSolicitationRsp": ggsnApnNeighborSolicitationRsp,
       "ggsnApnRouterSolicitationRcv": ggsnApnRouterSolicitationRcv,
       "ggsnApnRouterSolicitationRsp": ggsnApnRouterSolicitationRsp,
       "ggsnNbApnActivePdpPerTrafficClassConversational": ggsnNbApnActivePdpPerTrafficClassConversational,
       "ggsnNbApnActivePdpPerTrafficClassStreaming": ggsnNbApnActivePdpPerTrafficClassStreaming,
       "ggsnNbApnActivePdpPerTrafficClassInteractive": ggsnNbApnActivePdpPerTrafficClassInteractive,
       "ggsnNbApnActivePdpPerTrafficClassBackground": ggsnNbApnActivePdpPerTrafficClassBackground,
       "ggsnApnImsDedicatedCompletedActivation": ggsnApnImsDedicatedCompletedActivation,
       "ggsnApnImsDedicatedNotConfiguredActivationFailed": ggsnApnImsDedicatedNotConfiguredActivationFailed,
       "ggsnApnImsGeneralPurposeCompletedActivation": ggsnApnImsGeneralPurposeCompletedActivation,
       "ggsnApnImsGeneralNotConfiguredActivationFailed": ggsnApnImsGeneralNotConfiguredActivationFailed,
       "ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured": ggsnApnActivationFailedDuetoGeneralPurposeNotConfigured,
       "ggsnApnUnauthorizedImsPackets": ggsnApnUnauthorizedImsPackets,
       "ggsnApnRadiusAccountingFailure": ggsnApnRadiusAccountingFailure,
       "ggsnApnRadiusAuthenticationFailure": ggsnApnRadiusAuthenticationFailure,
       "ggsnApnSaccRsInstalledDynRules": ggsnApnSaccRsInstalledDynRules,
       "ggsnApnSaccRsActivePredefinedChargingRules": ggsnApnSaccRsActivePredefinedChargingRules,
       "ggsnApnSaccRsActivePredefinedChargingRuleBases": ggsnApnSaccRsActivePredefinedChargingRuleBases,
       "ggsnApnAvailableIpAddressesInInternalPool": ggsnApnAvailableIpAddressesInInternalPool,
       "ggsnApnIpAddressesInQuarantineInInternalPool": ggsnApnIpAddressesInQuarantineInInternalPool,
       "ggsnApn3gdtActiveContexts": ggsnApn3gdtActiveContexts,
       "ggsnApn3gdtTotalCompletedEstablishment": ggsnApn3gdtTotalCompletedEstablishment,
       "ggsnApn3gdtTotalAttemptedEstablishment": ggsnApn3gdtTotalAttemptedEstablishment,
       "ggsnApn3gdtErrorHandling": ggsnApn3gdtErrorHandling,
       "ggsnApnAttemptedUpdateGgsn": ggsnApnAttemptedUpdateGgsn,
       "ggsnApnCompletedUpdateGgsn": ggsnApnCompletedUpdateGgsn,
       "ggsnApnAttemptedActivationNonDuplicated": ggsnApnAttemptedActivationNonDuplicated,
       "ggsnApnActivePdpContextMaxDuringLastPeriod": ggsnApnActivePdpContextMaxDuringLastPeriod,
       "pgwApnActiveEpsBearer": pgwApnActiveEpsBearer,
       "pgwApnActiveIpv6EpsBearer": pgwApnActiveIpv6EpsBearer,
       "pgwApnAttemptedEpsBearerActivation": pgwApnAttemptedEpsBearerActivation,
       "pgwApnCompletedEpsBearerActivation": pgwApnCompletedEpsBearerActivation,
       "pgwApnAttemptedIpv6EpsBearerActivation": pgwApnAttemptedIpv6EpsBearerActivation,
       "pgwApnCompletedIpv6EpsBearerActivation": pgwApnCompletedIpv6EpsBearerActivation,
       "pgwApnAttemptedEpsBearerDeactivation": pgwApnAttemptedEpsBearerDeactivation,
       "pgwApnCompletedEpsBearerDeactivation": pgwApnCompletedEpsBearerDeactivation,
       "pgwApnAttemptedS5NetworkDeactivation": pgwApnAttemptedS5NetworkDeactivation,
       "pgwApnCompletedS5NetworkDeactivation": pgwApnCompletedS5NetworkDeactivation,
       "pgwApnAttemptedS5UeSgwModification": pgwApnAttemptedS5UeSgwModification,
       "pgwApnCompletedS5UeSgwModification": pgwApnCompletedS5UeSgwModification,
       "pgwApnAttemptedS5SgwSgsnModification": pgwApnAttemptedS5SgwSgsnModification,
       "pgwApnCompletedS5SgwSgsnModification": pgwApnCompletedS5SgwSgsnModification,
       "pgwApnAttemptedS5SgsnSgwModification": pgwApnAttemptedS5SgsnSgwModification,
       "pgwApnCompletedS5SgsnSgwModification": pgwApnCompletedS5SgsnSgwModification,
       "pgwApnAttemptedS5NetworkModification": pgwApnAttemptedS5NetworkModification,
       "pgwApnCompletedS5NetworkModification": pgwApnCompletedS5NetworkModification,
       "pgwApnAttemptedS5UeSgwDeactivation": pgwApnAttemptedS5UeSgwDeactivation,
       "pgwApnCompletedS5UeSgwDeactivation": pgwApnCompletedS5UeSgwDeactivation,
       "gnApnUplinkPackets": gnApnUplinkPackets,
       "gnApnUplinkBytes": gnApnUplinkBytes,
       "gnApnUplinkPacketsIpv6": gnApnUplinkPacketsIpv6,
       "gnApnUplinkBytesIpv6": gnApnUplinkBytesIpv6,
       "gnApnDownlinkPackets": gnApnDownlinkPackets,
       "gnApnDownlinkBytes": gnApnDownlinkBytes,
       "gnApnDownlinkPacketsIpv6": gnApnDownlinkPacketsIpv6,
       "gnApnDownlinkBytesIpv6": gnApnDownlinkBytesIpv6,
       "s5ApnUplinkPackets": s5ApnUplinkPackets,
       "s5ApnUplinkBytes": s5ApnUplinkBytes,
       "s5ApnUplinkPacketsIpv6": s5ApnUplinkPacketsIpv6,
       "s5ApnUplinkBytesIpv6": s5ApnUplinkBytesIpv6,
       "s5ApnDownlinkPackets": s5ApnDownlinkPackets,
       "s5ApnDownlinkBytes": s5ApnDownlinkBytes,
       "s5ApnDownlinkPacketsIpv6": s5ApnDownlinkPacketsIpv6,
       "s5ApnDownlinkBytesIpv6": s5ApnDownlinkBytesIpv6,
       "gnApn3gdtUplinkBytes": gnApn3gdtUplinkBytes,
       "gnApn3gdtUplinkBytesIpv6": gnApn3gdtUplinkBytesIpv6,
       "gnApn3gdtUplinkPackets": gnApn3gdtUplinkPackets,
       "gnApn3gdtUplinkPacketsIpv6": gnApn3gdtUplinkPacketsIpv6,
       "gnApn3gdtDownlinkBytes": gnApn3gdtDownlinkBytes,
       "gnApn3gdtDownlinkBytesIpv6": gnApn3gdtDownlinkBytesIpv6,
       "gnApn3gdtDownlinkPackets": gnApn3gdtDownlinkPackets,
       "gnApn3gdtDownlinkPacketsIpv6": gnApn3gdtDownlinkPacketsIpv6,
       "gnApn3gdtDownlinkDropsErrorHandling": gnApn3gdtDownlinkDropsErrorHandling,
       "ggsnApn3gdtGtpError": ggsnApn3gdtGtpError,
       "gnApn3gdtTotalCompletedEstablishment": gnApn3gdtTotalCompletedEstablishment,
       "gnApn3gdtTotalAttemptedEstablishment": gnApn3gdtTotalAttemptedEstablishment,
       "gnApn3gdtErrorHandling": gnApn3gdtErrorHandling,
       "pgwApnActiveDedicatedEpsBearer": pgwApnActiveDedicatedEpsBearer,
       "pgwApnAttemptedDedicatedEpsBearerActivation": pgwApnAttemptedDedicatedEpsBearerActivation,
       "pgwApnCompletedDedicatedEpsBearerActivation": pgwApnCompletedDedicatedEpsBearerActivation,
       "pgwApnAttemptedIpv6DedicatedEpsBearerActivation": pgwApnAttemptedIpv6DedicatedEpsBearerActivation,
       "pgwApnCompletedIpv6DedicatedEpsBearerActivation": pgwApnCompletedIpv6DedicatedEpsBearerActivation,
       "pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation": pgwApnAttemptedS5NetworkDedicatedEpsBearerDeactivation,
       "pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation": pgwApnCompletedS5NetworkDedicatedEpsBearerDeactivation,
       "pgwApnAttemptedS5NetworkDedicatedEpsBearerModification": pgwApnAttemptedS5NetworkDedicatedEpsBearerModification,
       "pgwApnCompletedS5NetworkDedicatedEpsBearerModification": pgwApnCompletedS5NetworkDedicatedEpsBearerModification,
       "pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation": pgwApnAttemptedS5UeSgwDedicatedEpsBearerDeactivation,
       "pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation": pgwApnCompletedS5UeSgwDedicatedEpsBearerDeactivation,
       "ggsnApnActivePdpContextCountIpv4v6": ggsnApnActivePdpContextCountIpv4v6,
       "pgwApnActiveIpv4v6EpsBearer": pgwApnActiveIpv4v6EpsBearer,
       "ggsnApnAttemptedActivationIpv4v6": ggsnApnAttemptedActivationIpv4v6,
       "ggsnApnCompletedActivationIpv4v6": ggsnApnCompletedActivationIpv4v6,
       "pgwApnAttemptedIpv4v6EpsBearerActivation": pgwApnAttemptedIpv4v6EpsBearerActivation,
       "pgwApnCompletedIpv4v6EpsBearerActivation": pgwApnCompletedIpv4v6EpsBearerActivation,
       "pgwApnActiveWlanEpsBearer": pgwApnActiveWlanEpsBearer,
       "s2aApnUplinkPackets": s2aApnUplinkPackets,
       "s2aApnUplinkBytes": s2aApnUplinkBytes,
       "s2aApnDownlinkPackets": s2aApnDownlinkPackets,
       "s2aApnDownlinkBytes": s2aApnDownlinkBytes,
       "s2aApnUplinkPacketsIpv6": s2aApnUplinkPacketsIpv6,
       "s2aApnUplinkBytesIpv6": s2aApnUplinkBytesIpv6,
       "s2aApnDownlinkPacketsIpv6": s2aApnDownlinkPacketsIpv6,
       "s2aApnDownlinkBytesIpv6": s2aApnDownlinkBytesIpv6,
       "ggsnSgsnStatsTable": ggsnSgsnStatsTable,
       "ggsnSgsnStatsEntry": ggsnSgsnStatsEntry,
       "ggsnSgsnIndex": ggsnSgsnIndex,
       "ggsnSgsnAddress": ggsnSgsnAddress,
       "ggsnSgsnUplinkPackets": ggsnSgsnUplinkPackets,
       "ggsnSgsnUplinkBytes": ggsnSgsnUplinkBytes,
       "ggsnSgsnUplinkDrops": ggsnSgsnUplinkDrops,
       "ggsnSgsnDownlinkPackets": ggsnSgsnDownlinkPackets,
       "ggsnSgsnDownlinkBytes": ggsnSgsnDownlinkBytes,
       "ggsnSgsnDownlinkDrops": ggsnSgsnDownlinkDrops,
       "ggsnL2tpTunnelStatsTable": ggsnL2tpTunnelStatsTable,
       "ggsnL2tpTunnelStatsEntry": ggsnL2tpTunnelStatsEntry,
       "ggsnL2tpTunnelIndex": ggsnL2tpTunnelIndex,
       "ggsnL2tpTunnelLocalTID": ggsnL2tpTunnelLocalTID,
       "ggsnL2tpTunnelRemoteTID": ggsnL2tpTunnelRemoteTID,
       "ggsnL2tpTunnelLocalIp": ggsnL2tpTunnelLocalIp,
       "ggsnL2tpTunnelRemoteIp": ggsnL2tpTunnelRemoteIp,
       "ggsnL2tpTunnelActiveSessions": ggsnL2tpTunnelActiveSessions,
       "ggsnL2tpTunnelControlTxPackets": ggsnL2tpTunnelControlTxPackets,
       "ggsnL2tpTunnelControlRxPackets": ggsnL2tpTunnelControlRxPackets,
       "ggsnL2tpTunnelDataTxPackets": ggsnL2tpTunnelDataTxPackets,
       "ggsnL2tpTunnelDataRxPackets": ggsnL2tpTunnelDataRxPackets,
       "ggsnL2tpTunnelDiscardedTxPackets": ggsnL2tpTunnelDiscardedTxPackets,
       "ggsnL2tpTunnelDiscardedRxPackets": ggsnL2tpTunnelDiscardedRxPackets,
       "pgwGlobalStats": pgwGlobalStats,
       "pgwAttemptedEpsBearerStats": pgwAttemptedEpsBearerStats,
       "pgwAttemptedEpsBearerActivation": pgwAttemptedEpsBearerActivation,
       "pgwAttemptedEpsBearerIpv6Activation": pgwAttemptedEpsBearerIpv6Activation,
       "pgwAttemptedEpsBearerModification": pgwAttemptedEpsBearerModification,
       "pgwAttemptedEpsBearerDeactivation": pgwAttemptedEpsBearerDeactivation,
       "pgwAttemptedDedicatedEpsBearerActivation": pgwAttemptedDedicatedEpsBearerActivation,
       "pgwAttemptedDedicatedEpsBearerIpv6Activation": pgwAttemptedDedicatedEpsBearerIpv6Activation,
       "pgwAttemptedEpsBearerIpv4v6Activation": pgwAttemptedEpsBearerIpv4v6Activation,
       "pgwAttempteds2aEpsBearerActivation": pgwAttempteds2aEpsBearerActivation,
       "pgwCompletedEpsBearerStats": pgwCompletedEpsBearerStats,
       "pgwCompletedEpsBearerActivation": pgwCompletedEpsBearerActivation,
       "pgwCompletedEpsBearerIpv6Activation": pgwCompletedEpsBearerIpv6Activation,
       "pgwCompletedEpsBearerModification": pgwCompletedEpsBearerModification,
       "pgwCompletedEpsBearerDeactivation": pgwCompletedEpsBearerDeactivation,
       "pgwCompletedDedicatedEpsBearerActivation": pgwCompletedDedicatedEpsBearerActivation,
       "pgwCompletedDedicatedEpsBearerIpv6Activation": pgwCompletedDedicatedEpsBearerIpv6Activation,
       "pgwCompletedEpsBearerIpv4v6Activation": pgwCompletedEpsBearerIpv4v6Activation,
       "pgwCompleteds2aEpsBearerActivation": pgwCompleteds2aEpsBearerActivation,
       "pgwNbrOfActiveEpsBearer": pgwNbrOfActiveEpsBearer,
       "pgwNbrOfActiveIpv6EpsBearer": pgwNbrOfActiveIpv6EpsBearer,
       "pgwNbrOfActiveIpv4v6EpsBearer": pgwNbrOfActiveIpv4v6EpsBearer,
       "pgwWlanNbrOfActiveEpsBearer": pgwWlanNbrOfActiveEpsBearer,
       "s6bInterface": s6bInterface,
       "s6bAarSent": s6bAarSent,
       "s6bAaaSuccRcvd": s6bAaaSuccRcvd,
       "s6bAaaFailRcvd": s6bAaaFailRcvd,
       "s6bAaaInvalidRcvd": s6bAaaInvalidRcvd,
       "s6bStrSent": s6bStrSent,
       "s6bStaSuccRcvd": s6bStaSuccRcvd,
       "s6bStaFailRcvd": s6bStaFailRcvd,
       "pdnConnectionsPgw": pdnConnectionsPgw,
       "nbrOfPgwPdnConnections": nbrOfPgwPdnConnections,
       "nbrOfPiscPdnConnections": nbrOfPiscPdnConnections,
       "nbrOfOnlineChargingPdnConnections": nbrOfOnlineChargingPdnConnections,
       "nbrOfDynamicPolicyControlPdnConnections": nbrOfDynamicPolicyControlPdnConnections,
       "nbrOfWlanPdnConnections": nbrOfWlanPdnConnections,
       "nbrOfGeranPdnConnections": nbrOfGeranPdnConnections,
       "nbrOfUtranPdnConnections": nbrOfUtranPdnConnections,
       "nbrOfHspaEvolutionPdnConnections": nbrOfHspaEvolutionPdnConnections,
       "nbrOfEutranPdnConnections": nbrOfEutranPdnConnections,
       "ggsnNodeName": ggsnNodeName,
       "pgwRRreroutedStatsTable": pgwRRreroutedStatsTable,
       "pgwRRreroutedStatsEntry": pgwRRreroutedStatsEntry,
       "pgwRoutingInstanceId": pgwRoutingInstanceId,
       "pgwRoutingInstanceName": pgwRoutingInstanceName,
       "pgwRRreroutedDataDownlinkPkts": pgwRRreroutedDataDownlinkPkts,
       "pgwRRreroutedDataRxPkts": pgwRRreroutedDataRxPkts,
       "pgwRRreroutedDataTxPkts": pgwRRreroutedDataTxPkts,
       "pgwRRreroutedDataIpv6DownlinkPkts": pgwRRreroutedDataIpv6DownlinkPkts,
       "pgwRRreroutedDataIpv6RxPkts": pgwRRreroutedDataIpv6RxPkts,
       "pgwRRreroutedDataIpv6TxPkts": pgwRRreroutedDataIpv6TxPkts,
       "ggsnGtpcInfo": ggsnGtpcInfo,
       "ggsnGtpcTable": ggsnGtpcTable,
       "ggsnGtpcEntry": ggsnGtpcEntry,
       "ggsnGtpcIndex": ggsnGtpcIndex,
       "ggsnGtpcVersion": ggsnGtpcVersion,
       "ggsnGtpcAddress": ggsnGtpcAddress,
       "ggsnGtpcPdpCapacity": ggsnGtpcPdpCapacity,
       "ggsnGtpcRole": ggsnGtpcRole,
       "ggsnGtpcStatus": ggsnGtpcStatus,
       "ggsnGtpcControlPacketDrops": ggsnGtpcControlPacketDrops,
       "ggsnGtpcNbrOfActivePdpContexts": ggsnGtpcNbrOfActivePdpContexts,
       "ggsnGtpcMemory": ggsnGtpcMemory,
       "ggsnGtpcMemoryUsed": ggsnGtpcMemoryUsed,
       "ggsnGtpcCpuUsage": ggsnGtpcCpuUsage,
       "ggsnGtpcTftFilterDepthMax": ggsnGtpcTftFilterDepthMax,
       "ggsnGtpcTftFilterDepthMean": ggsnGtpcTftFilterDepthMean,
       "ggsnGtpcControlLoad": ggsnGtpcControlLoad,
       "ggsnGtpcNbrOfActivePdpContextsIpv6": ggsnGtpcNbrOfActivePdpContextsIpv6,
       "ggsnGtpcPeakCpuUsage": ggsnGtpcPeakCpuUsage,
       "ggsnGtpcNbrOfActivePdpContextsIpv4v6": ggsnGtpcNbrOfActivePdpContextsIpv4v6,
       "ggsnChargingInfo": ggsnChargingInfo,
       "ggsnAcctPartialRecordGenerated": ggsnAcctPartialRecordGenerated,
       "ggsnAcctBillingGatewayTable": ggsnAcctBillingGatewayTable,
       "ggsnAcctBillingGatewayEntry": ggsnAcctBillingGatewayEntry,
       "ggsnAcctBillingGatewayIndex": ggsnAcctBillingGatewayIndex,
       "ggsnAcctBillingGatewayAddress": ggsnAcctBillingGatewayAddress,
       "ggsnAcctDataRecTransReqSent": ggsnAcctDataRecTransReqSent,
       "ggsnAcctDataRecTransReqSentDup": ggsnAcctDataRecTransReqSentDup,
       "ggsnAcctDataRecTransReqCancelled": ggsnAcctDataRecTransReqCancelled,
       "ggsnAcctDataRecTransRespReceived": ggsnAcctDataRecTransRespReceived,
       "ggsnAcctRedirectionReqReceived": ggsnAcctRedirectionReqReceived,
       "ggsnAcctRedirectionRespSent": ggsnAcctRedirectionRespSent,
       "ggsnDhcpInfo": ggsnDhcpInfo,
       "ggsnDhcpClientAddress": ggsnDhcpClientAddress,
       "ggsnDhcpServerTable": ggsnDhcpServerTable,
       "ggsnDhcpServerEntry": ggsnDhcpServerEntry,
       "ggsnDhcpServerIndex": ggsnDhcpServerIndex,
       "ggsnDhcpServerAddress": ggsnDhcpServerAddress,
       "ggsnDhcpServerName": ggsnDhcpServerName,
       "ggsnDhcpClientYiaddr": ggsnDhcpClientYiaddr,
       "ggsnDhcpClientState": ggsnDhcpClientState,
       "ggsnDhcpClientRequestsSent": ggsnDhcpClientRequestsSent,
       "ggsnDhcpClientRepliesReceived": ggsnDhcpClientRepliesReceived,
       "ggsnDhcpClientRepliesDiscarded": ggsnDhcpClientRepliesDiscarded,
       "ggsnDhcpClientDiscoversSent": ggsnDhcpClientDiscoversSent,
       "ggsnDhcpClientDeclinesSent": ggsnDhcpClientDeclinesSent,
       "ggsnDhcpClientReleasesSent": ggsnDhcpClientReleasesSent,
       "ggsnDhcpClientOffersReceived": ggsnDhcpClientOffersReceived,
       "ggsnDhcpClientAcksReceived": ggsnDhcpClientAcksReceived,
       "ggsnDhcpClientNaksReceived": ggsnDhcpClientNaksReceived,
       "ggsnDhcpClientSendErrors": ggsnDhcpClientSendErrors,
       "ggsnDhcpServerRoutingInstance": ggsnDhcpServerRoutingInstance,
       "ggsnAlarmInfo": ggsnAlarmInfo,
       "ggsnAlarmNumber": ggsnAlarmNumber,
       "ggsnAlarmCriticalNumber": ggsnAlarmCriticalNumber,
       "ggsnAlarmMajorNumber": ggsnAlarmMajorNumber,
       "ggsnAlarmMinorNumber": ggsnAlarmMinorNumber,
       "ggsnAlarmWarningNumber": ggsnAlarmWarningNumber,
       "ggsnAlarmUnknownNumber": ggsnAlarmUnknownNumber,
       "ggsnAlarmTable": ggsnAlarmTable,
       "ggsnAlarmEntry": ggsnAlarmEntry,
       "ggsnAlarmId": ggsnAlarmId,
       "ggsnAlarmName": ggsnAlarmName,
       "ggsnAlarmTime": ggsnAlarmTime,
       "ggsnAlarmSourceId": ggsnAlarmSourceId,
       "ggsnAlarmObjectClass": ggsnAlarmObjectClass,
       "ggsnAlarmObjectInstance": ggsnAlarmObjectInstance,
       "ggsnAlarmSeverity": ggsnAlarmSeverity,
       "ggsnAlarmDescription": ggsnAlarmDescription,
       "ggsnAlarmHistTable": ggsnAlarmHistTable,
       "ggsnAlarmHistEntry": ggsnAlarmHistEntry,
       "ggsnAlarmHistTime": ggsnAlarmHistTime,
       "ggsnAlarmHistEventCause": ggsnAlarmHistEventCause,
       "ggsnAlarmHistAlarmId": ggsnAlarmHistAlarmId,
       "ggsnAlarmHistAlarmName": ggsnAlarmHistAlarmName,
       "ggsnAlarmHistAlarmTime": ggsnAlarmHistAlarmTime,
       "ggsnAlarmHistAlarmSourceId": ggsnAlarmHistAlarmSourceId,
       "ggsnAlarmHistAlarmObjInstance": ggsnAlarmHistAlarmObjInstance,
       "ggsnAlarmHistAlarmSeverity": ggsnAlarmHistAlarmSeverity,
       "ggsnAlarmHistAlarmDescription": ggsnAlarmHistAlarmDescription,
       "ggsnGtpuInfo": ggsnGtpuInfo,
       "ggsnGtpuTable": ggsnGtpuTable,
       "ggsnGtpuEntry": ggsnGtpuEntry,
       "ggsnGtpuIndex": ggsnGtpuIndex,
       "ggsnGtpuVersion": ggsnGtpuVersion,
       "ggsnGtpuAddress": ggsnGtpuAddress,
       "ggsnGtpuPdpCapacity": ggsnGtpuPdpCapacity,
       "ggsnGtpuRole": ggsnGtpuRole,
       "ggsnGtpuStatus": ggsnGtpuStatus,
       "ggsnGtpuUserUplinkDrops": ggsnGtpuUserUplinkDrops,
       "ggsnGtpuUserDownlinkDrops": ggsnGtpuUserDownlinkDrops,
       "ggsnGtpuNbrOfActivePdpContexts": ggsnGtpuNbrOfActivePdpContexts,
       "ggsnGtpuMemory": ggsnGtpuMemory,
       "ggsnGtpuMemoryUsed": ggsnGtpuMemoryUsed,
       "ggsnGtpuCpuUsage": ggsnGtpuCpuUsage,
       "ggsnGtpuPayloadLoad": ggsnGtpuPayloadLoad,
       "ggsnGtpuNbrOfActivePdpContextsIpv6": ggsnGtpuNbrOfActivePdpContextsIpv6,
       "ggsnGtpuPeakCpuUsage": ggsnGtpuPeakCpuUsage,
       "ggsnGtpuUplinkPackets": ggsnGtpuUplinkPackets,
       "ggsnGtpuDownlinkPackets": ggsnGtpuDownlinkPackets,
       "ggsnGtpuNbrOfActivePdpContextsIpv4v6": ggsnGtpuNbrOfActivePdpContextsIpv4v6,
       "ggsnFbcInfo": ggsnFbcInfo,
       "ggsnFbcStats": ggsnFbcStats,
       "ggsnFbcInitiatedDeactivation": ggsnFbcInitiatedDeactivation,
       "ggsnFbcApplicationTransactionPps": ggsnFbcApplicationTransactionPps,
       "ggsnFbcApplicationTransactionPrs": ggsnFbcApplicationTransactionPrs,
       "ggsnApnFbcStatsTable": ggsnApnFbcStatsTable,
       "ggsnApnFbcStatsEntry": ggsnApnFbcStatsEntry,
       "ggsnApnFbcNbrOfPpsUsers": ggsnApnFbcNbrOfPpsUsers,
       "ggsnApnFbcNbrOfPpsPdpContexts": ggsnApnFbcNbrOfPpsPdpContexts,
       "ggsnApnFbcPpsCreate": ggsnApnFbcPpsCreate,
       "ggsnApnFbcPpsReject": ggsnApnFbcPpsReject,
       "ggsnApnFbcInitiatedDeactivation": ggsnApnFbcInitiatedDeactivation,
       "ggsnApnFbcInitialPrsReq": ggsnApnFbcInitialPrsReq,
       "ggsnApnFbcInitialPrsReqFailed": ggsnApnFbcInitialPrsReqFailed,
       "ggsnApnFbcUpdPrsReq": ggsnApnFbcUpdPrsReq,
       "ggsnApnFbcUpdPrsReqFailed": ggsnApnFbcUpdPrsReqFailed,
       "ggsnApnFbcStartCredReq": ggsnApnFbcStartCredReq,
       "ggsnApnFbcStartCredReqFailed": ggsnApnFbcStartCredReqFailed,
       "ggsnApnFbcUpdCredReq": ggsnApnFbcUpdCredReq,
       "ggsnApnFbcUpdCredReqFailed": ggsnApnFbcUpdCredReqFailed,
       "ggsnApnFbcStopCredReq": ggsnApnFbcStopCredReq,
       "ggsnApnFbcStopCredReqFailed": ggsnApnFbcStopCredReqFailed,
       "ggsnApnFbcExtPrsUpd": ggsnApnFbcExtPrsUpd,
       "ggsnApnFbcExtCreditUpd": ggsnApnFbcExtCreditUpd,
       "ggsnApnFbcDurationTime": ggsnApnFbcDurationTime,
       "ggsnApnFbcActivationBearerCtrlAccept": ggsnApnFbcActivationBearerCtrlAccept,
       "ggsnApnFbcActivationBearerCtrlReject": ggsnApnFbcActivationBearerCtrlReject,
       "ggsnApnFbcActivationBearerCtrlUpgrade": ggsnApnFbcActivationBearerCtrlUpgrade,
       "ggsnApnFbcActivationBearerCtrlDowngrade": ggsnApnFbcActivationBearerCtrlDowngrade,
       "ggsnApnFbcModificationBearerCtrlAccept": ggsnApnFbcModificationBearerCtrlAccept,
       "ggsnApnFbcModificationBearerCtrlDeactivate": ggsnApnFbcModificationBearerCtrlDeactivate,
       "ggsnApnFbcModificationBearerCtrlUpgrade": ggsnApnFbcModificationBearerCtrlUpgrade,
       "ggsnApnFbcModificationBearerCtrlDowngrade": ggsnApnFbcModificationBearerCtrlDowngrade,
       "ggsnApnFbcActivationNoBearerCtrlAccept": ggsnApnFbcActivationNoBearerCtrlAccept,
       "ggsnApnFbcActivationNoBearerCtrlReject": ggsnApnFbcActivationNoBearerCtrlReject,
       "ggsnApnFbcActivationNoBearerCtrlDowngrade": ggsnApnFbcActivationNoBearerCtrlDowngrade,
       "ggsnApnFbcModificationNoBearerCtrlAccept": ggsnApnFbcModificationNoBearerCtrlAccept,
       "ggsnApnFbcModificationNoBearerCtrlDeactivate": ggsnApnFbcModificationNoBearerCtrlDeactivate,
       "ggsnApnFbcModificationNoBearerCtrlDowngrade": ggsnApnFbcModificationNoBearerCtrlDowngrade,
       "ggsnApnSaccAttemptedServiceInitiatedQoSModification": ggsnApnSaccAttemptedServiceInitiatedQoSModification,
       "ggsnApnFbcServIdentStatsTable": ggsnApnFbcServIdentStatsTable,
       "ggsnApnFbcServIdentStatsEntry": ggsnApnFbcServIdentStatsEntry,
       "ggsnServIdentIndex": ggsnServIdentIndex,
       "ggsnApnFbcServIdentUplinkBytes": ggsnApnFbcServIdentUplinkBytes,
       "ggsnApnFbcServIdentDownlinkBytes": ggsnApnFbcServIdentDownlinkBytes,
       "ggsnApnFbcServIdentEventTrans": ggsnApnFbcServIdentEventTrans,
       "ggsnApnFbcServIdentEventTransFail": ggsnApnFbcServIdentEventTransFail,
       "ggsnApnFbcServIdentEventStartTrans": ggsnApnFbcServIdentEventStartTrans,
       "ggsnApnFbcServIdentEventSuccessTrans": ggsnApnFbcServIdentEventSuccessTrans,
       "ggsnApnFbcServClassStatsTable": ggsnApnFbcServClassStatsTable,
       "ggsnApnFbcServClassStatsEntry": ggsnApnFbcServClassStatsEntry,
       "ggsnServClassIndex": ggsnServClassIndex,
       "ggsnApnFbcServClassUplinkBytes": ggsnApnFbcServClassUplinkBytes,
       "ggsnApnFbcServClassDownlinkBytes": ggsnApnFbcServClassDownlinkBytes,
       "ggsnApnFbcServClassActiveTime": ggsnApnFbcServClassActiveTime,
       "ggsnFbcExtPrsUpdReqNoMatch": ggsnFbcExtPrsUpdReqNoMatch,
       "ggsnFbcExtCreditUpdReqNoMatch": ggsnFbcExtCreditUpdReqNoMatch,
       "ggsnFbcExtUpdReqFailure": ggsnFbcExtUpdReqFailure,
       "ggsnApnFbcPrasStatsTable": ggsnApnFbcPrasStatsTable,
       "ggsnApnFbcPrasStatsEntry": ggsnApnFbcPrasStatsEntry,
       "ggsnPrasIndex": ggsnPrasIndex,
       "ggsnApnFbcPrasName": ggsnApnFbcPrasName,
       "ggsnApnFbcPrasStartReq": ggsnApnFbcPrasStartReq,
       "ggsnApnFbcPrasStartReqFail": ggsnApnFbcPrasStartReqFail,
       "ggsnApnFbcPrasUpdateReq": ggsnApnFbcPrasUpdateReq,
       "ggsnApnFbcPrasUpdateReqFail": ggsnApnFbcPrasUpdateReqFail,
       "ggsnApnFbcPrasStopReq": ggsnApnFbcPrasStopReq,
       "ggsnApnFbcPrasStopReqFail": ggsnApnFbcPrasStopReqFail,
       "ggsnApnFbcPrasUserServiceDenied": ggsnApnFbcPrasUserServiceDenied,
       "ggsnApnFbcPrasUserUnknown": ggsnApnFbcPrasUserUnknown,
       "ggsnApnFbcCcasStatsTable": ggsnApnFbcCcasStatsTable,
       "ggsnApnFbcCcasStatsEntry": ggsnApnFbcCcasStatsEntry,
       "ggsnCcasIndex": ggsnCcasIndex,
       "ggsnApnFbcCcasName": ggsnApnFbcCcasName,
       "ggsnApnFbcCcasStartReq": ggsnApnFbcCcasStartReq,
       "ggsnApnFbcCcasStartReqFail": ggsnApnFbcCcasStartReqFail,
       "ggsnApnFbcCcasUpdateReq": ggsnApnFbcCcasUpdateReq,
       "ggsnApnFbcCcasUpdateReqFail": ggsnApnFbcCcasUpdateReqFail,
       "ggsnApnFbcCcasStopReq": ggsnApnFbcCcasStopReq,
       "ggsnApnFbcCcasStopReqFail": ggsnApnFbcCcasStopReqFail,
       "ggsnApnFbcCcasUserServiceDenied": ggsnApnFbcCcasUserServiceDenied,
       "ggsnApnFbcCcasUserUnknown": ggsnApnFbcCcasUserUnknown,
       "ggsnApnSaccCcasAuthReject": ggsnApnSaccCcasAuthReject,
       "ggsnApnSaccCcasCcNotApplicable": ggsnApnSaccCcasCcNotApplicable,
       "ggsnFbcDiamApplSysStatsTable": ggsnFbcDiamApplSysStatsTable,
       "ggsnFbcDiamApplSysStatsEntry": ggsnFbcDiamApplSysStatsEntry,
       "ggsnDiamApplSysIndex": ggsnDiamApplSysIndex,
       "ggsnFbcDiamApplSysName": ggsnFbcDiamApplSysName,
       "ggsnFbcDiamApplSysReq": ggsnFbcDiamApplSysReq,
       "ggsnApnFbcRateGroupStatsTable": ggsnApnFbcRateGroupStatsTable,
       "ggsnApnFbcRateGroupStatsEntry": ggsnApnFbcRateGroupStatsEntry,
       "ggsnRateGroupIndex": ggsnRateGroupIndex,
       "ggsnApnFbcRateGroupEventStartTrans": ggsnApnFbcRateGroupEventStartTrans,
       "ggsnApnFbcRateGroupEventSuccessTrans": ggsnApnFbcRateGroupEventSuccessTrans,
       "ggsnApnSaccPcrfStatsTable": ggsnApnSaccPcrfStatsTable,
       "ggsnApnSaccPcrfStatsEntry": ggsnApnSaccPcrfStatsEntry,
       "ggsnPcrfIndex": ggsnPcrfIndex,
       "ggsnApnSaccPcrfName": ggsnApnSaccPcrfName,
       "ggsnApnSaccPcrfAuthorFail": ggsnApnSaccPcrfAuthorFail,
       "ggsnApnSaccPcrfAuthenFail": ggsnApnSaccPcrfAuthenFail,
       "ggsnApnSaccPcrfUpdCcReqSessIdNoMatch": ggsnApnSaccPcrfUpdCcReqSessIdNoMatch,
       "ggsnApnSaccPcrfActivePdpContextUsageReporting": ggsnApnSaccPcrfActivePdpContextUsageReporting,
       "ggsnApnSaccPcrfActiveIPcanSessions": ggsnApnSaccPcrfActiveIPcanSessions,
       "ggsnApnSaccPcrfActiveDedicatedIPcanBearers": ggsnApnSaccPcrfActiveDedicatedIPcanBearers,
       "ggsnApnSaccRsStatsTable": ggsnApnSaccRsStatsTable,
       "ggsnApnSaccRsStatsEntry": ggsnApnSaccRsStatsEntry,
       "ggsnRsIndex": ggsnRsIndex,
       "ggsnApnSaccRsName": ggsnApnSaccRsName,
       "ggsnApnSaccRsUplinkBytes": ggsnApnSaccRsUplinkBytes,
       "ggsnApnSaccRsDownlinkBytes": ggsnApnSaccRsDownlinkBytes,
       "ggsnApnSaccRsServiceInstances": ggsnApnSaccRsServiceInstances,
       "ggsnApnSaccRsAuthDownlinkPacketsDropped": ggsnApnSaccRsAuthDownlinkPacketsDropped,
       "ggsnApnSaccRsAuthUplinkPacketsDropped": ggsnApnSaccRsAuthUplinkPacketsDropped,
       "ggsnApnSaccRsGateDownlinkPacketsDropped": ggsnApnSaccRsGateDownlinkPacketsDropped,
       "ggsnApnSaccRsGateUplinkPacketsDropped": ggsnApnSaccRsGateUplinkPacketsDropped,
       "ggsnApnSacc2ServIdentStatsTable": ggsnApnSacc2ServIdentStatsTable,
       "ggsnApnSacc2ServIdentStatsEntry": ggsnApnSacc2ServIdentStatsEntry,
       "ggsnSacc2ServIdentIndex": ggsnSacc2ServIdentIndex,
       "ggsnApnSacc2ServIdentUplinkBytes": ggsnApnSacc2ServIdentUplinkBytes,
       "ggsnApnSacc2ServIdentDownlinkBytes": ggsnApnSacc2ServIdentDownlinkBytes,
       "ggsnApnSacc2ServIdentEventTrans": ggsnApnSacc2ServIdentEventTrans,
       "ggsnApnSacc2ServIdentEventTransFail": ggsnApnSacc2ServIdentEventTransFail,
       "ggsnApnSacc2ServIdentEventStartTrans": ggsnApnSacc2ServIdentEventStartTrans,
       "ggsnApnSacc2ServIdentEventSuccessTrans": ggsnApnSacc2ServIdentEventSuccessTrans,
       "ggsnApnSacc2ServClassStatsTable": ggsnApnSacc2ServClassStatsTable,
       "ggsnApnSacc2ServClassStatsEntry": ggsnApnSacc2ServClassStatsEntry,
       "ggsnSacc2ServClassIndex": ggsnSacc2ServClassIndex,
       "ggsnApnSacc2ServClassUplinkBytes": ggsnApnSacc2ServClassUplinkBytes,
       "ggsnApnSacc2ServClassDownlinkBytes": ggsnApnSacc2ServClassDownlinkBytes,
       "ggsnApnSacc2ServClassActiveTime": ggsnApnSacc2ServClassActiveTime,
       "ggsnApnSacc3ServIdentStatsTable": ggsnApnSacc3ServIdentStatsTable,
       "ggsnApnSacc3ServIdentStatsEntry": ggsnApnSacc3ServIdentStatsEntry,
       "ggsnSacc3ServIdentIndex": ggsnSacc3ServIdentIndex,
       "ggsnApnSacc3ServIdentUplinkBytes": ggsnApnSacc3ServIdentUplinkBytes,
       "ggsnApnSacc3ServIdentDownlinkBytes": ggsnApnSacc3ServIdentDownlinkBytes,
       "ggsnApnSacc3RatingGroupStatsTable": ggsnApnSacc3RatingGroupStatsTable,
       "ggsnApnSacc3RatingGroupStatsEntry": ggsnApnSacc3RatingGroupStatsEntry,
       "ggsnRatingGroupIndex": ggsnRatingGroupIndex,
       "ggsnApnSacc3RatingGroupUplinkBytes": ggsnApnSacc3RatingGroupUplinkBytes,
       "ggsnApnSacc3RatingGroupDownlinkBytes": ggsnApnSacc3RatingGroupDownlinkBytes,
       "pgwApnSaccRatingGroupStatsTable": pgwApnSaccRatingGroupStatsTable,
       "pgwApnSaccRatingGroupStatsEntry": pgwApnSaccRatingGroupStatsEntry,
       "pgwRatingGroupIndex": pgwRatingGroupIndex,
       "pgwApnSaccRatingGroupUplinkBytes": pgwApnSaccRatingGroupUplinkBytes,
       "pgwApnSaccRatingGroupDownlinkBytes": pgwApnSaccRatingGroupDownlinkBytes,
       "ggsnFbcAuthorizationStats": ggsnFbcAuthorizationStats,
       "ggsnFbcAuthStats": ggsnFbcAuthStats,
       "ggsnFbcUserAuthPacketsDropped": ggsnFbcUserAuthPacketsDropped,
       "ggsnFbcDefaultAuthPacketsDropped": ggsnFbcDefaultAuthPacketsDropped,
       "ggsnFbcEmptyBucketPacketsDropped": ggsnFbcEmptyBucketPacketsDropped,
       "ggsnFbcComFailAuthPacketsDropped": ggsnFbcComFailAuthPacketsDropped,
       "ggsnFbcIdentErrorPacketsDropped": ggsnFbcIdentErrorPacketsDropped,
       "ggsnMbmsInfo": ggsnMbmsInfo,
       "ggsnMbmsGmbSessionStartAttempts": ggsnMbmsGmbSessionStartAttempts,
       "ggsnMbmsGmbSessionStartFailures": ggsnMbmsGmbSessionStartFailures,
       "ggsnMbmsCurrentNbrOfSessions": ggsnMbmsCurrentNbrOfSessions,
       "ggsnMbmsCurrentAggregatedMbr": ggsnMbmsCurrentAggregatedMbr,
       "ggsnMbmsGiIncomingPackets": ggsnMbmsGiIncomingPackets,
       "ggsnMbmsDiscardedPackets": ggsnMbmsDiscardedPackets,
       "ggsnMbmsSgsnUserPlaneTable": ggsnMbmsSgsnUserPlaneTable,
       "ggsnMbmsSgsnUserPlaneEntry": ggsnMbmsSgsnUserPlaneEntry,
       "ggsnMbmsSgsnUIndex": ggsnMbmsSgsnUIndex,
       "ggsnMbmsSgsnUAddress": ggsnMbmsSgsnUAddress,
       "ggsnMbmsSgsnForwardedPackets": ggsnMbmsSgsnForwardedPackets,
       "ggsnMbmsSgsnControlPlaneTable": ggsnMbmsSgsnControlPlaneTable,
       "ggsnMbmsSgsnControlPlaneEntry": ggsnMbmsSgsnControlPlaneEntry,
       "ggsnMbmsSgsnCIndex": ggsnMbmsSgsnCIndex,
       "ggsnMbmsSgsnCAddress": ggsnMbmsSgsnCAddress,
       "ggsnMbmsGnSessionStartAttempts": ggsnMbmsGnSessionStartAttempts,
       "ggsnMbmsGnSessionStartFailures": ggsnMbmsGnSessionStartFailures,
       "ggsnGtptInfo": ggsnGtptInfo,
       "ggsnGtptTable": ggsnGtptTable,
       "ggsnGtptEntry": ggsnGtptEntry,
       "ggsnGtptIndex": ggsnGtptIndex,
       "ggsnGtptVersion": ggsnGtptVersion,
       "ggsnGtptAddress": ggsnGtptAddress,
       "ggsnGtptCapacity": ggsnGtptCapacity,
       "ggsnGtptRole": ggsnGtptRole,
       "ggsnGtptStatus": ggsnGtptStatus,
       "ggsnGtptMemory": ggsnGtptMemory,
       "ggsnGtptMemoryUsed": ggsnGtptMemoryUsed,
       "ggsnGtptCpuUsage": ggsnGtptCpuUsage,
       "ggsnGtptPeakCpuUsage": ggsnGtptPeakCpuUsage,
       "ggsnRadiusInfo": ggsnRadiusInfo,
       "ggsnApnRadiusAuthServersStatsTable": ggsnApnRadiusAuthServersStatsTable,
       "ggsnApnRadiusAuthServersStatsEntry": ggsnApnRadiusAuthServersStatsEntry,
       "ggsnApnRadiusAuthServerIndex": ggsnApnRadiusAuthServerIndex,
       "ggsnApnRadiusAuthServerIpAddress": ggsnApnRadiusAuthServerIpAddress,
       "ggsnApnRadiusAuthServerAccessRequests": ggsnApnRadiusAuthServerAccessRequests,
       "ggsnApnRadiusAuthServerAccessAccepts": ggsnApnRadiusAuthServerAccessAccepts,
       "ggsnApnRadiusAuthServerAccessRejects": ggsnApnRadiusAuthServerAccessRejects,
       "ggsnApnRadiusAuthServerAccessRequestTimeouts": ggsnApnRadiusAuthServerAccessRequestTimeouts,
       "ggsnApnRadiusAuthServerAccessRequestRetransmits": ggsnApnRadiusAuthServerAccessRequestRetransmits,
       "ggsnApnRadiusAuthServerInvalidAuthenticators": ggsnApnRadiusAuthServerInvalidAuthenticators,
       "ggsnApnRadiusAcctServersStatsTable": ggsnApnRadiusAcctServersStatsTable,
       "ggsnApnRadiusAcctServersStatsEntry": ggsnApnRadiusAcctServersStatsEntry,
       "ggsnApnRadiusAcctServerIndex": ggsnApnRadiusAcctServerIndex,
       "ggsnApnRadiusAcctServerIpAddress": ggsnApnRadiusAcctServerIpAddress,
       "ggsnApnRadiusAcctServerAccountingRequests": ggsnApnRadiusAcctServerAccountingRequests,
       "ggsnApnRadiusAcctServerAccountingResponses": ggsnApnRadiusAcctServerAccountingResponses,
       "ggsnApnRadiusAcctServerAccountingRequestTimeouts": ggsnApnRadiusAcctServerAccountingRequestTimeouts,
       "ggsnApnRadiusAcctServerAccountingRequestRetransmits": ggsnApnRadiusAcctServerAccountingRequestRetransmits,
       "ggsnApnRadiusAcctServerInvalidAuthenticators": ggsnApnRadiusAcctServerInvalidAuthenticators,
       "pgwSharedIpPoolStatsTable": pgwSharedIpPoolStatsTable,
       "pgwSharedIpPoolStatsEntry": pgwSharedIpPoolStatsEntry,
       "pgwSharedIpPoolIndex": pgwSharedIpPoolIndex,
       "pgwSharedIpPoolName": pgwSharedIpPoolName,
       "pgwAvailableAddressesInSharedIpPool": pgwAvailableAddressesInSharedIpPool,
       "pgwAddressesInQuarantineInSharedIpPool": pgwAddressesInQuarantineInSharedIpPool,
       "ggsnMIBConformance": ggsnMIBConformance,
       "ggsnMIBCompliances": ggsnMIBCompliances,
       "ggsnMIBCompliance": ggsnMIBCompliance,
       "ggsnMIBGroups": ggsnMIBGroups,
       "ggsnSystemGroup": ggsnSystemGroup,
       "ggsnGlobalStatisticsGroup": ggsnGlobalStatisticsGroup,
       "ggsnApnStatisticsGroup": ggsnApnStatisticsGroup,
       "ggsnSgsnStatisticsGroup": ggsnSgsnStatisticsGroup,
       "ggsnAcctClientStatisticsGroup": ggsnAcctClientStatisticsGroup,
       "ggsnDhcpStatisticsGroup": ggsnDhcpStatisticsGroup,
       "ggsnAlarmsGroup": ggsnAlarmsGroup,
       "ggsnAlarmsEntryGroup": ggsnAlarmsEntryGroup,
       "ggsnNotificationsGroup": ggsnNotificationsGroup,
       "ggsnAlarmHistEntryGroup": ggsnAlarmHistEntryGroup,
       "ggsnOldObjectsGroup": ggsnOldObjectsGroup,
       "ggsnApnFbcStatisticsGroup": ggsnApnFbcStatisticsGroup,
       "ggsnFbcAuthStatisticsGroup": ggsnFbcAuthStatisticsGroup,
       "ggsnApnFbcServIdentStatsGroup": ggsnApnFbcServIdentStatsGroup,
       "ggsnApnFbcServClassStatsGroup": ggsnApnFbcServClassStatsGroup,
       "ggsnFbcStatsGroup": ggsnFbcStatsGroup,
       "ggsnApnFbcPrasStatsGroup": ggsnApnFbcPrasStatsGroup,
       "ggsnApnFbcCcasStatsGroup": ggsnApnFbcCcasStatsGroup,
       "ggsnFbcDiamApplSysStatsGroup": ggsnFbcDiamApplSysStatsGroup,
       "ggsnApnFbcRateGroupStatsGroup": ggsnApnFbcRateGroupStatsGroup,
       "ggsnL2tpTunnelStatsGroup": ggsnL2tpTunnelStatsGroup,
       "ggsnApnSaccPcrfStatsGroup": ggsnApnSaccPcrfStatsGroup,
       "ggsnApnSaccRsStatsGroup": ggsnApnSaccRsStatsGroup,
       "ggsnApnSacc2ServIdentStatsGroup": ggsnApnSacc2ServIdentStatsGroup,
       "ggsnApnSacc2ServClassStatsGroup": ggsnApnSacc2ServClassStatsGroup,
       "ggsnApnSacc3ServIdentStatsGroup": ggsnApnSacc3ServIdentStatsGroup,
       "ggsnApnSacc3RatingGroupStatsGroup": ggsnApnSacc3RatingGroupStatsGroup,
       "pgwGlobalStatisticsGroup": pgwGlobalStatisticsGroup,
       "pgwAttemptedEpsBearerStatsGroup": pgwAttemptedEpsBearerStatsGroup,
       "pgwCompletedEpsBearerStatsGroup": pgwCompletedEpsBearerStatsGroup,
       "pgwApnSaccRatingGroupStatsGroup": pgwApnSaccRatingGroupStatsGroup,
       "s6bInterfaceGroup": s6bInterfaceGroup,
       "ggsnTraps": ggsnTraps,
       "ggsnTrapNew": ggsnTrapNew,
       "ggsnTrapChanged": ggsnTrapChanged,
       "ggsnTrapCleared": ggsnTrapCleared}
)
