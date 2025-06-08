# SNMP MIB module (DIGI-NFS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-NFS-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiNFSTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiNFSTraps")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NfsIP_Type = IpAddress
_NfsIP_Object = MibScalar
nfsIP = _NfsIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21, 11),
    _NfsIP_Type()
)
nfsIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsIP.setStatus("mandatory")
_NfsMountPath_Type = DisplayString
_NfsMountPath_Object = MibScalar
nfsMountPath = _NfsMountPath_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21, 12),
    _NfsMountPath_Type()
)
nfsMountPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsMountPath.setStatus("mandatory")
_NfsDescription_Type = DisplayString
_NfsDescription_Object = MibScalar
nfsDescription = _NfsDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21, 13),
    _NfsDescription_Type()
)
nfsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nfsOnDisconnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21, 0, 1)
)
nfsOnDisconnection.setObjects(
      *(("DIGI-NFS-TRAPS-MIB", "nfsIP"),
        ("DIGI-NFS-TRAPS-MIB", "nfsMountPath"),
        ("DIGI-NFS-TRAPS-MIB", "nfsDescription"))
)
if mibBuilder.loadTexts:
    nfsOnDisconnection.setStatus(
        ""
    )

nfsOnDisconnectionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21, 1)
)
nfsOnDisconnectionNotification.setObjects(
      *(("DIGI-NFS-TRAPS-MIB", "nfsIP"),
        ("DIGI-NFS-TRAPS-MIB", "nfsMountPath"),
        ("DIGI-NFS-TRAPS-MIB", "nfsDescription"))
)
if mibBuilder.loadTexts:
    nfsOnDisconnectionNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-NFS-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "nfsOnDisconnection": nfsOnDisconnection,
       "nfsOnDisconnectionNotification": nfsOnDisconnectionNotification,
       "nfsIP": nfsIP,
       "nfsMountPath": nfsMountPath,
       "nfsDescription": nfsDescription}
)
