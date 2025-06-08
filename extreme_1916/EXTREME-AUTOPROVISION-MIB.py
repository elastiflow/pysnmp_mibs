# SNMP MIB module (EXTREME-AUTOPROVISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-AUTOPROVISION-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:22:20 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeAutoProvision = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40)
)
if mibBuilder.loadTexts:
    extremeAutoProvision.setRevisions(
        ("2010-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeAutoProvisionGeneral_ObjectIdentity = ObjectIdentity
extremeAutoProvisionGeneral = _ExtremeAutoProvisionGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 1)
)
_ExtremeAutoProvisionConfig_Type = TruthValue
_ExtremeAutoProvisionConfig_Object = MibScalar
extremeAutoProvisionConfig = _ExtremeAutoProvisionConfig_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 1, 1),
    _ExtremeAutoProvisionConfig_Type()
)
extremeAutoProvisionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAutoProvisionConfig.setStatus("current")
_ExtremeAutoProvisionNotificationObjects_ObjectIdentity = ObjectIdentity
extremeAutoProvisionNotificationObjects = _ExtremeAutoProvisionNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2)
)


class _ExtremeAutoProvisionResult_Type(Integer32):
    """Custom type extremeAutoProvisionResult based on Integer32"""
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
        *(("invalidConfigFileExtension", 1),
          ("tftpUnReachable", 2),
          ("fileNotExist", 3),
          ("success", 4))
    )


_ExtremeAutoProvisionResult_Type.__name__ = "Integer32"
_ExtremeAutoProvisionResult_Object = MibScalar
extremeAutoProvisionResult = _ExtremeAutoProvisionResult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 1),
    _ExtremeAutoProvisionResult_Type()
)
extremeAutoProvisionResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionResult.setStatus("current")
_ExtremeAutoProvisionIpAddress_Type = IpAddress
_ExtremeAutoProvisionIpAddress_Object = MibScalar
extremeAutoProvisionIpAddress = _ExtremeAutoProvisionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 2),
    _ExtremeAutoProvisionIpAddress_Type()
)
extremeAutoProvisionIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionIpAddress.setStatus("current")
_ExtremeAutoProvisionGateway_Type = IpAddress
_ExtremeAutoProvisionGateway_Object = MibScalar
extremeAutoProvisionGateway = _ExtremeAutoProvisionGateway_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 3),
    _ExtremeAutoProvisionGateway_Type()
)
extremeAutoProvisionGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionGateway.setStatus("current")
_ExtremeAutoProvisionTFTPServer_Type = IpAddress
_ExtremeAutoProvisionTFTPServer_Object = MibScalar
extremeAutoProvisionTFTPServer = _ExtremeAutoProvisionTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 4),
    _ExtremeAutoProvisionTFTPServer_Type()
)
extremeAutoProvisionTFTPServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionTFTPServer.setStatus("current")
_ExtremeAutoProvisionConfigFileName_Type = DisplayString
_ExtremeAutoProvisionConfigFileName_Object = MibScalar
extremeAutoProvisionConfigFileName = _ExtremeAutoProvisionConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 5),
    _ExtremeAutoProvisionConfigFileName_Type()
)
extremeAutoProvisionConfigFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionConfigFileName.setStatus("current")
_ExtremeAutoProvisionNotification_ObjectIdentity = ObjectIdentity
extremeAutoProvisionNotification = _ExtremeAutoProvisionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3)
)
_ExtremeAutoProvisionTrapPrefix_ObjectIdentity = ObjectIdentity
extremeAutoProvisionTrapPrefix = _ExtremeAutoProvisionTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0)
)

# Managed Objects groups


# Notification objects

extremeAutoProvisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0, 1)
)
extremeAutoProvisionStatus.setObjects(
      *(("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionResult"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionIpAddress"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionGateway"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionTFTPServer"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionConfigFileName"))
)
if mibBuilder.loadTexts:
    extremeAutoProvisionStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-AUTOPROVISION-MIB",
    **{"extremeAutoProvision": extremeAutoProvision,
       "extremeAutoProvisionGeneral": extremeAutoProvisionGeneral,
       "extremeAutoProvisionConfig": extremeAutoProvisionConfig,
       "extremeAutoProvisionNotificationObjects": extremeAutoProvisionNotificationObjects,
       "extremeAutoProvisionResult": extremeAutoProvisionResult,
       "extremeAutoProvisionIpAddress": extremeAutoProvisionIpAddress,
       "extremeAutoProvisionGateway": extremeAutoProvisionGateway,
       "extremeAutoProvisionTFTPServer": extremeAutoProvisionTFTPServer,
       "extremeAutoProvisionConfigFileName": extremeAutoProvisionConfigFileName,
       "extremeAutoProvisionNotification": extremeAutoProvisionNotification,
       "extremeAutoProvisionTrapPrefix": extremeAutoProvisionTrapPrefix,
       "extremeAutoProvisionStatus": extremeAutoProvisionStatus}
)
