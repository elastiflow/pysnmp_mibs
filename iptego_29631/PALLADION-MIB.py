# SNMP MIB module (PALLADION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/iptego_29631/PALLADION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:42 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

palladion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2)
)
if mibBuilder.loadTexts:
    palladion.setRevisions(
        ("2011-07-29 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Iptego_ObjectIdentity = ObjectIdentity
iptego = _Iptego_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631)
)
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1)
)
_AlertsNotifications_ObjectIdentity = ObjectIdentity
alertsNotifications = _AlertsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1)
)
_AlertsObjects_ObjectIdentity = ObjectIdentity
alertsObjects = _AlertsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2)
)


class _PldCounterName_Type(OctetString):
    """Custom type pldCounterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PldCounterName_Type.__name__ = "OctetString"
_PldCounterName_Object = MibScalar
pldCounterName = _PldCounterName_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 1),
    _PldCounterName_Type()
)
pldCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldCounterName.setStatus("current")
_PldCounterValue_Type = Integer32
_PldCounterValue_Object = MibScalar
pldCounterValue = _PldCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 2),
    _PldCounterValue_Type()
)
pldCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldCounterValue.setStatus("current")


class _PldAlertString_Type(OctetString):
    """Custom type pldAlertString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_PldAlertString_Type.__name__ = "OctetString"
_PldAlertString_Object = MibScalar
pldAlertString = _PldAlertString_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 3),
    _PldAlertString_Type()
)
pldAlertString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldAlertString.setStatus("current")


class _PldAlertUser_Type(OctetString):
    """Custom type pldAlertUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PldAlertUser_Type.__name__ = "OctetString"
_PldAlertUser_Object = MibScalar
pldAlertUser = _PldAlertUser_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 4),
    _PldAlertUser_Type()
)
pldAlertUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldAlertUser.setStatus("current")


class _PldAlertDev_Type(OctetString):
    """Custom type pldAlertDev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PldAlertDev_Type.__name__ = "OctetString"
_PldAlertDev_Object = MibScalar
pldAlertDev = _PldAlertDev_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 5),
    _PldAlertDev_Type()
)
pldAlertDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldAlertDev.setStatus("current")
_PldAlertSeverity_Type = Integer32
_PldAlertSeverity_Object = MibScalar
pldAlertSeverity = _PldAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 6),
    _PldAlertSeverity_Type()
)
pldAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldAlertSeverity.setStatus("current")


class _PldAlertDescr_Type(OctetString):
    """Custom type pldAlertDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PldAlertDescr_Type.__name__ = "OctetString"
_PldAlertDescr_Object = MibScalar
pldAlertDescr = _PldAlertDescr_Object(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 2, 7),
    _PldAlertDescr_Type()
)
pldAlertDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldAlertDescr.setStatus("current")
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0)
)
_PldTransportCounters_ObjectIdentity = ObjectIdentity
pldTransportCounters = _PldTransportCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 0)
)
_PldTransportBandwithCounters_ObjectIdentity = ObjectIdentity
pldTransportBandwithCounters = _PldTransportBandwithCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 0, 0)
)
_PldSIPCounters_ObjectIdentity = ObjectIdentity
pldSIPCounters = _PldSIPCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1)
)
_PldSIPRequestCounters_ObjectIdentity = ObjectIdentity
pldSIPRequestCounters = _PldSIPRequestCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 0)
)
_PldSIPReplyCounters_ObjectIdentity = ObjectIdentity
pldSIPReplyCounters = _PldSIPReplyCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 1)
)
_PldSIPMethodCounters_ObjectIdentity = ObjectIdentity
pldSIPMethodCounters = _PldSIPMethodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 2)
)
_PldSIPAnswRangeCounters_ObjectIdentity = ObjectIdentity
pldSIPAnswRangeCounters = _PldSIPAnswRangeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 3)
)
_PldSIPTransportCounters_ObjectIdentity = ObjectIdentity
pldSIPTransportCounters = _PldSIPTransportCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 4)
)
_PldSIPFragmentedCounters_ObjectIdentity = ObjectIdentity
pldSIPFragmentedCounters = _PldSIPFragmentedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 1, 5)
)
_PldTransactionCounters_ObjectIdentity = ObjectIdentity
pldTransactionCounters = _PldTransactionCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2)
)
_PldTxCompletedCounters_ObjectIdentity = ObjectIdentity
pldTxCompletedCounters = _PldTxCompletedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 0)
)
_PldTxCompletedMethodCounters_ObjectIdentity = ObjectIdentity
pldTxCompletedMethodCounters = _PldTxCompletedMethodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 1)
)
_PldTxCompletedMethodAnswRangeCounters_ObjectIdentity = ObjectIdentity
pldTxCompletedMethodAnswRangeCounters = _PldTxCompletedMethodAnswRangeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 2)
)
_PldTxCompletedAnswRangeCounters_ObjectIdentity = ObjectIdentity
pldTxCompletedAnswRangeCounters = _PldTxCompletedAnswRangeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 3)
)
_PldTxTimeout_ObjectIdentity = ObjectIdentity
pldTxTimeout = _PldTxTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 4)
)
_PldTxFirstResponseTime_ObjectIdentity = ObjectIdentity
pldTxFirstResponseTime = _PldTxFirstResponseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 5)
)
_PldTxFinalResponseTime_ObjectIdentity = ObjectIdentity
pldTxFinalResponseTime = _PldTxFinalResponseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 6)
)
_PldTxCompletedReqRetrans_ObjectIdentity = ObjectIdentity
pldTxCompletedReqRetrans = _PldTxCompletedReqRetrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 7)
)
_PldTxInviteFailedReplRetrans_ObjectIdentity = ObjectIdentity
pldTxInviteFailedReplRetrans = _PldTxInviteFailedReplRetrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 2, 8)
)
_PldDialogCounters_ObjectIdentity = ObjectIdentity
pldDialogCounters = _PldDialogCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3)
)
_PldDlgCallAttemptsCounters_ObjectIdentity = ObjectIdentity
pldDlgCallAttemptsCounters = _PldDlgCallAttemptsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 0)
)
_PldDlgCallsEstablisherCounters_ObjectIdentity = ObjectIdentity
pldDlgCallsEstablisherCounters = _PldDlgCallsEstablisherCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 1)
)
_PldDlgCallsClosedCounters_ObjectIdentity = ObjectIdentity
pldDlgCallsClosedCounters = _PldDlgCallsClosedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 2)
)
_PldDlgCallsTimeoutCounters_ObjectIdentity = ObjectIdentity
pldDlgCallsTimeoutCounters = _PldDlgCallsTimeoutCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 3)
)
_PldDlgActiveCallsCounters_ObjectIdentity = ObjectIdentity
pldDlgActiveCallsCounters = _PldDlgActiveCallsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 4)
)
_PldDlgLengthInterval_ObjectIdentity = ObjectIdentity
pldDlgLengthInterval = _PldDlgLengthInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 5)
)
_PldDlgRingingInterval_ObjectIdentity = ObjectIdentity
pldDlgRingingInterval = _PldDlgRingingInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 6)
)
_PldDlgClosedCallee_ObjectIdentity = ObjectIdentity
pldDlgClosedCallee = _PldDlgClosedCallee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 3, 7)
)
_PldRegistrationCounters_ObjectIdentity = ObjectIdentity
pldRegistrationCounters = _PldRegistrationCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4)
)
_PldRegisteredUsersCounters_ObjectIdentity = ObjectIdentity
pldRegisteredUsersCounters = _PldRegisteredUsersCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 0)
)
_PldRegisteredContactsCounters_ObjectIdentity = ObjectIdentity
pldRegisteredContactsCounters = _PldRegisteredContactsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 1)
)
_PldRegistrationsExpiredCounters_ObjectIdentity = ObjectIdentity
pldRegistrationsExpiredCounters = _PldRegistrationsExpiredCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 2)
)
_PldRegistrationsNewCounters_ObjectIdentity = ObjectIdentity
pldRegistrationsNewCounters = _PldRegistrationsNewCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 3)
)
_PldRegistrationsRefreshedCounters_ObjectIdentity = ObjectIdentity
pldRegistrationsRefreshedCounters = _PldRegistrationsRefreshedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 4)
)
_PldRegistrationsFailedCounters_ObjectIdentity = ObjectIdentity
pldRegistrationsFailedCounters = _PldRegistrationsFailedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 5)
)
_PldRegistrationsUnauthorizedCounters_ObjectIdentity = ObjectIdentity
pldRegistrationsUnauthorizedCounters = _PldRegistrationsUnauthorizedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 4, 6)
)
_PldMemoryCounters_ObjectIdentity = ObjectIdentity
pldMemoryCounters = _PldMemoryCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 5)
)
_PldDeviceCounters_ObjectIdentity = ObjectIdentity
pldDeviceCounters = _PldDeviceCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6)
)
_PldDeviceActiveInCounters_ObjectIdentity = ObjectIdentity
pldDeviceActiveInCounters = _PldDeviceActiveInCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 0)
)
_PldDeviceActiveOutCounters_ObjectIdentity = ObjectIdentity
pldDeviceActiveOutCounters = _PldDeviceActiveOutCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 1)
)
_PldDeviceActiveCounters_ObjectIdentity = ObjectIdentity
pldDeviceActiveCounters = _PldDeviceActiveCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 2)
)
_PldDeviceCallAttemptsCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallAttemptsCounters = _PldDeviceCallAttemptsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 3)
)
_PldDeviceCallsEstablishedCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallsEstablishedCounters = _PldDeviceCallsEstablishedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 4)
)
_PldDeviceCallsClosedCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallsClosedCounters = _PldDeviceCallsClosedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 5)
)
_PldDeviceCallsTimeoutCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallsTimeoutCounters = _PldDeviceCallsTimeoutCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 6)
)
_PldDeviceCallsFailedCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallsFailedCounters = _PldDeviceCallsFailedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 7)
)
_PldDeviceCallsAnswRangeCounters_ObjectIdentity = ObjectIdentity
pldDeviceCallsAnswRangeCounters = _PldDeviceCallsAnswRangeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 8)
)
_PldDeviceRegisteredUsersCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegisteredUsersCounters = _PldDeviceRegisteredUsersCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 9)
)
_PldDeviceRegisteredContactsCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegisteredContactsCounters = _PldDeviceRegisteredContactsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 10)
)
_PldDeviceRegistrationsExpiredCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsExpiredCounters = _PldDeviceRegistrationsExpiredCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 11)
)
_PldDeviceRegistrationsNewCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsNewCounters = _PldDeviceRegistrationsNewCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 12)
)
_PldDeviceRegistrationsRefreshedCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsRefreshedCounters = _PldDeviceRegistrationsRefreshedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 13)
)
_PldDeviceRegistrationsFailedCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsFailedCounters = _PldDeviceRegistrationsFailedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 14)
)
_PldDeviceRegistrationsUnauthorizedCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsUnauthorizedCounters = _PldDeviceRegistrationsUnauthorizedCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 15)
)
_PldDeviceRegistrationsAnswRangeCounters_ObjectIdentity = ObjectIdentity
pldDeviceRegistrationsAnswRangeCounters = _PldDeviceRegistrationsAnswRangeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 16)
)
_PldDeviceTransitTimeCounters_ObjectIdentity = ObjectIdentity
pldDeviceTransitTimeCounters = _PldDeviceTransitTimeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 17)
)
_PldDeviceResponseTimeCounters_ObjectIdentity = ObjectIdentity
pldDeviceResponseTimeCounters = _PldDeviceResponseTimeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 6, 18)
)
_PldAverageCounters_ObjectIdentity = ObjectIdentity
pldAverageCounters = _PldAverageCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 7)
)
_PldAverageAverageCounters_ObjectIdentity = ObjectIdentity
pldAverageAverageCounters = _PldAverageAverageCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 7, 0)
)
_PldCountersById_ObjectIdentity = ObjectIdentity
pldCountersById = _PldCountersById_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29631, 2, 2, 0, 256)
)

# Managed Objects groups


# Notification objects

pldAlertsCounters = NotificationType(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1, 1)
)
pldAlertsCounters.setObjects(
      *(("PALLADION-MIB", "pldCounterName"),
        ("PALLADION-MIB", "pldCounterValue"),
        ("PALLADION-MIB", "pldAlertString"),
        ("PALLADION-MIB", "pldAlertSeverity"),
        ("PALLADION-MIB", "pldAlertDescr"))
)
if mibBuilder.loadTexts:
    pldAlertsCounters.setStatus(
        "current"
    )

pldAlertsMon = NotificationType(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1, 3)
)
pldAlertsMon.setObjects(
      *(("PALLADION-MIB", "pldAlertUser"),
        ("PALLADION-MIB", "pldAlertString"),
        ("PALLADION-MIB", "pldAlertSeverity"))
)
if mibBuilder.loadTexts:
    pldAlertsMon.setStatus(
        "current"
    )

pldAlertsGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1, 4)
)
pldAlertsGeneric.setObjects(
      *(("PALLADION-MIB", "pldAlertString"),
        ("PALLADION-MIB", "pldAlertSeverity"))
)
if mibBuilder.loadTexts:
    pldAlertsGeneric.setStatus(
        "current"
    )

pldAlertsCountersBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1, 5)
)
pldAlertsCountersBack.setObjects(
      *(("PALLADION-MIB", "pldCounterName"),
        ("PALLADION-MIB", "pldCounterValue"),
        ("PALLADION-MIB", "pldAlertString"),
        ("PALLADION-MIB", "pldAlertSeverity"),
        ("PALLADION-MIB", "pldAlertDescr"))
)
if mibBuilder.loadTexts:
    pldAlertsCountersBack.setStatus(
        "current"
    )

pldAlertsClearMon = NotificationType(
    (1, 3, 6, 1, 4, 1, 29631, 2, 1, 1, 6)
)
pldAlertsClearMon.setObjects(
      *(("PALLADION-MIB", "pldAlertUser"),
        ("PALLADION-MIB", "pldAlertString"),
        ("PALLADION-MIB", "pldAlertSeverity"))
)
if mibBuilder.loadTexts:
    pldAlertsClearMon.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PALLADION-MIB",
    **{"iptego": iptego,
       "palladion": palladion,
       "alerts": alerts,
       "alertsNotifications": alertsNotifications,
       "pldAlertsCounters": pldAlertsCounters,
       "pldAlertsMon": pldAlertsMon,
       "pldAlertsGeneric": pldAlertsGeneric,
       "pldAlertsCountersBack": pldAlertsCountersBack,
       "pldAlertsClearMon": pldAlertsClearMon,
       "alertsObjects": alertsObjects,
       "pldCounterName": pldCounterName,
       "pldCounterValue": pldCounterValue,
       "pldAlertString": pldAlertString,
       "pldAlertUser": pldAlertUser,
       "pldAlertDev": pldAlertDev,
       "pldAlertSeverity": pldAlertSeverity,
       "pldAlertDescr": pldAlertDescr,
       "counters": counters,
       "pldTransportCounters": pldTransportCounters,
       "pldTransportBandwithCounters": pldTransportBandwithCounters,
       "pldSIPCounters": pldSIPCounters,
       "pldSIPRequestCounters": pldSIPRequestCounters,
       "pldSIPReplyCounters": pldSIPReplyCounters,
       "pldSIPMethodCounters": pldSIPMethodCounters,
       "pldSIPAnswRangeCounters": pldSIPAnswRangeCounters,
       "pldSIPTransportCounters": pldSIPTransportCounters,
       "pldSIPFragmentedCounters": pldSIPFragmentedCounters,
       "pldTransactionCounters": pldTransactionCounters,
       "pldTxCompletedCounters": pldTxCompletedCounters,
       "pldTxCompletedMethodCounters": pldTxCompletedMethodCounters,
       "pldTxCompletedMethodAnswRangeCounters": pldTxCompletedMethodAnswRangeCounters,
       "pldTxCompletedAnswRangeCounters": pldTxCompletedAnswRangeCounters,
       "pldTxTimeout": pldTxTimeout,
       "pldTxFirstResponseTime": pldTxFirstResponseTime,
       "pldTxFinalResponseTime": pldTxFinalResponseTime,
       "pldTxCompletedReqRetrans": pldTxCompletedReqRetrans,
       "pldTxInviteFailedReplRetrans": pldTxInviteFailedReplRetrans,
       "pldDialogCounters": pldDialogCounters,
       "pldDlgCallAttemptsCounters": pldDlgCallAttemptsCounters,
       "pldDlgCallsEstablisherCounters": pldDlgCallsEstablisherCounters,
       "pldDlgCallsClosedCounters": pldDlgCallsClosedCounters,
       "pldDlgCallsTimeoutCounters": pldDlgCallsTimeoutCounters,
       "pldDlgActiveCallsCounters": pldDlgActiveCallsCounters,
       "pldDlgLengthInterval": pldDlgLengthInterval,
       "pldDlgRingingInterval": pldDlgRingingInterval,
       "pldDlgClosedCallee": pldDlgClosedCallee,
       "pldRegistrationCounters": pldRegistrationCounters,
       "pldRegisteredUsersCounters": pldRegisteredUsersCounters,
       "pldRegisteredContactsCounters": pldRegisteredContactsCounters,
       "pldRegistrationsExpiredCounters": pldRegistrationsExpiredCounters,
       "pldRegistrationsNewCounters": pldRegistrationsNewCounters,
       "pldRegistrationsRefreshedCounters": pldRegistrationsRefreshedCounters,
       "pldRegistrationsFailedCounters": pldRegistrationsFailedCounters,
       "pldRegistrationsUnauthorizedCounters": pldRegistrationsUnauthorizedCounters,
       "pldMemoryCounters": pldMemoryCounters,
       "pldDeviceCounters": pldDeviceCounters,
       "pldDeviceActiveInCounters": pldDeviceActiveInCounters,
       "pldDeviceActiveOutCounters": pldDeviceActiveOutCounters,
       "pldDeviceActiveCounters": pldDeviceActiveCounters,
       "pldDeviceCallAttemptsCounters": pldDeviceCallAttemptsCounters,
       "pldDeviceCallsEstablishedCounters": pldDeviceCallsEstablishedCounters,
       "pldDeviceCallsClosedCounters": pldDeviceCallsClosedCounters,
       "pldDeviceCallsTimeoutCounters": pldDeviceCallsTimeoutCounters,
       "pldDeviceCallsFailedCounters": pldDeviceCallsFailedCounters,
       "pldDeviceCallsAnswRangeCounters": pldDeviceCallsAnswRangeCounters,
       "pldDeviceRegisteredUsersCounters": pldDeviceRegisteredUsersCounters,
       "pldDeviceRegisteredContactsCounters": pldDeviceRegisteredContactsCounters,
       "pldDeviceRegistrationsExpiredCounters": pldDeviceRegistrationsExpiredCounters,
       "pldDeviceRegistrationsNewCounters": pldDeviceRegistrationsNewCounters,
       "pldDeviceRegistrationsRefreshedCounters": pldDeviceRegistrationsRefreshedCounters,
       "pldDeviceRegistrationsFailedCounters": pldDeviceRegistrationsFailedCounters,
       "pldDeviceRegistrationsUnauthorizedCounters": pldDeviceRegistrationsUnauthorizedCounters,
       "pldDeviceRegistrationsAnswRangeCounters": pldDeviceRegistrationsAnswRangeCounters,
       "pldDeviceTransitTimeCounters": pldDeviceTransitTimeCounters,
       "pldDeviceResponseTimeCounters": pldDeviceResponseTimeCounters,
       "pldAverageCounters": pldAverageCounters,
       "pldAverageAverageCounters": pldAverageAverageCounters,
       "pldCountersById": pldCountersById}
)
