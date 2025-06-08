# SNMP MIB module (JUNIPER-HOSTRESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-HOSTRESOURCES-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:49:22 2025
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

(hrStorageEntry,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrStorageEntry")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxHostResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31)
)
if mibBuilder.loadTexts:
    jnxHostResourcesMIB.setRevisions(
        ("2004-08-18 00:00",
         "2004-05-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxHrStorage_ObjectIdentity = ObjectIdentity
jnxHrStorage = _JnxHrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1)
)
_JnxHrStorageTable_Object = MibTable
jnxHrStorageTable = _JnxHrStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1)
)
if mibBuilder.loadTexts:
    jnxHrStorageTable.setStatus("current")
_JnxHrStorageEntry_Object = MibTableRow
jnxHrStorageEntry = _JnxHrStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxHrStorageEntry.setStatus("current")
_JnxHrStoragePercentUsed_Type = Gauge32
_JnxHrStoragePercentUsed_Object = MibTableColumn
jnxHrStoragePercentUsed = _JnxHrStoragePercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1),
    _JnxHrStoragePercentUsed_Type()
)
jnxHrStoragePercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxHrStoragePercentUsed.setStatus("current")
_JnxHrSystem_ObjectIdentity = ObjectIdentity
jnxHrSystem = _JnxHrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 2)
)
_JnxHrSystemOpenFiles_Type = Gauge32
_JnxHrSystemOpenFiles_Object = MibScalar
jnxHrSystemOpenFiles = _JnxHrSystemOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 31, 2, 1),
    _JnxHrSystemOpenFiles_Type()
)
jnxHrSystemOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxHrSystemOpenFiles.setStatus("current")
hrStorageEntry.registerAugmentions(
    ("JUNIPER-HOSTRESOURCES-MIB",
     "jnxHrStorageEntry")
)
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-HOSTRESOURCES-MIB",
    **{"jnxHostResourcesMIB": jnxHostResourcesMIB,
       "jnxHrStorage": jnxHrStorage,
       "jnxHrStorageTable": jnxHrStorageTable,
       "jnxHrStorageEntry": jnxHrStorageEntry,
       "jnxHrStoragePercentUsed": jnxHrStoragePercentUsed,
       "jnxHrSystem": jnxHrSystem,
       "jnxHrSystemOpenFiles": jnxHrSystemOpenFiles}
)
