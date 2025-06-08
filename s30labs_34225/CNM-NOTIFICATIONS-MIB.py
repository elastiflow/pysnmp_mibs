# SNMP MIB module (CNM-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/s30labs_34225/CNM-NOTIFICATIONS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:09:28 2025
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S30labs_ObjectIdentity = ObjectIdentity
s30labs = _S30labs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225)
)
_CnmNotif_ObjectIdentity = ObjectIdentity
cnmNotif = _CnmNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 1)
)
_CnmNotifBase_ObjectIdentity = ObjectIdentity
cnmNotifBase = _CnmNotifBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1)
)
_CnmNotifData_ObjectIdentity = ObjectIdentity
cnmNotifData = _CnmNotifData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 102)
)
_CnmNotifCode_Type = Integer32
_CnmNotifCode_Object = MibScalar
cnmNotifCode = _CnmNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 34225, 102, 1),
    _CnmNotifCode_Type()
)
cnmNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmNotifCode.setStatus("mandatory")
_CnmNotifMsg_Type = DisplayString
_CnmNotifMsg_Object = MibScalar
cnmNotifMsg = _CnmNotifMsg_Object(
    (1, 3, 6, 1, 4, 1, 34225, 102, 2),
    _CnmNotifMsg_Type()
)
cnmNotifMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmNotifMsg.setStatus("mandatory")
_CnmNotifKey_Type = DisplayString
_CnmNotifKey_Object = MibScalar
cnmNotifKey = _CnmNotifKey_Object(
    (1, 3, 6, 1, 4, 1, 34225, 102, 3),
    _CnmNotifKey_Type()
)
cnmNotifKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmNotifKey.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cnmAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 1)
)
cnmAlarmSet.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmAlarmSet.setStatus(
        "current"
    )

cnmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 2)
)
cnmAlarmClear.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmAlarmClear.setStatus(
        "current"
    )

cnmInfoMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 3)
)
cnmInfoMsg.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmInfoMsg.setStatus(
        "current"
    )

cnmNotifNoLinkSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 100)
)
cnmNotifNoLinkSet.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmNotifNoLinkSet.setStatus(
        "current"
    )

cnmNotiIFDownfSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 102)
)
cnmNotiIFDownfSet.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmNotiIFDownfSet.setStatus(
        "current"
    )

cnmNotifMCNMBackupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 103)
)
cnmNotifMCNMBackupFailure.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmNotifMCNMBackupFailure.setStatus(
        "current"
    )

cnmNotifMCNMNoAccessToRemote = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 110)
)
cnmNotifMCNMNoAccessToRemote.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmNotifMCNMNoAccessToRemote.setStatus(
        "current"
    )

cnmNotifLogFileGetErrorSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 34225, 1, 1, 200)
)
cnmNotifLogFileGetErrorSet.setObjects(
      *(("CNM-NOTIFICATIONS-MIB", "cnmNotifCode"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifMsg"),
        ("CNM-NOTIFICATIONS-MIB", "cnmNotifKey"))
)
if mibBuilder.loadTexts:
    cnmNotifLogFileGetErrorSet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNM-NOTIFICATIONS-MIB",
    **{"DisplayString": DisplayString,
       "s30labs": s30labs,
       "cnmNotif": cnmNotif,
       "cnmNotifBase": cnmNotifBase,
       "cnmAlarmSet": cnmAlarmSet,
       "cnmAlarmClear": cnmAlarmClear,
       "cnmInfoMsg": cnmInfoMsg,
       "cnmNotifNoLinkSet": cnmNotifNoLinkSet,
       "cnmNotiIFDownfSet": cnmNotiIFDownfSet,
       "cnmNotifMCNMBackupFailure": cnmNotifMCNMBackupFailure,
       "cnmNotifMCNMNoAccessToRemote": cnmNotifMCNMNoAccessToRemote,
       "cnmNotifLogFileGetErrorSet": cnmNotifLogFileGetErrorSet,
       "cnmNotifData": cnmNotifData,
       "cnmNotifCode": cnmNotifCode,
       "cnmNotifMsg": cnmNotifMsg,
       "cnmNotifKey": cnmNotifKey}
)
