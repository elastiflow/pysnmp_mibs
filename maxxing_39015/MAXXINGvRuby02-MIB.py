# SNMP MIB module (MAXXINGvRuby02-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/maxxing_39015/MAXXINGvRuby02-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:46 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Maxxing_ObjectIdentity = ObjectIdentity
maxxing = _Maxxing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39015)
)
_Maxxprod_ObjectIdentity = ObjectIdentity
maxxprod = _Maxxprod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39015, 13)
)
_Maxxingtrap_ObjectIdentity = ObjectIdentity
maxxingtrap = _Maxxingtrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990)
)
_Maxxingobject_ObjectIdentity = ObjectIdentity
maxxingobject = _Maxxingobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991)
)
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("mandatory")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1)
)
monitorEntry.setIndexNames(
    (0, "MAXXINGvRuby02-MIB", "serverNumber"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("mandatory")


class _ServerNumber_Type(OctetString):
    """Custom type serverNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ServerNumber_Type.__name__ = "OctetString"
_ServerNumber_Object = MibTableColumn
serverNumber = _ServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 1),
    _ServerNumber_Type()
)
serverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNumber.setStatus("mandatory")


class _Criticity_Type(OctetString):
    """Custom type criticity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Criticity_Type.__name__ = "OctetString"
_Criticity_Object = MibTableColumn
criticity = _Criticity_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 2),
    _Criticity_Type()
)
criticity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticity.setStatus("mandatory")
_Timestamp_Type = DisplayString
_Timestamp_Object = MibTableColumn
timestamp = _Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 3),
    _Timestamp_Type()
)
timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timestamp.setStatus("mandatory")
_CodeProcess_Type = DisplayString
_CodeProcess_Object = MibTableColumn
codeProcess = _CodeProcess_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 4),
    _CodeProcess_Type()
)
codeProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codeProcess.setStatus("mandatory")


class _ReturnCode_Type(OctetString):
    """Custom type returnCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ReturnCode_Type.__name__ = "OctetString"
_ReturnCode_Object = MibTableColumn
returnCode = _ReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 5),
    _ReturnCode_Type()
)
returnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    returnCode.setStatus("mandatory")
_Description_Type = DisplayString
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 39015, 13, 991, 1, 1, 6),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")

# Managed Objects groups


# Notification objects

errMaxxingInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 1)
)
errMaxxingInterface.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingInterface.setStatus(
        ""
    )

errMaxxingFileTransfer = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 2)
)
errMaxxingFileTransfer.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingFileTransfer.setStatus(
        ""
    )

errMaxxingFileProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 3)
)
errMaxxingFileProcess.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingFileProcess.setStatus(
        ""
    )

errMaxxingRunPromo = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 4)
)
errMaxxingRunPromo.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingRunPromo.setStatus(
        ""
    )

errMaxxingService = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 5)
)
errMaxxingService.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingService.setStatus(
        ""
    )

errMaxxingSchtask = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 6)
)
errMaxxingSchtask.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingSchtask.setStatus(
        ""
    )

errMaxxingPatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 7)
)
errMaxxingPatch.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingPatch.setStatus(
        ""
    )

errMaxxingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39015, 13, 990, 0, 8)
)
errMaxxingAlert.setObjects(
      *(("MAXXINGvRuby02-MIB", "serverNumber"),
        ("MAXXINGvRuby02-MIB", "criticity"),
        ("MAXXINGvRuby02-MIB", "timestamp"),
        ("MAXXINGvRuby02-MIB", "codeProcess"),
        ("MAXXINGvRuby02-MIB", "returnCode"),
        ("MAXXINGvRuby02-MIB", "description"))
)
if mibBuilder.loadTexts:
    errMaxxingAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAXXINGvRuby02-MIB",
    **{"maxxing": maxxing,
       "maxxprod": maxxprod,
       "maxxingtrap": maxxingtrap,
       "errMaxxingInterface": errMaxxingInterface,
       "errMaxxingFileTransfer": errMaxxingFileTransfer,
       "errMaxxingFileProcess": errMaxxingFileProcess,
       "errMaxxingRunPromo": errMaxxingRunPromo,
       "errMaxxingService": errMaxxingService,
       "errMaxxingSchtask": errMaxxingSchtask,
       "errMaxxingPatch": errMaxxingPatch,
       "errMaxxingAlert": errMaxxingAlert,
       "maxxingobject": maxxingobject,
       "monitorTable": monitorTable,
       "monitorEntry": monitorEntry,
       "serverNumber": serverNumber,
       "criticity": criticity,
       "timestamp": timestamp,
       "codeProcess": codeProcess,
       "returnCode": returnCode,
       "description": description}
)
