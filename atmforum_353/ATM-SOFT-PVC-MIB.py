# SNMP MIB module (ATM-SOFT-PVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/ATM-SOFT-PVC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:04:44 2025
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

atmSoftPvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1)
)
if mibBuilder.loadTexts:
    atmSoftPvcMIB.setRevisions(
        ("1999-05-21 00:00",
         "1997-05-01 00:00",
         "1996-06-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSoftPvc_ObjectIdentity = ObjectIdentity
atmfSoftPvc = _AtmfSoftPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5)
)
_AtmSoftPvcMIBObjects_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBObjects = _AtmSoftPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1)
)
_AtmSoftPvcBaseGroup_ObjectIdentity = ObjectIdentity
atmSoftPvcBaseGroup = _AtmSoftPvcBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1)
)
_AtmSoftPvcCallFailuresTrapEnable_Type = TruthValue
_AtmSoftPvcCallFailuresTrapEnable_Object = MibScalar
atmSoftPvcCallFailuresTrapEnable = _AtmSoftPvcCallFailuresTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 1),
    _AtmSoftPvcCallFailuresTrapEnable_Type()
)
atmSoftPvcCallFailuresTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPvcCallFailuresTrapEnable.setStatus("current")
_AtmSoftPvcCallFailures_Type = Counter32
_AtmSoftPvcCallFailures_Object = MibScalar
atmSoftPvcCallFailures = _AtmSoftPvcCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 2),
    _AtmSoftPvcCallFailures_Type()
)
atmSoftPvcCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCallFailures.setStatus("current")
_AtmSoftPvcCurrentlyFailingSoftPVccs_Type = Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVccs_Object = MibScalar
atmSoftPvcCurrentlyFailingSoftPVccs = _AtmSoftPvcCurrentlyFailingSoftPVccs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 3),
    _AtmSoftPvcCurrentlyFailingSoftPVccs_Type()
)
atmSoftPvcCurrentlyFailingSoftPVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCurrentlyFailingSoftPVccs.setStatus("current")
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Type = Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Object = MibScalar
atmSoftPvcCurrentlyFailingSoftPVpcs = _AtmSoftPvcCurrentlyFailingSoftPVpcs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 4),
    _AtmSoftPvcCurrentlyFailingSoftPVpcs_Type()
)
atmSoftPvcCurrentlyFailingSoftPVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPvcCurrentlyFailingSoftPVpcs.setStatus("current")


class _AtmSoftPvcNotificationInterval_Type(Integer32):
    """Custom type atmSoftPvcNotificationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPvcNotificationInterval_Type.__name__ = "Integer32"
_AtmSoftPvcNotificationInterval_Object = MibScalar
atmSoftPvcNotificationInterval = _AtmSoftPvcNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 5),
    _AtmSoftPvcNotificationInterval_Type()
)
atmSoftPvcNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPvcNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmSoftPvcNotificationInterval.setUnits("seconds")
_AtmSoftPVccTable_Object = MibTable
atmSoftPVccTable = _AtmSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmSoftPVccTable.setStatus("current")
_AtmSoftPVccEntry_Object = MibTableRow
atmSoftPVccEntry = _AtmSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1)
)
atmSoftPVccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    atmSoftPVccEntry.setStatus("current")


class _AtmSoftPVccLeafReference_Type(Integer32):
    """Custom type atmSoftPVccLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmSoftPVccLeafReference_Type.__name__ = "Integer32"
_AtmSoftPVccLeafReference_Object = MibTableColumn
atmSoftPVccLeafReference = _AtmSoftPVccLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 1),
    _AtmSoftPVccLeafReference_Type()
)
atmSoftPVccLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSoftPVccLeafReference.setStatus("current")
_AtmSoftPVccTargetAddress_Type = AtmAddr
_AtmSoftPVccTargetAddress_Object = MibTableColumn
atmSoftPVccTargetAddress = _AtmSoftPVccTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 2),
    _AtmSoftPVccTargetAddress_Type()
)
atmSoftPVccTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetAddress.setStatus("current")


class _AtmSoftPVccTargetSelectType_Type(Integer32):
    """Custom type atmSoftPVccTargetSelectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("required", 1),
          ("any", 2))
    )


_AtmSoftPVccTargetSelectType_Type.__name__ = "Integer32"
_AtmSoftPVccTargetSelectType_Object = MibTableColumn
atmSoftPVccTargetSelectType = _AtmSoftPVccTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 3),
    _AtmSoftPVccTargetSelectType_Type()
)
atmSoftPVccTargetSelectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetSelectType.setStatus("current")


class _AtmSoftPVccTargetVpi_Type(Integer32):
    """Custom type atmSoftPVccTargetVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSoftPVccTargetVpi_Type.__name__ = "Integer32"
_AtmSoftPVccTargetVpi_Object = MibTableColumn
atmSoftPVccTargetVpi = _AtmSoftPVccTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 4),
    _AtmSoftPVccTargetVpi_Type()
)
atmSoftPVccTargetVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetVpi.setStatus("deprecated")


class _AtmSoftPVccTargetVci_Type(Integer32):
    """Custom type atmSoftPVccTargetVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccTargetVci_Type.__name__ = "Integer32"
_AtmSoftPVccTargetVci_Object = MibTableColumn
atmSoftPVccTargetVci = _AtmSoftPVccTargetVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 5),
    _AtmSoftPVccTargetVci_Type()
)
atmSoftPVccTargetVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetVci.setStatus("current")


class _AtmSoftPVccLastReleaseCause_Type(Integer32):
    """Custom type atmSoftPVccLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmSoftPVccLastReleaseCause_Type.__name__ = "Integer32"
_AtmSoftPVccLastReleaseCause_Object = MibTableColumn
atmSoftPVccLastReleaseCause = _AtmSoftPVccLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 6),
    _AtmSoftPVccLastReleaseCause_Type()
)
atmSoftPVccLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccLastReleaseCause.setStatus("current")


class _AtmSoftPVccLastReleaseDiagnostic_Type(OctetString):
    """Custom type atmSoftPVccLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmSoftPVccLastReleaseDiagnostic_Type.__name__ = "OctetString"
_AtmSoftPVccLastReleaseDiagnostic_Object = MibTableColumn
atmSoftPVccLastReleaseDiagnostic = _AtmSoftPVccLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 7),
    _AtmSoftPVccLastReleaseDiagnostic_Type()
)
atmSoftPVccLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccLastReleaseDiagnostic.setStatus("current")


class _AtmSoftPVccOperStatus_Type(Integer32):
    """Custom type atmSoftPVccOperStatus based on Integer32"""
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
        *(("other", 1),
          ("establishmentInProgress", 2),
          ("connected", 3),
          ("retriesExhausted", 4),
          ("noAddressSupplied", 5),
          ("lowerLayerDown", 6))
    )


_AtmSoftPVccOperStatus_Type.__name__ = "Integer32"
_AtmSoftPVccOperStatus_Object = MibTableColumn
atmSoftPVccOperStatus = _AtmSoftPVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 8),
    _AtmSoftPVccOperStatus_Type()
)
atmSoftPVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccOperStatus.setStatus("current")


class _AtmSoftPVccRestart_Type(Integer32):
    """Custom type atmSoftPVccRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("noop", 2))
    )


_AtmSoftPVccRestart_Type.__name__ = "Integer32"
_AtmSoftPVccRestart_Object = MibTableColumn
atmSoftPVccRestart = _AtmSoftPVccRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 9),
    _AtmSoftPVccRestart_Type()
)
atmSoftPVccRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccRestart.setStatus("current")


class _AtmSoftPVccRetryInterval_Type(Integer32):
    """Custom type atmSoftPVccRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPVccRetryInterval_Type.__name__ = "Integer32"
_AtmSoftPVccRetryInterval_Object = MibTableColumn
atmSoftPVccRetryInterval = _AtmSoftPVccRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 10),
    _AtmSoftPVccRetryInterval_Type()
)
atmSoftPVccRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmSoftPVccRetryInterval.setUnits("seconds")


class _AtmSoftPVccRetryTimer_Type(Integer32):
    """Custom type atmSoftPVccRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmSoftPVccRetryTimer_Type.__name__ = "Integer32"
_AtmSoftPVccRetryTimer_Object = MibTableColumn
atmSoftPVccRetryTimer = _AtmSoftPVccRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 11),
    _AtmSoftPVccRetryTimer_Type()
)
atmSoftPVccRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    atmSoftPVccRetryTimer.setUnits("seconds")


class _AtmSoftPVccRetryThreshold_Type(Integer32):
    """Custom type atmSoftPVccRetryThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccRetryThreshold_Type.__name__ = "Integer32"
_AtmSoftPVccRetryThreshold_Object = MibTableColumn
atmSoftPVccRetryThreshold = _AtmSoftPVccRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 12),
    _AtmSoftPVccRetryThreshold_Type()
)
atmSoftPVccRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccRetryThreshold.setStatus("current")
_AtmSoftPVccRetryFailures_Type = Gauge32
_AtmSoftPVccRetryFailures_Object = MibTableColumn
atmSoftPVccRetryFailures = _AtmSoftPVccRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 13),
    _AtmSoftPVccRetryFailures_Type()
)
atmSoftPVccRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVccRetryFailures.setStatus("current")


class _AtmSoftPVccRetryLimit_Type(Integer32):
    """Custom type atmSoftPVccRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccRetryLimit_Type.__name__ = "Integer32"
_AtmSoftPVccRetryLimit_Object = MibTableColumn
atmSoftPVccRetryLimit = _AtmSoftPVccRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 14),
    _AtmSoftPVccRetryLimit_Type()
)
atmSoftPVccRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccRetryLimit.setStatus("current")
_AtmSoftPVccRowStatus_Type = RowStatus
_AtmSoftPVccRowStatus_Object = MibTableColumn
atmSoftPVccRowStatus = _AtmSoftPVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 15),
    _AtmSoftPVccRowStatus_Type()
)
atmSoftPVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccRowStatus.setStatus("current")
_AtmSoftPVccTargetDlci_Type = Integer32
_AtmSoftPVccTargetDlci_Object = MibTableColumn
atmSoftPVccTargetDlci = _AtmSoftPVccTargetDlci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 16),
    _AtmSoftPVccTargetDlci_Type()
)
atmSoftPVccTargetDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetDlci.setStatus("current")


class _AtmSoftPVccTargetType_Type(Integer32):
    """Custom type atmSoftPVccTargetType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("atm", 2),
          ("frameRelay", 3))
    )


_AtmSoftPVccTargetType_Type.__name__ = "Integer32"
_AtmSoftPVccTargetType_Object = MibTableColumn
atmSoftPVccTargetType = _AtmSoftPVccTargetType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 17),
    _AtmSoftPVccTargetType_Type()
)
atmSoftPVccTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetType.setStatus("current")


class _AtmSoftPVccTargetVpci_Type(Integer32):
    """Custom type atmSoftPVccTargetVpci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVccTargetVpci_Type.__name__ = "Integer32"
_AtmSoftPVccTargetVpci_Object = MibTableColumn
atmSoftPVccTargetVpci = _AtmSoftPVccTargetVpci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 18),
    _AtmSoftPVccTargetVpci_Type()
)
atmSoftPVccTargetVpci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVccTargetVpci.setStatus("current")
_AtmSoftPVpcTable_Object = MibTable
atmSoftPVpcTable = _AtmSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmSoftPVpcTable.setStatus("current")
_AtmSoftPVpcEntry_Object = MibTableRow
atmSoftPVpcEntry = _AtmSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1)
)
atmSoftPVpcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    atmSoftPVpcEntry.setStatus("current")


class _AtmSoftPVpcLeafReference_Type(Integer32):
    """Custom type atmSoftPVpcLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63535),
    )


_AtmSoftPVpcLeafReference_Type.__name__ = "Integer32"
_AtmSoftPVpcLeafReference_Object = MibTableColumn
atmSoftPVpcLeafReference = _AtmSoftPVpcLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 1),
    _AtmSoftPVpcLeafReference_Type()
)
atmSoftPVpcLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSoftPVpcLeafReference.setStatus("current")
_AtmSoftPVpcTargetAddress_Type = AtmAddr
_AtmSoftPVpcTargetAddress_Object = MibTableColumn
atmSoftPVpcTargetAddress = _AtmSoftPVpcTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 2),
    _AtmSoftPVpcTargetAddress_Type()
)
atmSoftPVpcTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetAddress.setStatus("current")


class _AtmSoftPVpcTargetSelectType_Type(Integer32):
    """Custom type atmSoftPVpcTargetSelectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("required", 1),
          ("any", 2))
    )


_AtmSoftPVpcTargetSelectType_Type.__name__ = "Integer32"
_AtmSoftPVpcTargetSelectType_Object = MibTableColumn
atmSoftPVpcTargetSelectType = _AtmSoftPVpcTargetSelectType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 3),
    _AtmSoftPVpcTargetSelectType_Type()
)
atmSoftPVpcTargetSelectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetSelectType.setStatus("current")


class _AtmSoftPVpcTargetVpi_Type(Integer32):
    """Custom type atmSoftPVpcTargetVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmSoftPVpcTargetVpi_Type.__name__ = "Integer32"
_AtmSoftPVpcTargetVpi_Object = MibTableColumn
atmSoftPVpcTargetVpi = _AtmSoftPVpcTargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 4),
    _AtmSoftPVpcTargetVpi_Type()
)
atmSoftPVpcTargetVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetVpi.setStatus("deprecated")


class _AtmSoftPVpcLastReleaseCause_Type(Integer32):
    """Custom type atmSoftPVpcLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmSoftPVpcLastReleaseCause_Type.__name__ = "Integer32"
_AtmSoftPVpcLastReleaseCause_Object = MibTableColumn
atmSoftPVpcLastReleaseCause = _AtmSoftPVpcLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 5),
    _AtmSoftPVpcLastReleaseCause_Type()
)
atmSoftPVpcLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcLastReleaseCause.setStatus("current")


class _AtmSoftPVpcLastReleaseDiagnostic_Type(OctetString):
    """Custom type atmSoftPVpcLastReleaseDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmSoftPVpcLastReleaseDiagnostic_Type.__name__ = "OctetString"
_AtmSoftPVpcLastReleaseDiagnostic_Object = MibTableColumn
atmSoftPVpcLastReleaseDiagnostic = _AtmSoftPVpcLastReleaseDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 6),
    _AtmSoftPVpcLastReleaseDiagnostic_Type()
)
atmSoftPVpcLastReleaseDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcLastReleaseDiagnostic.setStatus("current")


class _AtmSoftPVpcOperStatus_Type(Integer32):
    """Custom type atmSoftPVpcOperStatus based on Integer32"""
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
        *(("other", 1),
          ("establishmentInProgress", 2),
          ("connected", 3),
          ("retriesExhausted", 4),
          ("noAddressSupplied", 5),
          ("lowerLayerDown", 6))
    )


_AtmSoftPVpcOperStatus_Type.__name__ = "Integer32"
_AtmSoftPVpcOperStatus_Object = MibTableColumn
atmSoftPVpcOperStatus = _AtmSoftPVpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 7),
    _AtmSoftPVpcOperStatus_Type()
)
atmSoftPVpcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcOperStatus.setStatus("current")


class _AtmSoftPVpcRestart_Type(Integer32):
    """Custom type atmSoftPVpcRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("noop", 2))
    )


_AtmSoftPVpcRestart_Type.__name__ = "Integer32"
_AtmSoftPVpcRestart_Object = MibTableColumn
atmSoftPVpcRestart = _AtmSoftPVpcRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 8),
    _AtmSoftPVpcRestart_Type()
)
atmSoftPVpcRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcRestart.setStatus("current")


class _AtmSoftPVpcRetryInterval_Type(Integer32):
    """Custom type atmSoftPVpcRetryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmSoftPVpcRetryInterval_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryInterval_Object = MibTableColumn
atmSoftPVpcRetryInterval = _AtmSoftPVpcRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 9),
    _AtmSoftPVpcRetryInterval_Type()
)
atmSoftPVpcRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryInterval.setUnits("seconds")


class _AtmSoftPVpcRetryTimer_Type(Integer32):
    """Custom type atmSoftPVpcRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmSoftPVpcRetryTimer_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryTimer_Object = MibTableColumn
atmSoftPVpcRetryTimer = _AtmSoftPVpcRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 10),
    _AtmSoftPVpcRetryTimer_Type()
)
atmSoftPVpcRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryTimer.setUnits("seconds")


class _AtmSoftPVpcRetryThreshold_Type(Integer32):
    """Custom type atmSoftPVpcRetryThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVpcRetryThreshold_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryThreshold_Object = MibTableColumn
atmSoftPVpcRetryThreshold = _AtmSoftPVpcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 11),
    _AtmSoftPVpcRetryThreshold_Type()
)
atmSoftPVpcRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryThreshold.setStatus("current")
_AtmSoftPVpcRetryFailures_Type = Gauge32
_AtmSoftPVpcRetryFailures_Object = MibTableColumn
atmSoftPVpcRetryFailures = _AtmSoftPVpcRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 12),
    _AtmSoftPVpcRetryFailures_Type()
)
atmSoftPVpcRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryFailures.setStatus("current")


class _AtmSoftPVpcRetryLimit_Type(Integer32):
    """Custom type atmSoftPVpcRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVpcRetryLimit_Type.__name__ = "Integer32"
_AtmSoftPVpcRetryLimit_Object = MibTableColumn
atmSoftPVpcRetryLimit = _AtmSoftPVpcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 13),
    _AtmSoftPVpcRetryLimit_Type()
)
atmSoftPVpcRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcRetryLimit.setStatus("current")
_AtmSoftPVpcRowStatus_Type = RowStatus
_AtmSoftPVpcRowStatus_Object = MibTableColumn
atmSoftPVpcRowStatus = _AtmSoftPVpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 14),
    _AtmSoftPVpcRowStatus_Type()
)
atmSoftPVpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcRowStatus.setStatus("current")


class _AtmSoftPVpcTargetVpci_Type(Integer32):
    """Custom type atmSoftPVpcTargetVpci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmSoftPVpcTargetVpci_Type.__name__ = "Integer32"
_AtmSoftPVpcTargetVpci_Object = MibTableColumn
atmSoftPVpcTargetVpci = _AtmSoftPVpcTargetVpci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 15),
    _AtmSoftPVpcTargetVpci_Type()
)
atmSoftPVpcTargetVpci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSoftPVpcTargetVpci.setStatus("current")
_AtmInterfaceSoftPvcAddressTable_Object = MibTable
atmInterfaceSoftPvcAddressTable = _AtmInterfaceSoftPvcAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressTable.setStatus("current")
_AtmInterfaceSoftPvcAddressEntry_Object = MibTableRow
atmInterfaceSoftPvcAddressEntry = _AtmInterfaceSoftPvcAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1)
)
atmInterfaceSoftPvcAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddress"),
)
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressEntry.setStatus("current")
_AtmInterfaceSoftPvcAddress_Type = AtmAddr
_AtmInterfaceSoftPvcAddress_Object = MibTableColumn
atmInterfaceSoftPvcAddress = _AtmInterfaceSoftPvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 1),
    _AtmInterfaceSoftPvcAddress_Type()
)
atmInterfaceSoftPvcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddress.setStatus("current")
_AtmInterfaceSoftPvcAddressRowStatus_Type = RowStatus
_AtmInterfaceSoftPvcAddressRowStatus_Object = MibTableColumn
atmInterfaceSoftPvcAddressRowStatus = _AtmInterfaceSoftPvcAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 2),
    _AtmInterfaceSoftPvcAddressRowStatus_Type()
)
atmInterfaceSoftPvcAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmInterfaceSoftPvcAddressRowStatus.setStatus("current")
_AtmCurrentlyFailingSoftPVccTable_Object = MibTable
atmCurrentlyFailingSoftPVccTable = _AtmCurrentlyFailingSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccTable.setStatus("current")
_AtmCurrentlyFailingSoftPVccEntry_Object = MibTableRow
atmCurrentlyFailingSoftPVccEntry = _AtmCurrentlyFailingSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1)
)
atmCurrentlyFailingSoftPVccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccEntry.setStatus("current")
_AtmCurrentlyFailingSoftPVccTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingSoftPVccTimeStamp_Object = MibTableColumn
atmCurrentlyFailingSoftPVccTimeStamp = _AtmCurrentlyFailingSoftPVccTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1, 1),
    _AtmCurrentlyFailingSoftPVccTimeStamp_Type()
)
atmCurrentlyFailingSoftPVccTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccTimeStamp.setStatus("current")
_AtmCurrentlyFailingSoftPVpcTable_Object = MibTable
atmCurrentlyFailingSoftPVpcTable = _AtmCurrentlyFailingSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcTable.setStatus("current")
_AtmCurrentlyFailingSoftPVpcEntry_Object = MibTableRow
atmCurrentlyFailingSoftPVpcEntry = _AtmCurrentlyFailingSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1)
)
atmCurrentlyFailingSoftPVpcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcEntry.setStatus("current")
_AtmCurrentlyFailingSoftPVpcTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingSoftPVpcTimeStamp_Object = MibTableColumn
atmCurrentlyFailingSoftPVpcTimeStamp = _AtmCurrentlyFailingSoftPVpcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1, 1),
    _AtmCurrentlyFailingSoftPVpcTimeStamp_Type()
)
atmCurrentlyFailingSoftPVpcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcTimeStamp.setStatus("current")
_AtmSoftPvcMIBTraps_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBTraps = _AtmSoftPvcMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2)
)
_AtmSoftPvcTraps_ObjectIdentity = ObjectIdentity
atmSoftPvcTraps = _AtmSoftPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1)
)
_AtmSoftPvcTrapsPrefix_ObjectIdentity = ObjectIdentity
atmSoftPvcTrapsPrefix = _AtmSoftPvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0)
)
_AtmSoftPvcMIBConformance_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBConformance = _AtmSoftPvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3)
)
_AtmSoftPvcMIBCompliances_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBCompliances = _AtmSoftPvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1)
)
_AtmSoftPvcMIBGroups_ObjectIdentity = ObjectIdentity
atmSoftPvcMIBGroups = _AtmSoftPvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2)
)

# Managed Objects groups

atmSoftPvcBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 1)
)
atmSoftPvcBaseMIBGroup.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailuresTrapEnable"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcNotificationInterval"))
)
if mibBuilder.loadTexts:
    atmSoftPvcBaseMIBGroup.setStatus("current")

atmSoftPvcVccMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 2)
)
atmSoftPvcVccMIBGroup.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetAddress"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetSelectType"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVpi"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVci"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseCause"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseDiagnostic"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccOperStatus"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRestart"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryInterval"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryTimer"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryThreshold"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryLimit"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRowStatus"))
)
if mibBuilder.loadTexts:
    atmSoftPvcVccMIBGroup.setStatus("deprecated")

atmSoftPvcVpcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 3)
)
atmSoftPvcVpcMIBGroup.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetAddress"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetSelectType"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetVpi"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseCause"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseDiagnostic"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcOperStatus"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRestart"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryInterval"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryTimer"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryThreshold"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryLimit"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRowStatus"))
)
if mibBuilder.loadTexts:
    atmSoftPvcVpcMIBGroup.setStatus("deprecated")

atmSoftPvcAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 4)
)
atmSoftPvcAddressMIBGroup.setObjects(
    ("ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddressRowStatus")
)
if mibBuilder.loadTexts:
    atmSoftPvcAddressMIBGroup.setStatus("current")

atmCurrentlyFailingSoftPVccMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 5)
)
atmCurrentlyFailingSoftPVccMIBGroup.setObjects(
    ("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVccTimeStamp")
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVccMIBGroup.setStatus("current")

atmCurrentlyFailingSoftPVpcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 6)
)
atmCurrentlyFailingSoftPVpcMIBGroup.setObjects(
    ("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVpcTimeStamp")
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingSoftPVpcMIBGroup.setStatus("current")

atmSoftPvcVccMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 7)
)
atmSoftPvcVccMIBGroup2.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetAddress"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetSelectType"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVpci"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVci"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseCause"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseDiagnostic"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccOperStatus"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRestart"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryInterval"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryTimer"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryThreshold"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryLimit"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccRowStatus"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetType"))
)
if mibBuilder.loadTexts:
    atmSoftPvcVccMIBGroup2.setStatus("current")

atmSoftPvcVpcMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 8)
)
atmSoftPvcVpcMIBGroup2.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetAddress"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetSelectType"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetVpci"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseCause"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseDiagnostic"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcOperStatus"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRestart"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryInterval"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryTimer"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryThreshold"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryLimit"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRowStatus"))
)
if mibBuilder.loadTexts:
    atmSoftPvcVpcMIBGroup2.setStatus("current")

atmSoftPvcVccFrameRelayMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 9)
)
atmSoftPvcVccFrameRelayMIBGroup.setObjects(
    ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetDlci")
)
if mibBuilder.loadTexts:
    atmSoftPvcVccFrameRelayMIBGroup.setStatus("current")


# Notification objects

atmSoftPvcCallFailuresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0, 1)
)
atmSoftPvcCallFailuresTrap.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
)
if mibBuilder.loadTexts:
    atmSoftPvcCallFailuresTrap.setStatus(
        "current"
    )


# Notifications groups

atmSoftPvcCallFailuresEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 10)
)
atmSoftPvcCallFailuresEventGroup.setObjects(
    ("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailuresTrap")
)
if mibBuilder.loadTexts:
    atmSoftPvcCallFailuresEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

atmSoftPvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1, 1)
)
atmSoftPvcMIBCompliance.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPvcBaseMIBGroup"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcVccMIBGroup"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcAddressMIBGroup"))
)
if mibBuilder.loadTexts:
    atmSoftPvcMIBCompliance.setStatus(
        "deprecated"
    )

atmSoftPvcMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1, 2)
)
atmSoftPvcMIBCompliance2.setObjects(
      *(("ATM-SOFT-PVC-MIB", "atmSoftPvcBaseMIBGroup"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcVccMIBGroup2"),
        ("ATM-SOFT-PVC-MIB", "atmSoftPvcAddressMIBGroup"))
)
if mibBuilder.loadTexts:
    atmSoftPvcMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-SOFT-PVC-MIB",
    **{"AtmAddr": AtmAddr,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSoftPvc": atmfSoftPvc,
       "atmSoftPvcMIB": atmSoftPvcMIB,
       "atmSoftPvcMIBObjects": atmSoftPvcMIBObjects,
       "atmSoftPvcBaseGroup": atmSoftPvcBaseGroup,
       "atmSoftPvcCallFailuresTrapEnable": atmSoftPvcCallFailuresTrapEnable,
       "atmSoftPvcCallFailures": atmSoftPvcCallFailures,
       "atmSoftPvcCurrentlyFailingSoftPVccs": atmSoftPvcCurrentlyFailingSoftPVccs,
       "atmSoftPvcCurrentlyFailingSoftPVpcs": atmSoftPvcCurrentlyFailingSoftPVpcs,
       "atmSoftPvcNotificationInterval": atmSoftPvcNotificationInterval,
       "atmSoftPVccTable": atmSoftPVccTable,
       "atmSoftPVccEntry": atmSoftPVccEntry,
       "atmSoftPVccLeafReference": atmSoftPVccLeafReference,
       "atmSoftPVccTargetAddress": atmSoftPVccTargetAddress,
       "atmSoftPVccTargetSelectType": atmSoftPVccTargetSelectType,
       "atmSoftPVccTargetVpi": atmSoftPVccTargetVpi,
       "atmSoftPVccTargetVci": atmSoftPVccTargetVci,
       "atmSoftPVccLastReleaseCause": atmSoftPVccLastReleaseCause,
       "atmSoftPVccLastReleaseDiagnostic": atmSoftPVccLastReleaseDiagnostic,
       "atmSoftPVccOperStatus": atmSoftPVccOperStatus,
       "atmSoftPVccRestart": atmSoftPVccRestart,
       "atmSoftPVccRetryInterval": atmSoftPVccRetryInterval,
       "atmSoftPVccRetryTimer": atmSoftPVccRetryTimer,
       "atmSoftPVccRetryThreshold": atmSoftPVccRetryThreshold,
       "atmSoftPVccRetryFailures": atmSoftPVccRetryFailures,
       "atmSoftPVccRetryLimit": atmSoftPVccRetryLimit,
       "atmSoftPVccRowStatus": atmSoftPVccRowStatus,
       "atmSoftPVccTargetDlci": atmSoftPVccTargetDlci,
       "atmSoftPVccTargetType": atmSoftPVccTargetType,
       "atmSoftPVccTargetVpci": atmSoftPVccTargetVpci,
       "atmSoftPVpcTable": atmSoftPVpcTable,
       "atmSoftPVpcEntry": atmSoftPVpcEntry,
       "atmSoftPVpcLeafReference": atmSoftPVpcLeafReference,
       "atmSoftPVpcTargetAddress": atmSoftPVpcTargetAddress,
       "atmSoftPVpcTargetSelectType": atmSoftPVpcTargetSelectType,
       "atmSoftPVpcTargetVpi": atmSoftPVpcTargetVpi,
       "atmSoftPVpcLastReleaseCause": atmSoftPVpcLastReleaseCause,
       "atmSoftPVpcLastReleaseDiagnostic": atmSoftPVpcLastReleaseDiagnostic,
       "atmSoftPVpcOperStatus": atmSoftPVpcOperStatus,
       "atmSoftPVpcRestart": atmSoftPVpcRestart,
       "atmSoftPVpcRetryInterval": atmSoftPVpcRetryInterval,
       "atmSoftPVpcRetryTimer": atmSoftPVpcRetryTimer,
       "atmSoftPVpcRetryThreshold": atmSoftPVpcRetryThreshold,
       "atmSoftPVpcRetryFailures": atmSoftPVpcRetryFailures,
       "atmSoftPVpcRetryLimit": atmSoftPVpcRetryLimit,
       "atmSoftPVpcRowStatus": atmSoftPVpcRowStatus,
       "atmSoftPVpcTargetVpci": atmSoftPVpcTargetVpci,
       "atmInterfaceSoftPvcAddressTable": atmInterfaceSoftPvcAddressTable,
       "atmInterfaceSoftPvcAddressEntry": atmInterfaceSoftPvcAddressEntry,
       "atmInterfaceSoftPvcAddress": atmInterfaceSoftPvcAddress,
       "atmInterfaceSoftPvcAddressRowStatus": atmInterfaceSoftPvcAddressRowStatus,
       "atmCurrentlyFailingSoftPVccTable": atmCurrentlyFailingSoftPVccTable,
       "atmCurrentlyFailingSoftPVccEntry": atmCurrentlyFailingSoftPVccEntry,
       "atmCurrentlyFailingSoftPVccTimeStamp": atmCurrentlyFailingSoftPVccTimeStamp,
       "atmCurrentlyFailingSoftPVpcTable": atmCurrentlyFailingSoftPVpcTable,
       "atmCurrentlyFailingSoftPVpcEntry": atmCurrentlyFailingSoftPVpcEntry,
       "atmCurrentlyFailingSoftPVpcTimeStamp": atmCurrentlyFailingSoftPVpcTimeStamp,
       "atmSoftPvcMIBTraps": atmSoftPvcMIBTraps,
       "atmSoftPvcTraps": atmSoftPvcTraps,
       "atmSoftPvcTrapsPrefix": atmSoftPvcTrapsPrefix,
       "atmSoftPvcCallFailuresTrap": atmSoftPvcCallFailuresTrap,
       "atmSoftPvcMIBConformance": atmSoftPvcMIBConformance,
       "atmSoftPvcMIBCompliances": atmSoftPvcMIBCompliances,
       "atmSoftPvcMIBCompliance": atmSoftPvcMIBCompliance,
       "atmSoftPvcMIBCompliance2": atmSoftPvcMIBCompliance2,
       "atmSoftPvcMIBGroups": atmSoftPvcMIBGroups,
       "atmSoftPvcBaseMIBGroup": atmSoftPvcBaseMIBGroup,
       "atmSoftPvcVccMIBGroup": atmSoftPvcVccMIBGroup,
       "atmSoftPvcVpcMIBGroup": atmSoftPvcVpcMIBGroup,
       "atmSoftPvcAddressMIBGroup": atmSoftPvcAddressMIBGroup,
       "atmCurrentlyFailingSoftPVccMIBGroup": atmCurrentlyFailingSoftPVccMIBGroup,
       "atmCurrentlyFailingSoftPVpcMIBGroup": atmCurrentlyFailingSoftPVpcMIBGroup,
       "atmSoftPvcVccMIBGroup2": atmSoftPvcVccMIBGroup2,
       "atmSoftPvcVpcMIBGroup2": atmSoftPvcVpcMIBGroup2,
       "atmSoftPvcVccFrameRelayMIBGroup": atmSoftPvcVccFrameRelayMIBGroup,
       "atmSoftPvcCallFailuresEventGroup": atmSoftPvcCallFailuresEventGroup}
)
