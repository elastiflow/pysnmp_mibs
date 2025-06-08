# SNMP MIB module (CISCO-SMART-LIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SMART-LIC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSmartLicMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831)
)
if mibBuilder.loadTexts:
    ciscoSmartLicMIB.setRevisions(
        ("2021-07-21 00:00",
         "2020-06-21 00:00",
         "2020-05-04 00:00",
         "2020-01-07 00:00",
         "2019-11-27 00:00",
         "2017-08-14 00:00",
         "2017-03-30 00:00",
         "2017-03-29 00:00",
         "2014-11-10 00:00",
         "2014-11-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSlaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSlaMIBObjects = _CiscoSlaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0)
)
_CiscoSlaInstanceId_Type = Unsigned32
_CiscoSlaInstanceId_Object = MibScalar
ciscoSlaInstanceId = _CiscoSlaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 1),
    _CiscoSlaInstanceId_Type()
)
ciscoSlaInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaInstanceId.setStatus("current")
_CiscoSlaSUDIInfo_Type = SnmpAdminString
_CiscoSlaSUDIInfo_Object = MibScalar
ciscoSlaSUDIInfo = _CiscoSlaSUDIInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 2),
    _CiscoSlaSUDIInfo_Type()
)
ciscoSlaSUDIInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaSUDIInfo.setStatus("current")
_CiscoSlaVersion_Type = SnmpAdminString
_CiscoSlaVersion_Object = MibScalar
ciscoSlaVersion = _CiscoSlaVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 3),
    _CiscoSlaVersion_Type()
)
ciscoSlaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaVersion.setStatus("current")
_CiscoSlaEnabled_Type = TruthValue
_CiscoSlaEnabled_Object = MibScalar
ciscoSlaEnabled = _CiscoSlaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 4),
    _CiscoSlaEnabled_Type()
)
ciscoSlaEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEnabled.setStatus("current")
_CiscoSlaEntitlementInfo_ObjectIdentity = ObjectIdentity
ciscoSlaEntitlementInfo = _CiscoSlaEntitlementInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5)
)
_CiscoSlaEntitlementInfoTable_Object = MibTable
ciscoSlaEntitlementInfoTable = _CiscoSlaEntitlementInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoSlaEntitlementInfoTable.setStatus("current")
_CiscoSlaEntitlementInfoEntry_Object = MibTableRow
ciscoSlaEntitlementInfoEntry = _CiscoSlaEntitlementInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1)
)
ciscoSlaEntitlementInfoEntry.setIndexNames(
    (0, "CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementInfoIndex"),
)
if mibBuilder.loadTexts:
    ciscoSlaEntitlementInfoEntry.setStatus("current")
_CiscoSlaEntitlementInfoIndex_Type = Unsigned32
_CiscoSlaEntitlementInfoIndex_Object = MibTableColumn
ciscoSlaEntitlementInfoIndex = _CiscoSlaEntitlementInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 1),
    _CiscoSlaEntitlementInfoIndex_Type()
)
ciscoSlaEntitlementInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementInfoIndex.setStatus("current")
_CiscoSlaEntitlementRequestCount_Type = Unsigned32
_CiscoSlaEntitlementRequestCount_Object = MibTableColumn
ciscoSlaEntitlementRequestCount = _CiscoSlaEntitlementRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 2),
    _CiscoSlaEntitlementRequestCount_Type()
)
ciscoSlaEntitlementRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementRequestCount.setStatus("current")
_CiscoSlaEntitlementTag_Type = SnmpAdminString
_CiscoSlaEntitlementTag_Object = MibTableColumn
ciscoSlaEntitlementTag = _CiscoSlaEntitlementTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 3),
    _CiscoSlaEntitlementTag_Type()
)
ciscoSlaEntitlementTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementTag.setStatus("current")
_CiscoSlaEntitlementVersion_Type = SnmpAdminString
_CiscoSlaEntitlementVersion_Object = MibTableColumn
ciscoSlaEntitlementVersion = _CiscoSlaEntitlementVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 4),
    _CiscoSlaEntitlementVersion_Type()
)
ciscoSlaEntitlementVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementVersion.setStatus("current")


class _CiscoSlaEntitlementEnforceMode_Type(Integer32):
    """Custom type ciscoSlaEntitlementEnforceMode based on Integer32"""
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
        *(("initialized", 1),
          ("waiting", 2),
          ("authorized", 3),
          ("outOfCompliance", 4),
          ("overage", 5),
          ("evaluationPeriod", 6),
          ("evaluationExpired", 7),
          ("authorizationExpired", 8),
          ("gracePeriodExpired", 9),
          ("disabled", 10),
          ("reservedAuthorized", 11),
          ("invalidTag", 12),
          ("notAuthorized", 13),
          ("notApplicable", 14),
          ("inUse", 15),
          ("notInUse", 16))
    )


_CiscoSlaEntitlementEnforceMode_Type.__name__ = "Integer32"
_CiscoSlaEntitlementEnforceMode_Object = MibTableColumn
ciscoSlaEntitlementEnforceMode = _CiscoSlaEntitlementEnforceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 5),
    _CiscoSlaEntitlementEnforceMode_Type()
)
ciscoSlaEntitlementEnforceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementEnforceMode.setStatus("current")
_CiscoSlaEntitlementDescription_Type = SnmpAdminString
_CiscoSlaEntitlementDescription_Object = MibTableColumn
ciscoSlaEntitlementDescription = _CiscoSlaEntitlementDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 6),
    _CiscoSlaEntitlementDescription_Type()
)
ciscoSlaEntitlementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementDescription.setStatus("current")
_CiscoSlaEntitlementFeatureName_Type = SnmpAdminString
_CiscoSlaEntitlementFeatureName_Object = MibTableColumn
ciscoSlaEntitlementFeatureName = _CiscoSlaEntitlementFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 7),
    _CiscoSlaEntitlementFeatureName_Type()
)
ciscoSlaEntitlementFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementFeatureName.setStatus("current")


class _CiscoSlaEntitlementExportAllowed_Type(Integer32):
    """Custom type ciscoSlaEntitlementExportAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CiscoSlaEntitlementExportAllowed_Type.__name__ = "Integer32"
_CiscoSlaEntitlementExportAllowed_Object = MibTableColumn
ciscoSlaEntitlementExportAllowed = _CiscoSlaEntitlementExportAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 5, 1, 1, 8),
    _CiscoSlaEntitlementExportAllowed_Type()
)
ciscoSlaEntitlementExportAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementExportAllowed.setStatus("current")
_CiscoSlaRegistrationStatusInfo_ObjectIdentity = ObjectIdentity
ciscoSlaRegistrationStatusInfo = _CiscoSlaRegistrationStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6)
)


class _CiscoSlaRegistrationStatus_Type(Integer32):
    """Custom type ciscoSlaRegistrationStatus based on Integer32"""
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
        *(("notRegistered", 1),
          ("registrationInProgress", 2),
          ("registrationFailed", 3),
          ("registrationRetryinProgress", 4),
          ("registrationCompleted", 5))
    )


_CiscoSlaRegistrationStatus_Type.__name__ = "Integer32"
_CiscoSlaRegistrationStatus_Object = MibScalar
ciscoSlaRegistrationStatus = _CiscoSlaRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 1),
    _CiscoSlaRegistrationStatus_Type()
)
ciscoSlaRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRegistrationStatus.setStatus("current")
_CiscoSlaVirtualAccount_Type = SnmpAdminString
_CiscoSlaVirtualAccount_Object = MibScalar
ciscoSlaVirtualAccount = _CiscoSlaVirtualAccount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 2),
    _CiscoSlaVirtualAccount_Type()
)
ciscoSlaVirtualAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaVirtualAccount.setStatus("current")
_CiscoSlaNextCertificateExpireTime_Type = Unsigned32
_CiscoSlaNextCertificateExpireTime_Object = MibScalar
ciscoSlaNextCertificateExpireTime = _CiscoSlaNextCertificateExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 3),
    _CiscoSlaNextCertificateExpireTime_Type()
)
ciscoSlaNextCertificateExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaNextCertificateExpireTime.setStatus("current")
_CiscoSlaEnterpriseAccountName_Type = SnmpAdminString
_CiscoSlaEnterpriseAccountName_Object = MibScalar
ciscoSlaEnterpriseAccountName = _CiscoSlaEnterpriseAccountName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 4),
    _CiscoSlaEnterpriseAccountName_Type()
)
ciscoSlaEnterpriseAccountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaEnterpriseAccountName.setStatus("current")
_CiscoSlaRegisterTime_ObjectIdentity = ObjectIdentity
ciscoSlaRegisterTime = _CiscoSlaRegisterTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 5)
)
_CiscoSlaRegisterInitTime_Type = Unsigned32
_CiscoSlaRegisterInitTime_Object = MibScalar
ciscoSlaRegisterInitTime = _CiscoSlaRegisterInitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 5, 1),
    _CiscoSlaRegisterInitTime_Type()
)
ciscoSlaRegisterInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRegisterInitTime.setStatus("current")
_CiscoSlaRegisterSuccess_Type = TruthValue
_CiscoSlaRegisterSuccess_Object = MibScalar
ciscoSlaRegisterSuccess = _CiscoSlaRegisterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 5, 2),
    _CiscoSlaRegisterSuccess_Type()
)
ciscoSlaRegisterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRegisterSuccess.setStatus("current")
_CiscoSlaRegisterFailureReason_Type = SnmpAdminString
_CiscoSlaRegisterFailureReason_Object = MibScalar
ciscoSlaRegisterFailureReason = _CiscoSlaRegisterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 5, 3),
    _CiscoSlaRegisterFailureReason_Type()
)
ciscoSlaRegisterFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRegisterFailureReason.setStatus("current")
_CiscoSlaRegisterNextRetryTime_Type = Unsigned32
_CiscoSlaRegisterNextRetryTime_Object = MibScalar
ciscoSlaRegisterNextRetryTime = _CiscoSlaRegisterNextRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 5, 4),
    _CiscoSlaRegisterNextRetryTime_Type()
)
ciscoSlaRegisterNextRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRegisterNextRetryTime.setStatus("current")
_CiscoSlaRenewTime_ObjectIdentity = ObjectIdentity
ciscoSlaRenewTime = _CiscoSlaRenewTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 6)
)
_CiscoSlaRenewInitTime_Type = Unsigned32
_CiscoSlaRenewInitTime_Object = MibScalar
ciscoSlaRenewInitTime = _CiscoSlaRenewInitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 6, 1),
    _CiscoSlaRenewInitTime_Type()
)
ciscoSlaRenewInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRenewInitTime.setStatus("current")
_CiscoSlaRenewSuccess_Type = TruthValue
_CiscoSlaRenewSuccess_Object = MibScalar
ciscoSlaRenewSuccess = _CiscoSlaRenewSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 6, 2),
    _CiscoSlaRenewSuccess_Type()
)
ciscoSlaRenewSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRenewSuccess.setStatus("current")
_CiscoSlaRenewFailureReason_Type = SnmpAdminString
_CiscoSlaRenewFailureReason_Object = MibScalar
ciscoSlaRenewFailureReason = _CiscoSlaRenewFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 6, 3),
    _CiscoSlaRenewFailureReason_Type()
)
ciscoSlaRenewFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRenewFailureReason.setStatus("current")
_CiscoSlaRenewNextRetryTime_Type = Unsigned32
_CiscoSlaRenewNextRetryTime_Object = MibScalar
ciscoSlaRenewNextRetryTime = _CiscoSlaRenewNextRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 6, 6, 4),
    _CiscoSlaRenewNextRetryTime_Type()
)
ciscoSlaRenewNextRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaRenewNextRetryTime.setStatus("current")
_CiscoSlaAuthorizationInfo_ObjectIdentity = ObjectIdentity
ciscoSlaAuthorizationInfo = _CiscoSlaAuthorizationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7)
)
_CiscoSlaAuthExpireTime_Type = Unsigned32
_CiscoSlaAuthExpireTime_Object = MibScalar
ciscoSlaAuthExpireTime = _CiscoSlaAuthExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 1),
    _CiscoSlaAuthExpireTime_Type()
)
ciscoSlaAuthExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthExpireTime.setStatus("current")
_CiscoSlaAuthComplianceStatus_Type = SnmpAdminString
_CiscoSlaAuthComplianceStatus_Object = MibScalar
ciscoSlaAuthComplianceStatus = _CiscoSlaAuthComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 2),
    _CiscoSlaAuthComplianceStatus_Type()
)
ciscoSlaAuthComplianceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthComplianceStatus.setStatus("current")
_CiscoSlaAuthOOCStartTime_Type = Unsigned32
_CiscoSlaAuthOOCStartTime_Object = MibScalar
ciscoSlaAuthOOCStartTime = _CiscoSlaAuthOOCStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 3),
    _CiscoSlaAuthOOCStartTime_Type()
)
ciscoSlaAuthOOCStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthOOCStartTime.setStatus("current")
_CiscoSlaAuthEvalPeriod_ObjectIdentity = ObjectIdentity
ciscoSlaAuthEvalPeriod = _CiscoSlaAuthEvalPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 4)
)
_CiscoSlaAuthEvalPeriodInUse_Type = TruthValue
_CiscoSlaAuthEvalPeriodInUse_Object = MibScalar
ciscoSlaAuthEvalPeriodInUse = _CiscoSlaAuthEvalPeriodInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 4, 1),
    _CiscoSlaAuthEvalPeriodInUse_Type()
)
ciscoSlaAuthEvalPeriodInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthEvalPeriodInUse.setStatus("current")
_CiscoSlaAuthEvalExpiredTime_Type = Unsigned32
_CiscoSlaAuthEvalExpiredTime_Object = MibScalar
ciscoSlaAuthEvalExpiredTime = _CiscoSlaAuthEvalExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 4, 2),
    _CiscoSlaAuthEvalExpiredTime_Type()
)
ciscoSlaAuthEvalExpiredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthEvalExpiredTime.setStatus("current")
_CiscoSlaAuthEvalPeriodLeft_Type = Unsigned32
_CiscoSlaAuthEvalPeriodLeft_Object = MibScalar
ciscoSlaAuthEvalPeriodLeft = _CiscoSlaAuthEvalPeriodLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 4, 3),
    _CiscoSlaAuthEvalPeriodLeft_Type()
)
ciscoSlaAuthEvalPeriodLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthEvalPeriodLeft.setStatus("current")
_CiscoSlaAuthRenewTime_ObjectIdentity = ObjectIdentity
ciscoSlaAuthRenewTime = _CiscoSlaAuthRenewTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 5)
)
_CiscoSlaAuthRenewInitTime_Type = Unsigned32
_CiscoSlaAuthRenewInitTime_Object = MibScalar
ciscoSlaAuthRenewInitTime = _CiscoSlaAuthRenewInitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 5, 1),
    _CiscoSlaAuthRenewInitTime_Type()
)
ciscoSlaAuthRenewInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthRenewInitTime.setStatus("current")
_CiscoSlaAuthRenewSuccess_Type = TruthValue
_CiscoSlaAuthRenewSuccess_Object = MibScalar
ciscoSlaAuthRenewSuccess = _CiscoSlaAuthRenewSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 5, 2),
    _CiscoSlaAuthRenewSuccess_Type()
)
ciscoSlaAuthRenewSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthRenewSuccess.setStatus("current")
_CiscoSlaAuthRenewFailureReason_Type = SnmpAdminString
_CiscoSlaAuthRenewFailureReason_Object = MibScalar
ciscoSlaAuthRenewFailureReason = _CiscoSlaAuthRenewFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 5, 3),
    _CiscoSlaAuthRenewFailureReason_Type()
)
ciscoSlaAuthRenewFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthRenewFailureReason.setStatus("current")
_CiscoSlaAuthRenewNextRetryTime_Type = Unsigned32
_CiscoSlaAuthRenewNextRetryTime_Object = MibScalar
ciscoSlaAuthRenewNextRetryTime = _CiscoSlaAuthRenewNextRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 7, 5, 4),
    _CiscoSlaAuthRenewNextRetryTime_Type()
)
ciscoSlaAuthRenewNextRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaAuthRenewNextRetryTime.setStatus("current")
_CiscoSlaNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSlaNotifObjects = _CiscoSlaNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 8)
)


class _CiscoSlaGlobalNotifEnable_Type(TruthValue):
    """Custom type ciscoSlaGlobalNotifEnable based on TruthValue"""
    defaultValue = 1


_CiscoSlaGlobalNotifEnable_Type.__name__ = "TruthValue"
_CiscoSlaGlobalNotifEnable_Object = MibScalar
ciscoSlaGlobalNotifEnable = _CiscoSlaGlobalNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 8, 1),
    _CiscoSlaGlobalNotifEnable_Type()
)
ciscoSlaGlobalNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSlaGlobalNotifEnable.setStatus("current")
_CiscoSlaEntitlementNotifEnable_Type = TruthValue
_CiscoSlaEntitlementNotifEnable_Object = MibScalar
ciscoSlaEntitlementNotifEnable = _CiscoSlaEntitlementNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 8, 2),
    _CiscoSlaEntitlementNotifEnable_Type()
)
ciscoSlaEntitlementNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSlaEntitlementNotifEnable.setStatus("current")
_CiscoSlaDeRegistrationInfo_ObjectIdentity = ObjectIdentity
ciscoSlaDeRegistrationInfo = _CiscoSlaDeRegistrationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 9)
)


class _CiscoSlaFailureReason_Type(Integer32):
    """Custom type ciscoSlaFailureReason based on Integer32"""
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
        *(("invalid", 0),
          ("alreadyRegistered", 1),
          ("dailyJobTimerReset", 2),
          ("deRegisterFailure", 3))
    )


_CiscoSlaFailureReason_Type.__name__ = "Integer32"
_CiscoSlaFailureReason_Object = MibScalar
ciscoSlaFailureReason = _CiscoSlaFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 9, 1),
    _CiscoSlaFailureReason_Type()
)
ciscoSlaFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaFailureReason.setStatus("current")
_CiscoSlaDeRegisterFailureMsg_Type = SnmpAdminString
_CiscoSlaDeRegisterFailureMsg_Object = MibScalar
ciscoSlaDeRegisterFailureMsg = _CiscoSlaDeRegisterFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 9, 2),
    _CiscoSlaDeRegisterFailureMsg_Type()
)
ciscoSlaDeRegisterFailureMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaDeRegisterFailureMsg.setStatus("current")
_CiscoSlaThirdPartyAndUtilityInfo_ObjectIdentity = ObjectIdentity
ciscoSlaThirdPartyAndUtilityInfo = _CiscoSlaThirdPartyAndUtilityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 10)
)
_CiscoSlaThirdPartyAndUtilityFailureMsg_Type = SnmpAdminString
_CiscoSlaThirdPartyAndUtilityFailureMsg_Object = MibScalar
ciscoSlaThirdPartyAndUtilityFailureMsg = _CiscoSlaThirdPartyAndUtilityFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 10, 1),
    _CiscoSlaThirdPartyAndUtilityFailureMsg_Type()
)
ciscoSlaThirdPartyAndUtilityFailureMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaThirdPartyAndUtilityFailureMsg.setStatus("current")
_CiscoSlaExportInfo_ObjectIdentity = ObjectIdentity
ciscoSlaExportInfo = _CiscoSlaExportInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 11)
)
_CiscoSlaExportFailureReason_Type = Integer32
_CiscoSlaExportFailureReason_Object = MibScalar
ciscoSlaExportFailureReason = _CiscoSlaExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 11, 1),
    _CiscoSlaExportFailureReason_Type()
)
ciscoSlaExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaExportFailureReason.setStatus("current")
_CiscoSlaExportFailureMessage_Type = SnmpAdminString
_CiscoSlaExportFailureMessage_Object = MibScalar
ciscoSlaExportFailureMessage = _CiscoSlaExportFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 11, 2),
    _CiscoSlaExportFailureMessage_Type()
)
ciscoSlaExportFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaExportFailureMessage.setStatus("current")
_CiscoSlaReportingInfo_ObjectIdentity = ObjectIdentity
ciscoSlaReportingInfo = _CiscoSlaReportingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 12)
)
_CiscoSlaDaysRUMAckNotReceived_Type = Unsigned32
_CiscoSlaDaysRUMAckNotReceived_Object = MibScalar
ciscoSlaDaysRUMAckNotReceived = _CiscoSlaDaysRUMAckNotReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 12, 1),
    _CiscoSlaDaysRUMAckNotReceived_Type()
)
ciscoSlaDaysRUMAckNotReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaDaysRUMAckNotReceived.setStatus("current")
_CiscoSlaDaysReportingRequired_Type = Unsigned32
_CiscoSlaDaysReportingRequired_Object = MibScalar
ciscoSlaDaysReportingRequired = _CiscoSlaDaysReportingRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 12, 2),
    _CiscoSlaDaysReportingRequired_Type()
)
ciscoSlaDaysReportingRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaDaysReportingRequired.setStatus("current")
_CiscoSlaPolicyModeInfo_ObjectIdentity = ObjectIdentity
ciscoSlaPolicyModeInfo = _CiscoSlaPolicyModeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 13)
)
_CiscoSlaPolicyModeFailureMessage_Type = SnmpAdminString
_CiscoSlaPolicyModeFailureMessage_Object = MibScalar
ciscoSlaPolicyModeFailureMessage = _CiscoSlaPolicyModeFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 13, 1),
    _CiscoSlaPolicyModeFailureMessage_Type()
)
ciscoSlaPolicyModeFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaPolicyModeFailureMessage.setStatus("current")
_CiscoSlaPolicyModeInitialACKState_Type = Integer32
_CiscoSlaPolicyModeInitialACKState_Object = MibScalar
ciscoSlaPolicyModeInitialACKState = _CiscoSlaPolicyModeInitialACKState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 0, 13, 2),
    _CiscoSlaPolicyModeInitialACKState_Type()
)
ciscoSlaPolicyModeInitialACKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSlaPolicyModeInitialACKState.setStatus("current")
_CiscoSlaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSlaMIBNotifs = _CiscoSlaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1)
)
_CiscoSlaMIBConform_ObjectIdentity = ObjectIdentity
ciscoSlaMIBConform = _CiscoSlaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2)
)
_CiscoSlaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSlaMIBCompliances = _CiscoSlaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 1)
)
_CiscoSlaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSlaMIBGroups = _CiscoSlaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2)
)

# Managed Objects groups

ciscoSlaMIBEntitlementInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 1)
)
ciscoSlaMIBEntitlementInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementRequestCount"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementTag"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementVersion"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementEnforceMode"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementFeatureName"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementDescription"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementExportAllowed"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBEntitlementInfoGroup.setStatus("current")

ciscoSlaMIBRegistrationStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 2)
)
ciscoSlaMIBRegistrationStatusInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaRegistrationStatus"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaVirtualAccount"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaNextCertificateExpireTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEnterpriseAccountName"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRegisterInitTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRegisterSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRenewInitTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRenewSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRenewFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRenewNextRetryTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRegisterFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaRegisterNextRetryTime"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBRegistrationStatusInfoGroup.setStatus("current")

ciscoSlaMIBAgentInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 4)
)
ciscoSlaMIBAgentInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaVersion"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEnabled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaInstanceId"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBAgentInfoGroup.setStatus("current")

ciscoSlaMIBNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 6)
)
ciscoSlaMIBNotificationEnableGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaGlobalNotifEnable"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBNotificationEnableGroup.setStatus("current")

ciscoSlaMIBAuthorizationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 7)
)
ciscoSlaMIBAuthorizationInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaAuthExpireTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthComplianceStatus"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthOOCStartTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthRenewInitTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthRenewSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthRenewFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthRenewNextRetryTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthEvalPeriodInUse"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthEvalExpiredTime"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaAuthEvalPeriodLeft"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBAuthorizationInfoGroup.setStatus("current")

ciscoSlaMIBDeRegistrationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 8)
)
ciscoSlaMIBDeRegistrationInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaDeRegisterFailureMsg"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBDeRegistrationInfoGroup.setStatus("current")

ciscoSlaMIBThirdPartyAndUtilityInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 9)
)
ciscoSlaMIBThirdPartyAndUtilityInfoGroup.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaThirdPartyAndUtilityFailureMsg")
)
if mibBuilder.loadTexts:
    ciscoSlaMIBThirdPartyAndUtilityInfoGroup.setStatus("current")

ciscoSlaMIBExportInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 10)
)
ciscoSlaMIBExportInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaExportFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaExportFailureMessage"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBExportInfoGroup.setStatus("current")

ciscoSlaMIBReportingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 11)
)
ciscoSlaMIBReportingInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaDaysRUMAckNotReceived"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaDaysReportingRequired"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBReportingInfoGroup.setStatus("current")

ciscoSlaMIBPolicyModeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 12)
)
ciscoSlaMIBPolicyModeInfoGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaPolicyModeFailureMessage"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaPolicyModeInitialACKState"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBPolicyModeInfoGroup.setStatus("current")


# Notification objects

ciscoSlaSmartAgentNotifyEnforcementMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 1)
)
ciscoSlaSmartAgentNotifyEnforcementMode.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementEnforceMode"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEnforcementMode.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 2)
)
ciscoSlaSmartAgentNotifyReady.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyReady.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 3)
)
ciscoSlaSmartAgentNotifyEnabled.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEnabled.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 4)
)
ciscoSlaSmartAgentNotifyDisabled.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyDisabled.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyRegisterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 5)
)
ciscoSlaSmartAgentNotifyRegisterFailed.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyRegisterFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyRegisterSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 6)
)
ciscoSlaSmartAgentNotifyRegisterSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyRegisterSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 7)
)
ciscoSlaSmartAgentNotifyIdCertExpired.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertExpired.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertRenewSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 8)
)
ciscoSlaSmartAgentNotifyIdCertRenewSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertRenewSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertRenewFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 9)
)
ciscoSlaSmartAgentNotifyIdCertRenewFail.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertRenewFail.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyAuthRenewSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 10)
)
ciscoSlaSmartAgentNotifyAuthRenewSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyAuthRenewSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyAuthRenewFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 11)
)
ciscoSlaSmartAgentNotifyAuthRenewFail.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyAuthRenewFail.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 12)
)
ciscoSlaSmartAgentNotifyCommunicationFailure.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyCommunicationFailure.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 13)
)
ciscoSlaSmartAgentNotifyCommunicationRestored.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyCommunicationRestored.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertRenewNotStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 14)
)
ciscoSlaSmartAgentNotifyIdCertRenewNotStarted.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertRenewNotStarted.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyEntitlementEnforceMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 15)
)
ciscoSlaSmartAgentNotifyEntitlementEnforceMode.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementRequestCount"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementTag"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementVersion"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementEnforceMode"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEntitlementEnforceMode.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 16)
)
ciscoSlaSmartAgentNotifyIdCertOutOfRange.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertOutOfRange.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifySystemClockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 17)
)
ciscoSlaSmartAgentNotifySystemClockChanged.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifySystemClockChanged.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyEvalExpiryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 18)
)
ciscoSlaSmartAgentNotifyEvalExpiryWarning.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEvalExpiryWarning.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyEvalExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 19)
)
ciscoSlaSmartAgentNotifyEvalExpired.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEvalExpired.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyIdCertExpiryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 20)
)
ciscoSlaSmartAgentNotifyIdCertExpiryWarning.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyIdCertExpiryWarning.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyDeRegisterSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 21)
)
ciscoSlaSmartAgentNotifyDeRegisterSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyDeRegisterSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyDeRegisterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 22)
)
ciscoSlaSmartAgentNotifyDeRegisterFailed.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaDeRegisterFailureMsg"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyDeRegisterFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyThirdpartyModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 23)
)
ciscoSlaSmartAgentNotifyThirdpartyModeEnabled.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyThirdpartyModeEnabled.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyThirdpartyModeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 24)
)
ciscoSlaSmartAgentNotifyThirdpartyModeDisabled.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyThirdpartyModeDisabled.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 25)
)
ciscoSlaSmartAgentNotifyUtilityCertExpired.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityCertExpired.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityCertRenewFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 26)
)
ciscoSlaSmartAgentNotifyUtilityCertRenewFailed.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaThirdPartyAndUtilityFailureMsg"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityCertRenewFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 27)
)
ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityDataReportingStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 28)
)
ciscoSlaSmartAgentNotifyUtilityDataReportingStarted.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityDataReportingStarted.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityDataReportingStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 29)
)
ciscoSlaSmartAgentNotifyUtilityDataReportingStopped.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityDataReportingStopped.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilitySendRUMFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 30)
)
ciscoSlaSmartAgentNotifyUtilitySendRUMFailed.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaThirdPartyAndUtilityFailureMsg"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilitySendRUMFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 31)
)
ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifySmartTransportNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 32)
)
ciscoSlaSmartAgentNotifySmartTransportNotConfigured.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifySmartTransportNotConfigured.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 33)
)
ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyExportRequestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 34)
)
ciscoSlaSmartAgentNotifyExportRequestFailure.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementFeatureName"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementTag"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaExportFailureMessage"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyExportRequestFailure.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyExportHAMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 35)
)
ciscoSlaSmartAgentNotifyExportHAMismatch.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaExportFailureReason"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaExportFailureMessage"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyExportHAMismatch.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 36)
)
ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyExportControlledTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 37)
)
ciscoSlaSmartAgentNotifyExportControlledTag.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementTag"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementExportAllowed"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyExportControlledTag.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyEndPointReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 38)
)
ciscoSlaSmartAgentNotifyEndPointReset.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyEndPointReset.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyExportRequestSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 39)
)
ciscoSlaSmartAgentNotifyExportRequestSuccess.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementFeatureName"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaEntitlementTag"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyExportRequestSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyAuthorizationInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 40)
)
ciscoSlaSmartAgentNotifyAuthorizationInstall.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyAuthorizationInstall.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyAuthorizationRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 41)
)
ciscoSlaSmartAgentNotifyAuthorizationRemove.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyAuthorizationRemove.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyPolicyInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 42)
)
ciscoSlaSmartAgentNotifyPolicyInstalled.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyPolicyInstalled.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyPolicyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 43)
)
ciscoSlaSmartAgentNotifyPolicyRemoved.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyPolicyRemoved.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyRUMACKNotReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 44)
)
ciscoSlaSmartAgentNotifyRUMACKNotReceived.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaDaysRUMAckNotReceived"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyRUMACKNotReceived.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyRUMACKReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 45)
)
ciscoSlaSmartAgentNotifyRUMACKReceived.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyRUMACKReceived.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyAuthorizationInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 46)
)
ciscoSlaSmartAgentNotifyAuthorizationInstallFailed.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyAuthorizationInstallFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyReportingRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 47)
)
ciscoSlaSmartAgentNotifyReportingRequired.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaDaysReportingRequired"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyReportingRequired.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyPolicyInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 48)
)
ciscoSlaSmartAgentNotifyPolicyInstallFailed.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaPolicyModeFailureMessage"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyPolicyInstallFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyPolicyInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 49)
)
ciscoSlaSmartAgentNotifyPolicyInstallSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyPolicyInstallSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyReportingNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 50)
)
ciscoSlaSmartAgentNotifyReportingNotSupported.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyReportingNotSupported.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyTrustInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 51)
)
ciscoSlaSmartAgentNotifyTrustInstallSuccess.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo")
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyTrustInstallSuccess.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyTrustInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 52)
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyTrustInstallFailed.setStatus(
        "current"
    )

ciscoSlaSmartAgentNotifyPolicyInitialACKState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 1, 53)
)
ciscoSlaSmartAgentNotifyPolicyInitialACKState.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSUDIInfo"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaPolicyModeInitialACKState"))
)
if mibBuilder.loadTexts:
    ciscoSlaSmartAgentNotifyPolicyInitialACKState.setStatus(
        "current"
    )


# Notifications groups

ciscoSlaMIBGlobalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 3)
)
ciscoSlaMIBGlobalNotificationGroup.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEnforcementMode"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyReady"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEnabled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyDisabled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyRegisterFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyRegisterSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertExpired"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertRenewSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertRenewFail"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyAuthRenewSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyAuthRenewFail"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyCommunicationFailure"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyCommunicationRestored"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertRenewNotStarted"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertOutOfRange"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifySystemClockChanged"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEvalExpiryWarning"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEvalExpired"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyIdCertExpiryWarning"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyDeRegisterSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyDeRegisterFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyThirdpartyModeEnabled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyThirdpartyModeDisabled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityCertExpired"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityCertRenewFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityDataReportingStarted"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityDataReportingStopped"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilitySendRUMFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifySmartTransportNotConfigured"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyExportRequestFailure"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyExportHAMismatch"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyExportControlledTag"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEndPointReset"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyExportRequestSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyAuthorizationInstall"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyAuthorizationRemove"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyPolicyInstalled"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyPolicyRemoved"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyRUMACKNotReceived"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyRUMACKReceived"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyAuthorizationInstallFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyReportingRequired"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyPolicyInstallFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyPolicyInstallSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyReportingNotSupported"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyTrustInstallSuccess"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyTrustInstallFailed"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyPolicyInitialACKState"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBGlobalNotificationGroup.setStatus(
        "current"
    )

ciscoSlaMIBEntitlementNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 2, 5)
)
ciscoSlaMIBEntitlementNotifGroup.setObjects(
    ("CISCO-SMART-LIC-MIB", "ciscoSlaSmartAgentNotifyEntitlementEnforceMode")
)
if mibBuilder.loadTexts:
    ciscoSlaMIBEntitlementNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSlaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 831, 2, 1, 1)
)
ciscoSlaMIBCompliance.setObjects(
      *(("CISCO-SMART-LIC-MIB", "ciscoSlaMIBEntitlementInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBRegistrationStatusInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBGlobalNotificationGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBAgentInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBEntitlementNotifGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBNotificationEnableGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBAuthorizationInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBDeRegistrationInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBThirdPartyAndUtilityInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBExportInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBReportingInfoGroup"),
        ("CISCO-SMART-LIC-MIB", "ciscoSlaMIBPolicyModeInfoGroup"))
)
if mibBuilder.loadTexts:
    ciscoSlaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SMART-LIC-MIB",
    **{"ciscoSmartLicMIB": ciscoSmartLicMIB,
       "ciscoSlaMIBObjects": ciscoSlaMIBObjects,
       "ciscoSlaInstanceId": ciscoSlaInstanceId,
       "ciscoSlaSUDIInfo": ciscoSlaSUDIInfo,
       "ciscoSlaVersion": ciscoSlaVersion,
       "ciscoSlaEnabled": ciscoSlaEnabled,
       "ciscoSlaEntitlementInfo": ciscoSlaEntitlementInfo,
       "ciscoSlaEntitlementInfoTable": ciscoSlaEntitlementInfoTable,
       "ciscoSlaEntitlementInfoEntry": ciscoSlaEntitlementInfoEntry,
       "ciscoSlaEntitlementInfoIndex": ciscoSlaEntitlementInfoIndex,
       "ciscoSlaEntitlementRequestCount": ciscoSlaEntitlementRequestCount,
       "ciscoSlaEntitlementTag": ciscoSlaEntitlementTag,
       "ciscoSlaEntitlementVersion": ciscoSlaEntitlementVersion,
       "ciscoSlaEntitlementEnforceMode": ciscoSlaEntitlementEnforceMode,
       "ciscoSlaEntitlementDescription": ciscoSlaEntitlementDescription,
       "ciscoSlaEntitlementFeatureName": ciscoSlaEntitlementFeatureName,
       "ciscoSlaEntitlementExportAllowed": ciscoSlaEntitlementExportAllowed,
       "ciscoSlaRegistrationStatusInfo": ciscoSlaRegistrationStatusInfo,
       "ciscoSlaRegistrationStatus": ciscoSlaRegistrationStatus,
       "ciscoSlaVirtualAccount": ciscoSlaVirtualAccount,
       "ciscoSlaNextCertificateExpireTime": ciscoSlaNextCertificateExpireTime,
       "ciscoSlaEnterpriseAccountName": ciscoSlaEnterpriseAccountName,
       "ciscoSlaRegisterTime": ciscoSlaRegisterTime,
       "ciscoSlaRegisterInitTime": ciscoSlaRegisterInitTime,
       "ciscoSlaRegisterSuccess": ciscoSlaRegisterSuccess,
       "ciscoSlaRegisterFailureReason": ciscoSlaRegisterFailureReason,
       "ciscoSlaRegisterNextRetryTime": ciscoSlaRegisterNextRetryTime,
       "ciscoSlaRenewTime": ciscoSlaRenewTime,
       "ciscoSlaRenewInitTime": ciscoSlaRenewInitTime,
       "ciscoSlaRenewSuccess": ciscoSlaRenewSuccess,
       "ciscoSlaRenewFailureReason": ciscoSlaRenewFailureReason,
       "ciscoSlaRenewNextRetryTime": ciscoSlaRenewNextRetryTime,
       "ciscoSlaAuthorizationInfo": ciscoSlaAuthorizationInfo,
       "ciscoSlaAuthExpireTime": ciscoSlaAuthExpireTime,
       "ciscoSlaAuthComplianceStatus": ciscoSlaAuthComplianceStatus,
       "ciscoSlaAuthOOCStartTime": ciscoSlaAuthOOCStartTime,
       "ciscoSlaAuthEvalPeriod": ciscoSlaAuthEvalPeriod,
       "ciscoSlaAuthEvalPeriodInUse": ciscoSlaAuthEvalPeriodInUse,
       "ciscoSlaAuthEvalExpiredTime": ciscoSlaAuthEvalExpiredTime,
       "ciscoSlaAuthEvalPeriodLeft": ciscoSlaAuthEvalPeriodLeft,
       "ciscoSlaAuthRenewTime": ciscoSlaAuthRenewTime,
       "ciscoSlaAuthRenewInitTime": ciscoSlaAuthRenewInitTime,
       "ciscoSlaAuthRenewSuccess": ciscoSlaAuthRenewSuccess,
       "ciscoSlaAuthRenewFailureReason": ciscoSlaAuthRenewFailureReason,
       "ciscoSlaAuthRenewNextRetryTime": ciscoSlaAuthRenewNextRetryTime,
       "ciscoSlaNotifObjects": ciscoSlaNotifObjects,
       "ciscoSlaGlobalNotifEnable": ciscoSlaGlobalNotifEnable,
       "ciscoSlaEntitlementNotifEnable": ciscoSlaEntitlementNotifEnable,
       "ciscoSlaDeRegistrationInfo": ciscoSlaDeRegistrationInfo,
       "ciscoSlaFailureReason": ciscoSlaFailureReason,
       "ciscoSlaDeRegisterFailureMsg": ciscoSlaDeRegisterFailureMsg,
       "ciscoSlaThirdPartyAndUtilityInfo": ciscoSlaThirdPartyAndUtilityInfo,
       "ciscoSlaThirdPartyAndUtilityFailureMsg": ciscoSlaThirdPartyAndUtilityFailureMsg,
       "ciscoSlaExportInfo": ciscoSlaExportInfo,
       "ciscoSlaExportFailureReason": ciscoSlaExportFailureReason,
       "ciscoSlaExportFailureMessage": ciscoSlaExportFailureMessage,
       "ciscoSlaReportingInfo": ciscoSlaReportingInfo,
       "ciscoSlaDaysRUMAckNotReceived": ciscoSlaDaysRUMAckNotReceived,
       "ciscoSlaDaysReportingRequired": ciscoSlaDaysReportingRequired,
       "ciscoSlaPolicyModeInfo": ciscoSlaPolicyModeInfo,
       "ciscoSlaPolicyModeFailureMessage": ciscoSlaPolicyModeFailureMessage,
       "ciscoSlaPolicyModeInitialACKState": ciscoSlaPolicyModeInitialACKState,
       "ciscoSlaMIBNotifs": ciscoSlaMIBNotifs,
       "ciscoSlaSmartAgentNotifyEnforcementMode": ciscoSlaSmartAgentNotifyEnforcementMode,
       "ciscoSlaSmartAgentNotifyReady": ciscoSlaSmartAgentNotifyReady,
       "ciscoSlaSmartAgentNotifyEnabled": ciscoSlaSmartAgentNotifyEnabled,
       "ciscoSlaSmartAgentNotifyDisabled": ciscoSlaSmartAgentNotifyDisabled,
       "ciscoSlaSmartAgentNotifyRegisterFailed": ciscoSlaSmartAgentNotifyRegisterFailed,
       "ciscoSlaSmartAgentNotifyRegisterSuccess": ciscoSlaSmartAgentNotifyRegisterSuccess,
       "ciscoSlaSmartAgentNotifyIdCertExpired": ciscoSlaSmartAgentNotifyIdCertExpired,
       "ciscoSlaSmartAgentNotifyIdCertRenewSuccess": ciscoSlaSmartAgentNotifyIdCertRenewSuccess,
       "ciscoSlaSmartAgentNotifyIdCertRenewFail": ciscoSlaSmartAgentNotifyIdCertRenewFail,
       "ciscoSlaSmartAgentNotifyAuthRenewSuccess": ciscoSlaSmartAgentNotifyAuthRenewSuccess,
       "ciscoSlaSmartAgentNotifyAuthRenewFail": ciscoSlaSmartAgentNotifyAuthRenewFail,
       "ciscoSlaSmartAgentNotifyCommunicationFailure": ciscoSlaSmartAgentNotifyCommunicationFailure,
       "ciscoSlaSmartAgentNotifyCommunicationRestored": ciscoSlaSmartAgentNotifyCommunicationRestored,
       "ciscoSlaSmartAgentNotifyIdCertRenewNotStarted": ciscoSlaSmartAgentNotifyIdCertRenewNotStarted,
       "ciscoSlaSmartAgentNotifyEntitlementEnforceMode": ciscoSlaSmartAgentNotifyEntitlementEnforceMode,
       "ciscoSlaSmartAgentNotifyIdCertOutOfRange": ciscoSlaSmartAgentNotifyIdCertOutOfRange,
       "ciscoSlaSmartAgentNotifySystemClockChanged": ciscoSlaSmartAgentNotifySystemClockChanged,
       "ciscoSlaSmartAgentNotifyEvalExpiryWarning": ciscoSlaSmartAgentNotifyEvalExpiryWarning,
       "ciscoSlaSmartAgentNotifyEvalExpired": ciscoSlaSmartAgentNotifyEvalExpired,
       "ciscoSlaSmartAgentNotifyIdCertExpiryWarning": ciscoSlaSmartAgentNotifyIdCertExpiryWarning,
       "ciscoSlaSmartAgentNotifyDeRegisterSuccess": ciscoSlaSmartAgentNotifyDeRegisterSuccess,
       "ciscoSlaSmartAgentNotifyDeRegisterFailed": ciscoSlaSmartAgentNotifyDeRegisterFailed,
       "ciscoSlaSmartAgentNotifyThirdpartyModeEnabled": ciscoSlaSmartAgentNotifyThirdpartyModeEnabled,
       "ciscoSlaSmartAgentNotifyThirdpartyModeDisabled": ciscoSlaSmartAgentNotifyThirdpartyModeDisabled,
       "ciscoSlaSmartAgentNotifyUtilityCertExpired": ciscoSlaSmartAgentNotifyUtilityCertExpired,
       "ciscoSlaSmartAgentNotifyUtilityCertRenewFailed": ciscoSlaSmartAgentNotifyUtilityCertRenewFailed,
       "ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess": ciscoSlaSmartAgentNotifyUtilityCertRenewSuccess,
       "ciscoSlaSmartAgentNotifyUtilityDataReportingStarted": ciscoSlaSmartAgentNotifyUtilityDataReportingStarted,
       "ciscoSlaSmartAgentNotifyUtilityDataReportingStopped": ciscoSlaSmartAgentNotifyUtilityDataReportingStopped,
       "ciscoSlaSmartAgentNotifyUtilitySendRUMFailed": ciscoSlaSmartAgentNotifyUtilitySendRUMFailed,
       "ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch": ciscoSlaSmartAgentNotifyUtilityCertFQDNMismatch,
       "ciscoSlaSmartAgentNotifySmartTransportNotConfigured": ciscoSlaSmartAgentNotifySmartTransportNotConfigured,
       "ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI": ciscoSlaSmartAgentNotifyHostnameMatchedWithUDI,
       "ciscoSlaSmartAgentNotifyExportRequestFailure": ciscoSlaSmartAgentNotifyExportRequestFailure,
       "ciscoSlaSmartAgentNotifyExportHAMismatch": ciscoSlaSmartAgentNotifyExportHAMismatch,
       "ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported": ciscoSlaSmartAgentNotifyExportAuthKeyNotSupported,
       "ciscoSlaSmartAgentNotifyExportControlledTag": ciscoSlaSmartAgentNotifyExportControlledTag,
       "ciscoSlaSmartAgentNotifyEndPointReset": ciscoSlaSmartAgentNotifyEndPointReset,
       "ciscoSlaSmartAgentNotifyExportRequestSuccess": ciscoSlaSmartAgentNotifyExportRequestSuccess,
       "ciscoSlaSmartAgentNotifyAuthorizationInstall": ciscoSlaSmartAgentNotifyAuthorizationInstall,
       "ciscoSlaSmartAgentNotifyAuthorizationRemove": ciscoSlaSmartAgentNotifyAuthorizationRemove,
       "ciscoSlaSmartAgentNotifyPolicyInstalled": ciscoSlaSmartAgentNotifyPolicyInstalled,
       "ciscoSlaSmartAgentNotifyPolicyRemoved": ciscoSlaSmartAgentNotifyPolicyRemoved,
       "ciscoSlaSmartAgentNotifyRUMACKNotReceived": ciscoSlaSmartAgentNotifyRUMACKNotReceived,
       "ciscoSlaSmartAgentNotifyRUMACKReceived": ciscoSlaSmartAgentNotifyRUMACKReceived,
       "ciscoSlaSmartAgentNotifyAuthorizationInstallFailed": ciscoSlaSmartAgentNotifyAuthorizationInstallFailed,
       "ciscoSlaSmartAgentNotifyReportingRequired": ciscoSlaSmartAgentNotifyReportingRequired,
       "ciscoSlaSmartAgentNotifyPolicyInstallFailed": ciscoSlaSmartAgentNotifyPolicyInstallFailed,
       "ciscoSlaSmartAgentNotifyPolicyInstallSuccess": ciscoSlaSmartAgentNotifyPolicyInstallSuccess,
       "ciscoSlaSmartAgentNotifyReportingNotSupported": ciscoSlaSmartAgentNotifyReportingNotSupported,
       "ciscoSlaSmartAgentNotifyTrustInstallSuccess": ciscoSlaSmartAgentNotifyTrustInstallSuccess,
       "ciscoSlaSmartAgentNotifyTrustInstallFailed": ciscoSlaSmartAgentNotifyTrustInstallFailed,
       "ciscoSlaSmartAgentNotifyPolicyInitialACKState": ciscoSlaSmartAgentNotifyPolicyInitialACKState,
       "ciscoSlaMIBConform": ciscoSlaMIBConform,
       "ciscoSlaMIBCompliances": ciscoSlaMIBCompliances,
       "ciscoSlaMIBCompliance": ciscoSlaMIBCompliance,
       "ciscoSlaMIBGroups": ciscoSlaMIBGroups,
       "ciscoSlaMIBEntitlementInfoGroup": ciscoSlaMIBEntitlementInfoGroup,
       "ciscoSlaMIBRegistrationStatusInfoGroup": ciscoSlaMIBRegistrationStatusInfoGroup,
       "ciscoSlaMIBGlobalNotificationGroup": ciscoSlaMIBGlobalNotificationGroup,
       "ciscoSlaMIBAgentInfoGroup": ciscoSlaMIBAgentInfoGroup,
       "ciscoSlaMIBEntitlementNotifGroup": ciscoSlaMIBEntitlementNotifGroup,
       "ciscoSlaMIBNotificationEnableGroup": ciscoSlaMIBNotificationEnableGroup,
       "ciscoSlaMIBAuthorizationInfoGroup": ciscoSlaMIBAuthorizationInfoGroup,
       "ciscoSlaMIBDeRegistrationInfoGroup": ciscoSlaMIBDeRegistrationInfoGroup,
       "ciscoSlaMIBThirdPartyAndUtilityInfoGroup": ciscoSlaMIBThirdPartyAndUtilityInfoGroup,
       "ciscoSlaMIBExportInfoGroup": ciscoSlaMIBExportInfoGroup,
       "ciscoSlaMIBReportingInfoGroup": ciscoSlaMIBReportingInfoGroup,
       "ciscoSlaMIBPolicyModeInfoGroup": ciscoSlaMIBPolicyModeInfoGroup}
)
